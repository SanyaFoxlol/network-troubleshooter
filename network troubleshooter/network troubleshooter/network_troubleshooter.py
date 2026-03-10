import socket
import time
import psutil
import os
import sys

host = "google.com"

browsers = {
    "chrome.exe": "Google Chrome",
    "firefox.exe": "Mozilla Firefox",
    "msedge.exe": "Microsoft Edge",
    "opera.exe": "Opera",
    "brave.exe": "Brave"
}

def get_browser():
    sys.stdout.write("\033[H\033[J")

    for proc in psutil.process_iter(['name']):
        name = proc.info['name']
        if name in browsers:
            return browsers[name]
    return "Browser not detected"

print("Hostname:", socket.gethostname())
print("IP:", socket.gethostbyname(socket.gethostname()))
print("-" * 30)

while True:
    try:
        start = time.time()
        socket.create_connection((host, 80), timeout=2)
        ping = (time.time() - start) * 1000
        ping_text = f"{round(ping,2)} ms"
    except:
        ping_text = "timeout"

    browser = get_browser()

    os.system("cls")  # щоб не спамило новими рядками

    print("PING MONITOR")
    print("-" * 30)
    print("Ping:", ping_text)
    print("Browser:", browser)

    time.sleep(1)