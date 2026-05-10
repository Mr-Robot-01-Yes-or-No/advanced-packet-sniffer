from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.dns import DNS
from colorama import init, Style
from datetime import datetime
import os

from utils import get_protocol_color


# =========================
# INITIALIZE COLORAMA
# =========================

init(autoreset=True)


# =========================
# SETTINGS
# =========================

SHOW_TCP = True
SHOW_UDP = True
SHOW_ICMP = True
SHOW_DNS = True

SAVE_TO_FILE = True

LOG_FILE = "packets.log"


# =========================
# STATS
# =========================

packet_count = 0

stats = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "DNS": 0
}


# =========================
# SAVE LOGS
# =========================

def save_log(data):

    if SAVE_TO_FILE:

        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(data + "\n")


# =========================
# SHOW STATS
# =========================

def show_stats():

    print("\n" + "=" * 60)
    print("PACKET STATISTICS")
    print("=" * 60)

    for protocol, count in stats.items():
        print(f"{protocol:<10}: {count}")

    print("=" * 60)


# =========================
# PROCESS PACKETS
# =========================

def process_packet(packet):

    global packet_count

    # Process only IP packets
    if not packet.haslayer(IP):
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    # Ignore localhost traffic
    if src_ip.startswith("127.") or dst_ip.startswith("127."):
        return

    protocol = "OTHER"

    src_port = "-"
    dst_port = "-"

    info = ""

    # =========================
    # TCP
    # =========================

    if packet.haslayer(TCP):

        if not SHOW_TCP:
            return

        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        flags = packet[TCP].flags

        # Ignore HTTPS spam traffic
        if dst_port == 443 or src_port == 443:
            return

        # Ignore browser noise ports
        noisy_ports = [1900, 5353, 5355]

        if dst_port in noisy_ports or src_port in noisy_ports:
            return

        protocol = "TCP"

        info = f"Flags={flags}"

        stats["TCP"] += 1

        # SYN detection
        if flags == "S":
            info += " [SYN]"

        # HTTP Detection
        if dst_port == 80 or src_port == 80:
            protocol = "HTTP"

    # =========================
    # UDP
    # =========================

    elif packet.haslayer(UDP):

        if not SHOW_UDP:
            return

        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

        # Ignore noisy UDP traffic
        noisy_ports = [1900, 5353, 5355]

        if dst_port in noisy_ports or src_port in noisy_ports:
            return

        protocol = "UDP"

        stats["UDP"] += 1

    # =========================
    # ICMP
    # =========================

    elif packet.haslayer(ICMP):

        if not SHOW_ICMP:
            return

        protocol = "ICMP"

        stats["ICMP"] += 1

    # =========================
    # DNS
    # =========================

    if packet.haslayer(DNS):

        if not SHOW_DNS:
            return

        protocol = "DNS"

        stats["DNS"] += 1

    packet_count += 1

    timestamp = datetime.now().strftime("%H:%M:%S")

    length = len(packet)

    color = get_protocol_color(protocol)

    output = (
        f"\n[{packet_count}] "
        f"[{timestamp}] "
        f"{protocol:<5}\n"
        f" SRC : {src_ip}:{src_port}\n"
        f" DEST: {dst_ip}:{dst_port}\n"
        f" LEN : {length}\n"
        f" INFO: {info}\n"
        f"{'-' * 60}"
    )

    print(color + output + Style.RESET_ALL)

    save_log(output)

    # Slow down output slightly
    import time
    time.sleep(0.5)


# =========================
# MAIN FUNCTION
# =========================

def main():

    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 60)
    print("ADVANCED PACKET SNIFFER")
    print("=" * 60)

    print("\nEnabled Filters:")

    if SHOW_TCP:
        print("[+] TCP")

    if SHOW_UDP:
        print("[+] UDP")

    if SHOW_ICMP:
        print("[+] ICMP")

    if SHOW_DNS:
        print("[+] DNS")

    print("\nPress CTRL + C to stop.\n")

    try:

        sniff(prn=process_packet, store=False)

    except KeyboardInterrupt:

        print("\nStopping sniffer...")

        show_stats()

        print(f"\nLogs saved to: {LOG_FILE}")


# =========================
# START PROGRAM
# =========================

if __name__ == "__main__":
    main()