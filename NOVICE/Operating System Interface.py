# import os
###--Operating System Interface
# print(os.getcwd())
# print(os.chdir('/Home/Adi/NOVICE/sound'))
# print(os.system('mkdir sounds'))

# print(dir(os))
# print(help(os))

# import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/Home/Adi', 'baru')


###--file Wildcards
# import glob
# print(glob.glob('*.py'))

###--Command Line Arguments
# import sys
# print(sys.argv)

# import argparse
# parser = argparse.ArgumentParser(
#     prog='top',
#     description='Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--line', type=int, default=10)
# args = parser.parse_args()
# print(args)

###---Error Output Redirection and Program Termination
# import sys
# sys.stderr.write('Warning, log file not found starting a new one\n')

###---String Patter Matching
# import re
# print(re.findall(r'\bs[a-z]*', 'which knife or blade fell sharpst'))   ##bs (mengeluarkan kata yang berawalan huruf 's')
# print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))   ##bf => digunakan untuk mencari awalan kata yang berawal huruf 'f')
# print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
# print('teh kita untuk'.replace('untuk', 'berdua'))

###--mathematics
# import math
# print(math.cos(math.pi / 4))
# print(math.log(1024, 2))

# import random
# print(random.choice(['apple', 'pear', 'banana']))
# print(random.sample(range(100), 10))
# print(random.random())
# print(random.randrange(6))

# import statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.variance(data))

# from urllib.request import urlopen
# with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
#     for line in response:
#         line = line.decode()
#         if line.startswith('datetime'):
#             print(line.rstrip())

# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('asmbrt@gmail.com', 'adisaputrodwi27@gmail.com',
# """To: adisaputrodwi27@gmail.com
# From: asmbrt@gmail.com

# # Beware the Ides of March.
# # """)
# print(server.quit())

###---Date and Times
# from datetime import date
# now = date.today()
# print(now)
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# birthday = date(1996, 6, 27)
# age = now - birthday
# print(age.days)


###---Data Compression
# import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))

# t = zlib.compress(s)
# print(len(t))

# print(zlib.decompress(t))
# print(zlib.crc32(s))


###----- Performance Measurement
# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())

###---Quality Control
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)
import doctest


import unittest
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
unittest.main()