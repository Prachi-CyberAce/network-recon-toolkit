
import ipaddress
import unittest


class TestNetworkTools(unittest.TestCase):

    def test_valid_ipv4(self):
        ip = ipaddress.IPv4Address("192.168.1.10")
        self.assertEqual(str(ip), "192.168.1.10")

    def test_invalid_ipv4(self):
        with self.assertRaises(ipaddress.AddressValueError):
            ipaddress.IPv4Address("192.168.1.999")

    def test_private_ipv4(self):
        ip = ipaddress.IPv4Address("192.168.1.10")
        self.assertTrue(ip.is_private)

    def test_subnet_network_address(self):
        network = ipaddress.ip_network("192.168.1.10/24", strict=False)
        self.assertEqual(str(network.network_address), "192.168.1.0")

    def test_subnet_broadcast_address(self):
        network = ipaddress.ip_network("192.168.1.10/24", strict=False)
        self.assertEqual(str(network.broadcast_address), "192.168.1.255")

    def test_subnet_host_count(self):
        network = ipaddress.ip_network("192.168.1.10/24", strict=False)
        self.assertEqual(network.num_addresses - 2, 254)


if __name__ == "__main__":
    unittest.main()
