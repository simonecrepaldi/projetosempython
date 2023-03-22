# Projeto 2 - Chute o número
# Objetivo: Criar um algoritmo que gera um número aleatório e o usuário tem que chutar um número até acertar
import random

class ChuteUmNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.TentarNovamente = True
        
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.TentarNovamente == True:
                if int(self.valor_usuario) > self.valor_aleatorio:
                    print('Chute um valor mais baixo!')
                    self.PedirValorAleatorio()
                elif int(self.valor_usuario) < self.valor_aleatorio: 
                    print('Chute um valor mais alto!')
                    self.PedirValorAleatorio()
                if int(self.valor_usuario) == self.valor_aleatorio:
                    self.TentarNovamente = False
                    print('PARABÉNS, VOCÊ ACERTOU!!!')
        except:
            print('Valor digitado inválido! Informe apenas números!')

            
    def PedirValorAleatorio(self):
        self.valor_usuario = input('Chute um número de 1 a 100: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteUmNumero()
chute.Iniciar()
