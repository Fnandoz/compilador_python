

ATRIB = ["="]
ARITIMETICO = ["+", "-", "*", "/"]
FIM_SENTENCA = [";"]
PALAVRAS_RESERVADAS = ["char", "int", "float"]

analise = {}
lista_temp = []


def separa_items(texto):
    nova_lista = []
    a = texto.split()
    for i in a[len(a)-1]:
        nova_lista.append(i)
    a.pop(len(a)-1)

    a += nova_lista
    global lista_temp
    lista_temp = a
    analise_tokens()


def checa_numero(valor):
    try:
        int(valor)
        return True
    except:
        return False


def analise_tokens():
    global analise
    for i in lista_temp:
        if i in ATRIB:
            analise["ATRIB"] = i

        elif i in ARITIMETICO:
            analise["ARITIMETICO"] = i

        elif i in FIM_SENTENCA:
            analise["Fim de Sentenca"] = i

        elif checa_numero(i):
            analise["Numero"] = i

        elif i in PALAVRAS_RESERVADAS:
            analise[i] = i

        else:
            analise["Identificador"] = i

    print analise


if __name__ == '__main__':
    tt = "char a = 1;"
    separa_items(tt)


