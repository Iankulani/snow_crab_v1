#!/usr/bin/env python3
"""
SNOW-CRAB-V1 Command Testing Suite
Tests all major commands and features
"""

import os
import sys
import unittest
import subprocess
import time
import socket
import threading

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Test configuration
TEST_HOST = "127.0.0.1"
TEST_PORT = 80
TEST_TIMEOUT = 30


class TestNetworkTools(unittest.TestCase):
    """Test network utility functions"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test class"""
        from snow_crab_v1 import NetworkTools
        cls.tools = NetworkTools()
    
    def test_ping_localhost(self):
        """Test ping to localhost"""
        result = self.tools.ping("127.0.0.1", count=2, timeout=5)
        self.assertIsNotNone(result)
        self.assertIsInstance(result.success, bool)
    
    def test_dns_lookup(self):
        """Test DNS lookup"""
        result = self.tools.dns_lookup("google.com", "A")
        self.assertIsNotNone(result)
    
    def test_get_local_ip(self):
        """Test getting local IP"""
        ip = self.tools.get_local_ip()
        self.assertIsNotNone(ip)
        self.assertRegex(ip, r'^\d+\.\d+\.\d+\.\d+$')
    
    def test_get_public_ip(self):
        """Test getting public IP"""
        ip = self.tools.get_public_ip()
        if ip:
            self.assertRegex(ip, r'^\d+\.\d+\.\d+\.\d+$')
    
    def test_port_scan(self):
        """Test port scanning"""
        results = self.tools.port_scan("127.0.0.1", [22, 80, 443], timeout=0.5)
        self.assertIsInstance(results, list)
    
    def test_whois(self):
        """Test WHOIS lookup"""
        result = self.tools.whois_lookup("google.com")
        self.assertIsNotNone(result)
    
    def test_geolocation(self):
        """Test IP geolocation"""
        result = self.tools.get_geolocation("8.8.8.8")
        self.assertIsInstance(result, dict)


class TestDatabaseManager(unittest.TestCase):
    """Test database operations"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test database"""
        from snow_crab_v1 import DatabaseManager
        cls.test_db_path = "test_snow_crab.db"
        cls.db = DatabaseManager(cls.test_db_path)
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test database"""
        cls.db.close()
        if os.path.exists(cls.test_db_path):
            os.remove(cls.test_db_path)
    
    def test_log_command(self):
        """Test command logging"""
        self.db.log_command("test_command", "test", "test", "user1", True, "output", 1.5)
        history = self.db.conn.execute(
            "SELECT * FROM command_history WHERE command = 'test_command'"
        ).fetchall()
        self.assertGreater(len(history), 0)
    
    def test_managed_ips(self):
        """Test IP management"""
        result = self.db.add_managed_ip("192.168.1.100", "test.local", "test")
        self.assertTrue(result)
        
        ips = self.db.get_managed_ips()
        self.assertGreater(len(ips), 0)
        
        self.db.remove_managed_ip("192.168.1.100")
    
    def test_block_unblock_ip(self):
        """Test IP blocking"""
        self.db.add_managed_ip("10.0.0.1", "test.local", "test")
        
        result = self.db.block_ip("10.0.0.1", "Test block")
        self.assertTrue(result)
        
        result = self.db.unblock_ip("10.0.0.1")
        self.assertTrue(result)
        
        self.db.remove_managed_ip("10.0.0.1")
    
    def test_statistics(self):
        """Test statistics retrieval"""
        stats = self.db.get_statistics()
        self.assertIsInstance(stats, dict)
    
    def test_phishing_links(self):
        """Test phishing link operations"""
        from snow_crab_v1 import PhishingLink
        import datetime
        
        link = PhishingLink(
            id="test123",
            platform="test",
            phishing_url="http://test.local",
            template="test",
            created_at=datetime.datetime.now().isoformat()
        )
        
        result = self.db.save_phishing_link(link)
        self.assertTrue(result)
        
        links = self.db.get_phishing_links()
        self.assertGreater(len(links), 0)
    
    def test_credential_capture(self):
        """Test credential capture"""
        self.db.save_captured_credential("test123", "user", "pass", "127.0.0.1", "TestAgent")
        creds = self.db.get_captured_credentials("test123")
        self.assertGreater(len(creds), 0)


class TestConfigManager(unittest.TestCase):
    """Test configuration management"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test config"""
        from snow_crab_v1 import ConfigManager
        cls.config = ConfigManager()
    
    def test_default_config(self):
        """Test default configuration"""
        self.assertIsNotNone(self.config.config)
        self.assertEqual(self.config.config.get("version"), "1.0.0")
    
    def test_get_set(self):
        """Test getting and setting values"""
        self.config.set("test.key", "test_value")
        value = self.config.get("test.key")
        self.assertEqual(value, "test_value")
    
    def test_nested_get(self):
        """Test nested configuration access"""
        value = self.config.get("animations.enabled")
        self.assertIsNotNone(value)


