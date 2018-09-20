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

from psychopy import visual, gui, data, core, event
import os
import stim_generator
import CPT_data


# Settings
# Set to trial duration, 60 frames = 1sec @ 60hz
trial_frames = 5
inter_stimulus_interval = 54


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'Biomarker Imaging Study'  # from the Builder filename that created this script
expInfo = dict(Gender=u'female', Handedness=u'Right', Participant=u'0001')
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if not dlg.OK:
    core.quit()  # user pressed cancel
expInfo['date']=data.getDateStr()
expInfo['expName']=expName
expInfo['troubleshooting']='' #1

# Setup the Window
win = visual.Window(size=(640, 480), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
                    monitor=u'testMonitor', color=[-1., -1., -1.], colorSpace='rgb',
                    blendMode='avg', useFBO=True)
instructions_K = "This is a test of concentration. You will be asked to hit the space bar each time you see the letter K. When you see the letter K, press the space bar as quickly as you can. First, the computer will count down from 5 to 1. Then you will see a series of letters on the screen. Remember, press the space bar only when you see the letter K. Do you have any questions?" \
                 "\n\n\n\nPress space bar when you are ready to begin."
instructions_AK = "This is a test of concentration. You will be asked to hit the space bar each time you see the letter K, but only if the letter K was immediately preceded by the letter A. In other words, press the space bar if A comes right before K. When you see the letter K, press the space bar as quickly as you can. First, the computer will count down from 5 to 1. Then you will see a series of letters on the screen. Remember, press the space bar only when you see the letter K. Do you have any questions?" \
                  "\n\n\n\nPress space bar when you are ready to begin."
quit_instructions = "Are you sure you want to quit? All data will be lost.\n\nPress Q to quit. Press any key to return."
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate']:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # couldn't get a reliable measure so guess

print frameDur

stim_list_K_1, stim_list_AK_1 = stim_generator.create_stim(verbose=False)
stim_list_K_2, stim_list_AK_2 = stim_generator.create_stim(verbose=False)
stim_list_K_3, stim_list_AK_3 = stim_generator.create_stim(verbose=False)
stim_list_K_4, stim_list_AK_4 = stim_generator.create_stim(verbose=False)

#print len(stim_list_1), len(stim_list_2)

Stim_letter = visual.TextStim(win=win, ori=0, name='Letter_CPT_X',
                              text='default text', font='Arial',
                              pos=[0, 0], height=0.2, wrapWidth=None,
                              color='white', colorSpace='rgb', opacity=1,
                              depth=0.0)
Instructions_Screen = visual.TextStim(win=win, ori=0, name='Instructions',
                                      text=instructions_K, font='Arial',
                                      pos=[0, 0], height=0.09, wrapWidth=None,
                                      color='white', colorSpace='rgb', opacity=1,
                                      depth=0.0)
Quit_Screen = visual.TextStim(win=win, ori=0, name='Instructions',
                              text=quit_instructions, font='Arial',
                              pos=[0, 0], height=0.09, wrapWidth=None,
                              color='white', colorSpace='rgb', opacity=1,
                              depth=0.0)
End_Screen = visual.TextStim(win=win, ori=0, name='Instructions',
                             text="This concludes the study. Let the researcher know you're done."
                                  "\n\nPress any key to end experiment.", font='Arial',
                             pos=[0, 0], height=0.09, wrapWidth=None,
                             color='white', colorSpace='rgb', opacity=1,
                             depth=0.0)

# print visual.getMsPerFrame(myWin=win)
trial_wait = core.StaticPeriod(screenHz=60)
trial_clock = core.Clock()

# Troubleshooting
if expInfo['troubleshooting'] == 1:
    stim_list_K_1 = stim_list_K_1[:5]
    stim_list_K_2 = stim_list_K_2[:5]
    stim_list_K_3 = stim_list_K_3[:5]
    stim_list_K_4 = stim_list_K_4[:5]
    stim_list_AK_1 = stim_list_AK_1[:5]
    stim_list_AK_2 = stim_list_AK_2[:5]
    stim_list_AK_3 = stim_list_AK_3[:5]
    stim_list_AK_4 = stim_list_AK_4[:5]
# Troubleshooting

K_stim_lists = (stim_list_K_1, stim_list_K_2, stim_list_K_3, stim_list_K_4)
AK_stim_lists = (stim_list_AK_1, stim_list_AK_2, stim_list_AK_3, stim_list_AK_4)

