from arm_control import RobotControl # edited 22.5.2023
import time
import math

rc = RobotControl()
class maze:
    i = 0
    def __init__(self, direction,turing,speed,turn_time,time,degree):
        self.rc = RobotControl()
        self.maze_direction = direction
        self.maze_speed = speed
        self.maze_time = time
        self.maze_turn_time = turn_time
        self.maze_turn = turing
        self.angle= degree
        self.lists = self.rc.get_laser(360)
        self.left = self.rc.get_laser(540)
        self.right = self.rc.get_laser(180)
    def achived (self):
        if  self.lists == math.inf and self.left == math.inf and self.right == math.inf and self.i == 0: 
                self.i = 1
                self.moving()
                print ("achived")
                print(self.lists,self.left,self.right)
        else:
            print ("not yet") 
            print (self.i) 
            print(self.lists,"front",self.left,"left",self.right,"right")

    def way_out (self): 
        while self.i == 0 :
            if (self.lists > 1):
                self.moving()
                self.lists = self.rc.get_laser(360)
                self.left = self.rc.get_laser(540)
                self.right = self.rc.get_laser(180)
                print('front:', self.lists)
            self. achived ()
            self.rc.stop_robot
            if (self.lists < 1):
                self.turn_robot()
            
    def turn_robot(self):
       
        if self.left < self.right :
                self.turn_right()
                self.lists = self.rc.get_laser(360)
                self.left = self.rc.get_laser(540)
                self.right = self.rc.get_laser(180)
                print('Turning right :', self.right)
                print('left:', self.left)
        elif self.right < self.left:
                self.turn_left()
                self.lists = self.rc.get_laser(360)
                self.left = self.rc.get_laser(540)
                self.right = self.rc.get_laser(180)
                print('Turning left :', self.left)
                print('right:', self.right)
        self.rc.stop_robot

    def moving(self):
           
            self.rc.move_straight_time(self.maze_direction, self.maze_speed,
                     self.maze_time)
            print("moving")
            



    def turn_right(self):
        self.rc.rotate(self.angle)

    def turn_left(self):
        self.rc.rotate(-self.angle)
        print("The angle is in opposite",-self.angle)

    def turning(self):
        self.rc.turn(self.maze_turn, self.maze_turn_speed,
                     self.maze_time)



if __name__ == '__main__':
    l = maze('forward', 'clockwise', 0.5, 5, 0.8, 23)
    while not rc.ctrl_c:
        l.way_out()
