from scapy.all import sniff


def handle_packet(packet):
    print(packet.summary())


def main():
    print("Starting capture... press Ctrl+C to stop.")
    sniff(prn=handle_packet, store=False)


if __name__ == "__main__":
    main()
