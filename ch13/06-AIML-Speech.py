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
