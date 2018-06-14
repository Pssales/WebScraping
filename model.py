import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

base="Ação","Aéreo","Arcade","Aventura","Beat &39;em Up","Clássicos","Corrida Arcade","Corrida Simulação","Esporte","Estratégia","Família","Fitness","Hack &#39;n&#39; Slash","Luta Arcade","Moba","Moto","Musical","Musou","Nave","Novel","Pinball","Plataforma","Puzzle","Quiz, Cartas e ...","RPG","Simulador","Terror","Tiro"
usuario="Ação","Aéreo","Arcade","Aventura"
jogo="Corrida Arcade","Corrida Simulação","Esporte","Estratégia","Família","Fitness"

jogo_encoded=[]
for i in range(len(base)):
    valor=0
    for j in range(len(jogo)):
        if(base[i]==jogo[j]):
            valor=1;
    jogo_encoded.append(valor)     

X=[]
Y=[]
for i in range(len(usuario)):
    linha=[]
    linha2=[]
    for j in range(len(base)):
        if(usuario[i]==base[j]):
            linha.append(1);
        else:
            linha.append(0)
        linha2.append(0)
    #consta
    X.append(linha)
    Y.append(1)
    #nao consta
    X.append(linha2)
    X.append(linha2)
    Y.append(0)
    Y.append(0)

np.savetxt("treino.csv", np.column_stack((X,Y)), delimiter=",", fmt='%s')

df=pd.read_csv("treino.csv",header=None)
dataset=df.values;

x=dataset[:,0:28].astype('float');
y=dataset[:,28]

from keras.utils import to_categorical
y_binary = to_categorical(y)

model=Sequential()
model.add(Dense(28,input_dim=28,activation='relu'))
model.add(Dense(2,activation='softmax'))
model.compile(optimizer='sgd',loss='categorical_crossentropy',metrics=['acc'])
model.fit(x,y_binary,epochs=850);

print("O usuário costuma jogar:",usuario)
print("jogo:",jogo)
##caso jogo tenha 2 generos em comum com que usuário costuma jogar
t=np.asmatrix(jogo_encoded);
resultado=model.predict(t);
print("chance de gostar do jogo:",resultado[0][1]*100,"%")

##np.savetxt("file_name.csv", dataset, delimiter=",", fmt='%s')
##np.savetxt("file_name.csv", np.column_stack((x, y)), delimiter=",", fmt='%s')
