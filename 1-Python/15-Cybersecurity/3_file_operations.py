import unittest
import shutil
import zipfile
import os


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('\n')

    def test_file(self):
        try:
            with open('test.txt', 'w') as file:
                file.write('this is a test file also')
        except IOError as e:
            print('Exception: Unable to write to file')
        except Exception as e:
            print('Another error occurred', e)
        else:
            print('File written to successfully')

    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_zip(self):
        # os.mkdir('cs')

        zf = zipfile.ZipFile('cs.zip', 'w')

        for dirname, subdirs, files in os.walk('cs'):
            zf.write(dirname)
            for filename in files:
                zf.write(os.path.join(dirname, filename))

        zf.close()
        print(dirname)


if __name__ == '__main__':
    unittest.main()
