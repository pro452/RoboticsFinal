map = [[9,9,5,9,9],
       [9,1,0,0,9], # zero representing no obstacle and one representing an obstacle and 9 representing the edge of the obstacle course
       [9,0,1,0,9],
       [9,0,0,0,9],
       [9,9,9,9,9]]

probaility = []

orientation = 'east'

for i in range(7): #Initilize
    probaility.append(1.0/7)

def possibile_locations(Left, Front, Right):
    probs = []
    for x in range(1,4):
        for y in range(1,4):
            #print(map[x][y])
            #print(orientation)
            if map[x][y] == 0:
                if orientation == 'north':
                    if (map[x][y-1] == Left or (map[x][y-1] == 9 and Left != 0)) and (map[x-1][y] == Front or (map[x-1][y] == 9 and Front != 0)) and (map[x][y+1] == Right or (map[x][y+1] == 9 and Right != 0)):
                        probs.append(str(x)+str(y)+'n')
                        print('wowza/')
                if orientation == 'east':
                    if (map[x-1][y] == Left or (map[x-1][y] == 9 and Left != 0)) and (map[x][y+1] == Front or (map[x][y+1] == 9 and Front != 0)) and (map[x+1][y] == Right or (map[x+1][y] == 9 and Right != 0)):
                        probs.append(str(x)+str(y)+'e')
                        print(str(map[x][y]) + "2")
                if orientation == 'south':
                    if (map[x][y+1] == Left or (map[x][y+1] == 9 and Left != 0)) and (map[x+1][y] == Front or (map[x+1][y] == 9 and Front != 0)) and (map[x][y-1] == Right or (map[x][y-1] == 9 and Right != 0)):
                        probs.append(str(x)+str(y)+'s')
                        print(str(map[x][y]) + "3")
                if orientation == 'west':
                    if (map[x+1][y] == Left or (map[x+1][y] == 9 and Left != 0)) and (map[x][y-1] == Front or (map[x][y-1] == 9 and Front != 0)) and (map[x-1][y] == Right or (map[x-1][y] == 9 and Right != 0)):
                        probs.append(str(x)+str(y)+'w')
                        print(str(map[x][y]) + "4")
    return probs

    #input the result from the 3 ultrasonic sensors
    #process: //This is the hard part
    #output possible locations of the robot based upon, the 3 ultrasonic senors

def update_stat(locations):
    locations_to_add_more_probability = []

    for index in range(len(locations)):
        if locations[index][0] == '1' and locations[index][1] == '2':
            locations_to_add_more_probability.append(0)
        if locations[index][0] == '1' and locations[index][1] == '3':
            locations_to_add_more_probability.append(1)
        if locations[index][0] == '2' and locations[index][1] == '1':
            locations_to_add_more_probability.append(2)
        if locations[index][0] == '2' and locations[index][1] == '3':
            locations_to_add_more_probability.append(3)
        if locations[index][0] == '3' and locations[index][1] == '1':
            locations_to_add_more_probability.append(4)
        if locations[index][0] == '3' and locations[index][1] == '2':
            locations_to_add_more_probability.append(5)
        if locations[index][0] == '3' and locations[index][1] == '3':
            locations_to_add_more_probability.append(6)


    for i in range(len(locations_to_add_more_probability)):  # Initilize
        probaility[locations_to_add_more_probability[i]] += 1.0/len(locations_to_add_more_probability)

    sum = 0

    for index in range(len(probaility)):
        sum += probaility[index]

    for index in range(len(probaility)):
        probaility[index] = probaility[index]/sum

    #print(probaility.index(max(probaility)))
    print(probaility)
    return locations_to_add_more_probability
    #input: the output of possible_locations
    #process: using Probabilistic locationlization, update where the robot could be
    #output an updated probablity array

