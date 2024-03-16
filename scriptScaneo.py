import nmap
import sys

def print_help():
    print("Uso: python scan_website.py <sitio_web> [opciones]")
    print("Opciones disponibles:")
    print("-T<0-5>: Establece la velocidad del escaneo (0 = lento, 5 = rápido)")
    print("-F: Escaneo rápido (solo los puertos más comunes)")
    print("--help: Muestra esta ayuda")
    # Agrega más opciones aquí según tus necesidades

def scan_website(target, options):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments=options)

    for host in nm.all_hosts():
        print(f"Host: {host}")
        for proto in nm[host].all_protocols():
            print(f"Protocolo: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Puerto: {port} - Estado: {nm[host][proto][port]['state']}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or "--help" in sys.argv:
        print_help()
        sys.exit(1)

    target_website = sys.argv[1]
    scan_options = " ".join(sys.argv[2:])  # Concatena las opciones ingresadas
    scan_website(target_website, scan_options)

