# robotics-projects
Projects in robotics, computer vision, human-robot interaction, and path planning


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

# Voice-Controlled Robot

This project explores how a mobile robot can understand spoken instructions and turn them into movement commands.

The user records a voice command through a microphone, such as “move forward one metre and turn left.” The speech is converted into text, interpreted as a sequence of robot actions, and then executed by a Pioneer P3-DX robot in CoppeliaSim.

The robot can also respond using a generated voice, creating a simple conversational interface between the user and the robot.

## Demo Videos

- https://drive.google.com/file/d/14WsPFdbcqEwbA6x8BBe7F1s6uqqCkVxm/view?usp=sharing
- https://drive.google.com/file/d/1zCQpxyH-BbLoFOxdKTPhNvGIOh2N-qNc/view

## Main File

[`voice_controlled_robot.py`](voice_controlled_robot.py)

## Technologies

- Python
- OpenAI speech-to-text, language and text-to-speech models
- CoppeliaSim
- ZeroMQ Remote API
- NumPy
- SoundDevice
- SoundFile

## How It Works

1. The user records a spoken command.
2. The audio is converted into text.
3. The command is interpreted as structured robot actions.
4. The robot provides a spoken response.
5. The Pioneer P3-DX executes the requested movements in CoppeliaSim.

## Main Features

- Push-to-talk voice recording
- Speech-to-text transcription
- Natural-language command interpretation
- Support for sequences of movement instructions
- Forward and backward movement
- Left and right rotations
- Spoken robot responses
- Wheel-odometry-based distance and angle control

## Example Commands

- “Move forward one metre.”
- “Turn left 90 degrees.”
- “Move forward two metres, then turn right.”
- “Go backward half a metre.”

