from psychopy import gui
from psychopy.core import quit
from psychopy.data import getDateStr
from psychopy.logging import log, info
import stim_generator


def test_info_gui(test_type='K'):
    if test_type not in ['K', 'AK']:
        log('Invalid value for test_type (supplied: {0}). Must be "K" or "AK".)'.format(test_type), info)
        quit()
    test_info = {'# of Runs': u''}
    dlg = gui.DlgFromDict(dictionary=test_info, title='TEST {0}'.format(test_type))
    if not dlg.OK:
        log('User pressed cancel', info)
        quit()  # user pressed cancel
    try:
        n_test = int(test_info['# of Runs'])
    except ValueError:
        log('User entered non-integer value "{0}" for {1} test'.format(test_info['# of Runs'], test_type), info)
        quit()
    if n_test < 0:
        log('User entered negative number for {0} test'.format(test_type), info)
        quit()
    log('User requests {0} round(s) of the {1} test'.format(n_test, test_type), info)
    return n_test


def experiment_info_gui(expName):
    # Store info about the experiment session
    expInfo = {u'Sex': u'female',
               u'Handedness': u'Right',
               u'Participant': u'001',
               u'Session': u'1',
               u'Age': u'18',
               u'Years of completed education': u'12',
               u'Activity Level': u'(1=low, 2=med, 3=hi)'}
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    if not dlg.OK:
        quit()  # user pressed cancel
    expInfo['date'] = getDateStr()
    expInfo['expName'] = expName
    return expInfo


def generate_stimuli(test_type, n_rounds):
    return_list = []
    if n_rounds == 0:
        return return_list
    # create all trials for each paradigm
    for n_rounds in xrange(n_rounds):
        return_list.append(stim_generator.create_stim(test_type))
    return return_list


def get_info(experiment_name=u'Continuous Performance Task'):
    n_k = test_info_gui(test_type='K')
    n_ak= test_info_gui(test_type='AK')
    exp_info = experiment_info_gui(experiment_name)
    k_list = generate_stimuli('K', n_k)
    ak_list = generate_stimuli('AK', n_ak)
    return {'K': k_list, 'AK': ak_list}, exp_info
