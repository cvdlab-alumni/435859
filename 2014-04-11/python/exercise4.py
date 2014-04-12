# homework 2 - exercise 4 - Marco Virgadamo - 435859

from exercise3 import *

def tree(params):
	h,r = params
	var = h-r
	troncoLar = larCylinder([0.5,var])([32,1])
	chiomaLar = larSphere(r)()
	
	tronco = STRUCT(MKPOLS(troncoLar))
	chioma = T(3)(var)( STRUCT(MKPOLS(chiomaLar)) )
	final = STRUCT([
		COLOR(brown)(tronco),
		COLOR(colorRGB([49,51,29]))(chioma)
		])
	return final

trees = STRUCT([
	T([1,2])([-25,25])(tree([6,2])),
	T([1,2])([-26,15])(tree([6,2])),
	T([1,2])([-36,13])(tree([6,2])),
	T([1,2])([-46,14])(tree([6,2])),
	T([1,2])([-56,12])(tree([6,2])),
	T([1,2])([-66,13])(tree([8,3])),
	T([1,2])([-40,60])(tree([6,2])),
	T([1,2])([-26,50])(tree([6,2])),
	T([1,2])([-36,45])(tree([6,2])),
	T([1,2])([-46,49])(tree([6,2])),
	T([1,2])([-56,54])(tree([6,2])),
	T([1,2])([-66,48])(tree([6,2])),
	T([1,2])([-75,94])(tree([6,2])),
	T([1,2])([-65,96])(tree([8,3])),
	T([1,2])([-59,94])(tree([6,2])),
	T([1,2])([-50,92])(tree([6,2])),
	T([1,2])([-50,82])(tree([6,2])),
	T([1,2])([-25,90])(tree([6,2])),
	T([1,2])([-35,67])(tree([6,2])),
	T([1,2])([-24,64])(tree([8,3])),
	T([1,2])([-15,80])(tree([8,3])),
	T([1,2])([-13,58])(tree([6,2])),
	T([1,2])([-26,60])(tree([6,2])),
	T([1,2])([-39,63])(tree([6,2])),
	T([1,2])([-48,65])(tree([6,2])),
	
	T([1,2])([15,94])(tree([6,2])),
	T([1,2])([20,88])(tree([6,2])),
	T([1,2])([38,96])(tree([6,2])),
	T([1,2])([52,93])(tree([8,3])),
	T([1,2])([70,82])(tree([6,2])),
	
	T([1,2])([50,75])(tree([6,2])),
	T([1,2])([30,65])(tree([6,2])),
	T([1,2])([28,55])(tree([8,3])),
	T([1,2])([26,33])(tree([8,3])),
	T([1,2])([20,50])(tree([6,2])),
	T([1,2])([10,58])(tree([6,2])),
	T([1,2])([6,48])(tree([6,2])),
	
	T([1,2])([28,18])(tree([6,2])),
	T([1,2])([65,15])(tree([8,3])),
	T([1,2])([40,24])(tree([6,2])),
	T([1,2])([45,10])(tree([6,2])),
	T([1,2])([52,15])(tree([8,3])),
	T([1,2])([56,24])(tree([6,2])),
	T([1,2])([70,12])(tree([6,2])),

	])
	
X = float(20)/3
gardenX = QUOTE([-1.5*X,2*X,-X,X,-X,2*X,-X,-2*X,-X,-2*X,-X,2*X,-X,X,-X,2*X,-1.5*X])
Y = float(10)/3
gardenY = QUOTE([-Y,15,-Y,15,-Y])
gardenLateral = PROD([gardenX,gardenY])	

Vcg = [[0,0],[13,0],[13,6],[6,13],[0,13],[20,0],[33,0],[33,13],[27,13],[20,6],[27,20],[33,20],[33,33],[20,33],[20,27],[0,20],[6,20],[13,27],[13,33],[0,33]]
FVcg = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19]]
larCentralGarden = Vcg,FVcg
centralGarden = S(2)(0.8)(T([1,2])([9.5*X,Y])(STRUCT(MKPOLS(larCentralGarden))))

garden2D = STRUCT([gardenLateral,centralGarden])
garden3D = COLOR(colorRGB([0,60,0]))(extrudeZ(2.5)(garden2D))

garden = T([1,2,3])([-80,-40,-6])(garden3D)

water_material = [0.1,0.4,0.47,1,0,0,0,0.6,2,2,2,1,0,0,0,1,50]

fountain_body = extrudeZ(1.5)(MAP(sphere1)(PROD([INTERVALS(2*PI)(32), QUOTE([4])])))
water = MATERIAL(water_material)(T(3)(1)(extrudeZ(0.5)(MAP(sphere1)(PROD([INTERVALS(2*PI)(32), QUOTE([3])])))))
fountain_empty = DIFFERENCE([fountain_body,water])
fountain = T([2,3])([-24,-6])(STRUCT([fountain_empty,water]))

area_with_details = STRUCT([
	area,
	trees,
	garden,
	fountain
	])
	
VIEW(area_with_details)