import pandas as pd
dfKB = pd.read_csv('../dataset/wineKB.csv')


KNOWLEDGE_BASE = "../dataset/knowledge.pl"

def is_empty(s):
    if s and s.strip():
        return True
    return False

file_data = ""


dfKB['nome'] = dfKB['nome'].astype(str)
dfKB['tipo'] = dfKB['tipo'].astype(str)
dfKB['produzione'] = dfKB['produzione'].astype(str)
dfKB['sapore'] = dfKB['sapore'].astype(str)
dfKB['prezzo'] = dfKB['prezzo'].astype(str)
dfKB['cibo'] = dfKB['cibo'].astype(str)

# Generating nome - sapore
for row in dfKB.itertuples():
    nome = row[1]
    sapore = row[4]
    string = "nome-sapore(\"" + nome + "\",\"" + sapore + "\")."

    if is_empty(nome) and is_empty(sapore) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - prezzo
for row in dfKB.itertuples():
    nome = row[1]
    prezzo = row[5]
    string = "nome-prezzo(\"" + nome + "\",\"" + prezzo + "\")."

    if is_empty(nome) and is_empty(prezzo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - tipo
for row in dfKB.itertuples():
    nome = row[1]
    tipo = row[2]
    string = "nome-tipo(\"" + nome + "\",\"" + tipo + "\")."

    if is_empty(nome) and is_empty(tipo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - cibo
for row in dfKB.itertuples():
    nome = row[1]
    cibo = row[6]
    string = "nome-cibo(\"" + nome + "\",\"" + cibo + "\")."

    if is_empty(nome) and is_empty(cibo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - tipo - sapore
for row in dfKB.itertuples():
    nome = row[1]
    tipo = row[2]
    sapore = row[4]
    string = "nome-tipo-sapore(\"" + nome + "\",\"" + tipo + "\",\"" + sapore + "\")."

    if is_empty(nome) and is_empty(tipo) and is_empty(sapore) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - tipo - prezzo
for row in dfKB.itertuples():
    nome = row[1]
    tipo = row[2]
    prezzo = row[5]
    string = "nome-tipo-prezzo(\"" + nome + "\",\"" + tipo + "\",\"" + prezzo + "\")."

    if is_empty(nome) and is_empty(tipo) and is_empty(prezzo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - tipo - cibo
for row in dfKB.itertuples():
    nome = row[1]
    tipo = row[2]
    cibo = row[6]
    string = "nome-tipo-cibo(\"" + nome + "\",\"" + tipo + "\",\"" + cibo + "\")."

    if is_empty(nome) and is_empty(tipo) and is_empty(cibo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - tipo - sapore - prezzo
for row in dfKB.itertuples():
    nome = row[1]
    tipo = row[2]
    sapore = row[4]
    prezzo = row[5]
    string = "nome-tipo-sapore-prezzo(\"" + nome + "\",\"" + tipo + "\",\"" + sapore + "\",\"" + prezzo + "\")."

    if is_empty(nome) and is_empty(tipo) and is_empty(sapore) and is_empty(prezzo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - tipo - sapore - cibo
for row in dfKB.itertuples():
    nome = row[1]
    tipo = row[2]
    sapore = row[4]
    cibo = row[6]
    string = "nome-tipo-sapore-cibo(\"" + nome + "\",\"" + tipo + "\",\"" + sapore + "\",\"" + cibo + "\")."

    if is_empty(nome) and is_empty(tipo) and is_empty(sapore) and is_empty(cibo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - tipo - prezzo - cibo
for row in dfKB.itertuples():
    nome = row[1]
    tipo = row[2]
    prezzo = row[5]
    cibo = row[6]
    string = "nome-tipo-prezzo-cibo(\"" + nome + "\",\"" + tipo + "\",\"" + prezzo + "\",\"" + cibo + "\")."

    if is_empty(nome) and is_empty(tipo) and is_empty(prezzo) and is_empty(cibo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - sapore - prezzo
for row in dfKB.itertuples():
    nome = row[1]
    sapore = row[4]
    prezzo = row[5]
    string = "nome-sapore-prezzo(\"" + nome + "\",\"" + sapore + "\",\"" + prezzo + "\")."

    if is_empty(nome) and is_empty(sapore) and is_empty(prezzo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - sapore - cibo
for row in dfKB.itertuples():
    nome = row[1]
    tipo = row[2]
    cibo = row[6]
    string = "nome-sapore-cibo(\"" + nome + "\",\"" + sapore + "\",\"" + cibo + "\")."

    if is_empty(nome) and is_empty(sapore) and is_empty(cibo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - sapore - prezzo - cibo
for row in dfKB.itertuples():
    nome = row[1]
    sapore = row[4]
    prezzo = row[5]
    cibo = row[6]
    string = "nome-sapore-prezzo-cibo(\"" + nome + "\",\"" + sapore + "\",\"" + prezzo + "\",\"" + cibo + "\")."

    if is_empty(nome) and is_empty(sapore) and is_empty(prezzo) and is_empty(cibo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating nome - prezzo - cibo
for row in dfKB.itertuples():
    nome = row[1]
    prezzo = row[5]
    cibo = row[6]
    string = "nome-prezzo-cibo(\"" + nome + "\",\"" + prezzo + "\",\"" + cibo + "\")."

    if is_empty(nome) and is_empty(prezzo) and is_empty(cibo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating all
for row in dfKB.itertuples():
    nome = row[1]
    tipo = row[2]
    sapore = row[4]
    prezzo = row[5]
    cibo = row[6]
    string = "all(\"" + nome + "\",\"" + tipo + "\",\"" + sapore + "\",\"" + prezzo + "\",\"" + cibo + "\")."

    if is_empty(nome) and is_empty(tipo) and is_empty(sapore) and is_empty(prezzo) and is_empty(cibo) and (string not in file_data):
        file_data += string + "\n"

knowledge_base = open(KNOWLEDGE_BASE, mode="w")
knowledge_base.write(file_data)
knowledge_base.close()
print("\nFile created in: ", KNOWLEDGE_BASE)