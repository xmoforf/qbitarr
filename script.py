import argparse
import logging
from getpass import getpass

import qbittorrentapi

class QBitArrError(Exception):
    def __init__(self, logmsg):
        logging.exception(logmsg)

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
    qbc = qbittorrentapi.Client(host=host, port=port, username=username, password=password)
    print("qbittorrent-api client is qbc\n")
    print("Example:\n    for torrent in qbc.torrents_info():\n        print(f'{torrent.infohash_v1}: {torrent.name}')\n\n")
