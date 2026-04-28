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
    printe: str = '        print(Resposta)'

    arq = 'novas_respostas.txt'
    dir = 'C:\\tmp\\'

    Resposta = str(input("Não tenho resposta para sua pergunta. Ajude no meu desenvolvimento e mande uma resposta cabível: "))

    frase = '    elif (Frase == "' + Frase + '"):'
    resposta = '        Resposta = "' + Resposta + '"'

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
        print() #Apenas para melhorar visualização em console
        if (cta == 0):
            print('Olá, eu sou a máquina que busca ser sua amiga! Faça perguntas para mim e se eu souber te responderei. Quando quiser ir embora, basta digitar Tchau.')
            cta = cta + 1
        Frase = str(input('O que você gostaria de dizer: '))
        respostas()




























#Perguntas e respostas armazenadas
def respostas():
    global Frase
    global Resposta

    if (Frase == 'Olá, tudo bem?'):
        Resposta = 'Oii, tudo sim!' + '\n' + 'E você está bem?'
        print (Resposta)
    elif (Frase == "Qual seu nome?"):
        Resposta = "Eu não tenho um :("
        print (Resposta)
    elif (Frase == "Hello World"):
        Resposta = "O mundo acena de volta!"
        print(Resposta)
    elif (Frase == "Oi"):
        Resposta = "Oi, tudo bem?"
        print(Resposta)


    else:
        coletor()

print('MÁQUINA ACUMULADORA DE RESPOSTAS' + '\n' + 'VERSÃO 1.2')
if (__name__ == '__main__'):
    main()
