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



gru_len = 128
Routings = 5
Num_capsule = 10
Dim_capsule = 16
dropout_p = 0.25
rate_drop_dense = 0.28

def squash(x, axis=-1):
    # s_squared_norm is really small
    # s_squared_norm = K.sum(K.square(x), axis, keepdims=True) + K.epsilon()
    # scale = K.sqrt(s_squared_norm)/ (0.5 + s_squared_norm)
    # return scale * x
    s_squared_norm = K.sum(K.square(x), axis, keepdims=True)
    scale = K.sqrt(s_squared_norm + K.epsilon())
    return x / scale


# # A Capsule Implement with Pure Keras
# class Capsule(Layer):
#     def __init__(self, num_capsule, dim_capsule, routings=3, kernel_size=(9, 1), share_weights=True,
#                  activation='default', **kwargs):
#         super(Capsule, self).__init__(**kwargs)
#         self.num_capsule = num_capsule
#         self.dim_capsule = dim_capsule
#         self.routings = routings
#         self.kernel_size = kernel_size
#         self.share_weights = share_weights
#         if activation == 'default':
#             self.activation = squash
#         else:
#             self.activation = Activation(activation)
#
#     def build(self, input_shape):
#         super(Capsule, self).build(input_shape)
#         input_dim_capsule = input_shape[-1]
#         if self.share_weights:
#             self.W = self.add_weight(name='capsule_kernel',
#                                      shape=(1, input_dim_capsule,
#                                             self.num_capsule * self.dim_capsule),
#                                      # shape=self.kernel_size,
#                                      initializer='glorot_uniform',
#                                      trainable=True)
#         else:
#             input_num_capsule = input_shape[-2]
#             self.W = self.add_weight(name='capsule_kernel',
#                                      shape=(input_num_capsule,
#                                             input_dim_capsule,
#                                             self.num_capsule * self.dim_capsule),
#                                      initializer='glorot_uniform',
#                                      trainable=True)
#
#     def call(self, u_vecs):
#         if self.share_weights:
#             u_hat_vecs = K.Conv1D(u_vecs, self.W)
#         else:
#             u_hat_vecs = K.local_conv1d(u_vecs, self.W, [1], [1])
#
#         batch_size = K.shape(u_vecs)[0]
#         input_num_capsule = K.shape(u_vecs)[1]
#         u_hat_vecs = K.reshape(u_hat_vecs, (batch_size, input_num_capsule,
#                                             self.num_capsule, self.dim_capsule))
#         u_hat_vecs = K.permute_dimensions(u_hat_vecs, (0, 2, 1, 3))
#         # final u_hat_vecs.shape = [None, num_capsule, input_num_capsule, dim_capsule]
#
#         b = K.zeros_like(u_hat_vecs[:, :, :, 0])  # shape = [None, num_capsule, input_num_capsule]
#         for i in range(self.routings):
#             b = K.permute_dimensions(b, (0, 2, 1))  # shape = [None, input_num_capsule, num_capsule]
#             c = K.softmax(b)
#             c = K.permute_dimensions(c, (0, 2, 1))
#             b = K.permute_dimensions(b, (0, 2, 1))
#             outputs = self.activation(K.batch_dot(c, u_hat_vecs, [2, 2]))
#             if i < self.routings - 1:
#                 b = K.batch_dot(outputs, u_hat_vecs, [2, 3])
#
#         return outputs
#
#     def compute_output_shape(self, input_shape):
#         return (None, self.num_capsule, self.dim_capsule)

Fold_PATH = '/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/api/Data_text'
# df = pd.read_excel('Data_text/Fakenews/English_TrainVal.xlsx')
df = pd.read_excel(
     os.path.join(Fold_PATH, "Fakenews", "English_TrainVal.xlsx"),
     engine='openpyxl',
)
# devdf = pd.read_excel('Data_text/Fakenews/English_Val.xlsx')
devdf = pd.read_excel(
     os.path.join(Fold_PATH, "Fakenews", "English_Val.xlsx"),
     engine='openpyxl',
)

df = df.dropna()
df = df.drop_duplicates(subset = ['text'],keep = False)
devdf = devdf.dropna()
print(df.info())
print(devdf.info())


# codemixed_embeddings = FastText.load('augmented_ft.bin')
# print(codemixed_embeddings )
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
data = pad_sequences(sequences, maxlen=150)
# print(data.shape)
sequences_d = tokenizer.texts_to_sequences(devdf['text'])
data_dev = pad_sequences(sequences_d, maxlen=150)
# print(data_dev.shape)
vocabulary_size = len(tokenizer.word_index) + 1 # 20648



# create a weight matrix for words in training docs# create
# embedding_matrix = np.zeros((vocabulary_size, 100))
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


y= df['label'].astype('category').cat.codes
y_dev = devdf['label'].astype('category').cat.codes


def define_model(length, vocabulary_size, embedding_matrix):
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
    model.summary()
    return model



model = define_model(150, vocabulary_size,embedding_matrix)
model.load_weights("/home/shivam/PycharmProjects/Django/Django_Warehouse/todo-django-rest-framework-master/todo_drf/api/models/aug_caps_weights_FND_CNN_trnval_HELIOS.h5")

# pred_dev = model.predict([data_dev])
# pred_test = model.predict([data_test])
# prd_dev = np.argmax(pred_dev,axis = 1)
# prd_test = np.argmax(pred_test,axis = 1)

# print(confusion_matrix(y_dev,prd_dev))
# print(classification_report(y_dev,prd))
# print("Accuracy : ",accuracy_score(prd,y_dev))
# print(f1_score(y_dev, prd_dev, average='weighted'))

# print(confusion_matrix(y_test,prd_test))
# print(classification_report(y_test,prd))
# print("Accuracy : ",accuracy_score(prd,y_test))
# print(f1_score(y_test, prd, average='weighted'))

in_text = [input('Enter a statement for verification.\n')]

pred_dev = model.predict(pad_sequences(tokenizer.texts_to_sequences(in_text), maxlen=150))
prd_dev = np.argmax(pred_dev,axis = 1)

print(prd_dev)
