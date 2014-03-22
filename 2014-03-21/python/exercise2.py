

def colorRGB(rgb):
	r,g,b = rgb
	return [float(r)/255,float(g)/255,float(b)/255]


lightGrey = colorRGB([224,228,227])
darkGrey = colorRGB([161,161,161])
brown = colorRGB([125,73,0])

def sphere1(p):
	a,r = p
	return [r*COS(a),r*SIN(a)]

def curveDoor(width):
	def curveDoor1(heigh):
		radius = (float(width)/float(2))
		rectangle = CUBOID([width,(heigh-radius)])
		circle = MAP(sphere1)(PROD( [INTERVALS(2*PI)(32), QUOTE([radius])] ))
		circleT = T([1,2])([radius,(heigh-radius)])(circle)
		return STRUCT([rectangle,circleT])
	return curveDoor1
	
	
# exercise1	

roomsColor = [0.643,0.552,0.376]
# common elements

bigBase = PROD([QUOTE([20]),QUOTE([18])])
littleBase = PROD([QUOTE([-6,8,-6]),QUOTE([-18,3])])
baseFloor = STRUCT([bigBase, littleBase])


def sphere1(p):
	a,r = p
	return [r*COS(a),r*SIN(a)]
circularRoom = T([1,2])([10,9])(MAP(sphere1)(PROD([INTERVALS(2*PI)(32), Q(3)])))

internalLongWalls = PROD([QUOTE([-6,1,-6,1,-6]), QUOTE([-1,17])])
centralSquare = PROD([QUOTE([-7,6,-7]),QUOTE([-5,8])])
centralRooms = PROD([QUOTE([-7,6,-7]),QUOTE([-1,4,-8,7,-1])])

# floor 0

horizWalls0 = PROD([QUOTE([-1,5,-8,5,-1]),QUOTE([-5,1])])
internalWalls0temp = STRUCT([internalLongWalls,centralSquare,horizWalls0])

door0a = PROD([QUOTE([-6,1]),QUOTE([-4,1])])
door0b = PROD([QUOTE([-13,1]),QUOTE([-1,1])])
door0c = PROD([QUOTE([-18,1]),QUOTE([-5,1])])
door0de = PROD([QUOTE([-6,1.2,-5.6,1.2]),QUOTE([-8.5,1])])
door0f = PROD([QUOTE([-9.5,1]),QUOTE([-11.8,1.2])])
door0gh = PROD([QUOTE([-6,1,-6,1]),QUOTE([-13,1])])

doors0 = STRUCT([door0a, door0b, door0c, door0de, door0f, door0gh])

internalWalls0 = DIFFERENCE([internalWalls0temp, circularRoom, doors0])

lateralRooms0 = PROD([QUOTE([-1,5,-8,5,-1]),QUOTE([-1,4,-1,11,-1])])
rooms0 = STRUCT([centralRooms,lateralRooms0,circularRoom])

floor0 = STRUCT([baseFloor, COLOR([0.5,0.5,0.5])(internalWalls0), COLOR(roomsColor)(rooms0)])

# floor 1

horizWall1a = PROD([QUOTE([-1,5]),QUOTE([-7.5,1])])
horizWall1b = PROD([QUOTE([-14,5]),QUOTE([-10.5,1])])
horizWall1c = PROD([QUOTE([-14,5]),QUOTE([-5,1])])
horizWalls1 = STRUCT([horizWall1a,horizWall1b,horizWall1c])
internalWalls1temp = STRUCT([internalLongWalls,centralSquare,horizWalls1])

door1a = PROD([QUOTE([-13,1]),QUOTE([-2.5,1])])
door1bc = PROD([QUOTE([-15,1]),QUOTE([-5,1,-4.5,1])])
door1de = PROD([QUOTE([-9.5,1]),QUOTE([-5,1.2,-5.6,1.2])])
door1fg = PROD([QUOTE([-6,1.2,-5.6,1.2]),QUOTE([-8.5,1])])
door1hi = PROD([QUOTE([-6,1,-6,1]),QUOTE([-14,1])])
door1j = PROD([QUOTE([-1,1]),QUOTE([-7.5,1])])

doors1 = STRUCT([door1a, door1bc, door1de, door1fg, door1hi, door1j])

internalWalls1 = DIFFERENCE([internalWalls1temp, circularRoom, doors1])

lateralRooms1left = PROD([QUOTE([-1,5]),QUOTE([-1,6.5,-1,8.5,-1])])
lateralRooms1right = PROD([QUOTE([-14,5,-1]),QUOTE([-1,4,-1,4.5,-1,5.5])])
lateralRooms1 = STRUCT([lateralRooms1left,lateralRooms1right])
rooms1 = STRUCT([centralRooms,lateralRooms1,circularRoom])

floor1 = STRUCT([baseFloor, COLOR([0.5,0.5,0.5])(internalWalls1), COLOR(roomsColor)(rooms1)])

floor2 = floor1

floor3 = baseFloor

two_and_half_model = STRUCT([floor0, T(3)(6)(floor1), T(3)(12)(floor2), T(3)(18)(floor3)])

#exercise 2

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

#mock up 3D
verticalNorth = R([2,3])(PI/2)(north)
verticalWest = R([1,2])(PI/2)(R([2,3])(PI/2)(west))
verticalEast = T(1)(20)(R([1,2])(PI/2)(R([2,3])(PI/2)(west)))
verticalSouthLateral1 = T(2)(18)(R([2,3])(PI/2)(southLateral))
verticalSouthLateral2 = T([1,2])([14,18])(R([2,3])(PI/2)(southLateral))
verticalSouthCentral = T([1,2])([6,21])(R([2,3])(PI/2)(southCentral))
verticalWestLittle = T([1,2])([6,18])(R([1,2])(PI/2)(R([2,3])(PI/2)(westLittle)))
verticalEastLittle = T([1,2])([14,18])(R([1,2])(PI/2)(R([2,3])(PI/2)(eastLittle)))
mock_up_3D = STRUCT([two_and_half_model, verticalNorth, verticalWest, verticalEast, verticalSouthLateral1, verticalSouthLateral2, verticalSouthCentral, verticalWestLittle, verticalEastLittle])
VIEW(mock_up_3D)