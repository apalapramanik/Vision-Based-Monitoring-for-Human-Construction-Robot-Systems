# Vision-Based-Monitoring-for-Human-Construction-Robot-Systems

## Install the following packages:

1) Download the github repository in ~your_ws/src/testrobots
2) Save the yolo.cfg and yolo.weights inside ~your_ws/src/testrobots/scripts/ 
3) catkin_make
4) pip install -U scikit-learn
5) Download the additional turtlebot3 folders inside ~your_ws/src/




## TURTLEBOT 3 PACKAGES REQUIRED:

https://github.com/ROBOTIS-GIT/turtlebot3

https://github.com/ROBOTIS-GIT/turtlebot3_simulations

https://github.com/ROBOTIS-GIT/turtlebot3_msgs



1)Copy the turtlebot3 folders inside the your_ws/src folder

2)Go to your_ws/src/turtlebot3/turtlebot3_navigations/maps and change the image parameter in
building4.yaml to
/home/$YOURDIRECTORY$/your_ws/src/turtlebot3/turtlebot3_navigation/maps/building4.pgm

3)Do Catkin_make to check everything is working fine.
```
echo 'export TURTLEBOT3_MODEL=waffle' >> ~/.bashrc

source ~/.bashrc
```

## LAUNCH FILE:
```
cd your_ws/my_pkg

catkin_make

source devel/setup.bash

roslaunch testrobots launch.launch

```


## TAB 1: LAUNCH GAZEBO ENVIRONMENT
```
cd testrobot/test_catkin

catkin_make

source devel/setup.bash

export TURTLEBOT3_MODEL=waffle

roslaunch turtlebot3_gazebo turtlebot3_house_scenario1.launch
```

## TAB 2: LAUNCH RVIZ 
```
cd testrobot/test_catkin

catkin_make

source devel/setup.bash

export TURTLEBOT3_MODEL=waffle

roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/apramani/catkin_ws/src/turtlebot3/turtlebot3_navigation/maps/building4.yaml
```
## TAB 3: RUN HUMAN DETECTION / YOLO NODE
```
cd testrobot/test_catkin

catkin_make

source devel/setup.bash

cd  src/testrobots/scripts

python3 human_detection.py
```
## TAB 4: RUN POINT CLOUD PROCESSING NODE
```
cd testrobot/test_catkin

catkin_make

source devel/setup.bash

rosrun testrobots organize
 ```
## TAB 5: RUN PREDICTION NODE
```
cd testrobot/test_catkin

catkin_make

source devel/setup.bash

cd  src/testrobots/scripts

python3 pred.py

```
## TAB 6: RUN MONITORING NODE
```
cd testrobot/test_catkin

catkin_make

source devel/setup.bash

cd  src/testrobots/scripts

python3 monitor.py

roslaunch testrobots monitor.launch
```
## TAB 7: RUN NAVIGATION NODE
```
cd testrobot/test_catkin

catkin_make

source devel/setup.bash

cd  src/testrobots/scripts

python3 goal.py
```

