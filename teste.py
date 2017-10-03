
TOKENS = ["char", "int", "string"]
ANALISE = {}
ESPACO_VAZIO = [0]

ANALISE_FINAL = []
posicao_espaco_vazio = 0

def separacao(texto):
    # PRIMEIRA ANALISE
    for i in range(0, len(texto)):
        ANALISE[i] = texto[i]

    print ANALISE


def analise_vazio():
    for i in range(len(ANALISE)):
        if ANALISE[i] == " ":
            ESPACO_VAZIO.append(i)


def analise_tokens():
    #for x, y in range(x=0, y=1, step=1):
     #   if(y == 5):
            #print texto[ESPACO_VAZIO[x]:]
      #      pass
      #  else:
            #print texto[ESPACO_VAZIO[x]:ESPACO_VAZIO[y]]
      #      pass

    print texto[ESPACO_VAZIO[0]:ESPACO_VAZIO[1]]
    print texto[ESPACO_VAZIO[1]:ESPACO_VAZIO[2]]
    print texto[ESPACO_VAZIO[2]:ESPACO_VAZIO[3]]
    print texto[ESPACO_VAZIO[3]:ESPACO_VAZIO[4]]
    print texto[ESPACO_VAZIO[4]:]




#SEGUNDA ANALISE
def analise(index):
    saida = ""
    for i in range(index, len(ANALISE)):
        if ANALISE[i] == " ":
            ESPACO_VAZIO.append(i)
            posicao_espaco_vazio = i
            for x in range(i):
                saida += ANALISE[x]
                if saida in TOKENS:
                    ANALISE_FINAL.append(saida)
    print ANALISE_FINAL, ESPACO_VAZIO
    #analise(posicao_espaco_vazio)



if __name__ == '__main__':
    #texto = str(raw_input("Codigo: "))
    texto = "char a = 1 ;"
    separacao(texto)
    analise_vazio()
    analise_tokens()
    print ESPACO_VAZIO, ANALISE_FINAL



