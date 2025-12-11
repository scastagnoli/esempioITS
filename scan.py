import argparse
import socket
import threading
def worker(target, port):
    s = socket.socket()
    try:
        s.settimeout(1)
        s.connect((target, port))
        print(f"[+] {target}:{port} open")
    except:
        print(f"[-] {target}:{port} closed")
    finally:
        s.close()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--threads", type=int, default=5)
    args = parser.parse_args()
    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=worker, args=(args.target, args.port))
        threads.append(t)
        t.start() 
    for t in threads:
        t.join()
