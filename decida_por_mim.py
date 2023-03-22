# Programa 3 - Decida por mim!
# Objetivo: Faça uma pergunta para o programa e ele terá que te dar uma resposta
import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza você deve fazer isso!',
            'Putz, não sei hein?!',
            'Não sei, você que sabe.',
            'Acho que não é o momento.',
            'Claro que sim!'
        ]
        
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim')]
        ]
        # criar a janela
        self.janela = sg.Window('Decida por Mim!',layout=layout)
        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.Read()
            # Fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
    
decida = DecidaPorMim()
decida.Iniciar()