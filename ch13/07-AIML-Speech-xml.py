# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"
"""
pip install pyttsx3
pip install pypiwin32

"""

import pyttsx3;
engine = pyttsx3.init();
engine.say('hello world')
engine.runAndWait() ;

import aiml
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("05-AIML-load.xml")
kernel.respond("load aiml b")
while True:   # Press CTRL-C to break this loop
    try:
        t2=input("Enter your message >> ")
        if t2=="*播放音樂*":
            playmusic()
        if t2 == "*開燈*":
                gpio()
        t1=kernel.respond(t2)
        print(t1)
        engine.say(t1)
        engine.runAndWait()
    except:
        t1=kernel.respond(raw_input("Enter your message >> "))
        print(t1)
        engine.say(t1)
        engine.runAndWait()
