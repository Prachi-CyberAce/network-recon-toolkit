
from ip_analyzer import analyze_ip
from subnet_calculator import calculate_subnet
from tcp_port_checker import check_tcp_ports


def main():
    while True:
        print("\n" + "=" * 40)
        print("       NETWORK RECON TOOLKIT")
        print("=" * 40)
        print("1. IPv4 Address Analyzer")
        print("2. Subnet Calculator")
        print("3. TCP Port Checker (localhost only)")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            analyze_ip()
        elif choice == "2":
            calculate_subnet()
        elif choice == "3":
            check_tcp_ports()
        elif choice == "4":
            print("Exiting Network Recon Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
