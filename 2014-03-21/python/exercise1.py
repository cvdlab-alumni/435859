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
#VIEW(two_and_half_model)

