# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:

import math, random, pylab, ps11_visualize

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        dirx = math.cos(angle)
        if dirx<=-0.5:
            delta_x = -1
        elif dirx>=0.5:
            delta_x = 1
        else:
            delta_x = 0
        delta_x = int(speed * delta_x)
        diry = math.sin(angle)
        if diry<=-0.5:
            delta_y = -1
        elif diry>=0.5:
            delta_y = 1
        else:
            delta_y = 0
        delta_y = int(speed * delta_y)
        # Add that to the existing position
        new_x = (old_x + delta_x)
        new_y = (old_y + delta_y)
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = int(width)
        self.height = int(height)
        self.tiles = {}
        for i in range (self.width):
            for j in range (self.height):
                self.tiles[(i,j)] = False
                
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x=pos.getX()
        y=pos.getY()
        self.tiles[(x,y)]=True
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[(m,n)]
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return len(self.tiles)
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        res = 0
        for tile in self.tiles.keys():
            if self.tiles[tile]==True:
                res +=1
        return res
    
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x=random.choice(range(self.width))
        y=random.choice(range(self.height))
        return Position(x, y)
        
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        x=pos.getX()
        y=pos.getY()
        return x<self.width and x>=0 and y<self.height and y>=0


class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.d = random.choice(range(361))
        self.p = self.room.getRandomPosition()
        
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.p
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.d
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.p = position
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.d = direction

# never ending loop possible!!!!!!!!!!!!!!! wrong exercise
class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        curr_pos = self.getRobotPosition()
        self.room.cleanTileAtPosition(curr_pos)
        while True:
            new_pos=curr_pos.getNewPosition(self.d, self.speed)
            if self.room.isPositionInRoom(new_pos):
                self.setRobotPosition(new_pos)
                self.setRobotDirection(random.choice(range(361)))
                self.room.cleanTileAtPosition(new_pos)
                break
            else:
                self.setRobotDirection(random.choice(range(361)))


# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    currMin = min_coverage
    res=[]
    for i in range (1, num_trials+1):
        anim = ps11_visualize.RobotVisualization(num_robots, width, height)
        resTrial = []
        room = RectangularRoom(width, height)
        robots=[]
        for j in range (1, num_robots+1):
            robot=robot_type(room,speed)
            robots.append(robot)
##        print('robots:', robots)
##        print('first robot x:', robot.getRobotPosition().getX())
##        print('first robot y:', robot.getRobotPosition().getY())
        currCoverage = 0
        while currMin>currCoverage:
            for r in robots:
                r.updatePositionAndClean()
##                print('new positions after update')                
##                print(r.getRobotPosition().getX())
##                print(r.getRobotPosition().getY())
            currCoverage = float(room.getNumCleanedTiles()/room.getNumTiles())
##            print('currCoverage:', currCoverage)
##            print(room.tiles)
            resTrial.append(currCoverage)
            anim.update(room, robots)
        res.append(resTrial)
        anim.done()
    return res
    
# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means
#print(computeMeans(avg))

# === Problem 5
#this Robot works very good!!!!
class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        curr_pos = self.getRobotPosition()
        self.room.cleanTileAtPosition(curr_pos)
        while True:
            new_pos=curr_pos.getNewPosition(self.d, self.speed)
            if self.room.isPositionInRoom(new_pos):
                self.setRobotPosition(new_pos)
                self.setRobotDirection(random.choice(range(361)))
                self.room.cleanTileAtPosition(new_pos)
                break
            else:
                self.setRobotDirection(random.choice(range(361)))
runSimulation(3, 1.0, 20, 20, 0.4, 4, RandomWalkRobot, False)
# === Problem 4
#helper function for computing the average length of all the lists
#returned by sunSimulation

def averageLength(list_of_lists):
    n = len(list_of_lists)
    totalsum = 0
    for i in range(n):
        totalsum+=len((list_of_lists)[i])
    return float(totalsum/n)

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    means = []
    for i in range(5, 30, 5):
        average = averageLength(runSimulation(1, 1.0, i, i, 0.75, 10, RandomWalkRobot, False))
        means.append(average)
    pylab.figure()
    xVals = range(5, 30, 5)
    pylab.plot(xVals, means)
    pylab.ylabel('timesteps')
    pylab.xlabel('room')
    pylab.xticks(range(5,30,5), ['0', '5x5', '10x10', '20x20', '25x25'])
    pylab.title('Time for a single robot to clean 75% of the room')
    pylab.show()
showPlot1()

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    means = []
    for i in range(1, 11):
        average = averageLength(runSimulation(i, 1.0, 25, 25, 0.75, 10, RandomWalkRobot, False))
        means.append(average)
    pylab.figure()
    xVals = range(1, 11)
    pylab.plot(xVals, means)
    pylab.ylabel('timesteps')
    pylab.xlabel('number of robots')
    pylab.xticks(range(1, 11), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    pylab.title('Time needed to clean 75% of the room')
    pylab.show()
showPlot2()

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    means = []
    average1 = averageLength(runSimulation(2, 1.0, 20, 20, 0.75, 10, RandomWalkRobot, False))
    means.append(average1)
    average2 = averageLength(runSimulation(2, 1.0, 25, 16, 0.75, 10, RandomWalkRobot, False))
    means.append(average2) 
    average3 = averageLength(runSimulation(2, 1.0, 40, 10, 0.75, 10, RandomWalkRobot, False))
    means.append(average3)
    average4 = averageLength(runSimulation(2, 1.0, 50, 8, 0.75, 10, RandomWalkRobot, False))
    means.append(average4)
    average5 = averageLength(runSimulation(2, 1.0, 80, 5, 0.75, 10, RandomWalkRobot, False))
    means.append(average5)
    average6 = averageLength(runSimulation(2, 1.0, 100, 4, 0.75, 10, RandomWalkRobot, False))
    means.append(average6)
    
    pylab.figure()
    xVals = range(1, 7)
    pylab.plot(xVals, means)
    pylab.ylabel('timesteps')
    pylab.xlabel('ratio of width to height')
    pylab.xticks(range(1, 7), ['1', '1.5625', '4', '6.25', '16', '25'])
    pylab.title('Time needed for 2 robots to clean 75% of the room')
    pylab.show()
##showPlot3()

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    pylab.figure()
    pylab.ylabel('timesteps')
    pylab.xlabel('number of robots')
    pylab.xticks(range(1, 11), ['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '9', '10'])
    pylab.title('Time needed to clean 75% of the room')
    for i in range(1, 5):
        means = []
        for j in range(10, 101, 10):
            average = averageLength(runSimulation(i, 1.0, 25, 25, j/100, 10, RandomWalkRobot, False))
            means.append(average)
        string = str(i) + ' robots(s)'
        pylab.plot(means, label=string)
        pylab.legend(loc='upper left')
    pylab.show()
#showPlot4()
            
##avg = runSimulation(10, 1.0, 20, 40, 0.8, 1, RandomWalkRobot, False)
##print(avg)
