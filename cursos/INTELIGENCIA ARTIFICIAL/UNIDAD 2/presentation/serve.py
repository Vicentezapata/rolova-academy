import http.server
import socketserver
import webbrowser

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"\nIniciando servidor EVA IPSS local en http://localhost:{PORT}")
    print("Abre 'preview.html' o 'presenter.html' en tu navegador.")
    print("Presiona Ctrl+C para detener el servidor.\n")
    try:
        webbrowser.open(f"http://localhost:{PORT}/preview.html")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
