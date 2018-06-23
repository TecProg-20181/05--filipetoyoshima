import unittest
import diskspace
import subprocess
import StringIO
import sys
from mock import patch, MagicMock  

class TestFunctions(unittest.TestCase):
    
    def test_subprocess_check(self):
        f_output = diskspace.subprocess_check_output('du -d 1')
        subprocess_output = subprocess.check_output(['du', '-d', '1'])
        self.assertEqual(f_output, subprocess_output)

    def test_byte(self):
        self.assertEqual(diskspace.bytes_to_readable(100), '50.00Kb')
        self.assertEqual(diskspace.bytes_to_readable(2048), '1.00Mb')
        self.assertEqual(diskspace.bytes_to_readable(0), '0.00B')
        self.assertEqual(diskspace.bytes_to_readable(999999999), '476.84Gb')

if __name__ == '__main__':
    unittest.main()