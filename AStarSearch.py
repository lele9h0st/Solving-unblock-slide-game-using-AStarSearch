import collections
from queue import PriorityQueue
import llist
from llist import sllist,sllistnode
import structlinks
from structlinks.DataStructures  import LinkedList
from Node import Node
class AStarSearch:
    hstep=[]
    wstep=[]
    num_frontier=1
    current_num_frontier=1
    def execute(self,root):
        frontier = LinkedList()
        explored=[]
        frontier.append(root)

        while  len(frontier)!=0:
            currentNode=frontier.pop(0)
            self.current_num_frontier+=1
            if currentNode.isFinish():
                print("finish")
                print(currentNode.blocks)
                current=currentNode
                while current!=root:
                    self.hstep.append(current.hStep)
                    self.wstep.append(current.wStep)
                    current=current.parent
                print("+++++++++++++++++++++")
                print(self.hstep)
                print(self.wstep)
                print(current.blocks) 
                print("+++++++++++++++++++++")
                return currentNode
            else:
                explored.append(currentNode)
                
                children=currentNode.getChildren()
                print("+++++++++++++++++"+str(len(children)))
                for child in children:
                    childNode=child.end
                    if (childNode not in explored) and (childNode not in frontier):
                        childNode.parent=currentNode
                        childNode.g=childNode.g+child.weight
                        frontier.append(childNode)
                               
                        self.num_frontier+=1
                        print(self.current_num_frontier)
                        print("========="+str(len(explored)))
                currentNode=None

              
        return None
    def isContain(self,frontier,childNode):
        if len(frontier)==0:
            return True
        for node  in frontier.values():
            if node==childNode:
                return False
        return True
    def getPath(root,goal):
        current=goal
        while current!=root:
            current=current.parent
            print(current.blocks) 




