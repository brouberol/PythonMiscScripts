import pickle

f = open("PickleTest.txt","w")
data = [1,2.003,"Plop",complex(1,2),[1,2,str(2)]]

pickle.dump(data,f)
f.close()

g = open("PickleTest.txt","r")
data2 = pickle.load(g)

g.close()

data == data2 #True !

#Attention, inutile (et faux) de lire les pickle files avec un readline(s)()

#Plus d'infos sur http://docs.python.org/library/pickle.html#module-pickleue
