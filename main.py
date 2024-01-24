import random
def jogar():
    arquivo = open('palavras.txt', 'r+')
    arquivo1 = arquivo.readlines()
    print('Bem vindo ao jogo da forca!')
    palavra_secreta = random.choice(arquivo1)
    tentativas = 0
    tentativas_erradas = []
    forca_atual1 = ['_' for let in palavra_secreta]
    forca_atual = ''.join(forca_atual1)

    while(True):
        print(f'Letras erradas: {tentativas_erradas}')
        chute = input('Tente acertar uma letra: ')
        index = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if letra.lower() == chute.lower():
                    forca_atual1[index] = chute
                    forca_atual = ''.join(forca_atual1)
                    print(f'Erros restantes: {7 - tentativas}')
                index += 1
        else:
            print(f'Errou! Erros restantes: {7 - tentativas}')
            tentativas_erradas.append(chute)
            tentativas += 1
        if '_' not in forca_atual1:
            print(f'Parabéns! Você acertou a palavra secreta: {palavra_secreta}')
            break
        print(f"Palavra: {forca_atual}")
        if tentativas > 7:
            print(f'Tentativas esgotadas! Você perdeu! A palavra era {palavra_secreta}')
            break


if(__name__ == '__main__'):
    jogar()