class TestCommandHandler(unittest.TestCase):
    """Test command handler"""
    
    @classmethod
    def setUpClass(cls):
        """Set up command handler"""
        from snow_crab_v1 import (
            DatabaseManager, CommandHandler, SocialEngineeringTools,
            NetworkTools
        )
        
        cls.test_db_path = "test_handler.db"
        cls.db = DatabaseManager(cls.test_db_path)
        cls.handler = CommandHandler(cls.db)
    
    @classmethod
    def tearDownClass(cls):
        """Clean up"""
        cls.db.close()
        if os.path.exists(cls.test_db_path):
            os.remove(cls.test_db_path)
    
    def test_ping_command(self):
        """Test ping command"""
        result = self.handler.execute("ping 127.0.0.1 1")
        self.assertIn('success', result)
        self.assertIn('output', result)
    
    def test_help_command(self):
        """Test help command"""
        result = self.handler.execute("help")
        self.assertTrue(result['success'])
        self.assertIn('SNOW-CRAB-V1', result['output'])
    
    def test_status_command(self):
        """Test status command"""
        result = self.handler.execute("status")
        self.assertTrue(result['success'])
    
    def test_history_command(self):
        """Test history command"""
        result = self.handler.execute("history 5")
        self.assertTrue(result['success'])
    
    def test_traffic_types_command(self):
        """Test traffic types command"""
        result = self.handler.execute("traffic_types")
        self.assertTrue(result['success'])
    
    def test_system_command(self):
        """Test system command"""
        result = self.handler.execute("system")
        self.assertTrue(result['success'])
    
    def test_list_templates_command(self):
        """Test list templates command"""
        result = self.handler.execute("list_templates")
        self.assertTrue(result['success'])
    
    def test_dns_command(self):
        """Test DNS command"""
        result = self.handler.execute("dns google.com A")
        self.assertIn('success', result)
    
    def test_location_command(self):
        """Test location command"""
        result = self.handler.execute("location 8.8.8.8")
        self.assertIn('success', result)
    
    def test_anim_spinner_command(self):
        """Test animation command"""
        result = self.handler.execute("anim_spinner 0.5")
        self.assertTrue(result['success'])


class TestTrafficGenerator(unittest.TestCase):
    """Test traffic generation"""
    
    @classmethod
    def setUpClass(cls):
        """Set up traffic generator"""
        from snow_crab_v1 import DatabaseManager, TrafficGeneratorEngine
        
        cls.test_db_path = "test_traffic.db"
        cls.db = DatabaseManager(cls.test_db_path)
        cls.traffic = TrafficGeneratorEngine(cls.db)
    
    @classmethod
    def tearDownClass(cls):
        """Clean up"""
        cls.traffic.stop()
        cls.db.close()
        if os.path.exists(cls.test_db_path):
            os.remove(cls.test_db_path)
    
    def test_get_available_types(self):
        """Test getting available traffic types"""
        types = self.traffic.get_available_types()
        self.assertIsInstance(types, list)
        self.assertGreater(len(types), 0)
    
    def test_generate_icmp(self):
        """Test ICMP traffic generation"""
        try:
            generator = self.traffic.generate("icmp", "127.0.0.1", 2, packet_rate=10)
            self.assertIsNotNone(generator)
            self.assertEqual(generator.target_ip, "127.0.0.1")
            
            time.sleep(3)
            self.traffic.stop(generator.id)
        except Exception as e:
            self.skipTest(f"Traffic generation not available: {e}")


