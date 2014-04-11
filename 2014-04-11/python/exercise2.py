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
northBorders = PROD([QUOTE([20]),QUOTE([-6,1,-5,1,-5,2])])
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
westBorders = PROD([QUOTE([18]),QUOTE([-6,1,-5,1,-5,2])])
westWindows = PROD([QUOTE([-1.71,1]*6),QUOTE([-7.5,3,-3,3])])
westNeutral = DIFFERENCE([westBlank, westWindows])
west = STRUCT([COLOR(lightGrey)(westNeutral), COLOR(darkGrey)(westBorders)])


#westLittle

westLittleBlank = CUBOID([3,20])
westLittleBorders = PROD([QUOTE([3]),QUOTE([-6,1,-5,1,-5,2])])
westLittleWindows = PROD([QUOTE([-1,1]),QUOTE([-7.5,3,-3,3])])
westLittleDoor = T(1)(1)(CUBOID([1,2.5]))
westLittleNeutral = DIFFERENCE([westLittleBlank, westLittleWindows, westLittleDoor])
westLittle = STRUCT([COLOR(lightGrey)(westLittleNeutral), COLOR(darkGrey)(westLittleBorders)])

#southLateral

southLateralBlank = CUBOID([6,20])
southLateralBorders = PROD([QUOTE([6]),QUOTE([-6,1,-5,1,-5,2])])
southLateralWindows = PROD([QUOTE([-1.33,1]*2),QUOTE([-1.5,3,-3,3,-3,3])])
southLateralNeutral = DIFFERENCE([southLateralBlank, southLateralWindows])
southLateral = STRUCT([COLOR(lightGrey)(southLateralNeutral), COLOR(darkGrey)(southLateralBorders)])

#southCentral

southCentralBlank = CUBOID([8,20])
southCentralBorders = PROD([QUOTE([8]),QUOTE([-6,1,-5,1,-5,2])])
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

#vertical 3D enclosures

#north

northNeutral_3D = extrudeZ(1)(northNeutral)
northBorders_3D = extrudeZ(1)(northBorders)
northDoor_3D = extrudeZ(1.1)(northDoor)
northStatues_3D = extrudeZ(1)(northStatues)
north_3D = STRUCT([ COLOR(lightGrey)(northNeutral_3D), COLOR(darkGrey)(northBorders_3D), COLOR(brown)(northDoor_3D), COLOR(darkGrey)(northStatues_3D)])

#west

westNeutral_3D = extrudeZ(1)(westNeutral)
westBorders_3D = extrudeZ(1)(westBorders)
west_3D = STRUCT([COLOR(lightGrey)(westNeutral_3D), COLOR(darkGrey)(westBorders_3D)])

#westLittle
westLittleNeutral_3D = extrudeZ(1)(westLittleNeutral)
westLittleBorders_3D = extrudeZ(1)(westLittleBorders)
westLittle_3D = STRUCT([COLOR(lightGrey)(westLittleNeutral_3D), COLOR(darkGrey)(westLittleBorders_3D)])

#eastLittle
eastLittle_3D = westLittle_3D

#east
east_3D = west_3D

#southLateral
southLateralNeutral_3D = extrudeZ(1)(southLateralNeutral)
southLateralBorders_3D = extrudeZ(1)(southLateralBorders)
southLateral_3D = STRUCT([COLOR(lightGrey)(southLateralNeutral_3D), COLOR(darkGrey)(southLateralBorders_3D)])

#southCentral
southCentralNeutral_3D = extrudeZ(1)(southCentralNeutral)
southCentralBorders_3D = extrudeZ(1)(southCentralBorders)
southCentralDoor_3D = extrudeZ(1)(southCentralDoor)
southCentralStatues_3D = extrudeZ(1)(southCentralStatues)
southCentral_3D = STRUCT([ COLOR(lightGrey)(southCentralNeutral_3D), COLOR(darkGrey)(southCentralBorders_3D), COLOR(darkGrey)(southCentralStatues_3D)])

verticalNorth_3D = T(2)(0.9)(R([2,3])(PI/2)(north_3D))
verticalEast_3D = R([1,2])(PI/2)(R([2,3])(PI/2)(east_3D))
verticalWest_3D = T(1)(19)(R([1,2])(PI/2)(R([2,3])(PI/2)(west_3D)))
verticalSouthLateral1_3D = T(2)(18)(R([2,3])(PI/2)(southLateral_3D))
verticalSouthLateral2_3D = T([1,2])([14,18])(R([2,3])(PI/2)(southLateral_3D))
verticalSouthCentral_3D = T([1,2])([6,21])(R([2,3])(PI/2)(southCentral_3D))
verticalWestLittle_3D = T([1,2])([6,18])(R([1,2])(PI/2)(R([2,3])(PI/2)(westLittle_3D)))
verticalEastLittle_3D = T([1,2])([13,18])(R([1,2])(PI/2)(R([2,3])(PI/2)(eastLittle_3D)))

solid_model_3D = STRUCT([internal_model_3D, verticalNorth_3D, verticalWest_3D, verticalEast_3D, verticalSouthLateral1_3D, verticalSouthLateral2_3D, verticalSouthCentral_3D, verticalWestLittle_3D, verticalEastLittle_3D])

VIEW(solid_model_3D)