def path_finder(start_location):

    #start_location = "320"
    counter = 0
    secondmap =[[9,9,9,9,9],
               [9,-1,5,0,9],
               [9,0,-1,0,9],
               [9,0,-1,0,9],
               [9,9,9,9,9]]

    #path_map[start_location] = counter
    list_of_nodes = []
    list_of_nodes.append(start_location)

    goalFound = False

    #This while loops builds the list of possible paths
    #The last character of each item in the list is the distance of steps it is located away from the start_location
    while(not goalFound):
        for index in range(len(list_of_nodes)):
            if int(list_of_nodes[index][2]) == counter:
                x = int(list_of_nodes[index][0])
                y = int(list_of_nodes[index][1])

                if secondmap[x][y-1] == 0 or secondmap[x][y-1] == 5:
                    list_of_nodes.append(str(x) + str(y-1) + str(counter + 1))
                    if secondmap[x][y-1] == 5:
                        goalFound = True
                    secondmap[x][y - 1] = -1
                if secondmap[x][y+1] == 0 or secondmap[x][y+1] == 5:
                    list_of_nodes.append(str(x) + str(y+1) + str(counter + 1))
                    if secondmap[x][y+1] == 5:
                        goalFound = True
                    secondmap[x][y + 1] = -1
                if secondmap[x-1][y] == 0 or secondmap[x-1][y] == 5:
                    list_of_nodes.append(str(x-1) + str(y) + str(counter + 1))
                    if secondmap[x-1][y] == 5:
                        goalFound = True
                    secondmap[x - 1][y] = -1
                if secondmap[x+1][y] == 0 or secondmap[x+1][y] == 5:
                    list_of_nodes.append(str(x+1) + str(y) + str(counter + 1))
                    if secondmap[x+1][y] == 5:
                        goalFound = True
                    secondmap[x + 1][y] = -1

        counter += 1

    #This loop finds where the goal is
    max = 0
    indexOfmaxvalue = -1
    for index in range(len(list_of_nodes)):
        if int(list_of_nodes[index][2]) > int(max):
            indexOfmaxvalue = index
            max = list_of_nodes[index][2]

    pathNeededToTravel = []
    pathNeededToTravel.append(list_of_nodes[indexOfmaxvalue])

    print(list_of_nodes)
    # print(list_of_nodes[indexOfmaxvalue][1])
    # print(int(list_of_nodes[0][1]) - 1)
    # print(list_of_nodes[indexOfmaxvalue][2])
    # print(int(list_of_nodes[0][2]) + 1)

    #This loop creates the path needed for the robot
    while counter > 0:
        for index in range(len(list_of_nodes)):

            maxValueX = int(list_of_nodes[indexOfmaxvalue][0])
            indexX = int(list_of_nodes[index][0])
            maxValueY = int(list_of_nodes[indexOfmaxvalue][1])
            indexY = int(list_of_nodes[index][1])
            maxValueCounter = int(list_of_nodes[indexOfmaxvalue][2])
            indexCounter = int(list_of_nodes[index][2]) + 1

            if maxValueX == indexX and maxValueY == indexY - 1 and maxValueCounter == indexCounter:
                pathNeededToTravel.append(list_of_nodes[index])
                indexOfmaxvalue = index
                counter = counter - 1
                break
            if maxValueX == indexX and maxValueY == indexY + 1 and maxValueCounter == indexCounter:
                pathNeededToTravel.append(list_of_nodes[index])
                indexOfmaxvalue = index
                counter = counter - 1
                break
            if maxValueX == indexX + 1 and maxValueY == indexY and maxValueCounter == indexCounter:
                pathNeededToTravel.append(list_of_nodes[index])
                indexOfmaxvalue = index
                counter = counter - 1
                break
            if maxValueX == indexX - 1 and maxValueY == indexY and maxValueCounter == indexCounter:
                pathNeededToTravel.append(list_of_nodes[index])
                indexOfmaxvalue = index
                counter = counter - 1
                break

    print(pathNeededToTravel)

    #This will figure out what to tell the robot to do next
    xtravel = int(pathNeededToTravel[len(pathNeededToTravel) - 2][0]) - int(pathNeededToTravel[len(pathNeededToTravel) - 1][0])
    ytravel = int(pathNeededToTravel[len(pathNeededToTravel) - 2][1]) - int(pathNeededToTravel[len(pathNeededToTravel) - 1][1])

    if ytravel == 1:
        print("EAST")
    if ytravel == -1:
        print("WEST")
    if xtravel == 1:
        print("SOUTH")
    if xtravel == -1:
        print("NORTH")

    #input: proablitity array
    #process: using highest probability from the probliity array what is the shortest path to the goal
    #output: Where should robot go next

while 1 == 1:
    orientation = input("Orientation: ")
    east = input("East: ")
    north = input("North: ")
    west = input("West: ")

    locations = possibile_locations(int(east),int(north),int(west))
    print(locations)
    print(update_stat(locations))

    start_location = input("Highest prob. location: ")
    path_finder(start_location)
