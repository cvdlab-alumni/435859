# homework 3 - exercise 2 - Marco Virgadamo - 435859

from exercise1 import *

def colorRGB(rgb):
	r,g,b = rgb
	return [float(r)/255,float(g)/255,float(b)/255]
	
verde = colorRGB([0,100,0])
marrone = colorRGB([92,64,51])
grigio_chiaro = colorRGB([158,158,158])
grigio_scuro = colorRGB([97,97,97])

def stairs (width,lenght,height,steps):
	stairs = STRUCT([CUBOID([0,0,0])])
	for i in range(steps):
		newStep = T([2,3])([i*float(lenght)/steps,i*float(height)/steps])(CUBOID([width, float(lenght)/steps, (float(height)/steps)]))
		stairs = STRUCT([stairs, newStep])
	return stairs

def bezCurve(controlpoints):
	dom = larDomain([32])
	mapping = larBezierCurve(controlpoints)
	obj = MKPOLS(larMap(mapping)(dom))
	return obj

def extrudeZ(heigh):
	def extrudeZ1(obj):
		return PROD([obj, QUOTE([heigh])])
	return extrudeZ1
	
def tree(params):
	h,r = params
	var = h-r
	tronco = STRUCT([CYLINDER([0.5,var])(32)])
	chioma = T(3)(var)(STRUCT([SPHERE(r)([16,16])]))
	
	final = STRUCT([
		COLOR(marrone)(tronco),
		COLOR(verde)(chioma)
		])
	return final

shapeA = [1,1,5]
sizePatternsA = [[13.6],[11.6],[3.5]*4+[0.5]]
blockA = assemblyDiagramInit(shapeA)(sizePatternsA)

blockA = diagram2cell(master,blockA,0)
blockA = diagram2cell(master,blockA,0)
blockA = diagram2cell(master,blockA,0)
blockA = diagram2cell(master,blockA,0)

blockHpcA = STRUCT(MKPOLS(blockA))
blockHpcB = T(1)(9)(R([1,2])(-PI/2)(blockHpcA))

pianerottolo1 = T(2)(-4.5)(CUBOID([9,4.5,.5]))
stairs1 = T([1,2,3])([6.5,-4.5,0.5])(R([1,2])(PI)(stairs(2.5, 6, 1.75, 10)))
stairs2 = T([1,2,3])([6.5,-10.5,0.5+1.75])(R([1,2])(0)(stairs(2.5, 6, 1.75, 10)))
pianerottolo2 = T([1,2,3])([4,-4.5-6-3,1.75])(CUBOID([5,3,.5]))
pianerottolo = STRUCT([pianerottolo1,stairs1,stairs2,pianerottolo2])
pianerottoli = STRUCT([pianerottolo,T(3)(3.5)]*3+[T([2])([-4.5])(CUBOID([9,4.5,.5]))])

cortile = T([1,2])([-15,-4.5])(CUBOID([15,16.1,.5]))

latoAiuola1 = [POLYLINE([[0,3.5],[0,0],[3.5,0]])]
curvaAiuola1 = bezCurve([[0,3.5],[3.5,3.5],[3.5,0]])
aiuola1 = T([1,2,3])([-1,0,0.5])(R([1,2])(PI/2)(COLOR(verde)(extrudeZ(0.2)(SOLIDIFY(STRUCT(latoAiuola1+curvaAiuola1))))))

domainGiardino = larDomain([48,48])
curvaGiardino1 = larBezierCurve([[0,0,0],[0,0,0],[8,0,0],[8,0,0]])
curvaGiardino2 = larBezierCurve([[0,3,0],[3,3,6],[6,3,0],[8,3,0]])
curvaGiardino3 = larBezierCurve([[0,6,0],[3,6,0],[6,6,0],[8,6,0]])
curvaGiardino4 = larBezierCurve([[0,9,0],[0,9,0],[8,9,0],[8,9,0]])

mapGiardino = BEZIER(S2)([curvaGiardino1,curvaGiardino2,curvaGiardino3,curvaGiardino4])
modelGiardino = STRUCT(MKPOLS(larMap(mapGiardino)(domainGiardino)))
giardino = T([1,2,3])([-15,0,0.5])(COLOR(verde)(modelGiardino))

albero1 = T([1,2,3])([-13,3,1])(tree([15,5]))
albero2 = T([1,2,3])([-10,7,.5])(tree([10,3]))

curvaPanchina1 = bezCurve([[1.56, 4.19], [1.94, 3.96], [2.41, 3.7], [2.41, 4.56]])
curvaPanchina2 = bezCurve([[2.41, 4.56], [2.42, 5.42], [1.84, 5.45], [2.26, 5.87]])
curvaPanchina3 = bezCurve([[2.26, 5.87], [2.94, 6.55], [1.37, 6.79], [1.47, 6.29]])
curvaPanchina4 = bezCurve([[1.47, 6.29], [1.57, 5.83], [1.09, 4.47], [1.56, 4.19]])
curvaPanchina = S([1,2])([1.8,1.8])(STRUCT(curvaPanchina1+curvaPanchina2+curvaPanchina3+curvaPanchina4))
pianoPanchina = T([1,2,3])([1,17,1.2])(R([1,2])(PI)(COLOR(grigio_chiaro)(extrudeZ(0.1)(SOLIDIFY(curvaPanchina)))))
zampa = T(3)(.5)(CUBOID([1,1,0.7]))
zampa1 = COLOR(grigio_scuro)(T([1,2])([-3,8.5])(zampa))
zampa2 = COLOR(grigio_scuro)(T([1,2])([-3,5.5])(zampa))
panchina = STRUCT([pianoPanchina,zampa1,zampa2])

edifici = STRUCT([blockHpcA,blockHpcB,pianerottoli])

VIEW(STRUCT([edifici,cortile,aiuola1,giardino,albero1,albero2,panchina]))

