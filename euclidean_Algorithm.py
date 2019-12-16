# Author: Ryan Habershaw
# Date: 02 December, 2019
#
# Purpose: This program will mimic the Euclidean algorithm and solve a few examples
#          using the steps of said algorithm.


def euclidean(b, a):  # I decided to use a function so that the user would not have to
    r = 1             # constantly open the program after running it.

    while r != 0:   # This while loop is the central piece of the program. It
        q = b // a  # stops running when 'r' = 0.
        r = b % a

        print('%s = %s(%s) + %s' % (b, a, q, r))  # Uses older style Python print formatting
                                                  # because that is what I know best.

        if r <= 0: print('Finished! The GCD is: %s \n' % a)  # Without this the output looks terrible.

        b = a  # These two lines allow successive steps of the algorithm to run.
        a = r

    return


euclidean(247, 117)  # Calls to my function, this makes testing much easier.
euclidean(465, 165)
euclidean(76, 123)
