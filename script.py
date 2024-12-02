import argparse
from getpass import getpass

import qbittorrentapi

class QBClient:
    def __init__(self, **conn_info):
        self.client = qbittorrentapi.Client(**conn_info)

    def torrents(self):
        for torrent in self.client.torrents_info():
            yield torrent
    
    def trackers(self, infohash):
        for tracker in self.client.torrents_trackers(infohash):
            yield tracker


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Iterate through torrents in qBittorrent.")
    parser.add_argument("--host", type=str, help="qBittorrent IP address (e.g., 192.168.1.10)")
    parser.add_argument("--port", type=int, help="qBittorrent port (e.g., 18080)")
    parser.add_argument("--username", type=str, help="qBittorrent username")
    args = parser.parse_args()

    host = args.host or input("Qbittorrent IP Address: ").strip()
    port = args.port or input("Qbittorrent Port: ").strip()
    username = args.username or input("Username: ").strip()
    password = getpass("Password: ").strip()

    qbc = QBClient(host=host, port=port, username=username, password=password)
    for torrent in qbc.torrents():
        print(torrent.name)