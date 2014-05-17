# homework 3 - exercise 4 - Marco Virgadamo - 435859

from larcc import *

def diagram2cell(diagram,master,cell):

   # manipolo il diagram per farlo delle dimensioni esatte, e nella posizione esatta
   mat = diagram2cellMatrix(diagram)(master,cell)
   diagram =larApply(mat)(diagram)  
   
   # elimino dalle celle del master la cella target
   master = master[0],[c for k,c in enumerate(master[1]) if k != cell]
   
   """
   # yet to finish coding
   masterBoundaryFaces = boundaryOfChain(CV,FV)([cell])
   diagramBoundaryFaces = lar2boundaryFaces(CV,FV)
   """
   
   # metto insieme i vertici e le celle senza duplicati
   V, CV1, CV2, n12 = vertexSieve(master,diagram)
   master = V, CV1+CV2
   return master
   
DRAW = COMP([VIEW,STRUCT,MKPOLS])

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


master = diagram2cell(subDiagram,master,3)

# rivisualizzo il nuovo master, notando che non ci sono vertici duplicati sovrapposti.
mV,mCV = master
mVV = [[i] for i in range(len(mV))]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering ((mV,mCV),hpc)(range(len(mCV)),YELLOW,5)
hpc = cellNumbering ((mV,mVV),hpc)(range(len(mVV)),RED,1)
VIEW(hpc)