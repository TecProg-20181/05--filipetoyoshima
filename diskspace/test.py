import unittest
import diskspace
import subprocess
import cStringIO
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

    def test_print_tree(self):
        stdout_ = sys.stdout
        output = cStringIO.StringIO()
        sys.stdout = output
        file_tree_node = {
            'children': [],
            'size': 4,
            'print_size': '200.00Kb'
        }

        file_tree = {
            'some/directory' : file_tree_node
        }

        diskspace.print_tree(file_tree,
                             file_tree_node,
                             'some/directory',
                             4,
                             4)
        expected_output = '200.00Kb  100%  some/directory\n'
        sys.stdout = stdout_
        self.assertEqual(expected_output, output.getvalue())

if __name__ == '__main__':
    unittest.main()