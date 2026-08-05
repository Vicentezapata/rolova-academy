import "./globals.css";

export const metadata = {
  title: "Rolova Academy",
  description: "Tu ecosistema de aprendizaje centralizado en Rolova Academy",
};

export default function RootLayout({ children }) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
