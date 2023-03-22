# Projeto 2 - Chute o número
# Objetivo: Criar um algoritmo que gera um número aleatório e o usuário tem que chutar um número até acertar
import random
import PySimpleGUI as sg
class ChuteUmNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.TentarNovamente = True
        
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Chute um número',size=(39,0))],
            [sg.Input(size=(20,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(39,10))]
        ]
        # Criar uma janela
        self.janela = sg.Window('Chute um número!',layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # Receber os valores
                self.evento, self.valores = self.janela.Read()
                # Fazer alguma coisa com estes valores
                if self.evento == 'Chutar!':
                    self.valor_usuario = self.valores['ValorChute']
                    while self.TentarNovamente == True:
                        if int(self.valor_usuario) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valor_usuario) < self.valor_aleatorio: 
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valor_usuario) == self.valor_aleatorio:
                            self.TentarNovamente = False
                            print('PARABÉNS, VOCÊ ACERTOU!!!')
                            break
        except:
            print('Valor digitado inválido! Informe apenas números!')
            self.Iniciar()


    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteUmNumero()
chute.Iniciar()
