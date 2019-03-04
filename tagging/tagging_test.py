# -*- coding: utf-8 -*-
import nltk
import re
import codecs
from pythainlp.tokenize import word_tokenize
features = []


def get_words_in_reviews(all_reviews):
    all_words = []
    for (words, sentiment) in all_reviews:
        all_words.extend(words)
    return all_words


def get_word_features(list_of_words):
    list_of_words = nltk.FreqDist(list_of_words)
    word_features = list_of_words.keys()
    return word_features


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in features:
        features['contains(%s)' % word] = (word in document_words)
    return features


def train():
    # สำหรับเปิดไฟล์ที่เป็น positive และ negative
    traffic_reviews_file = codecs.open('traffic.txt', 'r', "utf-8")
   # accident_reviews_file = codecs.open('carAccident.txt', 'r', "utf-8")
    disaster_review_file = codecs.open('disaster.txt', 'r', "utf-8")

    traffic_list = []
    for each_review in traffic_reviews_file:
        each_review = ' '.join(word_tokenize(each_review))  # ตัดคำ
        if each_review.endswith('\n'):
            each_review = each_review[:-1]
        if not each_review == '':
            traffic_list.append([each_review, 'traffic'])  # แท็ก pos
    # เก็บ negative ให้เป็น list -----------------------------------------

    # accident_list = []
    # for each_review in accident_reviews_file:
    #     each_review = ' '.join(word_tokenize(each_review))
    #     if each_review.endswith('\n'):
    #         each_review = each_review[:-1]
    #     if not each_review == '':
    #         accident_list.append([each_review, 'Acccident'])  # แท็ก neg

    # disaster List --------------------------------------------------
    disaster_list = []
    for each_review in disaster_review_file:
        each_review = ''.join(word_tokenize(each_review))
        if each_review.endswith('\n'):
            each_review = each_review[-1]
        if not each_review == '':
            disaster_list.append([each_review, 'disaster'])  # แท็ก neg


    all_reviews = []
    for (review, sentiment) in traffic_list  + disaster_list:
        reviews_filtered = [w.lower() for w in word_tokenize(review)]
        all_reviews.append((reviews_filtered, sentiment))
    global features
    features = get_word_features(get_words_in_reviews(all_reviews))
    training_set = nltk.classify.apply_features(extract_features, all_reviews)
    classifier = nltk.NaiveBayesClassifier.train(training_set)  # ทำการ train
    return classifier


classifier = train()
read_in = input('Enter >>> ')
while read_in != 'exit':
    print('\n' + classifier.classify(extract_features(word_tokenize(read_in))))
    read_in = input('Enter >>> ')
