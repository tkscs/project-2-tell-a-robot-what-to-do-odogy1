from simulator import robot, FORWARD, BACKWARD, STOP
import time
import turtle
m1 = 0
m2 = 0
x = 0
please = 0
# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

def zigzag():
    robot.motors(left=FORWARD, right=FORWARD, seconds=1)
    robot.motors(left=BACKWARD, right=FORWARD, seconds=0.5)
    robot.motors(left=FORWARD, right=FORWARD, seconds=0.5)
    while robot.left_sonar() > 10 and robot.left_sonar() < 170:
        robot.motors(left=FORWARD, right=BACKWARD, seconds=1)
        robot.motors(left=FORWARD, right=FORWARD, seconds=0.5)
        robot.motors(left=BACKWARD, right=FORWARD, seconds=1)
        robot.motors(left=FORWARD, right=FORWARD, seconds=0.5)
def cross():
    while robot.left_sonar() > 10 or robot.left_sonar() > 10:
        robot.motors(left=FORWARD, right=FORWARD, seconds=0.5)
        m1 = m1 + 0.5
    robot.motors(left=BACKWARD, right=BACKWARD, seconds=m1)
    m1=0
    robot.motors(left=FORWARD, right=BACKWARD, seconds=1.625)
    while robot.left_sonar() > 10 or robot.left_sonar() > 10:
        robot.motors(left=FORWARD, right=FORWARD, seconds=0.5)
        m1 = m1 + 0.5
    robot.motors(left=BACKWARD, right=BACKWARD, seconds=m1)
    m1=0
    robot.motors(left=FORWARD, right=BACKWARD, seconds=1.625)
    while robot.left_sonar() > 10 or robot.left_sonar() > 10:
        robot.motors(left=FORWARD, right=FORWARD, seconds=0.5)
        m1 = m1 + 0.5
    robot.motors(left=BACKWARD, right=BACKWARD, seconds=m1)
    m1=0
    robot.motors(left=FORWARD, right=BACKWARD, seconds=1.625)
    while robot.left_sonar() > 10 or robot.left_sonar() > 10:
        robot.motors(left=FORWARD, right=FORWARD, seconds=0.5)
        m1 = m1 + 0.5
    robot.motors(left=BACKWARD, right=BACKWARD, seconds=m1)
    m1=0
    robot.motors(left=FORWARD, right=BACKWARD, seconds=1.625)
def spin():
    robot.motors(left=FORWARD, right=BACKWARD, seconds=2)
    print("Weeeeeeeeeeeee")
    robot.motors(left=FORWARD, right=BACKWARD, seconds=4)
    print("I'm getting dizzy!")
    robot.motors(left=FORWARD, right=FORWARD, seconds=1)
    robot.motors(left=BACKWARD, right=BACKWARD, seconds=1)
    help = input("Do you want me to keep spining? y/n ")
    if help == "y":
        please = input("Are you sure? ")
        if please == "y":
            print("Okay then")
            robot.motors(left=FORWARD, right=BACKWARD, seconds=4)
            print("Ugggggg, I don't think I can go on!")
        elif please == "n":
            print("I am ever indentured to you for freeing me from this servitude!")

    elif help == "n":
        print("I am ever indentured to you for freeing me from this servitude!")
    time.sleep(3)
    checker = input("Officer: Hey! Did you make the robot spin too much? You: Option 1: Yes, I'm sorry. Option 2: No, the robot spun by it's self. Option 3: It's a robot, they can handle it! ")
    if checker == "1":
        print("Officer: Thanks for telling the truth. Your free to go.")
    elif checker == "2":
        if please == "y":
            print("Officer: Good thing we have cameras in here! (Checks cameras) Hey! You didn't tell the truth! Say good bye to your accsess!")
            x = 1
        elif please == "n" or help == "n":
            print("Officer: Thanks for telling the truth. Your free to go.")
    elif checker == "3":
        print("Robot: Heeeelllllllp.")
        robot.motors(left=FORWARD, right=FORWARD, seconds=1)
        robot.motors(left=BACKWARD, right=BACKWARD, seconds=1)
        print("Officer: Hey that's no way to talk to robots! It's time to go buddy!")
        x = 1





while x == 0:
    response = input("Do you want to zig-zag, make a cross, or spin?")

    if response == "zig-zag":
        zigzag()
        
    elif response == "cross":
        cross()



    elif response == "spin":
        spin()
    elif response == "exit":
        print("Bye!!!!!")
        time.sleep(3)
        print("Charge!!!!")
        robot.motors(left= FORWARD, right= FORWARD, seconds=20)
        print("Did I escape?")
        x=1
    elif response =="test":
        m1 = (robot.left_sonar() + robot.right_sonar())/2
        robot.motors(left=FORWARD, right=FORWARD, seconds=3)
        m2 = (robot.left_sonar() + robot.right_sonar())/2
        m3 = m2 - m1
        turtle.forward(m3)



do_stuff()  

    
# When you're done, close the simulator
robot.exit()

