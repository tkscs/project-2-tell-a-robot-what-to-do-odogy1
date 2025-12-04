from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

while robot.left_sonar() > 1:
    robot.motors(left=FORWARD, right=FORWARD, seconds=0.1)
print("That was close!")
while robot.left_sonar() < 180:
    robot.motors(left=BACKWARD, right=BACKWARD, seconds=0.1)
print("weonvs")
robot.motors(left=FORWARD, right=FORWARD, seconds=1)
robot.motors(left=BACKWARD, right=FORWARD, seconds=0.5)
robot.motors(left=FORWARD, right=FORWARD, seconds=0.5)
while robot.left_sonar() > 5:
    robot.motors(left=FORWARD, right=BACKWARD, seconds=1)
    robot.motors(left=FORWARD, right=FORWARD, seconds=0.5)
    robot.motors(left=BACKWARD, right=FORWARD, seconds=1)
    robot.motors(left=FORWARD, right=FORWARD, seconds=0.5)
if robot.left_sonar() > robot.right_sonar():
    while robot.left_sonar() <= robot.right_sonar():
        robot.motors(left=FORWARD, right=BACKWARD, seconds=0.01)
if robot.left_sonar() < robot.right_sonar():
    while robot.left_sonar() >= robot.right_sonar():
        robot.motors(left=BACKWARD, right=FORWARD, seconds=0.01)
print("Done")
robot.motors(left=BACKWARD, right=BACKWARD, seconds=5)
# When you're done, close the simulator
robot.exit()