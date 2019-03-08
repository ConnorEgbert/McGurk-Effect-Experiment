#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.5),
    on Wed Mar  6 13:56:40 2019
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
    originPath='/Users/x/Documents/PsychoPy/Experiment/Experiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Initialize components for Routine "Audio_Tuning"
Audio_TuningClock = core.Clock()
debug = False

# Initialize components for Routine "Video_Tuning"
Video_TuningClock = core.Clock()
debug = False

# Initialize components for Routine "Outro"
OutroClock = core.Clock()
Outro_text = visual.TextStim(win=win, name='Outro_text',
    text='This concludes the test.',
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
routineTimer.add(7.500000)
# update component parameters for each repeat
# keep track of which components have finished
IntroComponents = [Intro_text]
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
    frameRemains = 0.0 + 7.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Intro_text.status == STARTED and t >= frameRemains:
        Intro_text.setAutoDraw(False)
    
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

# set up handler to look after randomisation of conditions etc
Audio_testing = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Audio_testing')
thisExp.addLoop(Audio_testing)  # add the loop to the experiment
thisAudio_testing = Audio_testing.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAudio_testing.rgb)
if thisAudio_testing != None:
    for paramName in thisAudio_testing:
        exec('{} = thisAudio_testing[paramName]'.format(paramName))

for thisAudio_testing in Audio_testing:
    currentLoop = Audio_testing
    # abbreviate parameter names if possible (e.g. rgb = thisAudio_testing.rgb)
    if thisAudio_testing != None:
        for paramName in thisAudio_testing:
            exec('{} = thisAudio_testing[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Audio_Tuning"-------
    t = 0
    Audio_TuningClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    from psychopy import core
    
    ## Setup Section
    textHeight = 50
    textString = "Audio_test"
    message = visual.TextStim(win, text=textString)
    
    ## Experiment Section
    message.draw()
    win.flip()
    c = event.waitKeys() # read a character
    message = visual.TextStim(win, text="You pressed: " + c[0])
    message.draw()
    win.flip()
    
    core.wait(3)
    
    # keep track of which components have finished
    Audio_TuningComponents = []
    for thisComponent in Audio_TuningComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Audio_Tuning"-------
    while continueRoutine:
        # get current time
        t = Audio_TuningClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
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
    
    # the Routine "Audio_Tuning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2 repeats of 'Audio_testing'


# set up handler to look after randomisation of conditions etc
Video_testing = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Video_testing')
thisExp.addLoop(Video_testing)  # add the loop to the experiment
thisVideo_testing = Video_testing.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVideo_testing.rgb)
if thisVideo_testing != None:
    for paramName in thisVideo_testing:
        exec('{} = thisVideo_testing[paramName]'.format(paramName))

for thisVideo_testing in Video_testing:
    currentLoop = Video_testing
    # abbreviate parameter names if possible (e.g. rgb = thisVideo_testing.rgb)
    if thisVideo_testing != None:
        for paramName in thisVideo_testing:
            exec('{} = thisVideo_testing[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Video_Tuning"-------
    t = 0
    Video_TuningClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    from psychopy import core
    
    ## Setup Section
    textHeight = 50
    textString = "Video_test"
    message = visual.TextStim(win, text=textString)
    
    ## Experiment Section
    message.draw()
    win.flip()
    c = event.waitKeys() # read a character
    message = visual.TextStim(win, text="You pressed: " + c[0])
    message.draw()
    win.flip()
    
    core.wait(1)
    # keep track of which components have finished
    Video_TuningComponents = []
    for thisComponent in Video_TuningComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Video_Tuning"-------
    while continueRoutine:
        # get current time
        t = Video_TuningClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
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
    
    # the Routine "Video_Tuning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2 repeats of 'Video_testing'


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
