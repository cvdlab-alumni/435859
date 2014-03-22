from exercise2 import *

def extrudeZ(heigh):
	def extrudeZ1(obj):
		return PROD([obj, QUOTE([heigh])])
	return extrudeZ1
	
#exercise 3

circularRoom_3D = extrudeZ(6)(circularRoom)
centralRooms_3D = extrudeZ(1)(centralRooms)
baseFloor_3D = extrudeZ(1)(baseFloor)

#floor0 3d

internalWalls0temp_3D = extrudeZ(6)(internalWalls0temp)

doors0_3D = extrudeZ(3)(doors0)

internalWalls0_3D = DIFFERENCE([internalWalls0temp_3D, circularRoom_3D, doors0_3D])

lateralRooms0_3D = extrudeZ(1)(lateralRooms0)

rooms0_3D = STRUCT([centralRooms_3D,lateralRooms0_3D])

floor0_3D = STRUCT([baseFloor_3D, COLOR([0.5,0.5,0.5])(internalWalls0_3D), COLOR(roomsColor)(rooms0_3D)])

#floor1 3d

internalWalls1temp_3D = extrudeZ(6)(internalWalls1temp)

doors1_3D = extrudeZ(3)(doors1)

internalWalls1_3D = DIFFERENCE([internalWalls1temp_3D, circularRoom_3D, doors1_3D])

lateralRooms1_3D = extrudeZ(1)(lateralRooms1)

rooms1_3D = STRUCT([centralRooms_3D,lateralRooms1_3D])

floor1_3D = STRUCT([baseFloor_3D, COLOR([0.5,0.5,0.5])(internalWalls1_3D), COLOR(roomsColor)(rooms1_3D)])

#floor2 3d
floor2_3D = floor1_3D

#floor3 3d
floor3_3D = STRUCT([baseFloor_3D])

internal_model_3D = STRUCT([floor0_3D, T(3)(6)(floor1_3D), T(3)(12)(floor2_3D), T(3)(18)(floor3_3D)])

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

street = DIFFERENCE([T([1,2])([-15,-10])(CUBOID([50,20,6])),CUBOID([20,20,20])])
solid_model_3D = STRUCT([street, internal_model_3D, verticalNorth_3D, verticalWest_3D, verticalEast_3D, verticalSouthLateral1_3D, verticalSouthLateral2_3D, verticalSouthCentral_3D, verticalWestLittle_3D, verticalEastLittle_3D])

#VIEW(solid_model_3D)