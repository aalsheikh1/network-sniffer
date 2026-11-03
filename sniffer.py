from scapy.all import IP, sniff


def handle_packet(packet):
    if IP not in packet:
        return

    src = packet[IP].src
    dst = packet[IP].dst
    print(f"{src} -> {dst}")


def main():
    print("Starting capture... press Ctrl+C to stop.")
    sniff(prn=handle_packet, store=False)


if __name__ == "__main__":
    main()
