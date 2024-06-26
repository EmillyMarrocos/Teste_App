'''# Widgets Básicos: GridLayout
# Criando um GridLayout
# Adicionando Widgets
# Espaçamento e Alinhamento
# Expandindo e Reduzindo Células
# Exemplo Prático

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MinhaApp(App):
    def build(self):
        layout = GridLayout(cols=2, spacing=[10, 10], padding=[20, 20])
        for i in range():
            botao= Button(text='Botão {}'.format(i+1))
            layout.add_widget(botao)
            return layout
        
MinhaApp().run()'''

# Criando um menu com Gridlayout e BoxLayout

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        # Layout Principal
        layout_principal = GridLayout(cols=2)

        # Coluna à esquerda (30% da tela)
        coluna_esquerda = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        menu_itens= ['Arquivo', 'Editar','Seleção', 'Ver', 'Acessar', 'Sair']
        label1= Label(text='Menu')
        coluna_esquerda.add_widget(label1) 
        for item in menu_itens:
            botao= Button(text=item)
            coluna_esquerda.add_widget(botao)
        
        # Coluna à direita dividida em três partes iguais
        coluna_direita= GridLayout(cols= 1, rows= 3)
        for i in range(3):
            botao= Button(text= 'Botão {}'.format(i+7))
            coluna_direita.add_widget(botao)

        # Adicionando as colunas ao layout principal
        layout_principal.add_widget(coluna_esquerda)
        layout_principal.add_widget(coluna_direita)
        return layout_principal
    
if __name__ == "__main__":
    MinhaApp().run()
