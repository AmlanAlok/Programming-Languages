import sys
import os
from collections import Counter
import platform
from platform import python_implementation, python_version_tuple
import subprocess
import threading
import time

num_threads = 4


def thread_message(message):
    global num_threads
    num_threads -= 1
    print('Message from thread %s\n' % message)


while num_threads > 0:
    print('I am the %s thread' % num_threads)
    threading.Thread(target=thread_message('I am the %s thread' % num_threads)).start()
    time.sleep(0.1)



# command_ping = '/bin/ping'
# ping_parameter = '-c 1'
# domain = 'google.com'
# p = subprocess.Popen([command_ping, ping_parameter, domain], shell=False, stderr=subprocess.PIPE)
# out = p.stderr.read(1)
# sys.stdout.write(str(out.decode('utf-8')))
# sys.stdout.flush()






# operating_system = platform.system()
# print(operating_system)
#
# if operating_system == 'Darwin':
#     ping_cmd = 'ping -c 127.0.0.1'
#     print(ping_cmd)
#     net_cmd = 'ipconfig getifaddr en1'
#     print(net_cmd)
#
#
# print(python_implementation())
# for attribute in python_version_tuple():
#     print(attribute)



# # print(os.path)
# print('\n')
#
# if len(sys.argv) == 1:
#
#     filename = sys.argv[0]
#     print(filename)
#
#     if os.path.isfile(filename):
#         print('File exists')
#     if not os.path.isfile(filename):
#         print('File does not exist')
#     if not os.access(filename, os.R_OK):
#         print('Access Denied')
#     # exit(0)
# else:
#     print(f"Length is not 2. It is {len(sys.argv)}")


# pwd = os.getcwd()
# print(pwd)
# list_directory = os.listdir(pwd)
#
# for directory in list_directory:
#     print('[+]', directory)


# counts = Counter()
#
# '''os.walk is a generator func and returns iterators'''
#
# for root, directories, files in os.walk('.', topdown=False):
#
#     for file in files:
#         print('[+]', os.path.join(root, file))
#         first_part, extension = os.path.splitext(file)
#         counts[extension] += 1
#
#     for directory in directories:
#         print('[++] ', directory)
#
#
# for extension, count in counts.items():
#     print(f"{extension:8}{count}")
