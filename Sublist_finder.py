import random

def find_sublist(sublist, main_list):
    r = []
    L = len(sublist)
    for i in range(len(main_list)):
        if main_list[i:i+L] == sublist:
            r.append(i)
    return r

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
test = [1] #### Set test to have an element to start

while test:
    final_trialsK = list(trialsK)
    random.shuffle(final_trialsK)
    test = find_sublist(['K', 'K', 'K', 'K'], final_trialsK)
    print test

print final_trialsK

for i in xrange(len(final_trialsK)):
    print "%03d:%s" % (i, final_trialsK[i])

# Create list of letters for 'AK' trials
trialsAK = list(_K_list)
trialsAK += 2 * alphaSansK
print trialsAK
test = [1]

while test:
    final_trialsAK = list(trialsAK)
    random.shuffle(final_trialsAK)
    test = find_sublist(['K', 'K', 'K', 'K'], final_trialsAK)
    print test

for i in xrange(len(final_trialsAK)):
    print "%03d:%s" % (i, final_trialsAK[i])
