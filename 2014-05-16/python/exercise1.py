# homework 3 - exercise 1

from larcc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

shape = [13,13,2]
sizePatterns = [[.4,4,.1,2,.1,1,.1,1,.1,2.5,.4,1.5,.4],[.4,1.5,.1,1.5,.1,2,.1,1.5,.1,1.5,.4,2,0.4],[0.5,3]]

master = assemblyDiagramInit(shape)(sizePatterns)
V,CV = master

# svuoto stanze
toRemoveSala = [29,31,33,35,37,39,41,43,45,49]
toRemoveCorridoio = [81,85,87,89,91,93,97,99,101]
toRemoveCorridoio2 = [119,145,171,197]
toRemoveCucina = [133,135,137,159,161,163,185,187,189,211,213,215,237,239,241,289,291,293,295,297]
toRemoveBagno = [193,219,245]
toRemoveCamera1 = [123,149,175,201,125,151,177,203,127,153,179,205]
toRemoveCamera2 = [249,251,253,255,257,275,277,279,281,283,301,303,305,307,309]
toRemove = toRemoveSala + toRemoveCorridoio + toRemoveCorridoio2 + toRemoveCucina + toRemoveBagno + toRemoveCamera1 + toRemoveCamera2
master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

# rifinisco celle
portaX = assemblyDiagramInit([3,1,2])([[.15,.7,.15],[0.1],[2.2,0.8]])
portaX = portaX[0],[cell for k,cell in enumerate(portaX[1]) if not (k in [2])]
master = diagram2cell(portaX,master,72)
master = diagram2cell(portaX,master,78)
master = diagram2cell(portaX,master,152)

portaY = assemblyDiagramInit([1,3,2])([[0.1],[.15,.7,.15],[2.2,0.8]])
portaY = portaY[0],[cell for k,cell in enumerate(portaY[1]) if not (k in [2])]
master = diagram2cell(portaY,master,49)
master = diagram2cell(portaY,master,89)
master = diagram2cell(portaY,master,200)
master = diagram2cell(portaY,master,64)
master = diagram2cell(portaY,master,168)

ingressoX = assemblyDiagramInit([3,1,2])([[2,1.3,.7],[0.4],[2.2,0.8]])
ingressoX = ingressoX[0],[cell for k,cell in enumerate(ingressoX[1]) if not (k in [2])]
master = diagram2cell(ingressoX,master,27)

finestreSalaX = assemblyDiagramInit([5,1,3])([[.5,1,.1,1.9,.5],[0.4],[1,1.2,0.8]])
finestreSalaX = finestreSalaX[0],[cell for k,cell in enumerate(finestreSalaX[1]) if not (k in [3,4,10])]
master = diagram2cell(finestreSalaX,master,37)

finestreX = assemblyDiagramInit([3,1,3])([[.1,.8,.1],[0.4],[1,1.2,0.8]])
finestreX = finestreX[0],[cell for k,cell in enumerate(finestreX[1]) if not (k in [4])]
master = diagram2cell(finestreX,master,78)
master = diagram2cell(finestreX,master,191)
master = diagram2cell(finestreX,master,226)

finestreY = assemblyDiagramInit([1,3,3])([[0.4],[.1,.8,.1],[1,1.2,0.8]])
finestreY = finestreY[0],[cell for k,cell in enumerate(finestreY[1]) if not (k in [4])]
master = diagram2cell(finestreY,master,201)

ringhiera = assemblyDiagramInit([1,1,3])([[1],[1],[1,.1,1.9]])
ringhiera = ringhiera[0],[cell for k,cell in enumerate(ringhiera[1]) if not (k in [0,2])]
master = diagram2cell(ringhiera,master,23)
master = diagram2cell(ringhiera,master,38)
master = diagram2cell(ringhiera,master,226)
master = diagram2cell(ringhiera,master,227)
master = diagram2cell(ringhiera,master,228)
master = diagram2cell(ringhiera,master,229)
master = diagram2cell(ringhiera,master,230)

#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1.5)
#VIEW(STRUCT([hpc,SKEL_1(CUBOID([13.6,11.6,3.5]))]))