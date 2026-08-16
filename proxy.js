import { NextResponse } from 'next/server';

// La protección solo se activa si APP_PASSWORD está definida: en local queda abierta.
const PASSWORD = process.env.APP_PASSWORD;
const REALM = 'Rolova Academy';

function constantTimeEquals(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

function unauthorized() {
  return new NextResponse('Autenticación requerida', {
    status: 401,
    headers: { 'WWW-Authenticate': `Basic realm="${REALM}", charset="UTF-8"` },
  });
}

export function proxy(request) {
  if (!PASSWORD) return NextResponse.next();

  const header = request.headers.get('authorization') || '';
  const [scheme, encoded] = header.split(' ');
  if (scheme !== 'Basic' || !encoded) return unauthorized();

  let decoded;
  try {
    decoded = atob(encoded);
  } catch {
    return unauthorized();
  }

  const provided = decoded.slice(decoded.indexOf(':') + 1);
  return constantTimeEquals(provided, PASSWORD) ? NextResponse.next() : unauthorized();
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
};
