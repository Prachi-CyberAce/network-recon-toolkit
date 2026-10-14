
import socket

def check_tcp_ports():
    target = "127.0.0.1"

    # Ports commonly used by network services
    ports = [22, 53, 80, 443, 8080, 1521]

    print("\n" + "=" * 40)
    print("        TCP PORT CHECKER")
    print("=" * 40)
    print(f"Target: {target} (your own computer)")
    print("\nChecking selected TCP ports...\n")

    for port in ports:
        connection = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        connection.settimeout(3)

        try:
            connection.connect((target, port))
            print(f"TCP Port {port}: OPEN")

        except ConnectionRefusedError:
            print(f"TCP Port {port}: CLOSED")

        except TimeoutError:
            print(f"TCP Port {port}: NO RESPONSE (timeout)")

        except OSError as error:
            print(f"TCP Port {port}: ERROR ({error})")

        finally:
            connection.close()

if __name__ == "__main__":
    check_tcp_ports()
