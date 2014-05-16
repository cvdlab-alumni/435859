# homework 3 - exercise 2

from exercise1 import *

shapeA = [1,1,5]
sizePatternsA = [[13.6],[11.6],[3.5]*4+[0.5]]
blockA = assemblyDiagramInit(shapeA)(sizePatternsA)

blockA = diagram2cell(master,blockA,0)
blockA = diagram2cell(master,blockA,0)
blockA = diagram2cell(master,blockA,0)
blockA = diagram2cell(master,blockA,0)



blockHpcA = STRUCT(MKPOLS(blockA))
blockHpcB = T(1)(9)(R([1,2])(-PI/2)(blockHpcA))


VIEW(STRUCT([blockHpcA,blockHpcB,blockHpcC]))
