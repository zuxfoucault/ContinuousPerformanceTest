import random

# coding=utf-8
__author__ = 'Joshua Zosky'


"""
    Copyright 2016 Joshua Zosky
    joshua.e.zosky@gmail.com

    This file is part of "Continuous Performance Test Clinical Software".

    "Continuous Performance Test Clinical Software" is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    "Continuous Performance Test Clinical Software" is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with "Continuous Performance Test Clinical Software".  If not, see <http://www.gnu.org/licenses/>.
"""


def find_sublist(sublist, main_list):
    r = []
    L = len(sublist)
    for i in range(len(main_list)):
        if main_list[i:i + L] == sublist:
            r.append(i)
    return r


def create_stim(verbose=True):
    alphabet = map(chr, range(65, 91))
    alphaSansK = list(alphabet)
    alphaSansAK = list(alphabet)

    alphaSansK.remove('K')  ####Delete K from the list
    alphaSansAK.remove('K')
    alphaSansAK.remove('A')

    # Create static lists for K and A
    _K_list = ["K" for i in xrange(36)]
    _A_list = ["A" for i in xrange(36)]

    # Create list of letters for 'K' trials
    trialsK = list(_K_list)
    trialsK += 3 * alphaSansK
    random.shuffle(alphaSansK)
    # print alphaSansK
    for i in xrange(9):
        trialsK.append(alphaSansK[i])
    test = [1]  #### Set test to have an element to start

    while test:
        final_trialsK = list(trialsK)
        random.shuffle(final_trialsK)
        test = find_sublist(['K', 'K', 'K', 'K'], final_trialsK)
        if verbose:
            print test
    if verbose:
        print final_trialsK
        for i in xrange(len(final_trialsK)):
            print "%03d:%s" % (i, final_trialsK[i])

    # Create list of letters for 'AK' trials
    trialsAK = list(_K_list)
    trialsAK += 2 * alphaSansAK
    if verbose:
        print trialsAK
    test = [1]

    while test:
        pre_final_trialsAK = list(trialsAK)
        random.shuffle(pre_final_trialsAK)
        test = find_sublist(['K', 'K', 'K', 'K'], pre_final_trialsAK)
        if verbose:
            print test

    final_trialsAK = []
    for letter in pre_final_trialsAK:
        if letter is 'K':
            final_trialsAK.append('A')
        final_trialsAK.append(letter)

    if verbose:
        for i in xrange(len(final_trialsAK)):
            print "%03d:%s" % (i, final_trialsAK[i])

    return final_trialsK, final_trialsAK


if __name__ == '__main__':
    create_stim()
