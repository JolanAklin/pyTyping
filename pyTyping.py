#!/usr/bin/env python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import random

shownLetter = 0
rightLetter = 0
allTypedLetter = 0

#this function is called when a letter is entered in the textbox. It's verifying if the letter is right or wrong
def text_inserted(arg):
    letterDisplay.set_name("letterDisplay")
    tbx = builder.get_object('tbx')
    tbxText=tbx.get_text()
    if(tbxText != ""):
        global allTypedLetter
        allTypedLetter += 1
        lblAllTypedLetter.set_text('all typed letter: ' + str(allTypedLetter))
        tbx.set_text("")
        if(tbxText == randLetter):
            letterDisplay.set_name("letterDisplayRight")
            global rightLetter
            rightLetter += 1
            lblRightLetter.set_text('right letter: ' + str(rightLetter))
            changeLetter()
        else:
            letterDisplay.set_name("letterDisplayError")
 

#pick a letter randomly
def randomLetter(letterArray):
    randint = random.randint(0,len(letterArray)-1)
    return letterArray[randint]

#change the letter on the display
def changeLetter():
    global randLetter
    global shownLetter
    shownLetter += 1
    lblTotLetter.set_text('shown letter: ' + str(shownLetter))
    randLetter = randomLetter(letterArray)
    letterDisplay.set_markup(str(randLetter))
    
#load the css stylesheet
screen = Gdk.Screen.get_default()

css_provider = Gtk.CssProvider()
css_provider.load_from_path('style.css')

context = Gtk.StyleContext()
context.add_provider_for_screen(screen, css_provider,
  Gtk.STYLE_PROVIDER_PRIORITY_USER)

#letter that while be random picked
letterArray = ['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'y', 'x', 'c', 'v', 'b', 'n', 'm']

builder = Gtk.Builder()
builder.add_from_file('testui.glade')

window = builder.get_object('main_window')
window.connect('delete-event', Gtk.main_quit)

global resultWindow
resultWindow = builder.get_object('result_window')

#defining globally the text counter
global lblTotLetter
lblTotLetter = builder.get_object('lblTotLetter')
global lblRIghtLetter
lblRightLetter = builder.get_object('lblRightLetter')
global lblAllTypedLetter
lblAllTypedLetter = builder.get_object('lblAllTypedLetter')

global letterDisplay
letterDisplay = builder.get_object('letterDisplay')
changeLetter()


#event handler
handler = {'on_insert_text': text_inserted}
builder.connect_signals(handler)

window.show_all()
Gtk.main()
