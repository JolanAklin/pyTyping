#!/usr/bin/env python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import random

shownLetter = 0
rightLetter = 0
allTypedLetter = 0

def text_inserted(label):
    tbx = builder.get_object('tbx')
    tbxText=tbx.get_text()
    if(tbxText != ""):
        global allTypedLetter
        allTypedLetter += 1
        lblAllTypedLetter.set_text('all typed letter: ' + str(allTypedLetter))
        label.set_text(tbx.get_text())
        tbx.set_text("")
        if(tbxText == randLetter):
            global rightLetter
            rightLetter += 1
            lblRightLetter.set_text('right letter: ' + str(rightLetter))
            changeLetter()
 

def randomLetter(letterArray):
    randint = random.randint(0,len(letterArray)-1)
    return letterArray[randint]


def changeLetter():
    global randLetter
    global shownLetter
    shownLetter += 1
    lblTotLetter.set_text('shown letter: ' + str(shownLetter))
    randLetter = randomLetter(letterArray)
    letterDisplay.set_markup('<span background="blue">'+str(randLetter)+'</span>')
    #letterDisplay.set_text(randLetter)
    

screen = Gdk.Screen.get_default()

css_provider = Gtk.CssProvider()
css_provider.load_from_path('test.css')

context = Gtk.StyleContext()
context.add_provider_for_screen(screen, css_provider,
  Gtk.STYLE_PROVIDER_PRIORITY_USER)

letterArray = ['a', 'b', 'c', 'd', 'e', 'f']
builder = Gtk.Builder()
builder.add_from_file('testui.glade')  # Rentrez évidemment votre fichier, pas le miens!

window = builder.get_object('main_window')
# Peut se faire dans Glade mais je préfère le faire ici, à vous de voir
window.connect('delete-event', Gtk.main_quit)

global lblTotLetter
lblTotLetter = builder.get_object('lblTotLetter')
global lblRIghtLetter
lblRightLetter = builder.get_object('lblRightLetter')
global lblAllTypedLetter
lblAllTypedLetter = builder.get_object('lblAllTypedLetter')

global letterDisplay
letterDisplay = builder.get_object('letterDisplay')
changeLetter()


# Le handler
handler = {'on_insert_text': text_inserted}
builder.connect_signals(handler)

window.show_all()
Gtk.main()
