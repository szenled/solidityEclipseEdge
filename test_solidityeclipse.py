# test_solidityeclipse.py
"""
Tests for solidityEclipse module.
"""

import unittest
from solidityeclipse import solidityEclipse

class TestsolidityEclipse(unittest.TestCase):
    """Test cases for solidityEclipse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = solidityEclipse()
        self.assertIsInstance(instance, solidityEclipse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = solidityEclipse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
