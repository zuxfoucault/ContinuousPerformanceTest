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

from psychopy import visual, gui, data, core, event
import os  # handy system and path functions
import stim_generator

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

stim_list_1, stim_list_2 = stim_generator.create_stim(verbose=False)

print stim_list_1, stim_list_2

Stim_letter = visual.TextStim(win=win, ori=0, name='Letter_CPT_X',
                               text='default text', font='Arial',
                               pos=[0, 0], height=0.5, wrapWidth=None,
                               color='white', colorSpace='rgb', opacity=1,
                               depth=0.0)
print visual.getMsPerFrame(myWin=win)
trial_wait = core.StaticPeriod(screenHz=60)
trial_clock = core.Clock()
trial_data = []
stim_list_1 = stim_list_1[:10]
stim_list_2 = stim_list_2[:10]
hits = []
false_alarms = []
miss = []
cor_rej = []
all_data = [hits, false_alarms, miss, cor_rej]

for stim_list in (stim_list_1, stim_list_2):
    trial_counter = 0
    for stim in stim_list:
        trial_counter += 1
        Stim_letter.setText(stim)
        Stim_letter.draw()
        win.flip()
        trial_clock.reset()
        trial_wait.start(.5)
        trial_wait.complete()
        win.flip(clearBuffer=True)
        trial_response = event.getKeys(timeStamped=trial_clock)
        trial_data.append((stim, trial_response, trial_counter))
        if trial_response and stim == 'K':
            hits.append(trial_data[-1])
        elif trial_response and stim != 'K':
            false_alarms.append(trial_data[-1])
        elif not trial_response and stim == 'K':
            miss.append(trial_data[-1])
        elif not trial_response and stim != 'K':
            cor_rej.append(trial_data[-1])
        else:
            print "What happened with %s" % trial_data[-1]
        core.wait(.1)
    print trial_data
    Stim_letter.setText("Next list")
    Stim_letter.draw()
    win.flip()
    core.wait(2)
    win.flip(clearBuffer=True)

for i in all_data:
    print i

'''
for trial_info in trial_data:
    trial_letter, trial_response, trial_number = trial_info
    if trial_response and trial_letter == 'K':
        hits.append((trial_number, trial_response))
    elif trial_response and trial_letter != 'K':
        false_alarms.append((trial_number, trial_response))

print hits
print false_alarms
'''