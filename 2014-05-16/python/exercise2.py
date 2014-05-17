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

def stairs (width,lenght,height,steps):
	stairs = STRUCT([CUBOID([0,0,0])])
	for i in range(steps):
		newStep = T([2,3])([i*float(lenght)/steps,i*float(height)/steps])(CUBOID([width, float(lenght)/steps, (float(height)/steps)]))
		stairs = STRUCT([stairs, newStep])
	return stairs

pianerottolo1 = T(2)(-4.5)(CUBOID([9,4.5,.5]))
stairs1 = T([1,2,3])([6.5,-4.5,0.5])(R([1,2])(PI)(stairs(2.5, 6, 1.75, 10)))
stairs2 = T([1,2,3])([6.5,-10.5,0.5+1.75])(R([1,2])(0)(stairs(2.5, 6, 1.75, 10)))
pianerottolo2 = T([1,2,3])([4,-4.5-6-3,1.75])(CUBOID([5,3,.5]))
pianerottolo = STRUCT([pianerottolo1,stairs1,stairs2,pianerottolo2])
pianerottoli = STRUCT([pianerottolo,T(3)(3.5)]*3+[T([2])([-4.5])(CUBOID([9,4.5,.5]))])

VIEW(STRUCT([blockHpcA,blockHpcB,pianerottoli]))
