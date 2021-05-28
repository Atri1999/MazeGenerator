import random
import drawMaze as dm

class Node:
    def __init__(self) -> None:
        self.value=0
        self.visited=False
        self.connected=[]

class Maze:
    def __init__(self,width,height) -> None:
        
        self.WIDTH=width
        self.HEIGHT=height
        self.Platform=[]
        for i in range(width):
            temp=[]
            for j in range(height):
                temp.append(Node())
            self.Platform.append(temp)

    def chooseRandom(self,x,y):
        l=[[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        #print(l)
        if x==0:
            l.remove([x-1,y])
        if x>=self.WIDTH-1:
            l.remove([x+1,y])
        
        if y==0:
            l.remove([x,y-1])
        if y>=self.HEIGHT-1:
            l.remove([x,y+1])
        #print(l)
        #print(len(l))
        res=[]
        i=0

        #self.printPlatform()
        while(i<len(l)):
            tx=l[i][0]
            ty=l[i][1]
            #print(tx,ty)
            if self.Platform[tx][ty].value==0:
                res.append(l[i])
            #print(res)
            i+=1

        #print(res)
        if len(res)==0:
            return None
        if len(res)==1:
            return res[0]
        
        res=list(random.choice(tuple(res)))
        return res

    def makeMaze(self,x,y):
        self.Platform[x][y].value=1
        dm.drawCube(x,y)
        #self.printPlatform()
        node=self.chooseRandom(x,y)
        #print(node)
        while node!=None:
            #print(node[0],node[1])
            self.Platform[x][y].connected.append(node)
            self.Platform[node[0]][node[1]].connected.append([x,y])
            dm.drawfill(x,y,node[0],node[1])
            #self.printPlatform()
            self.makeMaze(node[0],node[1])
            node=self.chooseRandom(x,y)

        return


    def printPlatform(self):
        for rows in self.Platform:
            for column in rows:
                print(column.value,end=" ")
                #print(column.connected,end=" ")
            print()
        print()

    def tempFunc(self,x,y):
        self.Platform[x][y].value=1


if __name__=="__main__":

    maze=Maze(5,5)
    #print(type(maze.Platform[0][0]))
    #maze.printPlatform()
    
    #maze.printPlatform()
    #print(maze.chooseRandom(0,0))
    maze.makeMaze(3,2)
    maze.printPlatform()



