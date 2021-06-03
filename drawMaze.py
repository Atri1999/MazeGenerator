from random import random
import Maze
import pygame
import sys

W,H=500,500
WIDTH,HEIGHT=20,20
Grid_Width,Grid_Height=W//WIDTH, H//HEIGHT
WHITE=(255,255,255)
BLACK=(0,0,0)
win=pygame.display.set_mode(((W//WIDTH)*(W//WIDTH),(H//HEIGHT)*(H//HEIGHT)))                    
pygame.display.set_caption("Maze")
clock=pygame.time.Clock()
FPS=1

def drawfill(x,y,x1,y1):
    if x==x1:
        if y1==y-1:
            x1,y1=(x1)*(Grid_Width),(y1)*(Grid_Height)
            pygame.draw.rect(win,(200,200,200),pygame.Rect(x1+2,y1+(Grid_Height//2),Grid_Width-4,Grid_Height-4))
        
        if y1==y+1:
            x1,y1=(x1)*(Grid_Width),(y1)*(Grid_Height)
            pygame.draw.rect(win,(200,200,200),pygame.Rect(x1+2,y1-(Grid_Height//2),Grid_Width-4,Grid_Height-4))

    if y==y1:
        if x1==x-1:
            x1,y1=(x1)*(Grid_Width),(y1)*(Grid_Height)
            pygame.draw.rect(win,(200,200,200),pygame.Rect(x1+(Grid_Width//2),y1+2,Grid_Width-4,Grid_Height-4))
        
        if x1==x+1:
            x1,y1=(x1)*(Grid_Width),(y1)*(Grid_Height)
            pygame.draw.rect(win,(200,200,200),pygame.Rect(x1-(Grid_Width//2),y1+2,Grid_Width-4,Grid_Height-4))


    pygame.display.update()

def drawCube(x,y,color=(200,200,200)):
    pygame.time.delay(20)
    x1,y1=(x)*(Grid_Width),(y)*(Grid_Height)
    #x2,y2=(x+1)*(Grid_Width),(y+1)*(Grid_Height)
    #pygame.draw.rect(win,(120,0,0),pygame.Rect(x1,y1,Grid_Width,Grid_Height),2)
    pygame.draw.rect(win,color,pygame.Rect(x1+2,y1+2,Grid_Width-4,Grid_Height-4))
    pygame.display.update()


def drawGrid(color=(0,128,0)):
    for i in range(1,WIDTH+1):
        x=i*(Grid_Width)
        pygame.draw.line(win,color,(x,0),(x,H))
    for i in range(1,HEIGHT+1):
        y=i*(Grid_Height)
        pygame.draw.line(win,color,(0,y),(W,y))
    pygame.display.update()

def drawDFS(stack):
    pygame.time.delay(500)
    for node in stack:
        #print(node)
        drawCube(node[0],node[1],color=(10,100,10))
        

def main():
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():     #quiting function
            if event.type==pygame.QUIT:
                run=False
            
    pygame.quit()
    sys.exit()


if __name__=="__main__":


    pygame.init()

    maze=Maze.Maze(Grid_Width,Grid_Height)
    
    #drawGrid()
    
    #drawfill(2,3,2,2)
    #drawfill(2,3,2,4)
    #drawfill(2,3,3,3)
    #drawfill(2,3,1,3)
    maze.makeMaze(int(random()*Grid_Width),int(random()*Grid_Height))    
    #drawCube(20,20,color=(120,0,0))
    input()
    maze.depthFirstSearch(0,0,Grid_Width-1,Grid_Height-1)


    main()
    

