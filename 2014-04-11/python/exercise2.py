# homework 2 - exercise 2 - Marco Virgadamo - 435859

from exercise1 import *

def curveDoor(width):
	def curveDoor1(heigh):
		radius = (float(width)/float(2))
		rectangle = CUBOID([width,(heigh-radius)])
		circle = MAP(sphere1)(PROD( [INTERVALS(2*PI)(32), QUOTE([radius])] ))
		circleT = T([1,2])([radius,(heigh-radius)])(circle)
		return STRUCT([rectangle,circleT])
	return curveDoor1

#north
northBlank = CUBOID([20,20])
northBorders = PROD([QUOTE([20]),QUOTE([-6,1,-5,1,-5,2.1])])
northLateralWindows = PROD([QUOTE([-1,1,-16,1,-1]),QUOTE([-7.5,3,-3,3])])
northCentralWindow = PROD([QUOTE([-9,2,-9]),QUOTE([-15,2])])
northWindows = STRUCT([northLateralWindows,northCentralWindow])
northDoor = T([1,2])([8,6])(curveDoor(4)(8))
northStatue = curveDoor(1)(3)
northStatueA = T([1,2])([5,8])(northStatue)
northStatueB = T([1,2])([14,8])(northStatue)
northStatueC = T([1,2])([5,14])(northStatue)
northStatueD = T([1,2])([14,14])(northStatue)

northStatues = STRUCT([ northStatueA,northStatueB,northStatueC,northStatueD ])

northNeutral = DIFFERENCE([northBlank, northWindows])
north = STRUCT([COLOR(lightGrey)(northNeutral), COLOR(darkGrey)(northBorders), COLOR(brown)(northDoor), COLOR(darkGrey)(northStatues)])

#west
westBlank = CUBOID([18,20])
westBorders = PROD([QUOTE([18]),QUOTE([-6,1,-5,1,-5,2.1])])
westWindows = PROD([QUOTE([-1.71,1]*6),QUOTE([-7.5,3,-3,3])])
westNeutral = DIFFERENCE([westBlank, westWindows])
west = STRUCT([COLOR(lightGrey)(westNeutral), COLOR(darkGrey)(westBorders)])


#westLittle
westLittleBlank = CUBOID([3,20])
westLittleBorders = PROD([QUOTE([3]),QUOTE([-6,1,-5,1,-5,2.1])])
westLittleWindows = PROD([QUOTE([-1,1]),QUOTE([-7.5,3,-3,3])])
westLittleDoor = T(1)(1)(CUBOID([1,3.5]))
westLittleNeutral = DIFFERENCE([westLittleBlank, westLittleWindows, westLittleDoor])
westLittle = STRUCT([COLOR(lightGrey)(westLittleNeutral), COLOR(darkGrey)(westLittleBorders)])

#southLateral
southLateralBlank = CUBOID([6,20])
southLateralBorders = PROD([QUOTE([6]),QUOTE([-6,1,-5,1,-5,2.1])])
southLateralWindows = PROD([QUOTE([-1.33,1]*2),QUOTE([-1.5,3,-3,3,-3,3])])
southLateralNeutral = DIFFERENCE([southLateralBlank, southLateralWindows])
southLateral = STRUCT([COLOR(lightGrey)(southLateralNeutral), COLOR(darkGrey)(southLateralBorders)])

#southCentral
southCentralBlank = CUBOID([8,20])
southCentralBorders = PROD([QUOTE([8]),QUOTE([-6,1,-5,1,-5,2.1])])
southCentralLowWindows = PROD([QUOTE([-1,1,-4,1,-1]),QUOTE([-1.5,3])])
southCentralMidWindow = PROD([QUOTE([-3,2]),QUOTE([-7.5,3])])
southCentralUpWindow = T([1,2])([3,14])(curveDoor(2)(3))
southCentralWindows = STRUCT([southCentralLowWindows,southCentralMidWindow,southCentralUpWindow])

southCentralStatue = curveDoor(1)(3)
southCentralStatueA = T([1,2])([1,8])(southCentralStatue)
southCentralStatueB = T([1,2])([6,8])(southCentralStatue)
southCentralStatueC = T([1,2])([1,14])(southCentralStatue)
southCentralStatueD = T([1,2])([6,14])(southCentralStatue)

