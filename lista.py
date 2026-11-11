lista = [];
lista.append("alguma coisa");
lista.append(True);
lista.append(1423);
lista.append(0.354);
for indice, i in enumerate(lista):
    print (i)
    if (i == True):
        lista.pop(i)
print(lista)
