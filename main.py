map = [1,1,0,
       1,0,0,
       0,0,1]

probaility = []

for i in range(len(map)):
    probaility.append(1.0/len(map))

def possibile_locations():
    #input the result from the 3 ultrasonic sensors
    #process: //This is the hard part
    #output possible locations of the robot based upon, the 3 ultrasonic senors

def update_stat():
    #input: the output of possible_locations
    #process: using Probabilistic locationlization, update where the robot could be
    #output an updated probablity array

def path_finder():
    #input: proablitity array
    #process: using highest probability from the probliity array what is the shortest path to the goal
    #output: Where should robot go next



