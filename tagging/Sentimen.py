# ใช้ตัดคำภาษาไทย
import deepcut
# ใช้งาน regex
import re
# จัดการเกี่ยวกับ array
import numpy as np
# สำหรับทำ classify และทดสอบโมเดล
from nltk import FreqDist, precision, recall, f_measure, NaiveBayesClassifier
from nltk.classify import apply_features
from nltk.classify import util
# สำหรับสร้างชุดข้อมูลสำหรับ train และ test เพื่อทดสอบประสิทธิภาพ
from sklearn.model_selection import KFold
import collections, itertools

data_pos = [(line.strip(), 'pos') for line in open("pos.txt", 'r')]
data_neg = [(line.strip(), 'neg') for line in open("neg.txt", 'r')]
def split_words (sentence):
    return deepcut.tokenize(''.join(sentence.lower().split()))
sentences = [(split_words(sentence), sentiment) for (sentence, sentiment) in data_pos + data_neg]