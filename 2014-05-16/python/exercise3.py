# homework 3 - exercise 3 - Marco Virgadamo - 435859

from larcc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

# funzione per mappamento multiplo. Argomenti: sottodiagramma, lista di celle del sottodiagramma da eliminare, diagramma master, lista di celle del diagramma master in cui mappare il sotto diagramma (i numeri devono essere in riferimento alla numerazione del master originario.
def multipleDiagram2cell(subDiagram,toRemove,master,toMerges):
	subDiagram = subDiagram[0],[cell for k,cell in enumerate(subDiagram[1]) if not (k in toRemove)]
	toMerges = list(sort(toMerges))
	for i in range(len(toMerges)):
		master = diagram2cell(subDiagram,master,toMerges[i]-i)
	return master

# esempio

# creo la struttura master
shape = [7,3,1]
sizePatterns = [[.5,5]*3+[.5],[.5,5,.5],[3]]
master = assemblyDiagramInit(shape)(sizePatterns)
toRemove = [4,10,16]
master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
mV,mCV = master
mVV = [[i] for i in range(len(mV))]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering ((mV,mCV),hpc)(range(len(mCV)),YELLOW,5)
hpc = cellNumbering ((mV,mVV),hpc)(range(len(mVV)),RED,1)
VIEW(hpc)
DRAW(master)

# creo la struttura subDiagram
subShape = [3,1,3]
subSizePatterns = [[1.5,2,1.5],[.5],[1,1,1]]
subDiagram = assemblyDiagramInit(subShape)(subSizePatterns)
sV,sCV = subDiagram
sVV = [[i] for i in range(len(sV))]
shpc = SKEL_1(STRUCT(MKPOLS(subDiagram)))
shpc = cellNumbering ((sV,sCV),shpc)(range(len(sCV)),YELLOW,5)
shpc = cellNumbering ((sV,sVV),shpc)(range(len(sVV)),RED,1)
VIEW(shpc)
# noto che la cella relativa al buco della finesra che voglio fare ha numero 4, me la segno

# applico questo diagramma a multiple celle del master
master = multipleDiagram2cell(subDiagram,[4],master,[3,13,8,4,9,14])

# rivisualizzo il nuovo master
mV,mCV = master
mVV = [[i] for i in range(len(mV))]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering ((mV,mCV),hpc)(range(len(mCV)),YELLOW,5)
hpc = cellNumbering ((mV,mVV),hpc)(range(len(mVV)),RED,1)
VIEW(hpc)
DRAW(master)