class TestSSHManager(unittest.TestCase):
    """Test SSH manager"""
    
    @classmethod
    def setUpClass(cls):
        """Set up SSH manager"""
        try:
            from snow_crab_v1 import DatabaseManager, SSHManager, PARAMIKO_AVAILABLE
            if not PARAMIKO_AVAILABLE:
                raise ImportError("Paramiko not available")
            
            cls.test_db_path = "test_ssh.db"
            cls.db = DatabaseManager(cls.test_db_path)
            cls.ssh = SSHManager(cls.db)
        except ImportError:
            cls.ssh = None
    
    @classmethod
    def tearDownClass(cls):
        """Clean up"""
        if hasattr(cls, 'db'):
            cls.db.close()
            if os.path.exists(cls.test_db_path):
                os.remove(cls.test_db_path)
    
    def test_ssh_available(self):
        """Test SSH availability check"""
        if self.ssh is None:
            self.skipTest("SSH not available")
        self.assertTrue(self.ssh.is_available())
    
    def test_add_connection(self):
        """Test adding SSH connection"""
        if self.ssh is None:
            self.skipTest("SSH not available")
        
        conn = self.ssh.add_connection(
            "test", "192.168.1.100", "testuser", "testpass"
        )
        self.assertIsNotNone(conn)
        self.assertEqual(conn.name, "test")


class TestSocialEngineering(unittest.TestCase):
    """Test social engineering tools"""
    
    @classmethod
    def setUpClass(cls):
        """Set up social engineering tools"""
        from snow_crab_v1 import DatabaseManager, SocialEngineeringTools
        
        cls.test_db_path = "test_social.db"
        cls.db = DatabaseManager(cls.test_db_path)
        cls.social = SocialEngineeringTools(cls.db)
    
    @classmethod
    def tearDownClass(cls):
        """Clean up"""
        cls.social.stop_server()
        cls.db.close()
        if os.path.exists(cls.test_db_path):
            os.remove(cls.test_db_path)
    
    def test_get_templates(self):
        """Test getting templates"""
        templates = self.social.get_available_templates()
        self.assertIsInstance(templates, list)
        self.assertGreater(len(templates), 0)
    
    def test_generate_phishing_link(self):
        """Test generating phishing link"""
        result = self.social.generate_phishing_link("facebook")
        self.assertTrue(result['success'])
        self.assertIn('link_id', result)


class TestKeylogger(unittest.TestCase):
    """Test keylogger"""
    
    @classmethod
    def setUpClass(cls):
        """Set up keylogger"""
        try:
            from snow_crab_v1 import DatabaseManager, KeyloggerEngine, PYNPUT_AVAILABLE
            if not PYNPUT_AVAILABLE:
                raise ImportError("Pynput not available")
            
            cls.test_db_path = "test_keylog.db"
            cls.db = DatabaseManager(cls.test_db_path)
            cls.config = type('Config', (), {'get': lambda s, k, d=None: d})()
            cls.keylogger = KeyloggerEngine(cls.db, cls.config)
        except ImportError:
            cls.keylogger = None
    
    @classmethod
    def tearDownClass(cls):
        """Clean up"""
        if hasattr(cls, 'db'):
            cls.db.close()
            if os.path.exists(cls.test_db_path):
                os.remove(cls.test_db_path)
    
    def test_keylogger_available(self):
        """Test keylogger availability"""
        if self.keylogger is None:
            self.skipTest("Keylogger not available")
        self.assertIsNotNone(self.keylogger)


class TestIntegration(unittest.TestCase):
    """Integration tests"""
    
    def test_full_workflow(self):
        """Test a complete workflow"""
        from snow_crab_v1 import (
            DatabaseManager, CommandHandler, SocialEngineeringTools
        )
        
        test_db_path = "test_integration.db"
        
        try:
            # Initialize components
            db = DatabaseManager(test_db_path)
            handler = CommandHandler(db)
            
            # Test help
            result = handler.execute("help")
            self.assertTrue(result['success'])
            
            # Test status
            result = handler.execute("status")
            self.assertTrue(result['success'])
            
            # Test ping
            result = handler.execute("ping 127.0.0.1 1")
            self.assertIn('success', result)
            
            # Test system
            result = handler.execute("system")
            self.assertTrue(result['success'])
            
        finally:
            db.close()
            if os.path.exists(test_db_path):
                os.remove(test_db_path)


def run_tests():
    """Run all tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestNetworkTools,
        TestDatabaseManager,
        TestConfigManager,
        TestCommandHandler,
        TestTrafficGenerator,
        TestSSHManager,
        TestSocialEngineering,
        TestKeylogger,
        TestIntegration
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    print("=" * 70)
    print("SNOW-CRAB-V1 Test Suite")
    print("=" * 70)
    print()
    
    success = run_tests()
    
    print()
    print("=" * 70)
    if success:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed!")
    print("=" * 70)
    
    sys.exit(0 if success else 1)
