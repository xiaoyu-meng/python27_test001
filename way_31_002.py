# -*- coding:utf-8 -*-
#find_sender.py
#匹配 From; Foo Fie <foo@bar.baz>  这个句子中的Foo Fie

import  re,fileinput
pat=re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
    m=pat.match(line,)
    if m:
        print m.group(1)


