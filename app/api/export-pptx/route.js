import { NextResponse } from 'next/server';
import puppeteer from 'puppeteer';
import pptxgen from 'pptxgenjs';

export async function POST(request) {
  let browser;
  try {
    const { url, title } = await request.json();

    // Solo se permiten rutas servidas por esta app: evita SSRF hacia hosts arbitrarios
    if (typeof url !== 'string' || !url.startsWith('/api/file/') || url.includes('..')) {
      return NextResponse.json({ error: 'URL no permitida' }, { status: 400 });
    }

    const fullUrl = new URL(request.url).origin + url;

    console.log(`[Export-PPTX] Iniciando exportación de: ${fullUrl}`);

    browser = await puppeteer.launch({
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const page = await browser.newPage();

    // Puppeteer se conecta a esta misma app: si hay contraseña, debe autenticarse.
    if (process.env.APP_PASSWORD) {
      await page.authenticate({ username: 'internal', password: process.env.APP_PASSWORD });
    }

    // Resolucion 1280x720 con Device Scale 2 = 2560x1440 para alta definición en el PPTX
    await page.setViewport({ width: 1280, height: 720, deviceScaleFactor: 2 });

    console.log(`[Export-PPTX] Cargando página...`);
    await page.goto(fullUrl, { waitUntil: 'networkidle0', timeout: 30000 });

    const totalSlides = await page.evaluate(() => {
      // Contar la cantidad de divs que envuelven los iframes
      return document.querySelectorAll('.slide-wrap').length;
    });

    console.log(`[Export-PPTX] Encontradas ${totalSlides} diapositivas.`);

    if (totalSlides === 0) {
      return NextResponse.json(
        { error: 'No se encontraron diapositivas en la presentación.' },
        { status: 422 }
      );
    }

    let pres = new pptxgen();
    pres.layout = 'LAYOUT_16x9';

    for (let i = 0; i < totalSlides; i++) {
      console.log(`[Export-PPTX] Capturando slide ${i + 1}/${totalSlides}...`);
      
      await page.evaluate((idx) => {
        // Ejecuta la función nativa 'show' del preview.html para ir a la slide deseada
        if (typeof show === 'function') {
          show(idx);
        }
      }, i);

      // Pequeña espera para permitir que las animaciones (CSS, Mermaid, etc.) se completen
      await new Promise(r => setTimeout(r, 800));

      const base64Image = await page.screenshot({ encoding: 'base64' });

      let slide = pres.addSlide();
      // Ocultar márgenes y estirar imagen al borde
      slide.addImage({ data: 'image/png;base64,' + base64Image, x: 0, y: 0, w: '100%', h: '100%' });
    }

    await browser.close();
    browser = undefined;
    console.log(`[Export-PPTX] Generando archivo PPTX...`);

    const pptxBuffer = await pres.write({ outputType: 'nodebuffer' });
    
    const safeTitle = (title || 'presentacion').replace(/[^a-z0-9]/gi, '_').toLowerCase();

    return new NextResponse(pptxBuffer, {
      status: 200,
      headers: {
        'Content-Disposition': `attachment; filename="${safeTitle}.pptx"`,
        'Content-Type': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
      }
    });

  } catch (err) {
    console.error('[Export-PPTX] Error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  } finally {
    if (browser) await browser.close().catch(() => {});
  }
}