K_block = 0
AK_block = 0

for stim_list in (stim_list_K_1,
                  stim_list_K_2,
                  stim_list_K_3,
                  stim_list_K_4,
                  stim_list_AK_1,
                  stim_list_AK_2,
                  stim_list_AK_3,
                  stim_list_AK_4):
    trial_counter = 0
    hits = []
    false_alarms = []
    miss = []
    cor_rej = []
    error_commission = []
    all_data = [hits, false_alarms, miss, cor_rej, error_commission]
    n_trials = len(stim_list)
    if stim_list in K_stim_lists:
        K_block += 1
        task_name = 'K Trials %s' % K_block
        file_path = CPT_data.create_data_file(expInfo, task_name)
        if K_block == 1:
            overall_data_list = []
            std_list = []
            Instructions_Screen.draw()
            win.flip()
            event.waitKeys()
            for i in xrange(5,0, -1):
                i = "%s" % i
                Stim_letter.setText(i)
                Stim_letter.draw()
                win.flip()
                core.wait(.08)
                win.flip()
                core.wait(.9)
    elif stim_list in AK_stim_lists:
        AK_block += 1
        task_name = 'A-K Trials %s' % AK_block
        file_path = CPT_data.create_data_file(expInfo, task_name)
        if AK_block == 1:
            overall_data_list = []
            std_list = []
            Instructions_Screen.setText(instructions_AK)
            Instructions_Screen.draw()
            win.flip()
            event.waitKeys()
            for i in xrange(5,0, -1):
                i = "%s" % i
                Stim_letter.setText(i)
                Stim_letter.draw()
                win.flip()
                core.wait(.08)
                win.flip()
                core.wait(.9)
    else:
        quit()
    for stim in stim_list:
        trial_data = []
        response = 'None'
        response_time = 0
        trial_counter += 1
        Stim_letter.setText(stim)
        Stim_letter.draw()
        event.clearEvents('keyboard')
        win.callOnFlip(trial_clock.reset)
        win.flip()
        #
        # trial_wait.start(1)
        frameN = 0
        trial_wait = True
        while trial_wait:
            frameN += 1
            #print frameN
            if frameN <= trial_frames:
                Stim_letter.draw()
            else:
                win.clearBuffer()
            trial_response = event.getKeys()
            if trial_response:
                response = trial_response[0]
                response_time = trial_clock.getTime()
                if "escape" in trial_response:
                    win.flip()
                    Quit_Screen.draw()
                    win.flip()
                    esc_key = event.waitKeys()
                    if esc_key[0] in ('Q', 'q'):
                        quit()
            if frameN > (trial_frames + inter_stimulus_interval):
                trial_wait = False
            if trial_wait:
                win.flip()
        # trial_wait.complete()
        #
        win.flip()
        win.flip()
        #
        trial_data.extend([stim, response, response_time, trial_counter])
        #  Participant number
        #  Trial number
        #  Task
        #  Letter
        #  Correct Response
        #  Response
        #  Correct
        #  Accuracy
        #  Response Time
        #  Trial time
        #  Trial Type
        if response != 'None':
            if stim == 'K':
                correct_response = 1
                correct = 1
                trial_type = 1
                trial_data.extend([correct_response, correct, trial_type])
                hits.append(tuple(trial_data))
            elif task_name[0] == 'A':
                if response and stim == 'A':
                    correct_response = 0
                    correct = 0
                    trial_type = 5
                    trial_data.extend([correct_response, correct, trial_type])
                    error_commission.append(tuple(trial_data))
                elif stim != 'K':
                    correct_response = 0
                    correct = 0
                    trial_type = 2
                    trial_data.extend([correct_response, correct, trial_type])
                    false_alarms.append(tuple(trial_data))
            elif stim != 'K':
                correct_response = 0
                correct = 0
                trial_type = 2
                trial_data.extend([correct_response, correct, trial_type])
                false_alarms.append(tuple(trial_data))
        elif response == 'None':
            if stim == 'K':
                correct_response = 1
                correct = 0
                trial_type = 3
                trial_data.extend([correct_response, correct, trial_type])
                miss.append(tuple(trial_data))
            elif stim != 'K':
                correct_response = 0
                correct = 1
                trial_type = 4
                trial_data.extend([correct_response, correct, trial_type])
                cor_rej.append(tuple(trial_data))
        else:
            print "What happened with %s" % trial_data[-1]
        #
        #
        CPT_data.write_data(file_path, [expInfo['Participant'],
                                        trial_counter,
                                        task_name,
                                        stim,
                                        correct_response,
                                        response,
                                        correct,
                                        1,
                                        response_time,
                                        1,
                                        trial_type])
        #  Participant number
        #  Trial number
        #  Task
        #  Letter
        #  Correct Response
        #  Response
        #  Correct
        #  Accuracy
        #  Response Time
        #  Trial time
        #  Trial Type
        core.wait(.2)
    summary_file = CPT_data.create_data_file(expInfo, "%s Block Summary" % task_name, header="Participant number,"
                                                                                       "Hits,"
                                                                                       "Hits Proportion,"
                                                                                       "Hits RT,"
                                                                                       "False Alarms,"
                                                                                       "False Alarms Proportion,"
                                                                                       "False Alarms RT,"
                                                                                       "Misses,"
                                                                                       "Misses Proportion,"
                                                                                       "Misses RT,"
                                                                                       "Correct Rejections,"
                                                                                       "Correct Rejections Proportion,"
                                                                                       "Correct Rejections RT,"
                                                                                       "Errors of Commission,"
                                                                                       "Errors of Commission Proportion,"
                                                                                       "Errors of Commission RT")
    averages_list = [expInfo['Participant']]
    for dataType in all_data:
        nDataType = float(len(dataType))
        dataToAvg = 0.0
        respTimeToAvg = 0.0
        nRespTimes = 0.0
        for dataTuple in dataType:
            if dataTuple[2]:
                nRespTimes += 1
                respTimeToAvg += dataTuple[2]
        if nDataType:
            avgData = nDataType / float(36)
        else:
            avgData = 0
        if respTimeToAvg:
            avgDataRT = respTimeToAvg / nRespTimes
        else:
            avgDataRT = 0
        averages_list.extend([nDataType, avgData, avgDataRT])
    std_list.append(averages_list[2])
    if overall_data_list == []:
        overall_data_list.extend(averages_list)
    else:
        for i in xrange(1, len(averages_list)):
            overall_data_list[i] += averages_list[i]
            if i in (2,3,5,6,8,9,11,12,14,15):
                if averages_list[i] != 0:
                    overall_data_list[i] /= 2
    CPT_data.write_data(summary_file, averages_list)
    if int(task_name[-1]) == 2:
        half_summary_file = CPT_data.create_data_file(expInfo, "%s Half-Task Summary" % task_name, header="Participant number,"
                                                                                           "Hits,"
                                                                                           "Hits Proportion,"
                                                                                           "Hits RT,"
                                                                                           "False Alarms,"
                                                                                           "False Alarms Proportion,"
                                                                                           "False Alarms RT,"
                                                                                           "Misses,"
                                                                                           "Misses Proportion,"
                                                                                           "Misses RT,"
                                                                                           "Correct Rejections,"
                                                                                           "Correct Rejections Proportion,"
                                                                                           "Correct Rejections RT,"
                                                                                           "Errors of Commission,"
                                                                                           "Errors of Commission Proportion,"
                                                                                           "Errors of Commission RT")
        CPT_data.write_data(half_summary_file, overall_data_list)
    elif int(task_name[-1]) == 4:
        half_summary_file = CPT_data.create_data_file(expInfo, "%s Task Summary" % task_name, header="Participant number,"
                                                                                       "Hits,"
                                                                                       "Hits Proportion,"
                                                                                       "Hits RT,"
                                                                                       "False Alarms,"
                                                                                       "False Alarms Proportion,"
                                                                                       "False Alarms RT,"
                                                                                       "Misses,"
                                                                                       "Misses Proportion,"
                                                                                       "Misses RT,"
                                                                                       "Correct Rejections,"
                                                                                       "Correct Rejections Proportion,"
                                                                                       "Correct Rejections RT,"
                                                                                       "Errors of Commission,"
                                                                                       "Errors of Commission Proportion,"
                                                                                       "Errors of Commission RT,"
                                                                                       "Standard Deviation of Hits Proportion")
        trial_std = CPT_data.standard_deviation(std_list, population=True)
        overall_data_list.append(trial_std)
        CPT_data.write_data(half_summary_file, overall_data_list)
    #print trial_data
    #Stim_letter.setText("Next list")
    #Stim_letter.draw()
    #win.flip()
    #event.waitKeys()
    win.flip()

End_Screen.draw()
win.flip()
event.waitKeys()
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