import os

#algoritmo máquina
#declarar
Frase: str = ''
Resposta: str = ''
arq: str = ''
dir: str = ''
arquivo: str = ''




def coletor():
    global Frase
    global Resposta
    arq: str = ''
    dir: str = ''
    arquivo: str = ''
    tipo: str = ''
    enc: str = ''
    conteudo: str = ''
    frase: str = ''
    resposta: str = ''

    arq = 'novas_respostas.txt'
    dir = 'C:\\tmp\\'

    Resposta = str(input("Não tenho resposta para sua pergunta. Ajude no meu desenvolvimento e mande uma resposta cabível: "))

    frase = '    elif (Frase == "' + Frase + '"):'
    resposta = '        Resposta == "' + Resposta + '"'

    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        enc = 'utf-8'
        arquivo = dir + arq

        if (os.path.exists(arquivo)):
            tipo = 'a'
        
        conteudo = frase + '\n' + resposta + '\n'
        with open (arquivo, tipo, encoding=enc) as file:
            file.write(conteudo)

    

def main():
    global Frase
    global Resposta
    cta = 0

    while (Frase != 'Tchau'):
        if (cta == 0):
            print('Olá, eu sou a máquina que busca ser sua amiga! Faça perguntas para mim e se eu souber te responderei. Quando quiser ir embora, basta digitar Tchau.')
        Frase = str(input('O que você gostaria de dizer: '))
        respostas()




























#Perguntas e respostas armazenadas
def respostas():
    if (Frase == 'Olá, tudo bem?'):
        Resposta == 'Oii, tudo sim!' + '\n' + 'E você está bem?'

    else:
        coletor()

if (__name__ == '__main__'):
    main()
















#BANCO DE PERGUNTAS E RESPOSTAS: