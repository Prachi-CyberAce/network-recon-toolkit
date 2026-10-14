**Network Reconnaissance Toolkit**

A beginner-friendly Python cybersecurity project for learning IPv4 addressing, subnet calculations and TCP connection testing.

 **Features**

- **IPv4 Address Analyzer:** Validates IPv4 addresses and displays address properties.
- **Subnet Calculator:** Calculates network addresses, subnet masks, broadcast addresses and host counts from CIDR notation.
- **TCP Port Checker:** Checks selected TCP ports on the local computer (`127.0.0.1`).
- **Interactive Menu:** Access the tools through a single command-line interface.
- **Automated Tests:** Tests basic IP validation and subnet calculations using Python's built-in `unittest` framework.

**Technologies**

- Python 3
- `ipaddress`
- `socket`
- `unittest`

No third-party Python packages are required.

**Requirements**

Python 3.8 or newer.

**Project Structure**

```text
network-recon-toolkit/
├── main.py
├── ip_analyzer.py
├── subnet_calculator.py
├── tcp_port_checker.py
├── README.md
└── tests/
    └── test_network_tools.py
```

**How to Run**

Open Command Prompt in the project directory.

Start the application:

```bash
python main.py
```

Choose an option from the menu and follow the prompts.

Run the automated tests:

```bash
python -m unittest discover -s tests -v
```

On Windows, you can use `py` instead of `python` if required.

**Example**

For the subnet input `192.168.1.10/24`, the calculator should report:

- Network address: `192.168.1.0`
- Subnet mask: `255.255.255.0`
- Broadcast address: `192.168.1.255`
- Usable host count: `254`

**Learning Objectives**

- IPv4 address validation
- Private, loopback and other special IP address properties
- CIDR notation and subnetting
- TCP socket connections and timeouts
- Python functions, modules, loops and exception handling
- Basic automated testing

**Limitations**

- The TCP checker tests only selected ports on the local computer.
- Port results do not identify vulnerabilities or prove that a service is secure.
- A failed connection does not necessarily mean a port is closed; network errors and timeouts require careful interpretation.
- Automated tests cover basic IP and subnet calculations and do not yet test every application feature.

**Safety**

This project is intended for educational use. The TCP checker is configured for localhost. Only test other systems when you have explicit authorization.

**Author**

Prachi Raut