southCentralStatues = STRUCT([ southCentralStatueA,southCentralStatueB,southCentralStatueC,southCentralStatueD ])
southCentralDoor = T([1])([3])(curveDoor(2)(5))
southCentralNeutral = DIFFERENCE([southCentralBlank, southCentralWindows, southCentralDoor])
southCentral = STRUCT([COLOR(lightGrey)(southCentralNeutral), COLOR(darkGrey)(southCentralBorders), COLOR(darkGrey)(southCentralStatues)])

#east
east = west

#eastLittle
eastLittle = westLittle

#northBlock
northBlockBlank = CUBOID([8,7])
northBlockBorders = PROD([QUOTE([8]),QUOTE([-6,1.1])])
northBlockWindows = PROD([QUOTE([-1,1,-1.5,1,-1.5,1,-1]),QUOTE([-3,2])])
northBlockNeutral = DIFFERENCE([northBlockBlank, northBlockWindows])
northBlock = STRUCT([COLOR(lightGrey)(northBlockNeutral), COLOR(darkGrey)(northBlockBorders)])

#westBlock
westBlock = northBlock

#eastBlock
eastBlock = northBlock

#southBlock
southBlockBlank = CUBOID([8,7])
southBlockBorders = PROD([QUOTE([8]),QUOTE([-6,1.1])])
southBlockWindows = PROD([QUOTE([-1,1,-4,1,-1]),QUOTE([-3,2])])
southBlockDoor = T([1])([3])(curveDoor(2)(3))
southBlockNeutral = DIFFERENCE([southBlockBlank, southBlockWindows, southBlockDoor])
southBlock = STRUCT([COLOR(lightGrey)(southBlockNeutral), COLOR(darkGrey)(southBlockBorders)])

# 3D enclosures

#north
northNeutral_3D = DIFFERENCE([extrudeZ(1)(northNeutral),extrudeZ(1)(northStatues)])
northBorders_3D = T(3)(-0.2)(extrudeZ(1.4)(northBorders))
northDoor_3D = extrudeZ(1.2)(northDoor)
northStatues_3D = T(3)(0.4)(extrudeZ(0.2)(northStatues))
north_3D = STRUCT([ COLOR(lightGrey)(northNeutral_3D), COLOR(darkGrey)(northBorders_3D), COLOR(darkGrey)(northDoor_3D), COLOR(darkGrey)(northStatues_3D)])

#west
westNeutral_3D = extrudeZ(1)(westNeutral)
westBorders_3D = T(3)(-0.2)(extrudeZ(1.4)(westBorders))
west_3D = STRUCT([COLOR(lightGrey)(westNeutral_3D), COLOR(darkGrey)(westBorders_3D)])

#westLittle
westLittleNeutral_3D = extrudeZ(1)(westLittleNeutral)
westLittleBorders_3D = T(3)(-0.2)(extrudeZ(1.4)(westLittleBorders))
westLittle_3D = STRUCT([COLOR(lightGrey)(westLittleNeutral_3D), COLOR(darkGrey)(westLittleBorders_3D)])

#eastLittle
eastLittle_3D = westLittle_3D

#east
east_3D = west_3D

#southLateral
southLateralNeutral_3D = extrudeZ(1)(southLateralNeutral)
southLateralBorders_3D = T(3)(-0.2)(extrudeZ(1.4)(southLateralBorders))
southLateral_3D = STRUCT([COLOR(lightGrey)(southLateralNeutral_3D), COLOR(darkGrey)(southLateralBorders_3D)])

#southCentral
southCentralNeutral_3D = DIFFERENCE([extrudeZ(1)(southCentralNeutral),extrudeZ(1)(southCentralStatues)])
southCentralBorders_3D = T(3)(-0.2)(extrudeZ(1.4)(southCentralBorders))
southCentralDoor_3D = extrudeZ(1)(southCentralDoor)
southCentralStatues_3D = T(3)(0.4)(extrudeZ(0.2)(southCentralStatues))
southCentral_3D = STRUCT([ COLOR(lightGrey)(southCentralNeutral_3D), COLOR(darkGrey)(southCentralBorders_3D), COLOR(darkGrey)(southCentralStatues_3D)])

