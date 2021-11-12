import numpy as np
from pyswip import Prolog

prolog = Prolog()
prolog.consult("../dataset/knowledge.pl")

def addAssert(prolog, str):
    prolog.assertz(str)


def deleteAssert(prolog, str):
    prolog.retract(str)


def query(prolog, str):
    return list(prolog.query(str))

def nomeTipoSearch(tip):
    tip = tip.lower()
    return query(prolog, "nome - tipo(X,\"" + tip + "\").")

def nomeSaporeSearch(sap):
    #a = input("Che sapore preferisci? [fruttato,secco]")
    sap = sap.lower()
    #print(query(prolog, "nome - sapore(X,\"" + a + "\")."))
    return query(prolog, "nome - sapore(X,\"" + sap + "\").")

def nomePrezzoSearch(prez):
    prez = float(prez)
    interval = np.arange(1, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "nome - prezzo(X,\"" + i + "\").")!= []):
        my_list.append(query(prolog, "nome - prezzo(X,\"" + i + "\")."))
    return my_list

def nomeCiboSearch(abb):
    abb = abb.lower()
    return query(prolog, "nome - cibo(X,\"" + abb + "\").")

def tipoSaporeSearch(tip,sap):
    tip = tip.lower()
    sap = sap.lower()
    return query(prolog, "nome - tipo - sapore(X,\"" + tip + "\",\"" + sap + "\").")

def tipoPrezzoSearch(tip,prez):
    tip = tip.lower()
    interval = np.arange(1, prez + 1)
    my_list = []
    for i in interval:
        i = i.astype(str)
        if (query(prolog, "nome - tipo - prezzo(X,\"" + tip + "\",\"" + i + "\").")!= []):
            my_list.append(query(prolog, "nome - tipo - prezzo(X,\"" + tip + "\",\"" + i + "\")."))
    return my_list

def tipoCibo(tip,abb):
    tip = tip.lower()
    abb = abb.lower()
    return query(prolog, "nome - tipo - cibo(X,\"" + tip + "\",\"" + abb + "\").")

def tipoSaporePrezzo(tip,sap,prez):
    tip = tip.lower()
    sap = sap.lower()
    interval = np.arange(1, prez + 1)
    my_list = []
    for i in interval:
        i = i.astype(str)
        if (query(prolog, "nome - tipo - sapore - prezzo(X,\"" + tip + "\",\"" + sap + "\",\"" + i +"\").") != []):
            my_list.append(query(prolog, "nome - tipo - sapore - prezzo(X,\"" + tip + "\",\"" + sap + "\",\"" + i +"\")."))
    return my_list

def tipoSaporeCibo(tip,sap,abb):
    tip = tip.lower()
    sap = sap.lower()
    abb = abb.lower()
    return query(prolog, "nome - tipo - sapore - cibo(X,\"" + tip + "\",\"" + sap + "\",\"" + abb + "\").")

def tipoPrezzoCibo(tip,prez,abb):
    tip = tip.lower()
    abb = abb.lower()
    interval = np.arange(1, prez + 1)
    my_list = []
    for i in interval:
        i = i.astype(str)
        if (query(prolog, "nome - tipo - prezzo - cibo(X,\"" + tip + "\",\"" + i + "\",\"" + abb + "\").") != []):
            my_list.append(query(prolog, "nome - tipo - prezzo - cibo(X,\"" + tip + "\",\"" + i + "\",\"" + abb +"\")."))
    return my_list

def saporePrezzo(sap,prez):
    sap = sap.lower()
    interval = np.arange(1, prez + 1)
    my_list = []
    for i in interval:
        i = i.astype(str)
        if (query(prolog, "nome - sapore - prezzo(X,\"" + sap + "\",\"" + i + "\").") != []):
            my_list.append(query(prolog, "nome - sapore - prezzo(X,\"" + sap + "\",\"" + i + "\")."))
    return my_list

def saporeCibo(sap,abb):
    sap = sap.lower()
    abb = abb.lower()
    return query(prolog, "nome - sapore - cibo(X,\"" + sap + "\",\"" + abb + "\").")

def saporePrezzoCibo(sap,prez,abb):
    sap = sap.lower()
    abb = abb.lower()
    interval = np.arange(1, prez + 1)
    my_list = []
    for i in interval:
        i = i.astype(str)
        if (query(prolog, "nome - sapore - prezzo - cibo(X,\"" + sap + "\",\"" + i + "\",\"" + abb +"\").") != []):
            my_list.append(query(prolog, "nome - sapore - prezzo - cibo(X,\"" + sap + "\",\"" + i + "\",\"" + abb +"\")."))
    return my_list

def prezzoCibo(prez,abb):
    abb = abb.lower()
    interval = np.arange(1, prez + 1)
    my_list = []
    for i in interval:
        i = i.astype(str)
        if (query(prolog, "nome - prezzo - cibo(X,\"" + abb + "\",\"" + i + "\").") != []):
            my_list.append(query(prolog, "nome - prezzo - cibo(X,\"" + abb + "\",\"" + i + "\")."))
    return my_list

def allSearch(tip,sap,prez,abb):
    tip = tip.lower()
    sap = sap.lower()
    interval = np.arange(1, prez+1)
    abb = abb.lower()
    my_list = []
    for i in interval:
        i = i.astype(str)
        if (query(prolog, "all(X,\"" + tip + "\",\"" + sap + "\",\"" + i + "\",\"" + abb + "\").")!= []):
            my_list.append(query(prolog, "all(X,\"" + tip + "\",\"" + sap + "\",\"" + i + "\",\"" + abb + "\")."))
    return my_list