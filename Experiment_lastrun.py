#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.5),
    on Mon Mar 18 12:27:34 2019
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
expInfo = {'participant': '', 'session': '001'}
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
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
Intro_text = visual.TextStim(win=win, name='Intro_text',
    text='Listen or watch for what is being said.\n\nSelect the option that best fits the stimulus.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text = visual.TextStim(win=win, name='text',
    text='Wait for the speaker to finish.\nPress b if the speaker says "BA".\nPress d if the speaker says "DA".\nPress g if the speaker says "GA".',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=10, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Video_Tuning"
Video_TuningClock = core.Clock()
debug = True
accuracy = 0
target_accuracy = .5
noise_level = 0
minimum_iterations = 10

margin_of_error = .05

options = ["BA", "DA", "GA"]
video_stimulus = visual.MovieStim3(
    win=win, name='video_stimulus',
    noAudio = True,
    filename='GA.mov',
    ori=0, pos=(0, 0), opacity=1,
    depth=-1.0,
    )
prompt = visual.TextStim(win=win, name='prompt',
    text='What was said:\nBA, DA, or GA?\nPress B, D, or G.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
video_noise = visual.NoiseStim(
    win=win, name='video_noise',
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=(1, 1), sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1, blendmode='avg', contrast=1.0,
    texRes=128,
    noiseType='Isotropic', noiseElementSize=0.0625, noiseBaseSf=8.0,
    noiseBW=1, noiseBWO=1, noiseFractalPower=0.0,noiseFilterLower=1.0, noiseFilterUpper=8.0, noiseFilterOrder=0.0, noiseClip=3.0, interpolate=False, depth=-3.0)
video_noise.buildNoise()

# Initialize components for Routine "Audio_Tuning"
Audio_TuningClock = core.Clock()
debug = True
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
    text='Audio is playing.',
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
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
IntroComponents = [Intro_text, text]
for thisComponent in IntroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Intro"-------
while continueRoutine and routineTimer.getTime() > 0:
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
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Intro_text.status == STARTED and t >= frameRemains:
        Intro_text.setAutoDraw(False)
    
    # *text* updates
    if t >= 3 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 3 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
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
        video_noise.draw
        win.flip()

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
Video_TuningComponents = [video_stimulus, prompt, video_noise]
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
    
    # *video_noise* updates
    if t >= 0.0 and video_noise.status == NOT_STARTED:
        # keep track of start time/frame for later
        video_noise.tStart = t
        video_noise.frameNStart = frameN  # exact frame index
        video_noise.setAutoDraw(True)
    frameRemains = 0.0 + 0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if video_noise.status == STARTED and t >= frameRemains:
        video_noise.setAutoDraw(False)
    if video_noise.status == STARTED:
        if video_noise._needBuild:
            video_noise.buildNoise()
    
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
        print("Option " + options[index] + " average: %" + str(sum(option)/len(option) * 100))
    except:
        pass

# the Routine "Video_Tuning" was not non-slip safe, so reset the non-slip timer
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
    while output_stim.status != visual.FINISHED:
        audio_text.draw()
        output_stim.draw()
        video_noise.draw
        win.flip()

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
        print("Option " + options[index] + " average: %" + str(sum(option)/len(option) * 100))
    except:
        pass
# the Routine "Audio_Tuning" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Outro"-------
t = 0
OutroClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
OutroComponents = [Outro_text]
for thisComponent in OutroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Outro"-------
while continueRoutine and routineTimer.getTime() > 0:
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
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Outro_text.status == STARTED and t >= frameRemains:
        Outro_text.setAutoDraw(False)
    
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


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
