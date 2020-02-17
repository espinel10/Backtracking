import turtle
import os
import time
import sys
import random
############################################################
class Node:
    def __init__(self, label, parent):
        self.label = label
        self.mov='p'
        self.bandera=0
        self.left = None
        self.right = None
        self.parent = parent
        self.dx=0
        self.dy=0

        # Métodos para asignar nodos
    def setDx(self,dx):
         self.dx=dx

    def getDx(self):
        return self.dx

    def setDy(self,dy):
         self.dy=dy
    def getDy(self):
        return self.dy
    def getLabel(self):
        return self.label
    def setLabel(self, label):
        self.label = label

    def setMov(self, mov):
        self.mov = mov

    def getMov(self):
        return self.mov

    def setBandera(self, bandera):
         self.bandera=bandera

    def getBandera(self):
        return self.bandera


    def getMov(self):
        return self.mov

    def getMov(self):
        return self.mov
    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

##########################################################################################
class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):
        # Creamos un nuevo nodo
        new_node = Node(label, None)
        # Si el árbol esta vacio
        if self.empty():
            self.root = new_node
        else:
            # Si el árbol no esta vacio
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                if new_node.getLabel() < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            new_node.setParent(parent_node)

    # Operación de borrado
    def delete(self, label):
        if (not self.empty()):
            node = self.getNode(label)
            if(node is not None):
                if(node.getLeft() is None and node.getRight() is None):
                    self.__reassignNodes(node, None)
                    node = None
                elif(node.getLeft() is None and node.getRight() is not None):
                    self.__reassignNodes(node, node.getRight())
                elif(node.getLeft() is not None and node.getRight() is None):
                    self.__reassignNodes(node, node.getLeft())
                else:
                    tmpNode = self.getMax(node.getLeft())
                    self.delete(tmpNode.getLabel())
                    node.setLabel(tmpNode.getLabel())

    def getNode(self, label):
        curr_node = None
        if(not self.empty()):
            curr_node = self.getRoot()
            while curr_node is not None and curr_node.getLabel() is not label:
                if label < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
        return curr_node

    def getRoot(self):
        return self.root


    def getMax(self, root = None):
        if(root is not None):
            curr_node = root
        else:
            curr_node = self.getRoot()
        if(not self.empty()):
            while(curr_node.getRight() is not None):
                curr_node = curr_node.getRight()
        return curr_node

    def getMin(self, root = None):
        if(root is not None):
            curr_node = root
        else:
            curr_node = self.getRoot()
        if(not self.empty()):
            curr_node = self.getRoot()
            while(curr_node.getLeft() is not None):
                curr_node = curr_node.getLeft()
        return curr_node

    def empty(self):
        if self.root is None:
            return True
        return False
    def __InOrderTraversal(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList





################################################################################################################################################################

def aleatorioIntervalo(num,num2):
    return random.uniform(num, num2)


def aleatorio(num):
    if len(num)==2:
        pass
        return num[random.randrange(1)]
    else:
        pass
        return num[0]





def direccion(x,y,Ax,Ay):
    if Ax==x-1 and y==Ay:
        return 'a'
    if Ax==x+1 and y==Ay:
        return 'd'
    if x==Ax and y==Ay-1:
        return 's'
    if x==Ax and y==Ay+1:
        return 'w'

def opuesto(dir):
    if dir=='s':
        pass
        return 'w'
    if dir=='w':
        pass
        return 's'
    if dir=='a':
        pass
        return 'd'
    if dir=='d':
        pass
        return 'a'


def opciones(mapa,x,y,dir):
    num=[]
    if mapa[y+1][x]==0:
        num.append('s')
    if mapa[y][x+1]==0:
        num.append('d')
    if mapa[y-1][x]==0:
        num.append('w')
    if mapa[y][x-1]==0:
        num.append('a')
    num.remove(dir)
    return num








def main():
    arb = BinarySearchTree()
    mapa = [[1,1,1,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,1,0,1],
            [1,0,1,0,1,1,0,0,0,1],
            [1,0,1,0,1,1,1,1,1,1],
            [1,0,1,0,1,1,1,1,1,1],
            [1,0,1,0,1,0,0,0,1,1],
            [1,0,1,0,0,0,1,1,1,1],
            [1,1,1,1,1,0,0,0,1,1],
            [1,1,1,1,1,1,1,0,1,1],
            [1,1,1,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,0,1,0,1],
            [1,0,1,0,1,1,0,0,0,1],
            [1,0,1,0,1,1,1,1,1,1],
            [1,0,1,0,1,1,1,1,1,1],
            [1,0,1,0,1,0,0,0,1,1],
            [1,0,1,0,0,0,1,1,1,1],
            [1,1,1,1,1,0,0,0,1,1],
            [1,1,1,1,1,1,1,0,1,1]]

    x=8
    y=1
    mapa[y][x]=3
    bandera=0
    numero=20
    min=20
    max=20
    arb.insert(20)
    op='w'
    lan=0
    lis=[]
    min=20
    algo=0
    condition=0
    contidion2=0
    conditio3=0
    ns=[]
    while bandera==0:
        pass
        cant=len(opciones(mapa,x,y,op))
        if len(opciones(mapa,x,y,op))==1:
            pass
            if numero==arb.getMin().getLabel():
                pass
                c=aleatorioIntervalo(numero-4,numero)
                arb.insert(c)
                numero=c
                mov=opciones(mapa,x,y,op)
                arb.getNode(numero).setMov(mov[0])
                tecla=arb.getNode(numero).getMov()
                lis.append(tecla)
                op=opuesto(tecla)

            else:
                pass
                aux=numero
                while arb.getNode(aux).getRight()==None:
                    pass
                    aux=arb.getNode(aux).getParent().getLabel()
                c=aleatorioIntervalo(aux,numero)
                numero=c
                arb.insert(numero)
                mov=opciones(mapa,x,y,op)
                ######################################################
                arb.getNode(numero).setMov(mov[0])
                tecla=arb.getNode(numero).getMov()
                lis.append(tecla)
                op=opuesto(tecla)
                numero=c
        elif len(opciones(mapa,x,y,op))==2:
            pass
            if numero==arb.getMin().getLabel():
                pass
                c=aleatorioIntervalo(numero-4,numero)
                arb.insert(c)
                arb.getNode(numero).setBandera(1)
                arb.getNode(numero).setDx(x)
                arb.getNode(numero).setDy(y)
                numero=c
                mov=opciones(mapa,x,y,op)
                ##############################
                arb.getNode(numero).setMov(mov[1])
                ##############################
                tecla=arb.getNode(numero).getMov()
                lis.append(tecla)
                op=opuesto(tecla)


            else:
                pass
                aux=numero
                while arb.getNode(aux).getRight()==None:
                    pass
                    aux=arb.getNode(aux).getParent().getLabel()
                c=aleatorioIntervalo(aux,numero)
                arb.insert(c)
                mov=opciones(mapa,x,y,op)
                ###############################
                ################################
                arb.getNode(numero).setBandera(1)
                arb.getNode(numero).setDx(x)
                arb.getNode(numero).setDy(y)
                numero=c
                arb.getNode(numero).setMov(mov[1])
                tecla=arb.getNode(numero).getMov()
                lis.append(tecla)
                op=opuesto(tecla)

                numero=c



        elif len(opciones(mapa,x,y,op))==0:
            pass
            while arb.getNode(numero).getBandera()==0:
                pass
                numero=arb.getNode(numero).getParent().getLabel()
            mapa[y][x]=0
            x=arb.getNode(numero).getDx()
            y=arb.getNode(numero).getDy()
            mapa[y][x]=3
            aux=arb.getNode(numero).getParent().getLabel()
            c=aleatorioIntervalo(numero,aux)
            op=opuesto(arb.getNode(aux).getMov())
            mov=opciones(mapa,x,y,op)
            arb.insert(c)
            mov.remove(arb.getNode(numero).getLeft().getMov())
            arb.getNode(c).setMov(mov[0])
            numero=c
            tecla=arb.getNode(numero).getMov()
            lis.append(tecla)
            op=opuesto(tecla)


                ######################################
    ##    elif arb.getNode(numero).getBandera()==1:
            ##pass

            ##################################




        if tecla=='s' and mapa[y+1][x]==0:
            pass
            mapa[y][x]=0
            mapa[y+1][x]=3
            y=y+1
        if tecla=='a' and mapa[y][x-1]==0:
            pass
            mapa[y][x]=0
            mapa[y][x-1]=3
            x=x-1
        if tecla=='w' and mapa[y-1][x]==0:
            pass
            mapa[y][x]=0
            mapa[y-1][x]=3
            y=y-1
        if tecla=='d' and mapa[y][x+1]==0:
            pass
            mapa[y][x]=0
            mapa[y][x+1]=3
            x=x+1
        if x==7  and y==17:
            pass
            bandera=1
        time.sleep(0.01)
        mostrar_mapa(mapa)
        print(x,"  ",y)
        print(lis)
        print(op)

        lan=0
    print("######################LO LOGRASTE ##########################")
    exit()


def mostrar_mapa(mapa):
    os.system('cls')

    ###y 9 x 10
    for i in range (0,18):
        for j in range(0,10):
            if mapa[i][j]==3:
                print("X ",end="")
            if mapa[i][j]==1:
                print("# ",end="")
            if mapa[i][j]==0:
                print("  ",end="")
        print()

if __name__ == '__main__':
    main()
