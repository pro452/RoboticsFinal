#This file was written entirely by Michael Matthews

map = [[9,9,9,9,9,9,9,9],
       [9,1,0,1,0,1,1,9], # zero representing no obstacle and one representing an obstacle and nine representing the edge of the obstacle course
       [9,1,0,0,0,1,1,9],
       [9,1,1,0,1,1,1,9],
       [9,1,1,0,0,1,1,9],
       [9,9,9,9,9,9,9,9]]

probaility = []
orientation = 'east'

for i in range(8): #Initilize
    probaility.append(1.0/8)

#This function determines where the robot could be base upon its sensors detecting wether or not an obstacle is next to it or not
def possibile_locations(Left, Front, Right):
    probs = []
    for x in range(1,5):
        for y in range(1,7):
            if map[x][y] == 0:
                if orientation == 'north':
                    if (map[x][y-1] == Left or (map[x][y-1] == 9 and Left != 0)) and (map[x-1][y] == Front or (map[x-1][y] == 9 and Front != 0)) and (map[x][y+1] == Right or (map[x][y+1] == 9 and Right != 0)):
                        probs.append(str(x)+str(y)+'n')
                if orientation == 'east':
                    if (map[x-1][y] == Left or (map[x-1][y] == 9 and Left != 0)) and (map[x][y+1] == Front or (map[x][y+1] == 9 and Front != 0)) and (map[x+1][y] == Right or (map[x+1][y] == 9 and Right != 0)):
                        probs.append(str(x)+str(y)+'e')
                if orientation == 'south':
                    if (map[x][y+1] == Left or (map[x][y+1] == 9 and Left != 0)) and (map[x+1][y] == Front or (map[x+1][y] == 9 and Front != 0)) and (map[x][y-1] == Right or (map[x][y-1] == 9 and Right != 0)):
                        probs.append(str(x)+str(y)+'s')
                if orientation == 'west':
                    if (map[x+1][y] == Left or (map[x+1][y] == 9 and Left != 0)) and (map[x][y-1] == Front or (map[x][y-1] == 9 and Front != 0)) and (map[x-1][y] == Right or (map[x-1][y] == 9 and Right != 0)):
                        probs.append(str(x)+str(y)+'w')
    return probs

#This function updates the probablistic model so that it can approximate where it is currently located
def update_stat(locations):
    locations_to_add_more_probability = []

    for index in range(len(locations)):
        if locations[index][0] == '1' and locations[index][1] == '2':
            locations_to_add_more_probability.append(0)
        if locations[index][0] == '1' and locations[index][1] == '4':
            locations_to_add_more_probability.append(1)
        if locations[index][0] == '2' and locations[index][1] == '2':
            locations_to_add_more_probability.append(2)
        if locations[index][0] == '2' and locations[index][1] == '3':
            locations_to_add_more_probability.append(3)
        if locations[index][0] == '2' and locations[index][1] == '4':
            locations_to_add_more_probability.append(4)
        if locations[index][0] == '3' and locations[index][1] == '3':
            locations_to_add_more_probability.append(5)
        if locations[index][0] == '4' and locations[index][1] == '3':
            locations_to_add_more_probability.append(6)
        if locations[index][0] == '4' and locations[index][1] == '4':
            locations_to_add_more_probability.append(7)

    for i in range(len(locations_to_add_more_probability)):
        probaility[locations_to_add_more_probability[i]] += 1.0/len(locations_to_add_more_probability)

    sum = 0

    for index in range(len(probaility)):
        sum += probaility[index]

    for index in range(len(probaility)):
        probaility[index] = probaility[index]/sum

    return locations_to_add_more_probability

#This function finds the path to the goal based upon where the robot thinks its located and tells the robot which direction to go to
def path_finder(start_location):

    counter = 0
    secondmap=[[9,9,9,9,9,9,9,9],
               [9,-1, 0,-1, 5,-1,-1,9],
               [9,-1, 0, 0, 0,-1,-1,9],
               [9,-1,-1, 0,-1,-1,-1,9],
               [9,-1,-1, 0, 0,-1,-1,9],
               [9,9,9,9,9,9,9,9]]

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

    indexOfmaxvalue = -1

    pathNeededToTravel = []

    pathNeededToTravel.append("14" + str(counter)) #Where the goal is located

    for index in range(len(list_of_nodes)):
        if int(list_of_nodes[index][0]) == 1 and int(list_of_nodes[index][1]) == 4:
           indexOfmaxvalue = index

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

    #This will figure out what to tell the robot to do next
    xtravel = int(pathNeededToTravel[len(pathNeededToTravel) - 2][0]) - int(pathNeededToTravel[len(pathNeededToTravel) - 1][0])
    ytravel = int(pathNeededToTravel[len(pathNeededToTravel) - 2][1]) - int(pathNeededToTravel[len(pathNeededToTravel) - 1][1])

    if ytravel == 1:
        return "EAST"
    if ytravel == -1:
        return "WEST"
    if xtravel == 1:
        return "SOUTH"
    if xtravel == -1:
        return "NORTH"

listOfPrevSteps = []

while 1 == 1:
    orientation = input("Orientation: ")
    east = input("East: ")
    north = input("North: ")
    west = input("West: ")
    steps = 0

    locations = possibile_locations(int(east),int(north),int(west))
    highestProbLocation = update_stat(locations)

    #This function figures out where the robot is located
    def findStartlocation():
        start_location = -1
        if highestProbLocation[0] == 0:
            start_location = 120
        if highestProbLocation[0] == 1:
            start_location = 140
        if highestProbLocation[0] == 2:
            start_location = 220
        if highestProbLocation[0] == 3:
            start_location = 230
        if highestProbLocation[0] == 4:
            start_location = 240
        if highestProbLocation[0] == 5:
            start_location = 330
        if highestProbLocation[0] == 6:
            start_location = 430
        if highestProbLocation[0] == 7:
            start_location = 440

        return start_location

    start_location = findStartlocation()
    whichDirectionToMove = path_finder(str(start_location))
    listOfPrevSteps.append(whichDirectionToMove)
    print(whichDirectionToMove)
    remove = input("Remove? ")

    if remove == 'yes':
        highestProbLocation.pop(0)
        start_location = findStartlocation()
        path_finder(str(start_location))
