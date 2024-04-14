import unittest
import sys
import os
from collections import Counter


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('\n')

    def test_01(self):
        print('\n')
        filename = sys.argv[1]
        print(filename)
        print(len(sys.argv))
        print(sys.platform)
        self.assertEqual('darwin', sys.platform)
        self.assertEqual('utf-8', sys.getfilesystemencoding())
        self.assertEqual('utf-8', sys.getdefaultencoding())
        print(sys.version)
        print(sys.getfilesystemencoding())
        print(sys.getdefaultencoding())
        print(sys.path)
        # self.assertEqual(True, False)

    def test_02(self):
        """
        OS library is used to collect system info. Like InMap is u
        """
        print(os.path)

        if len(sys.argv) == 2:

            filename = sys.argv[1]
            print(filename)

            if os.path.isfile(filename):
                print('File exists')
            if not os.path.isfile(filename):
                print('File does not exist')
            if not os.access(filename, os.R_OK):
                print('Access Denied')
            # exit(0)
        else:
            print(f"Length is not 2. It is {len(sys.argv)}")

    def test_03(self):
        pwd = os.getcwd()
        print(pwd)
        list_directory = os.listdir(pwd)

        for directory in list_directory:
            print('[+]', directory)

    def test_04(self):
        counts = Counter()

        '''os.walk is a generator func and returns iterators'''

        for root, directories, files in os.walk('.', topdown=False):

            for file in files:
                print('[+]', os.path.join(root, file))
                first_part, extension = os.path.splitext(file)
                counts[extension] += 1

            for directory in directories:
                print('[++] ', directory)

        for extension, count in counts.items():
            print(f"{extension:8}{count}")


if __name__ == '__main__':
    unittest.main()
