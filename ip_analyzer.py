
import ipaddress


def analyze_ip():
    print("=" * 40)
    print("     NETWORK RECON TOOLKIT")
    print("        IPv4 ANALYZER")
    print("=" * 40)

    user_input = input("\nEnter an IPv4 address: ").strip()

    try:
        ip = ipaddress.IPv4Address(user_input)

        print("\n--- Analysis Results ---")
        print(f"IP Address: {ip}")
        print(f"Valid IPv4: Yes")
        print(f"Private Address: {ip.is_private}")
        print(f"Loopback Address: {ip.is_loopback}")
        print(f"Multicast Address: {ip.is_multicast}")
        print(f"Reserved Address: {ip.is_reserved}")

        if ip.is_loopback:
            category = "Loopback"
        elif ip.is_multicast:
            category = "Multicast"
        elif ip.is_private:
            category = "Private"
        elif ip.is_reserved:
            category = "Reserved"
        else:
            category = "Other / Public-range candidate"

        print(f"Address Category: {category}")

    except ipaddress.AddressValueError:
        print("\nInvalid IPv4 address!")
        print("Example of a valid address: 192.168.1.10")


if __name__ == "__main__":
    analyze_ip()
