import { Inter, Outfit, JetBrains_Mono } from "next/font/google";
import { NO_FLASH_SCRIPT } from "./lib/theme-store";
import "./globals.css";

const inter = Inter({ subsets: ["latin"], variable: "--font-sans", display: "swap" });
const outfit = Outfit({ subsets: ["latin"], variable: "--font-display", display: "swap" });
// Solo se usa en las etiquetas 3D, que se montan tarde: precargarla desperdicia ancho de banda.
const mono = JetBrains_Mono({ subsets: ["latin"], variable: "--font-mono", display: "swap", preload: false });

export const metadata = {
  title: "Rolova Academy",
  description: "Tu ecosistema de aprendizaje centralizado en Rolova Academy",
};

export default function RootLayout({ children }) {
  return (
    <html
      lang="es"
      className={`${inter.variable} ${outfit.variable} ${mono.variable}`}
      suppressHydrationWarning
    >
      <head>
        <script dangerouslySetInnerHTML={{ __html: NO_FLASH_SCRIPT }} />
      </head>
      <body>{children}</body>
    </html>
  );
}
