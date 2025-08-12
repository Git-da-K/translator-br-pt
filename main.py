import random
import time


eng_words = ['Hi','Bye','Task', 'Programm']
pt_words = ['Oi','Tchau','Tarefa', 'Programa']
score = 0

mode = input("Selecione um modo: 0 - adicionar novas palavras, 1 - treinamento: \n")
while ((mode != '0') and (mode != '1')):
    mode = input("Símbolo inválido! Escolha 0 ou 1. (0 adiciona novas palavras e 1 inicia o treinamento) \n")

if mode == "1":
    print("Traduza o máximo de palavras que puder! Você tem 10 tentativas!")
    for i in range(10):
        number = random.randint(0, len(eng_words)-1)
        print("Como devemos traduzir: " + eng_words[number])
        if input() == pt_words[number]:
            print("Ótimo!!!")
            score += 1
        else:
            print("Incorreto... A palavra correta é - " + pt_words[number])
else:
    word = input("Digite uma palavra em português: ")
    translate = input("Digite a tradução desta palavra: ")
    if len(word) > 0 and len(translate) > 0:
        pt_words.append(word)
        eng_words.append(translate)
        print("A palavra foi adicionada com sucesso!")
