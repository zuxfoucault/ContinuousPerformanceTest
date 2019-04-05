import random

# coding=utf-8
__author__ = 'Joshua Zosky'


"""
    Copyright 2016 Joshua Zosky
    joshua.e.zosky@gmail.com

    This file is part of "Continuous_Performance_Test Clinical Software".

    "Continuous_Performance_Test Clinical Software" is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    "Continuous_Performance_Test Clinical Software" is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with "Continuous_Performance_Test Clinical Software".  If not, see <http://www.gnu.org/licenses/>.
"""


def find_sublist(sublist, main_list):
    r = []
    L = len(sublist)
    for i in range(len(main_list)):
        if main_list[i:i + L] == sublist:
            r.append(i)
    return r


def create_stim(test_type='K', verbose=True):
    if test_type not in ['K', 'AK']:
        print('wrong value for test_type (must be "K" or "AK")')
        return
    alphabet = map(chr, range(65, 91))
    alphaSansK = list(alphabet)
    alphabet = map(chr, range(65, 91))
    alphaSansAK = list(alphabet)

    alphaSansK.remove('K')  ####Delete K from the list
    alphaSansAK.remove('K')
    alphaSansAK.remove('A')

    # Create static lists for K
    target_list = ["K" for i in range(36)]

    if test_type == "K":
        # Create list of letters for 'K' trials
        trials = list(target_list)
        trials += 3 * alphaSansK
        random.shuffle(alphaSansK)
        # print alphaSansK
        for i in range(9):
            trials.append(alphaSansK[i])
        test = [1]  #### Set test to have an element to start

        while test:
            final_trials = list(trials)
            random.shuffle(final_trials)
            test = find_sublist(['K', 'K', 'K', 'K'], final_trials)
            if verbose:
                print(test)
        if verbose:
            print(final_trials)
            for i in range(len(final_trials)):
                print("%03d:%s" % (i, final_trials[i]))
    elif test_type == "AK":
        # Create list of letters for 'AK' trials
        trials = list(target_list)
        trials += 2 * alphaSansAK
        if verbose:
            print(trials)
        test = [1]

        while test:
            pre_final_trials = list(trials)
            random.shuffle(pre_final_trials)
            test = find_sublist(['K', 'K', 'K', 'K'], pre_final_trials)
            if verbose:
                print(test)

        final_trials = []
        for letter in pre_final_trials:
            if letter is 'K':
                final_trials.append('A')
            final_trials.append(letter)

        if verbose:
            for i in range(len(final_trials)):
                print("%03d:%s" % (i, final_trials[i]))

    return final_trials


if __name__ == '__main__':
    create_stim()
