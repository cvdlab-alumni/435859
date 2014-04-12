# homework 2 - exercise 3 - Marco Virgadamo - 435859

from exercise2 import *

beige = colorRGB([204,178,154])
grass = colorRGB([119,127,72])

upper_plan = T(3)(-0.05)(COLOR(grass)(DIFFERENCE([
	T(1)(-80)(CUBOID([160,100,0.05])),
	T(1)(-9)(CUBOID([18,16,0.05])),
	T(1)(-12)(CUBOID([24,6,0.05]))
	])))
lower_plan = COLOR(beige)(T([1,2,3])([-80,-40,-6])(CUBOID([160,40])))
plans_wall = T([1,3])([-80,-0.05])(R([1,3])(-PI/2)(PROD([CUBOID([6,6]),QUOTE([68,-24,68])])))

terrain = STRUCT([upper_plan,lower_plan,plans_wall])

semicircle = T(2)(22)(MAP(sphere1)(PROD([INTERVALS(PI)(32), QUOTE([25])])))

Vcs = [[-25,0],[-12,0],[-12,6],[-25,6],[-10,6],[-10,16],[-25,16],[10,16],[25,16],[25,22],[-25,22],[10,6],[12,6],[25,6],[12,0],[25,0]]
FVcs = [[0,1,2,3],[3,4,5,6],[6,8,9,10],[11,13,8,7],[14,15,13,12]]
larCentralStreets = Vcs,FVcs
centralStreets = STRUCT(MKPOLS(larCentralStreets))

Vws = [[-50,16],[-25,16],[-25,22],[-50,22],[-50,47],[-80,47],[-80,16]]
FVws = [[0,1,2,3],[0,4,5,6]]
larWestStreets = Vws,FVws
westStreets = STRUCT(MKPOLS(larWestStreets))

larNorthStreet = [[-2,46],[2,46],[2,76],[-2,76]],LIST(range(4))
northStreet = STRUCT(MKPOLS(larNorthStreet))
northCircle = T(2)(83)(MAP(sphere1)(PROD([INTERVALS(2*PI)(32), QUOTE([8])])))

Ves = [[2,53],[40,34],[40,22],[76,22],[76,75],[40,75],[40,38],[2,57]]
FVes = [[0,1,6,7],[2,3,4,5]]
larEastStreets = Ves,FVes
eastStreets = STRUCT(MKPOLS(larEastStreets))


streets = COLOR(colorRGB([203,195,187]))(extrudeZ(0.05)(STRUCT([semicircle, centralStreets, westStreets, northStreet, northCircle, eastStreets])))

def house(width,lenght,body_height,roof_height,body_color,roof_color):
	body = CUBOID([width,lenght,body_height])
	Vroof = [[0,0],[width,0],[float(width)/2,roof_height]]
	FVroof = LIST(range(3))
	flatRoof = STRUCT(MKPOLS((Vroof,FVroof)))
	roof = T([2,3])([lenght,body_height])(R([2,3])(PI/2)(extrudeZ(lenght)(flatRoof)))
	final = STRUCT([
		COLOR(body_color)(body),
		COLOR(roof_color)(roof)
	])
	return final

house1 = house(6,10,5,2,lightGrey,colorRGB([189,122,112]))
house2 = house(6,10,10,2,lightGrey,beige)

Vh3 = [[3,0,0],[6,0,0],[9,3,0],[9,6,0],[6,9,0],[3,9,0],[0,6,0],[0,3,0],[3,0,3],[6,0,3],[9,3,3],[9,6,3],[6,9,3],[3,9,3],[0,6,3],[0,3,3],[3,3,4],[6,3,4],[6,6,4],[3,6,4]]
FVh3 = LIST(range(20))
larHouse3 = Vh3,FVh3
house3 = COLOR(colorRGB([88,111,108]))(STRUCT(MKPOLS(larHouse3)))

house4 = house(6,10,3,1.5,lightGrey,colorRGB([189,122,112]))

house5_body = COLOR(lightGrey)(extrudeZ(6)(MAP(sphere1)(PROD([INTERVALS(2*PI)(64), QUOTE([5])]))))
house5_roof = COLOR(colorRGB([52,47,49]))(extrudeZ(1)(MAP(sphere1)(PROD([INTERVALS(2*PI)(64), QUOTE([5])]))))
house5 = STRUCT([house5_body,T(3)(6)(house5_roof)])

houses = STRUCT([
	T([1,2])([-40,22])(R([1,2])(PI/2)(house1)),
	T([1,2])([-65,36])(R([1,2])(PI/2)(house2)),
	T([1,2])([-65,70])(house3),
	T([1,2])([60,60])(R([1,2])(-PI/8)(house4)),
	T([1,2])([50,50])(house5),
	])

area = STRUCT([
	T([1,2,3])([10,16,-6])(R([1,2])(PI)(complete_building_3D)),
	terrain,
	streets,
	houses
	])

VIEW(area)