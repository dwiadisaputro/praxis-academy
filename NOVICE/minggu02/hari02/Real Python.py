# assert sum([1, 2, 3]) == 6, "Should be 6"
# assert sum([1, 1, 1]) == 6, "Should be 6"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError: Should be 6

##menyiapkan file test_sum.py terlebih dahulu pada directory, dan masukkan script dibawah ini:
# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"

# if __name__ == "__main__":
#     test_sum()
#     print("Everything passed")

##menyiapkan file test_sum_2.py terlebih dahulu dengan script dibawah ini:
# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"

# def test_sum_tuple():
#     assert sum((1, 2, 2)) == 6, "Should be 6"

# if __name__ == "__main__":
#     test_sum()
#     test_sum_tuple()
#     print("Everything passed")




##menyiapkan file test_sum_unittest.py terlebih dahulu dengan script dibawah ini:
# import unittest


# class TestSum(unittest.TestCase):

#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

# if __name__ == '__main__':
#     unittest.main()


##---Instal nose terlebih dahulu--
# pip install nose2
##--- hasilnya
# Collecting nose2
#   Downloading nose2-0.11.0-py2.py3-none-any.whl (144 kB)
#      |████████████████████████████████| 144 kB 126 kB/s 
# Requirement already satisfied: six>=1.7 in /usr/lib/python3/dist-packages (from nose2) (1.14.0)
# Collecting coverage>=4.4.1
#   Downloading coverage-6.3.2-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (212 kB)
#      |████████████████████████████████| 212 kB 10 kB/s 
# Installing collected packages: coverage, nose2
# Successfully installed coverage-6.3.2 nose2-0.11.0


# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"

# def test_sum_tuple():
#     assert sum((1, 2, 2)) == 6, "Should be 6"


# def sum(arg):
#     total = 0
#     for val in arg:
#         total += val
#     return total


# import unittest

# from my_sum import sum


# class TestSum(unittest.TestCase):
#     def test_list_int(self):
#         """
#         Test that it can sum a list of integers
#         """
#         data = [1, 2, 3]
#         result = sum(data)
#         self.assertEqual(result, 6)

# if __name__ == '__main__':
#     unittest.main()

####---catatan hasilnya---
####---tes masukkan '$ python3 -m unittest test--
# #--hasilnya--
## blk@blk-HP-Pavilion-Gaming-Laptop-15-dk1xxx:~/Adi$ python3 -m unittest test

## ----------------------------------------------------------------------
## Ran 0 tests in 0.000s

## OK

####---tes masukkan '$ python3 -m unittest -v test--
# #--hasilnya--
# blk@blk-HP-Pavilion-Gaming-Laptop-15-dk1xxx:~/Adi$ python3 -m unittest -v test

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK


####---tes masukkan '$ python3 -m unittest discover--
# blk@blk-HP-Pavilion-Gaming-Laptop-15-dk1xxx:~/Adi$ python3 -m unittest discover

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK

####---tes masukkan '$ python3 -m unittest discover -s tests--
# blk@blk-HP-Pavilion-Gaming-Laptop-15-dk1xxx:~/Adi$ python3 -m unittest discover -s test
# .....................s.....................
# ----------------------------------------------------------------------
# Ran 43 tests in 2.980s

# OK (skipped=1)

# import unittest
# from my_sum import sum
# from fraction import Fraction

# class TestSum(unittest.TestCase):
#     def test_list_int(self):
#         """ Test that it can sum a list of integers """
#         data = [1, 2, 3]
#         result = sum(data)
#         self.assertEqual(result, 6)
    
#     def test_list_fraction(self): """ Test that it can sum a list of fractions """
#     data = [Fraction(1,4), fraction(2, 5)]
#     result = sum(data)
#     self.assertEqual(result, 1)
# if __name__ == '__main__':
#     unittest.main()
##jika dijalankan di terminal akan : python3 -m unittest coba(sesuai nama filenya)
"""
FF
======================================================================
FAIL: test_list_fraction (coba.TestSum)
Test that it can sum a list of fraction
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/blk/Adi/NOVICE/minggu02/hari02/project/coba.py", line 20, in test_list_fraction
    self.assertEqual(result, 1)
AssertionError: None != 1

======================================================================
FAIL: test_list_int (coba.TestSum)
Test that it can sum a list of integers
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/blk/Adi/NOVICE/minggu02/hari02/project/coba.py", line 12, in test_list_int
    self.assertEqual(result, 6)
AssertionError: None != 6

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=2)
"""