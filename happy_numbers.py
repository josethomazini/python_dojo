import unittest

'''
A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number either equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for
which this process ends in 1 are happy numbers, while those that do not end in
1 are unhappy numbers (or sad numbers).

For example, 19 is happy, as the associated sequence is:

1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1.

The 143 happy numbers up to 1,000 are:

1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100,
103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226,
230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329,
331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409,
440, 446, 464, 469, 478, 487, 490, 496, 536, 556, 563, 565, 566, 608, 617, 622,
623, 632, 635, 637, 638, 644, 649, 653, 655, 656, 665, 671, 673, 680, 683, 694,
700, 709, 716, 736, 739, 748, 761, 763, 784, 790, 793, 802, 806, 818, 820, 833,
836, 847, 860, 863, 874, 881, 888, 899, 901, 904, 907, 910, 912, 913, 921, 923,
931, 932, 937, 940, 946, 964, 970, 973, 989, 998, 1000

https://en.wikipedia.org/wiki/Happy_number
'''


def happy(num):
    cur_num = num
    proc_nums = []

    while True:
        num_array = [int(c) for c in str(cur_num)]
        cur_total = sum([n ** 2 for n in num_array])
        if len(num_array) == 1 and cur_total in proc_nums:
            return cur_total == 1
        else:
            proc_nums.append(cur_total)
            cur_num = cur_total


class TestHappyNumber(unittest.TestCase):

    def test_one_is_happy(self):
        self.assertTrue(happy(1))

    def test_seven_is_happy(self):
        self.assertTrue(happy(7))

    def test_ten_is_happy(self):
        self.assertTrue(happy(10))

    def test_thirteen_is_happy(self):
        self.assertTrue(happy(13))

    def test_two_is_not_happy(self):
        self.assertFalse(happy(2))

    def test_one_thousand_is_happy(self):
        self.assertTrue(happy(1000))

    def test_battery(self):
        first_one_thousand_numbers = range(1, 1001)
        happies = [
            1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91,
            94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192,
            193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293,
            301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365,
            367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446,
            464, 469, 478, 487, 490, 496, 536, 556, 563, 565, 566, 608, 617,
            622, 623, 632, 635, 637, 638, 644, 649, 653, 655, 656, 665, 671,
            673, 680, 683, 694, 700, 709, 716, 736, 739, 748, 761, 763, 784,
            790, 793, 802, 806, 818, 820, 833, 836, 847, 860, 863, 874, 881,
            888, 899, 901, 904, 907, 910, 912, 913, 921, 923, 931, 932, 937,
            940, 946, 964, 970, 973, 989, 998, 1000
        ]

        unhappies = [n for n in first_one_thousand_numbers if n not in happies]

        for item in happies:
            self.assertTrue(happy(item), '%d should be happy' % item)

        for item in unhappies:
            self.assertFalse(happy(item), '%d should be unhappy' % item)


if __name__ == '__main__':
    unittest.main()
