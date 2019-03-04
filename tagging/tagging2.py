# เขียนโดย นาย วรรณพงษ์  ภัททิยไพบูลย์
# ใช้ประกอบบทความใน python3.wannaphong.com
# cc-by 3.0 Thai Sentiment Text https://github.com/wannaphongcom/lexicon-thai/tree/master/ข้อความ/
# อ่านบทความได้ที่ https://python3.wannaphong.com/2017/02/ทำ-sentiment-analysis-ภาษาไทยใน-python.html
from nltk import NaiveBayesClassifier as nbc
from pythainlp.tokenize import word_tokenize
import codecs
from itertools import chain
# pos.txt
with codecs.open('carAccident.txt', 'r', "utf-8") as f:
    lines = f.readlines()
    ac_list=[e.strip() for e in lines]
del lines
f.close() # ปิดไฟล์
# neg.txt
with codecs.open('traffic.txt', 'r', "utf-8") as f:
    lines = f.readlines()
    tf_list=[e.strip() for e in lines]
f.close() # ปิดไฟล์

with codecs.open('disaster.txt','r',"utf-8") as f :
    lines = f.readlines()
    ds_list = [e.strip() for e in lines]
f.close()

lines
#tag outputpart 
accident=['Accident']*len(ac_list)
traffic=['Traffic']*len(tf_list)
disaster = ['disaster']* len (ds_list)

training_data = list(zip(ac_list,accident)+ list(zip(tf_list,traffic)+list(ds_list,disaster)))
vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in training_data]))
feature_set = [({i:(i in word_tokenize(sentence.lower())) for i in vocabulary},tag) for sentence, tag in training_data]
classifier = nbc.train(feature_set)
while True:
	test_sentence = input('\nข้อความ : ')
	featurized_test_sentence =  {i:(i in word_tokenize(test_sentence.lower())) for i in vocabulary}
	print("test_sent:",test_sentence)
	print("tag:",classifier.classify(featurized_test_sentence)) # ใช้โมเดลที่ train ประมวลผล