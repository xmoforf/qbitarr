import argparse
import logging
from getpass import getpass

import qbittorrentapi

logging.basicConfig(level=logging.DEBUG)

class QBitArrError(Exception):
    def __init__(self, logmsg):
        logging.exception(logmsg)

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
    parser.add_argument('--log-level', default='INFO', help='Logging level (e.g., DEBUG, INFO, WARNING).')
    args = parser.parse_args()

    # Configure logging
    log_level = args.log_level.upper()
    log_level_numeric = logging.getLevelNamesMapping().get(log_level, None)
    if log_level_numeric:
        logging.basicConfig(level=log_level)
    else:
        raise QBitArrError(f"Invalid log level: {log_level}")
        
    host = args.host or input("Qbittorrent IP Address: ").strip()
    port = args.port or input("Qbittorrent Port: ").strip()
    username = args.username or input("Username: ").strip()
    password = getpass("Password: ").strip()


    logging.info(f"Connecting to client at {host}:{port} username={username}")
    qbc = QBClient(host=host, port=port, username=username, password=password)
    print("qbittorrent-api client is qbc.")
    print("Example:\nfor torrent in qbc.torrents():\n    print(torrent.name)\n")
