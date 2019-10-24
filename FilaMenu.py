from Node import No
from Cdados import Dadu
import time

class Fila: 
    def __init__ ( self, head = None):
        self._head = head
    def isEmpty(self):
        if self._head.get_dado() == None:
            return True
        else: print(False)
    def add(self, elem):
        elem.set_proximo(self._head)
        self._head = elem
        return elem.get_dado()
    def remove(self):
        p = self._head
        while p.get_proximo().get_proximo() != None: #penultimo 
            p = p.get_proximo()
        #print(p.get_dado())
        p.set_proximo(None)
    def sizef(self):
        p = self._head
        count = 0 
        while p.get_proximo() != None:
            count+=1
            p = p.get_proximo()
        count+=1
        return count
    def showhead(self):
        p = self._head
        while p.get_proximo() != None:
            p = p.get_proximo()
        return p.get_dado().get_filmeeano()


fil = Fila()
r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar o head
Digite sua opção: 
""")
while (r != '0') :
    if r == "1":
        a = input("Qual FILME você quer adicionar: ")
        b = input("Qual ANO você quer adicionar: ")
        fil.add(No(Dadu(a,b)))
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("O elemento foi adicionado com sucesso!")
        time.sleep(1)
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar o head
Digite sua opção:
""")
    elif r == "2":
        print("...")
        time.sleep(1)
        fil.remove()
        print("O elemento da fila foi removido!")
        time.sleep(1)
        r = input("""
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar o head
Digite sua opção:     
""")
    elif r =="3":
        fil.isEmpty()
        time.sleep(1)
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar o head
Digite sua opção: """)
    elif r == "4":
        print("O tamanho da pilha é: ",fil.sizef())
        time.sleep(1)
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar o head
Digite sua opção:""")
    elif r == "5":
        print("O head é : ",fil.showhead())
        time.sleep((1))
        r = input(""" 
0) sair do Menu
1) adicionar
2) remover
3) Mostrar se está vazia
4) Mostrar tamanho da Fila
5) Mostrar o head
Digite sua opção: """)