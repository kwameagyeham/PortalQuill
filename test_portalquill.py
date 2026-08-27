# test_portalquill.py
"""
Tests for PortalQuill module.
"""

import unittest
from portalquill import PortalQuill

class TestPortalQuill(unittest.TestCase):
    """Test cases for PortalQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PortalQuill()
        self.assertIsInstance(instance, PortalQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PortalQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
