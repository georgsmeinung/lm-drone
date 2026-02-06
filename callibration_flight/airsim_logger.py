# logger.py  -- run this in a separate terminal
import cosysairsim as airsim
import time
import csv
import math
from datetime import datetime

def quaternion_to_euler(q):
    """Convert quaternion to Euler angles (roll, pitch, yaw)"""
    # Extract quaternion values
    w, x, y, z = q.w_val, q.x_val, q.y_val, q.z_val
    
    # Roll (x-axis rotation)
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = math.atan2(sinr_cosp, cosr_cosp)
    
    # Pitch (y-axis rotation)
    sinp = 2 * (w * y - z * x)
    if abs(sinp) >= 1:
        pitch = math.copysign(math.pi / 2, sinp)
    else:
        pitch = math.asin(sinp)
    
    # Yaw (z-axis rotation)
    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = math.atan2(siny_cosp, cosy_cosp)
    
    return roll, pitch, yaw

INTERVAL = 0.1          # 10 Hz
client = airsim.MultirotorClient()   # defaults to localhost:41451
client.confirmConnection()

# No enableApiControl() here!

csv_file = f"telemetry_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["time", "sim_t", "x", "y", "z", "vx", "vy", "vz", "yaw_deg"])

    print("Logging started (Ctrl+C to stop)")
    try:
        while True:
            start = time.time()
            state = client.getMultirotorState()

            pos = state.kinematics_estimated.position
            vel = state.kinematics_estimated.linear_velocity
            _, _, yaw = quaternion_to_euler(state.kinematics_estimated.orientation)
            yaw_deg = yaw * 180 / math.pi

            """"
            writer.writerow([
                datetime.now().isoformat(),
                state.timestamp / 1e9,
                pos.x_val, pos.y_val, pos.z_val,
                vel.x_val, vel.y_val, vel.z_val,
                yaw_deg
            ])
            f.flush()
            """ 
            print(
                f"time={datetime.now().isoformat()}, sim_t={state.timestamp / 1e9:.2f}, "
                f"pos=({pos.x_val:.2f}, {pos.y_val:.2f}, {pos.z_val:.2f}), "
                f"vel=({vel.x_val:.2f}, {vel.y_val:.2f}, {vel.z_val:.2f}), "
                f"yaw={yaw_deg:.2f}"
            )

            dt = time.time() - start
            time.sleep(max(0.001, INTERVAL - dt))   # tight loop, still ~accurate rate

    except KeyboardInterrupt:
        print("\nLogging stopped")