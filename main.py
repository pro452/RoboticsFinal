
map = [[9,9,9,9,9],
       [9,1,1,0,9], # zero representing no obstacle and one representing an obstacle and 9 representing the edge of the obstacle course
       [9,1,0,0,9],
       [9,0,0,1,9],
       [9,9,9,9,9]]

probaility = []

for i in range(len(map)): #Initilize
    probaility.append(1.0/9)

def possibile_locations(Left, Front, Right):
    locations = []
    for x in range(1,4):
        for y in range(1,4):
            print(map[x][y])
            if map[x][y] == 0:
                if map[x][y-1] == Left or map[x][y-1] == 9 and map[x-1][y] == Front or map[x-1][y] == 9 and map[x][y+1] == Right or map[x][y+1] == 9:
                    locations.append(str(x)+str(y))
                elif map[x-1][y] == Left or map[x-1][y] == 9 and map[x][y+1] == Front or map[x][y+1] == 9 and map[x+1][y] == Right or map[x+1][y] == 9:
                    locations.append(str(x)+str(y))
                elif map[x][y+1] == Left or map[x][y+1] == 9 and map[x+1][y] == Front or map[x+1][y] == 9 and map[x][y-1] == Right or map[x][y-1] == 9:
                    locations.append(str(x)+str(y))
                elif map[x+1][y] == Left or map[x+1][y] == 9 and map[x][y-1] == Front or map[x][y-1] == 9 and map[x-1][y] == Right or map[x-1][y] == 9:
                    locations.append(str(x)+str(y))

    return locations

    #input the result from the 3 ultrasonic sensors
    #process: //This is the hard part
    #output possible locations of the robot based upon, the 3 ultrasonic senors

def update_stat():
    print('holder text')
    #input: the output of possible_locations
    #process: using Probabilistic locationlization, update where the robot could be
    #output an updated probablity array

def path_finder():
    print('holder text')
    #input: proablitity array
    #process: using highest probability from the probliity array what is the shortest path to the goal
    #output: Where should robot go next

print(possibile_locations(0,1,0))


