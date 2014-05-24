# homework 3 - exercise 1 - Marco Virgadamo - 435859

from larcc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

def fastCellNumbering(model):
	return cellNumbering(model,SKEL_1(STRUCT(MKPOLS(model))))(range(len(model[1])),CYAN,1.5)

def multipleDiagram2cell(subDiagram,toRemove,master,toMerges):
	subDiagram = subDiagram[0],[cell for k,cell in enumerate(subDiagram[1]) if not (k in toRemove)]
	toMerges = list(sort(toMerges))
	toMerges.reverse()
	for i in range(len(toMerges)):
		master = diagram2cell(subDiagram,master,toMerges[i])
	return master

shape = [1,1,2]
sizePatterns = [[.4+4+.1+2+.1+1+.1+1+.1+2.5+.4+1.5+.4],[.4+1.5+.1+1.5+.1+2+.1+1.5+.1+1.5+.4+2+0.4],[0.5,3]]
master = assemblyDiagramInit(shape)(sizePatterns)

shape = [5,3,1]
sizePatterns = [[.4,4,.1,2+.1+1+.1+1+.1+2.5+.4+1.5,.4],[.4,1.5+.1+1.5+.1+2+.1+1.5+.1+1.5+.4+2,0.4],[3]]
division = assemblyDiagramInit(shape)(sizePatterns)
master = diagram2cell(division,master,1)

shape = [1,3,1]
sizePatterns = [[4],[1.5+.1+1.5+.1+2+.1+1.5+.1+1.5,.4,2],[3]]
balconeSala = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(balconeSala,[],master,[2,5,8])

shape = [1,3,1]
sizePatterns = [[2+.1+1+.1+1+.1+2.5+.4+1.5],[1.5+.1+1.5+.1+2,.1,1.5+.1+1.5+.4+2],[3]]
giornoNotte = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(giornoNotte,[],master,[8,11])

shape = [5,1,1]
sizePatterns = [[2,.1,1+.1+1+.1+2.5,.4,1.5],[1.5+.1+1.5+.1+2],[3]]
cucinaBalcone = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(cucinaBalcone,[],master,[23])

shape = [1,3,1]
sizePatterns = [[1+.1+1+.1+2.5],[1.5+.1+1.5,.1,2],[3]]
cucinaBagno = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(cucinaBagno,[],master,[27,28])

shape = [3,1,1]
sizePatterns = [[1,.1,1+.1+2.5],[1.5+.1+1.5+.1+2],[3]]
armadio = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(armadio,[],master,[33])

shape = [3,1,1]
sizePatterns = [[2+.1+1+.1+1,.1,2.5+.4+1.5],[1.5+.1+1.5+.4+2],[3]]
camere = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(camere,[],master,[23,24,8])

shape = [1,3,1]
sizePatterns = [[2+.1+1+.1+1],[1.5,.1,1.5+.4+2],[3]]
cameretta = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(cameretta,[],master,[33,34])

shape = [1,3,1]
sizePatterns = [[2],[1.5,.1,1.5+.1+2],[3]]
bagnetto = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(bagnetto,[],master,[22])

shape = [3,1,1]
sizePatterns = [[2,.1,1+.1+1],[.1],[3]]
corridoio = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(corridoio,[],master,[33])

toRemove = [13,15,44,46,47,41,43,27,31,32,23]
master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

ringhiera = assemblyDiagramInit([1,1,3])([[1],[1],[1,.1,1.9]])
master = multipleDiagram2cell(ringhiera,[0,2],master,[16,4,17])

shape = [1,3,1]
sizePatterns = [[.1],[1.5+.1,1.5,.1+2+.1+1.5+.1+1.5],[3]]
muroSalone = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(muroSalone,[],master,[9])

shape = [1,3,1]
sizePatterns = [[.1],[1.5+.1,1.5,.1+2],[3]]
muroCucina = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(muroCucina,[],master,[16])

shape = [2,1,1]
sizePatterns = [[1+.1,1],[.1],[3]]
muroBagno = assemblyDiagramInit(shape)(sizePatterns)
master = multipleDiagram2cell(muroBagno,[],master,[33])

quarantaSessantaX = assemblyDiagramInit([2,1,1])([[.5+1+.1,1.9+.5],[0.4],[3]])
master = multipleDiagram2cell(quarantaSessantaX,[],master,[11,30])

sessantaQuarantaX = assemblyDiagramInit([2,1,1])([[1.9+.5,.5+1+.1],[0.4],[3]])
master = multipleDiagram2cell(sessantaQuarantaX,[],master,[3,23,25])

sessantaQuarantaY = assemblyDiagramInit([1,2,1])([[0.4],[1.9+.5,.5+1+.1],[3]])
master = multipleDiagram2cell(sessantaQuarantaY,[],master,[14])

cornicePortaY = assemblyDiagramInit([1,3,2])([[0.1],[.15,.7,.15],[2.2,0.8]])
master = multipleDiagram2cell(cornicePortaY,[],master,[9,31,34,22,48])

cornicePortaX = assemblyDiagramInit([3,1,2])([[.15,.7,.15],[0.1],[2.2,0.8]])
master = multipleDiagram2cell(cornicePortaX,[],master,[43,36,23,34])

corniceFinestreX = assemblyDiagramInit([3,1,3])([[.1,.8,.1],[0.4],[1,1.2,0.8]])
master = multipleDiagram2cell(corniceFinestreX,[],master,[34,35,36,37])

corniceFinestreY = assemblyDiagramInit([1,3,3])([[0.4],[.1,.8,.1],[1,1.2,0.8]])
master = multipleDiagram2cell(corniceFinestreY,[],master,[14])

cornicePortaBagno = assemblyDiagramInit([1,1,2])([[1],[1],[2.2,0.8]])
master = multipleDiagram2cell(cornicePortaBagno,[],master,[31])

portaX = assemblyDiagramInit([3,3,5])([[1,5,1],[1,1,1],[1,4,2,5,1]])
toRemovePortaX = [0,1,2,3,4,15,16,17,18,19,30,31,32,33,34,21,23,10,11,12,13,14,25,26,27,28,29,40,41,42,43,44]
master = multipleDiagram2cell(portaX,toRemovePortaX,master,[67,73,85,79,134])

portaY = assemblyDiagramInit([3,3,5])([[1,1,1],[1,5,1],[1,4,2,5,1]])
toRemovePortaY = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,21,23,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]
master = multipleDiagram2cell(portaY,toRemovePortaY,master,[49,61,43,55,37])

finestraX = assemblyDiagramInit([5,3,5])([[1,4,1,4,1],[1,1,1],[1,3,1,3,1]])
toRemoveFinestraX = [0,1,2,3,4,15,16,17,18,19,30,31,32,33,34,45,46,47,48,49,60,61,62,63,64,21,23,51,53,10,11,12,13,14,25,26,27,28,29,40,41,42,43,44,55,56,57,58,59,70,71,72,73,74]
master = multipleDiagram2cell(finestraX,toRemoveFinestraX,master,[111,84,102,93])

finestraY = assemblyDiagramInit([3,5,5])([[1,1,1],[1,4,1,4,1],[1,3,1,3,1]])
toRemoveFinestraY = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,31,33,41,43,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74]
master = multipleDiagram2cell(finestraY,toRemoveFinestraY,master,[116])

VIEW(STRUCT([fastCellNumbering(master)]))
DRAW(master)