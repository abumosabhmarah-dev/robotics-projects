

import math
import time
import cv2
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient



def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def wrap_to_pi(a):
    while a > math.pi:
        a -= 2 * math.pi
    while a < -math.pi:
        a += 2 * math.pi
    return a


def dist2(x, y):
    return math.hypot(x, y)


def read_dist(sim, sensor, max_dist=2.5):
    detected, d, *_ = sim.readProximitySensor(sensor)
    return float(d) if detected else max_dist



def get_ultrasonic_sensors(sim):
    sensors = []
    for i in range(16):
        sensors.append(sim.getObject(
            f"/PioneerP3DX/visible/ultrasonicSensor[{i}]"
        ))
    print("✓ Found 16 ultrasonic sensors")
    return sensors



def main():
    client = RemoteAPIClient()
    sim = client.getObject("sim")

    sim.setStepping(True)

    robot = sim.getObject("/PioneerP3DX")
    left_motor = sim.getObject("/PioneerP3DX/leftMotor")
    right_motor = sim.getObject("/PioneerP3DX/rightMotor")
    goal = sim.getObject("/goal")

    sensors = get_ultrasonic_sensors(sim)

    
    dt = 0.02            

    V_FWD = 3.8          # faster forward speed
    V_MAX = 6.5
    V_TURN = 3.0

    GOAL_TOL = 0.25

    FRONT_BLOCK = 0.40
    FRONT_CLEAR = 0.55
    FRONT_EMERGENCY = 0.22

    RIGHT_TARGET = 0.35
    RIGHT_TOO_FAR = 0.70

    K_GOAL = 1.8         
    K_WALL = 1.6
    K_FRONT_AVOID = 1.5

    LEAVE_MARGIN = 0.10

    # Velocity smoothing 
    ALPHA = 0.85         

    # Sensor grouping
    FRONT_IDS = [3, 4, 5, 6, 7]
    RIGHT_IDS = [0, 1, 2, 15, 14]
    LEFT_IDS  = [8, 9, 10, 11]

    def min_group(ids):
        return min(read_dist(sim, sensors[i]) for i in ids)

   
    # State machine
    
    GO_TO_GOAL = 0
    FOLLOW_RIGHT_WALL = 1
    state = GO_TO_GOAL
    d_hit = None

    
    # Velocity memory 
    
    v_l_filt = 0.0
    v_r_filt = 0.0

   
    # Path drawing setup
    
    path = []
    scale = 120
    canvas = np.ones((600, 600, 3), np.uint8) * 255

    def world_to_img(x, y):
        return int(300 + x * scale), int(300 - y * scale)

    print(" Bug2 controller running (stable)")

    while True:
        pos = sim.getObjectPosition(robot, -1)
        yaw = sim.getObjectOrientation(robot, -1)[2]
        gpos = sim.getObjectPosition(goal, -1)

        dx = gpos[0] - pos[0]
        dy = gpos[1] - pos[1]
        d_goal = dist2(dx, dy)

        # Save path
        path.append((pos[0], pos[1]))

        if d_goal < GOAL_TOL:
            sim.setJointTargetVelocity(left_motor, 0.0)
            sim.setJointTargetVelocity(right_motor, 0.0)
            print("✓ Goal reached")
            break

        d_front = min_group(FRONT_IDS)
        d_right = min_group(RIGHT_IDS)
        d_left  = min_group(LEFT_IDS)

        # Emergency
        if d_front < FRONT_EMERGENCY:
            v_l_cmd, v_r_cmd = -V_TURN, +V_TURN
        else:
            if state == GO_TO_GOAL and d_front < FRONT_BLOCK:
                state = FOLLOW_RIGHT_WALL
                d_hit = d_goal

            elif state == FOLLOW_RIGHT_WALL:
                if d_hit and d_goal < d_hit - LEAVE_MARGIN and d_front > FRONT_CLEAR:
                    state = GO_TO_GOAL
                    d_hit = None

            if state == GO_TO_GOAL:
                desired = math.atan2(dy, dx)
                err = wrap_to_pi(desired - yaw)
                steer = K_GOAL * err
                speed = V_FWD

                if d_front < FRONT_CLEAR:
                    alpha = clamp((d_front - FRONT_BLOCK) / (FRONT_CLEAR - FRONT_BLOCK), 0, 1)
                    speed *= (0.4 + 0.6 * alpha)

                if d_left < 0.30:
                    steer += 0.5 * (0.30 - d_left)
                if d_right < 0.30:
                    steer -= 0.5 * (0.30 - d_right)

            else:
                speed = V_FWD * 0.9
                e = d_right - RIGHT_TARGET
                steer = -K_WALL * e

                if d_front < FRONT_CLEAR:
                    steer += K_FRONT_AVOID * (FRONT_CLEAR - d_front)

                if d_right > RIGHT_TOO_FAR and d_front > FRONT_BLOCK:
                    steer -= 0.6

            v_l_cmd = clamp(speed - steer, -V_MAX, V_MAX)
            v_r_cmd = clamp(speed + steer, -V_MAX, V_MAX)

       
        # VELOCITY SMOOTHING 
        
        v_l_filt = ALPHA * v_l_filt + (1 - ALPHA) * v_l_cmd
        v_r_filt = ALPHA * v_r_filt + (1 - ALPHA) * v_r_cmd

        sim.setJointTargetVelocity(left_motor, float(v_l_filt))
        sim.setJointTargetVelocity(right_motor, float(v_r_filt))

        
        # drow the path
        
        canvas[:] = 255
        for p in path:
            cv2.circle(canvas, world_to_img(p[0], p[1]), 1, (0, 0, 255), -1)

        cv2.circle(canvas, world_to_img(gpos[0], gpos[1]), 6, (0, 255, 0), -1)
        cv2.imshow("Robot Path (Bug2)", canvas)
        cv2.waitKey(1)

        sim.step()
        time.sleep(dt)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
