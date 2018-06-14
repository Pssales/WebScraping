import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("usuario.csv",header=None)
dataset=df.values;

x=dataset[:,0:28].astype('float');
y=dataset[:,28]

from keras.utils import to_categorical
y_binary = to_categorical(y)

model=Sequential()
model.add(Dense(56,input_dim=28,activation='relu'))
model.add(Dense(2,activation='softmax'))
model.compile(optimizer='sgd',loss='categorical_crossentropy',metrics=['acc'])
model.fit(x,y_binary,epochs=2500);

#caso jogo tenha 2 generos em comum com que usuário costuma jogar
i=[0, 0, 0,1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t=np.asmatrix(i);
resultado=model.predict(t);
print(i)
print("chance de gostar do jogo:",resultado[0][1]*100,"%")

