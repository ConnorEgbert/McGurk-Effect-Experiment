#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.5),
    on Mon Apr  1 13:30:42 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.5'
expName = 'Experiment'  # from the Builder filename that created this script
expInfo = {'participant': '0', 'session': '01'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/x/Documents/McGurk-Effect-Experiment/Experiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='Black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
Intro_text = visual.TextStim(win=win, name='Intro_text',
    text='Listen or watch for what is being said.\n\nSelect the option that best fits the stimulus.\n\nPress space to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
options = ["BA", "DA", "GA"]

# Don't touch these unless you know what you're doing.
debug = False
win.recordFrameIntervals = False
win.waitBlanking = False


# Initialize components for Routine "Intro_2"
Intro_2Clock = core.Clock()
Intro_2_text = visual.TextStim(win=win, name='Intro_2_text',
    text='Wait for the speaker to finish.\nPress b if the speaker says "BA".\nPress d if the speaker says "DA".\nPress g if the speaker says "GA".\n\nPress space to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Video_intro"
Video_introClock = core.Clock()
video_intro_text = visual.TextStim(win=win, name='video_intro_text',
    text='This marks the begining of the visual section.\nWatch the video and respond accordingly.\n\nPress space to begin.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Video_Tuning"
Video_TuningClock = core.Clock()
accuracy = 0
target_accuracy = .5
noise_level = 0
minimum_iterations = 10

margin_of_error = .05

noise = visual.NoiseStim(
    win,
    noiseType="white",
    noiseElementSize=.1,
    opacity=.5,
    size=(2,2)
)
video_stimulus = visual.MovieStim3(
    win=win, name='video_stimulus',units='norm', 
    noAudio = True,
    filename='GA.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(2, 2),
    depth=-1.0,
    )
prompt = visual.TextStim(win=win, name='prompt',
    text='What was said:\nBA, DA, or GA?\nPress B, D, or G.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Audio_intro"
Audio_introClock = core.Clock()
audio_intro_text = visual.TextStim(win=win, name='audio_intro_text',
    text='This marks the begining of the audio section.\nListen to the audio and respond accordingly.\n\nPress space to begin.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Audio_Tuning"
Audio_TuningClock = core.Clock()
accuracy = 0
target_accuracy = .5
noise_level = 0
minimum_iterations = 10

margin_of_error = .05
Audio_from_video_file = visual.MovieStim3(
    win=win, name='Audio_from_video_file',
    noAudio = False,
    filename='GA.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(0, 0),
    depth=-1.0,
    )
audio_text = visual.TextStim(win=win, name='audio_text',
    text='Listen for audio.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Test_intro"
Test_introClock = core.Clock()
intro_test_text = visual.TextStim(win=win, name='intro_test_text',
    text='Now audio and video will be combined.\nWatch the video and respond accordingly.\n\nPress space to begin.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Testing"
TestingClock = core.Clock()
debug = True
accuracy = 0
target_accuracy = .5
noise_level = 0
minimum_iterations = 10

margin_of_error = .05
test_video = visual.MovieStim3(
    win=win, name='test_video',units='norm', 
    noAudio = True,
    filename='BA.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(2, 2),
    depth=-1.0,
    )
test_text = visual.TextStim(win=win, name='test_text',
    text='How many trials had speakers that did not match the video?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Outro"
OutroClock = core.Clock()
Outro_text = visual.TextStim(win=win, name='Outro_text',
    text='This concludes the experiment.',
    font='Arial',
    pos=(0, 0), height=.1, wrapWidth=10, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro"-------
t = 0
IntroClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()

# keep track of which components have finished
IntroComponents = [Intro_text, key_resp_2]
for thisComponent in IntroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Intro"-------
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro_text* updates
    if t >= 0.0 and Intro_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Intro_text.tStart = t
        Intro_text.frameNStart = frameN  # exact frame index
        Intro_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()

# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro_2"-------
t = 0
Intro_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
Intro_2Components = [Intro_2_text, key_resp_3]
for thisComponent in Intro_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Intro_2"-------
while continueRoutine:
    # get current time
    t = Intro_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro_2_text* updates
    if t >= 0.0 and Intro_2_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Intro_2_text.tStart = t
        Intro_2_text.frameNStart = frameN  # exact frame index
        Intro_2_text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro_2"-------
for thisComponent in Intro_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Intro_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Video_intro"-------
t = 0
Video_introClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
Video_introComponents = [video_intro_text, key_resp_5]
for thisComponent in Video_introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Video_intro"-------
while continueRoutine:
    # get current time
    t = Video_introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *video_intro_text* updates
    if t >= 0.0 and video_intro_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        video_intro_text.tStart = t
        video_intro_text.frameNStart = frameN  # exact frame index
        video_intro_text.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Video_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Video_intro"-------
for thisComponent in Video_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys=None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "Video_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Video_Tuning"-------
t = 0
Video_TuningClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
from psychopy import core
import random

output_stim = video_stimulus

def start_video(video_file, noise_level):
    output_stim.setMovie(video_file)
    output_stim.seek(0)
    output_stim.play()
    while output_stim.status != visual.FINISHED:
        output_stim.draw()
        noise.draw()
        win.flip()
        noise.updateNoise()

## Setup Section
iteration_count = 0
target_met = False

subject_video_answers = [[] for x in range(len(options))]

## Experiment Section
while iteration_count < minimum_iterations:
    # Select a stimulus from the list of files
    correct_answer_index = random.randint(0, len(options)-1)
    correct_answer = options[correct_answer_index]
    test_file = correct_answer + ".mov"
    correct_answer = correct_answer[0].lower()
    
    # Play the video
    start_video(test_file, noise_level)
    
    # Get response
    prompt.draw()
    win.flip()
    
    # Read a character
    c = event.waitKeys()
    if c[0] == correct_answer:
        subject_video_answers[correct_answer_index].append(1)
        noise_level += 1
        accuracy += 1
    elif c[0] == 'space':
        break
    else:
        subject_video_answers[correct_answer_index].append(0)
        noise_level -= 1
    iteration_count += 1
# keep track of which components have finished
Video_TuningComponents = [video_stimulus, prompt]
for thisComponent in Video_TuningComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Video_Tuning"-------
while continueRoutine:
    # get current time
    t = Video_TuningClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *video_stimulus* updates
    if t >= 0.0 and video_stimulus.status == NOT_STARTED:
        # keep track of start time/frame for later
        video_stimulus.tStart = t
        video_stimulus.frameNStart = frameN  # exact frame index
        video_stimulus.setAutoDraw(True)
    frameRemains = 0.0 + 0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if video_stimulus.status == STARTED and t >= frameRemains:
        video_stimulus.setAutoDraw(False)
    
    # *prompt* updates
    if t >= 0.0 and prompt.status == NOT_STARTED:
        # keep track of start time/frame for later
        prompt.tStart = t
        prompt.frameNStart = frameN  # exact frame index
        prompt.setAutoDraw(True)
    frameRemains = 0.0 + 0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if prompt.status == STARTED and t >= frameRemains:
        prompt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Video_TuningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Video_Tuning"-------
for thisComponent in Video_TuningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
for index, option in enumerate(subject_video_answers):
    try:
        print(options[index] + " average: %" + str(sum(option)/len(option) * 100))
    except:
        pass

# the Routine "Video_Tuning" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Audio_intro"-------
t = 0
Audio_introClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()
# keep track of which components have finished
Audio_introComponents = [audio_intro_text, key_resp_6]
for thisComponent in Audio_introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Audio_intro"-------
while continueRoutine:
    # get current time
    t = Audio_introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *audio_intro_text* updates
    if t >= 0.0 and audio_intro_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        audio_intro_text.tStart = t
        audio_intro_text.frameNStart = frameN  # exact frame index
        audio_intro_text.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Audio_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Audio_intro"-------
for thisComponent in Audio_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys=None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "Audio_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Audio_Tuning"-------
t = 0
Audio_TuningClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
from psychopy import core
import random

output_stim = Audio_from_video_file

def start_video(video_file, noise_level):
    output_stim.setMovie(video_file)
    output_stim.seek(0)
    output_stim.play()
    
    data = np.random.uniform(-1,1,44100)
    white_noise = sound.Sound("chatter.wav")
    white_noise.play()
    
    while output_stim.status != visual.FINISHED:
        audio_text.draw()
        output_stim.draw()
        win.flip()

    white_noise.stop()

## Setup Section
iteration_count = 0
target_met = False

subject_audio_answers = [[] for x in range(len(options))]

## Experiment Section
while iteration_count < minimum_iterations:
    # Select a stimulus from the list of files
    correct_answer_index = random.randint(0, len(options)-1)
    correct_answer = options[correct_answer_index]
    test_file = correct_answer + ".mov"
    correct_answer = correct_answer[0].lower()
    
    # Play the video
    start_video(test_file, noise_level)
    
    # Get response
    prompt.draw()
    win.flip()
    
    # Read a character
    c = event.waitKeys()
    if c[0] == correct_answer:
        subject_audio_answers[correct_answer_index].append(1)
        noise_level += 1
        accuracy += 1
    elif c[0] == 'space':
        break
    else:
        subject_audio_answers[correct_answer_index].append(0)
        noise_level -= 1
    iteration_count += 1

# keep track of which components have finished
Audio_TuningComponents = [Audio_from_video_file, audio_text]
for thisComponent in Audio_TuningComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Audio_Tuning"-------
while continueRoutine:
    # get current time
    t = Audio_TuningClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *Audio_from_video_file* updates
    if t >= 0.0 and Audio_from_video_file.status == NOT_STARTED:
        # keep track of start time/frame for later
        Audio_from_video_file.tStart = t
        Audio_from_video_file.frameNStart = frameN  # exact frame index
        Audio_from_video_file.setAutoDraw(True)
    frameRemains = 0.0 + 0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Audio_from_video_file.status == STARTED and t >= frameRemains:
        Audio_from_video_file.setAutoDraw(False)
    
    # *audio_text* updates
    if t >= 0.0 and audio_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        audio_text.tStart = t
        audio_text.frameNStart = frameN  # exact frame index
        audio_text.setAutoDraw(True)
    frameRemains = 0.0 + 0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if audio_text.status == STARTED and t >= frameRemains:
        audio_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Audio_TuningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Audio_Tuning"-------
for thisComponent in Audio_TuningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
for index, option in enumerate(subject_audio_answers):
    try:
        print(options[index] + " average: %" + str(sum(option)/len(option) * 100))
    except:
        pass
# the Routine "Audio_Tuning" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Test_intro"-------
t = 0
Test_introClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
Test_introComponents = [intro_test_text, key_resp_7]
for thisComponent in Test_introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Test_intro"-------
while continueRoutine:
    # get current time
    t = Test_introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_test_text* updates
    if t >= 0.0 and intro_test_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        intro_test_text.tStart = t
        intro_test_text.frameNStart = frameN  # exact frame index
        intro_test_text.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Test_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Test_intro"-------
for thisComponent in Test_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys=None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "Test_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Testing"-------
t = 0
TestingClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
from psychopy import core
import random

video_stim = test_video

def show_test(video_file, audio_file, video_noise_level, audio_noise_level):
    video_stim.setMovie(video_file)
    video_stim.seek(0)
    video_stim.play()
    while video_stim.status != visual.FINISHED:
        video_stim.draw()
        noise.draw()
        win.flip()
        noise.updateNoise()

## Setup Section
iteration_count = 0
target_met = False

subject_audio_answers = [[] for x in range(len(options))]

## Experiment Section
while iteration_count < minimum_iterations:
    # Select a stimulus from the list of files
    correct_answer_index = random.randint(0, len(options)-1)
    correct_answer = options[correct_answer_index]
    test_file = correct_answer + ".mov"
    correct_answer = correct_answer[0].lower()
    
    # Play the video
    show_test(test_file, test_file, 0, noise_level)
    
    # Get response
    prompt.draw()
    win.flip()
    
    # Read a character
    c = event.waitKeys()
    if c[0] == correct_answer:
        subject_audio_answers[correct_answer_index].append(1)
        noise_level += 1
        accuracy += 1
    elif c[0] == 'space':
        break
    else:
        subject_audio_answers[correct_answer_index].append(0)
        noise_level -= 1
    iteration_count += 1

# keep track of which components have finished
TestingComponents = [test_video, test_text]
for thisComponent in TestingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Testing"-------
while continueRoutine:
    # get current time
    t = TestingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *test_video* updates
    if t >= 0.0 and test_video.status == NOT_STARTED:
        # keep track of start time/frame for later
        test_video.tStart = t
        test_video.frameNStart = frameN  # exact frame index
        test_video.setAutoDraw(True)
    frameRemains = 0.0 + 0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if test_video.status == STARTED and t >= frameRemains:
        test_video.setAutoDraw(False)
    
    # *test_text* updates
    if t >= 0.0 and test_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        test_text.tStart = t
        test_text.frameNStart = frameN  # exact frame index
        test_text.setAutoDraw(True)
    frameRemains = 0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if test_text.status == STARTED and t >= frameRemains:
        test_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TestingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Testing"-------
for thisComponent in TestingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
for index, option in enumerate(subject_audio_answers):
    try:
        print(options[index] + " average: %" + str(sum(option)/len(option) * 100))
    except:
        pass
# the Routine "Testing" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Outro"-------
t = 0
OutroClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
OutroComponents = [Outro_text, key_resp_4]
for thisComponent in OutroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Outro"-------
while continueRoutine:
    # get current time
    t = OutroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Outro_text* updates
    if t >= 0.0 and Outro_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Outro_text.tStart = t
        Outro_text.frameNStart = frameN  # exact frame index
        Outro_text.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in OutroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Outro"-------
for thisComponent in OutroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "Outro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
