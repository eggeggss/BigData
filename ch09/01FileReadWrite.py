#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

#a+: append  w:clear and wite
fr = open('workfile.txt', 'a+')
fr.write('This is a test\n')
fr.close()


fw = open('workfile.txt', 'r')
for line in fw:
    print(line)
fw.close()
