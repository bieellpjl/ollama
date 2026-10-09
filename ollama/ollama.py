import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}Sparda e Eva {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}Absorver o dano no momento exato para carregar um contra-ataque {os.linesep} ')
    elif resposta == '3':
        print(f'{os.linesep}{nome} Rebellion e Yamato {os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} Nero {os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome} Arkham se disfarçava de Jester para abrir o portal para o submundo {os.linesep}')
        exit()

    else: 
        print('Digite apenas 1, 2, 3, 4, 5 para finalizar o programa.')



def start():
    #Apresentar o ChatBot
    print('olá! Bem-Vindo ao Oxetech curiosidades')

    #Pedir o nome do jogador:
    nome = input('Digite o seu nome: ')

    #Pedir o email do jogador
    email = input('Digite o seu E-mail : ')
    while True:
        #Oferecer o menu de opções
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}'
                f'[1] - quem são os pais biológicos dos irmãos gêmeos Dante e Vergil? {os.linesep}'
                f'[2] - No Devil May Cry 3, qual é a principal mecânica e vantagem do estilo de luta "Royalguard"? {os.linesep} '
                f'[3] - Qual par de espadas demoníacas representa as lâminas assinaturas de Dante e Vergil, respectivamente? {os.linesep}'
                f'[4] - Introduzido em Devil May Cry 4, qual jovem cavaleiro da Ordem da Espada é revelado mais tarde como o filho biológico de Vergil? {os.linesep}'
                f'[5] - No Devil May Cry 3, qual é a identidade real do chefe "Jester", o palhaço misterioso que fica zombando de Dante ao longo da torre Temen-ni-gru?{os.linesep}'
         )
        processar_resposta(resposta, nome)
if __name__ == '__main__':
    start()


