from django.apps import AppConfig
import os
# Keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Flatten, LSTM, Conv1D, MaxPooling1D, Dropout, Activation,Conv2D,MaxPooling2D
from keras.layers import Input, Embedding, Add
from keras import layers
from keras import layers
from keras.layers.embeddings import Embedding
from keras.models import Model
from keras.utils import to_categorical
# NLTK
import nltk
from gensim.models import FastText
from gensim.models import Word2Vec
# Other
import re
import string
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score, f1_score
from sklearn import svm
from keras.layers.merge import concatenate
from keras.layers import Bidirectional
# from keras.layers import K, Activation
import keras.layers as K
from keras.layers import Activation
from keras.engine import Layer
from keras.layers import Dense, Input, Embedding, Dropout, Bidirectional, GRU, Flatten, SpatialDropout1D
# ========================================================
# from here until app config studd
# Text based classification
Fold_PATH = '/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/api/Data_text'
# df = pd.read_excel('Data_text/Fakenews/English_TrainVal.xlsx')
df = pd.read_excel(
     os.path.join(Fold_PATH, "Fakenews", "English_TrainVal.xlsx"),
     engine='openpyxl',
)
# # devdf = pd.read_excel('Data_text/Fakenews/English_Val.xlsx')
# devdf = pd.read_excel(
#      os.path.join(Fold_PATH, "Fakenews", "English_Val.xlsx"),
#      engine='openpyxl',
# )

df = df.dropna()
df = df.drop_duplicates(subset = ['text'],keep = False)
# devdf = devdf.dropna()


embeddings_index = dict()
f = open('/home/shivam/Data/Projects/Fakenews/augmented/glove.6B.200d.txt')

for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()
# print('Loaded %s word vectors.' % len(embeddings_index))


tokenizer = Tokenizer()
tokenizer.fit_on_texts(df['text'])
sequences = tokenizer.texts_to_sequences(df['text'])
vocabulary_size = len(tokenizer.word_index) + 1 # 20648

embedding_matrix = np.zeros((vocabulary_size, 200))
for word, index in tokenizer.word_index.items():
    if index > vocabulary_size - 1:
        break
    else:
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[index] = embedding_vector
#         else:
#             embedding_vector = codemixed_embeddings[word]
#             if embedding_vector is not None:
#                 embedding_matrix[index] = embedding_vector


def define_text_model(length, vocabulary_size, embedding_matrix):
    input1 = Input(shape=(length,))
    embedding1 = Embedding(vocabulary_size, 200, weights=[embedding_matrix], trainable=False)(input1)
    conv1 = Conv1D(filters=32, kernel_size=3, activation='relu')(embedding1)
    conv1 = Dropout(0.5)(conv1)
    # capsule1 = Capsule(num_capsule=Num_capsule, dim_capsule=Dim_capsule, routings=3, share_weights=True)(conv1)
    flat1 = Flatten()(conv1)

    dense = Dense(32, activation='relu')(flat1)
    output = Dense(2, activation='softmax')(dense)
    model = Model(inputs=[input1], outputs=output)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # model.summary()
    return model

class FrontendConfig(AppConfig):
    name = 'frontend'
class FrontendAppConfig(AppConfig):
    def __init__(self):
        name = 'frontend'

    def text_FNF_classify(in_txt):
        res_list = []
        model_FNF = define_text_model(150, vocabulary_size, embedding_matrix)
        model_FNF.load_weights(
            "/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/api/models/aug_caps_weights_FND_CNN_trnval_HELIOS.h5")

        pred_dev = model_FNF.predict(pad_sequences(tokenizer.texts_to_sequences(in_txt), maxlen=150))
        # print(np.shape(pred_dev))
        # print(pred_dev)
        prd_dev = np.argmax(pred_dev, axis=1)
        # print(prd_dev)
        for i in prd_dev:
            if i==1:
                res_list.append('real')
            else:
                res_list.append('fake')
        # print(res_list)
        prob_list = np.round(np.max(pred_dev, axis=1), decimals=2)
        # prob=0
        # print(prob_list)
        # if prd_dev[0] == 1:
        #     lab = 'real'
        # else:
        #     lab = 'fake'
        # print(res_list, prob_list)
        return res_list, prob_list