#northBlock
northBlockNeutral_3D = extrudeZ(1)(northBlockNeutral)
northBlockBorders_3D = T(3)(-0.2)(extrudeZ(1.4)(northBlockBorders))
northBlock_3D = STRUCT([COLOR(lightGrey)(northBlockNeutral_3D), COLOR(darkGrey)(northBlockBorders_3D)])

#westBlock
westBlock_3D = northBlock_3D

#eastBlock
eastBlock_3D = northBlock_3D

#southBlock
southBlockNeutral_3D = extrudeZ(1)(southBlockNeutral)
southBlockBorders_3D = T(3)(-0.2)(extrudeZ(1.4)(southBlockBorders))
southBlock_3D = STRUCT([COLOR(lightGrey)(southBlockNeutral_3D), COLOR(darkGrey)(southBlockBorders_3D)])

#vertical 3D
verticalNorth_3D = T(2)(0.9)(R([2,3])(PI/2)(north_3D))
verticalEast_3D = R([1,2])(PI/2)(R([2,3])(PI/2)(east_3D))
verticalWest_3D = T(1)(19)(R([1,2])(PI/2)(R([2,3])(PI/2)(west_3D)))
verticalSouthLateral1_3D = T(2)(18)(R([2,3])(PI/2)(southLateral_3D))
verticalSouthLateral2_3D = T([1,2])([14,18])(R([2,3])(PI/2)(southLateral_3D))
verticalSouthCentral_3D = T([1,2])([6,21])(R([2,3])(PI/2)(southCentral_3D))
verticalWestLittle_3D = T([1,2])([6,18])(R([1,2])(PI/2)(R([2,3])(PI/2)(westLittle_3D)))
verticalEastLittle_3D = T([1,2])([13,18])(R([1,2])(PI/2)(R([2,3])(PI/2)(eastLittle_3D)))
verticalNorthBlock_3D = T([1,2,3])([6,6,19])(R([2,3])(PI/2)(northBlock_3D))
verticalWestBlock_3D = T([1,2,3])([13,5,19])(R([1,2])(PI/2)(R([2,3])(PI/2)(westBlock_3D)))
verticalEastBlock_3D = T([1,2,3])([7,13,19])(R([1,2])(PI*1.5)(R([2,3])(PI/2)(eastBlock_3D)))
verticalSouthBlock_3D = T([1,2,3])([14,12,19])(R([1,2])(PI)(R([2,3])(PI/2)(southBlock_3D)))

building = STRUCT([
	internal_model_3D, 
	verticalNorth_3D, 
	verticalWest_3D, 
	verticalEast_3D, 
	verticalSouthLateral1_3D, 
	verticalSouthLateral2_3D, 
	verticalSouthCentral_3D, 
	verticalWestLittle_3D, 
	verticalEastLittle_3D, 
	verticalNorthBlock_3D, 
	verticalWestBlock_3D, 
	verticalEastBlock_3D,
	verticalSouthBlock_3D
	])

def stairs (width,lenght,height,steps):
	stairs = STRUCT([CUBOID([width,lenght,0])])
	for i in range(steps):
		newStep = T(2)(i*float(lenght)/steps)(CUBOID([width, float(lenght)/steps, (float(height)/steps)*i]))
		stairs = STRUCT([stairs, newStep])
	return stairs

pianerottoloW = T([1,2])([20,16])(CUBOID([2,2,3]))
stairsSW = T([1,2])([28,16])(R([1,2])(PI/2)(stairs(2,6,3,15)))
stairsWW = T([1,2,3])([22,16,3])(R([1,2])(PI)(stairs(2,6,3,15)))
stairsW = STRUCT([stairsSW, stairsWW, pianerottoloW])

pianerottoloE = T([1,2])([-2,16])(CUBOID([2,2,3]))
stairsSE = T([1,2])([-8,18])(R([1,2])(PI*1.5)(stairs(2,6,3,15)))
stairsEE = T([1,2,3])([0,16,3])(R([1,2])(PI)(stairs(2,6,3,15)))
stairsE = STRUCT([stairsSE, stairsEE, pianerottoloE])

frontal_stairs = T([1,2])([6,21])(CUBOID([8,0.5,0.5]))

stairs_all = STRUCT([stairsW,stairsE,frontal_stairs])

complete_building_3D = STRUCT([
	building,
	stairs_all,

	])
	
#VIEW(complete_building_3D)

