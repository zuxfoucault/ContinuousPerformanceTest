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
import random

'''
from psychopy import visual, gui, data, core
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'Biomarker Imaging Study'  # from the Builder filename that created this script
expInfo = {u'Gender': u'female', u'Handedness': u'Right', u'participant': u'SKY100'}
# dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
# if not dlg.OK: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup the Window
win = visual.Window(size=(640, 480), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[-1.,-1.,-1.], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

print frameDur
'''
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
'''

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
# print trialsK[-10:-1]
# print trialsK
random.shuffle(trialsK)

final_trialsK = []
for asdf in xrange(100):
    for i in xrange(len(trialsK)/3):
        finished = False
        if len(trialsK) >= 6:
            while not finished:
                if (trialsK[-4:] == ["K"] * 4) or\
                        (trialsK[-5:-1] == ["K"] * 4) or\
                        (trialsK[-6:-2] == ["K"] * 4):
                    random.shuffle(trialsK)
                else:
                    finished = True
                    final_trialsK.extend(trialsK[-3:])
                    del trialsK[-3:]
    test = find_sublist(['K', 'K', 'K'], final_trialsK)

test = find_sublist(['K', 'K', 'K', 'K'], final_trialsK)

print test

for i in xrange(len(final_trialsK)):
    print final_trialsK[i]
'''
'''
# Create list of letters for 'AK' trials
trialsAK = list(_K_list)
trialsAK += 2 * alphaSansK
print trialsAK
random.shuffle(trialsAK)

final_trialsAK = []
trialsAK.extend(['K','N','X','K','K','K'])

for i in xrange((len(trialsAK)+36)/3):
    finished = False
    if len(trialsAK) >= 6:
        while not finished:
            if (trialsAK[-4:] == ["K"] * 4) or\
                    (trialsAK[-5:-1] == ["K"] * 4) or\
                    (trialsAK[-6:-2] == ["K"] * 4):
                random.shuffle(trialsAK)
            elif len(final_trialsAK) >= 3:
                if ((trialsAK[-3] == ["K"]) and (final_trialsAK[-3:] == ["K"] * 3)) or\
                        ((trialsAK[-3:-1] == ["K"] * 2) and (final_trialsAK[-2:] == ["K"] * 2)) or\
                        ((trialsAK[-3:] == ["K"] * 3) and (final_trialsAK[-1] == ["K"])):
                    random.shuffle(trialsAK)
            else:
                finished = True
                final_trialsAK.extend(trialsAK[-3:])
                del trialsAK[-3:]


for i in xrange(len(final_trialsAK)):
    print final_trialsAK[i]
'''

quit()

Letter_CPT_K = visual.TextStim(win=win, ori=0, name='Letter_CPT_X',
                               text='default text', font='Arial',
                               pos=[0, 0], height=0.5, wrapWidth=None,
                               color='white', colorSpace='rgb', opacity=1,
                               depth=0.0)
print visual.getMsPerFrame(myWin=win)
for i in xrange(len(trialsK)):
    Letter_CPT_K.setText(trialsK[i])
    Letter_CPT_K.draw()
    win.flip()
    print win.fps()
    core.wait(.5)
    win.flip(clearBuffer=True)
    core.wait(.5)
    print win.fps()
