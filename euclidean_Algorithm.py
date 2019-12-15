# Author: Ryan Habershaw
# Date: 02 December, 2019
#
# Purpose: This program will mimic the Euclidean algorithm and solve a few examples
#          using the steps of said algorithm.


def euclidean(b, a):
    q = 0
    r = 1

    while r != 0:
        q = b // a
        r = b % a

        print('%s = %s(%s) + %s' % (b, a, q, r))
        print()

        b = a
        a = r

    return

/Users/ryanhabershaw/PycharmProjects/euclidean_Algorithm/euclidean_Algorithm.py
euclidean(247, 117)
euclidean(465, 165)
euclidean(76, 123)




