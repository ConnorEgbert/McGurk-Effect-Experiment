#!/usr/bin/env python
# -*- coding: utf-8 -*-
# There is little experiment if the participant cannot give any input.
# Here we changed assignment 2 a bit so that it waits for a keys, rather
# than waiting 5 s. Note that we need to import the event module from
# PsychoPy to make this work.
from psychopy import core, visual, event

debug = True

## Setup Section
#win = visual.Window()
textString = "Select a test\n1) Audio\n2) Video"
if debug:
    textString += "\nProgram is being run in debug mode."
message = visual.TextStim(win, text=textString)

## Experiment Section
message.draw()
win.flip()
c = event.waitKeys() # read a character
if debug:
    if c[0] == "1":
        message = visual.TextStim(win, text="Selected audio")
    elif c[0] == "2":
        message = visual.TextStim(win, text="Selected video")
    else:
        message = visual.TextStim(win, text="Invalid selection: " + c[0])
    message.draw()
    win.flip()
    event.waitKeys()


## Closing Section
win.close()
core.quit()
