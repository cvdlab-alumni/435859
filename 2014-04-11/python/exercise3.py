# homework 2 - exercise 3 - Marco Virgadamo - 435859

from exercise2 import *

upper_plan = DIFFERENCE([
	T(1)(-80)(CUBOID([160,140])),
	T(1)(-9)(CUBOID([18,16])),
	T(1)(-12)(CUBOID([24,6]))
	])
lower_plan = T([1,2,3])([-80,-40,-6])(CUBOID([160,40]))

plans_wall = T(1)(-80)(R([1,3])(-PI/2)(PROD([CUBOID([6,6]),QUOTE([68,-24,68])])))

area = STRUCT([
	T([1,2,3])([10,16,-6])(R([1,2])(PI)(complete_building_3D)),
	upper_plan,
	lower_plan,
	plans_wall
	])

VIEW(area)
	

