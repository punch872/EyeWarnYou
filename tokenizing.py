# -*- coding: utf-8 -*-
from pythainlp.tokenize import word_tokenize
a = 'ฉันรักภาษาไทยเพราะฉันเป็นคนไทย' # u'ฉันรักภาษาไทยเพราะฉันเป็นคนไทย' ใน Python 2.7
b = word_tokenize(a)
print(b) # ['ฉัน', 'รัก', 'ภาษาไทย', 'เพราะ', 'ฉัน', 'เป็น', 'คนไทย']