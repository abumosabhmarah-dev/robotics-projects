# robotics-projects
Projects in robotics, computer vision, human-robot interaction, and path planning

"""
Pioneer P3-DX Autonomous Maze Navigation

This project demonstrates autonomous navigation of a Pioneer P3-DX mobile robot
inside a maze using the Bug2 path-planning algorithm. The controller combines
goal-seeking and wall-following behaviors to safely reach a destination while
avoiding obstacles detected by the robot's ultrasonic sensors.

The implementation includes smooth velocity control, adaptive obstacle avoidance,
and real-time trajectory visualization, resulting in stable and reliable navigation
in a simulated environment.

## Code

- **Main file:** `bug2_maze_solver.py`

## Demo Video

🎥 Watch the project demonstration here:

https://drive.google.com/file/d/1F7OqdhZeDJ1fH2hwB3euyxY_cy1bi8-L/view?usp=sharing

Tools and Libraries:
- Python
- CoppeliaSim ZeroMQ Remote API
- OpenCV
- NumPy


# Hand Gesture Robot Control

This project explores an intuitive way of controlling a Pioneer P3-DX mobile robot using hand gestures. A webcam captures the user's hand movements, while MediaPipe detects the hand landmarks and recognizes different gestures. These gestures are then translated into movement commands that control the robot in the CoppeliaSim environment.

The goal of this project was to combine computer vision and robotics to create a simple and interactive human-robot interface. Different gestures allow the robot to move forward, stop, turn, reverse, and increase its speed, making the interaction natural and easy to use.

## Demo Video

https://drive.google.com/file/d/16vN71feMwbLZqi2RgM3dBNau1jTxjY0X/view?usp=sharing
## Main File

`hand_gesture_robot_control.py`

## Technologies

- Python
- MediaPipe
- OpenCV
- CoppeliaSim
- ZeroMQ Remote API

## Key Features

- Hand tracking and gesture recognition in real time
- Robot control through intuitive hand gestures
- Forward, reverse, left, and right movement
- Speed boost using a pinch gesture
- Smooth motion control for more stable navigation
- Live camera interface with gesture feedback
