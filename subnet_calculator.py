
import ipaddress


def calculate_subnet():
    print("=" * 40)
    print("       SUBNET CALCULATOR")
    print("=" * 40)

    user_input = input(
        "\nEnter an IPv4 address with CIDR (example: 192.168.1.10/24): "
    ).strip()

    try:
        interface = ipaddress.IPv4Interface(user_input)
        network = interface.network

        print("\n--- Subnet Analysis ---")
        print(f"IP Address: {interface.ip}")
        print(f"Network Address: {network.network_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"CIDR Prefix: /{network.prefixlen}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Total Addresses: {network.num_addresses}")

        if network.prefixlen <= 30:
            first_host = network.network_address + 1
            last_host = network.broadcast_address - 1
            usable_hosts = network.num_addresses - 2
        elif network.prefixlen == 31:
            first_host = network.network_address
            last_host = network.broadcast_address
            usable_hosts = 2
        else:
            first_host = network.network_address
            last_host = network.network_address
            usable_hosts = 1

        print(f"First Usable Host: {first_host}")
        print(f"Last Usable Host: {last_host}")
        print(f"Usable Host Count: {usable_hosts}")

    except (ipaddress.AddressValueError,
            ipaddress.NetmaskValueError,
            ValueError):
        print("\nInvalid input!")
        print("Use an IPv4 address with a prefix from /0 to /32.")
        print("Example: 192.168.1.10/24")


if __name__ == "__main__":
    calculate_subnet()
