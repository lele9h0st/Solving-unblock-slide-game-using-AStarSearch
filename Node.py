import this
import copy
from numpy import block
from Edge import Edge


class Node:
    
    parent=None
    blocks=[[]]
    g=0
    def __init__(self,blocks):
        self.blocks=blocks
       
    def __init__(self,blocks,h):
        self.blocks=blocks
        self.h=h
    
    def __init__(self,blocks,wStep,hStep):
        self.blocks=blocks
        self.wStep=wStep
        self.hStep=hStep
        self.children=[]

    def addEdge(self,that,cost):
        edge=Edge(this,that,cost)
        self.children.append(edge)

    def addEdge(self,that):
        edge=Edge(this,that)
        self.children.append(edge)
    def getChildren(self):
        self.generateChildren()
        return self.children
    def generateChildren(self):
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                if self.blocks[i][j]==0:
                    clone=copy.deepcopy(self.blocks)
                    hp=""
                    wp=""
                    if j>1 and (clone[i][j-1]<=10 and clone[i][j-1]>0 or clone[i][j-1]==100):
                        clone[i][j] = clone[i][j - 1]
                        clone[i][j - 1] = clone[i][j - 2]
                        if j - 3 >= 0 and clone[i][j - 3] == clone[i][j]:
                            clone[i][j - 2] = clone[i][j - 3]
                            clone[i][j - 3] = 0
                        else:
                            clone[i][j - 2] = 0
                        wp = str(j) + "-" + str(j - 1)
                        hp = str(i) + "-" + str(i)
                        n=Node(clone,wp,hp)
                        self.addEdge(n)
                    clone=copy.deepcopy(self.blocks)
                    if j<5 and (clone[i][j+1]<=10 and clone[i][j+1]>0 or clone[i][j+1]==100):
                        clone[i][j] = clone[i][j + 1]
                        clone[i][j + 1] = clone[i][j + 2]
                        if j + 3 <len(clone[0]) and clone[i][j + 3] == clone[i][j]:
                            clone[i][j + 2] = clone[i][j+ 3]
                            clone[i][j + 3] = 0
                        else:
                            clone[i][j + 2] = 0
                        wp = str(j) + "-" + str(j + 1)
                        hp = str(i) + "-" + str(i)
                        n=Node(clone,wp,hp)
                        self.addEdge(n)

                    clone=copy.deepcopy(self.blocks)
                    if i>1 and clone[i-1][j]>10 and clone[i-1][j]!=100:
                        clone[i][j]=clone[i-1][j]
                        clone[i-1][j]=clone[i-2][j]
                        if i-3>=0 and clone[i-3][j]==clone[i][j]:
                            clone[i - 2][j] = clone[i - 3][j]
                            clone[i - 3][j] = 0
                        else:
                            clone[i - 2][j] = 0
                        wp = str(j) + "-" + str(j)
                        hp= str(i) + "-" + str(i - 1)
                        n=Node(clone,wp,hp)
                        self.addEdge(n)
                    clone=copy.deepcopy(self.blocks)
                    if i<5 and clone[i+1][j]>10 and clone[i+1][j]!=100:
                        clone[i][j]=clone[i+1][j]
                        clone[i+1][j]=clone[i+2][j]
                        if i+3< len(clone[0]) and clone[i+3][j]==clone[i][j]:
                            clone[i + 2][j] = clone[i + 3][j]
                            clone[i + 3][j] = 0
                        else:
                            clone[i + 2][j] = 0
                        wp = str(j) + "-" + str(j)
                        hp= str(i) + "-" + str(i + 1)
                        n=Node(clone,wp,hp)
                        self.addEdge(n)
    def isFinish(self):
        sum=0
        for i in range(5,0,-1):
            if self.blocks[2][i]==100:
                break
            else:
                sum+=self.blocks[2][i]
        return sum==0
    
    def __eq__(self,  other) :
        if not isinstance(other, Node):
            return False
        if other==None:
            return False
        if self.blocks==None:
            if other.blocks!=None:
                return False
        else:
            for i in range(len(self.blocks)):
                for j in range(len(self.blocks[0])):
                    if self.blocks[i][j]!=other.blocks[i][j]:
                        return False
        return True
    # def __ne__(self, other):
    #     return not (self == other)

    # def __lt__(self, other):
    #     if other==None:
    #         return False
    #     else:
    #         return (self.blocks < other.blocks)and (self.parent < other.parent)

    # def __gt__(self, other):
    #     if other==None:
    #         return False
    #     else:
    #         return (self.blocks > other.blocks) and (self.parent > other.parent)

    # def __le__(self, other):
    #     return (self < other) or (self == other)

    # def __ge__(self, other):
    #     return (self > other) or (self == other)
    def __hash__(self):
        # prime = 31
        # result = 1
        # result = prime * result 
        # if self.blocks != None:
        #     result+=hash(self.blocks)
        # return result
        return hash(self.blocks)