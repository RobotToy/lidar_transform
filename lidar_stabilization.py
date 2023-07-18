#lidar_stabilizationn

# IMPORT NECESSARY LIBRARIES
import rclpy
from rclpy.node import NotInitializedException
import numpy as np
import pyzed.sl as sl #TODO: figure out what sl means




#OPENING THE CAMERA
# create a ZED camera object
zed = sl.Camera()

# set configuration parameters
init_params = sl.InitParameters()
# No depth computation is required here
init_params.depth_mode = sl.DEPTH_MODE.NONE

# Open the camera
err = zed.open(init_params)
if err != sl.ERROR_CODE.SUCCESS :
    print(repr(err))
    zed.close()
    exit(1)

#CAPTURE IMU DATA
sensors_data = sl.SensorsData()

#grabs new frames and retrieve sensors data
while zed.grab() == sl.ERROR_CODE.SUCCESS :
    #grabs frames only from synchronized data
    zed.get_sensors_data(sensors_data, sl.TIME_REFERENCE.IMAGE)

    #extract IMU data
    imu_data = sensors_data.get_imu_data()

    #Recieve variables
    linear_acceleration = imu_data.get_linear_acceleration()
    angular_velocity = imu_data.get_angular_velocity()
    pose_covarince = imu_data.get_pose_covariance()
    camera_imu_transform = imu_data.get_camera_imu_transform()

#UPDATE SENSOR DATA

#Store timestamps and check for data updates
ts_handler = TimestampHandler()
if ts_handler.is_new(sensors_data.get_imu_data()):
    sensors_data.get_imu_data()

# Check if IMU data has been updated
if ts_handler.is_new(sensors_data.get_imu_data()):
    quaternion = sensors_data.get_imu_data().get_pose().get_orientation().get()
    print("IMU Orientation: {}".format(quaternion))
    linear_acceleration = sensors_data.get_imu_data().get_linear_acceleration()
    print("IMU Acceleration: {} [m/sec^2]".format(linear_acceleration))
    angular_velocity = sensors_data.get_imu_data().get_angular_velocity()
    print("IMU Angular Velocity: {} [deg/sec]".format(angular_velocity))

'''
# Check if Magnetometer data has been updated
if ts_handler.is_new(sensors_data.get_magnetometer_data()):
    magnetic_field_calibrated = sensors_data.get_magnetometer_data().get_magnetic_field_calibrated()
    print("Magnetometer Magnetic Field: {} [uT]".format(magnetic_field_calibrated))

# Check if Barometer data has been updated 
if ts_handler.is_new(sensors_data.get_barometer_data()):
    magnetic_field_calibrated = sensors_data.get_barometer_data().pressure
    print("Barometer Atmospheric pressure: {} [hPa]".format(sensors_data.get_barometer_data().pressure))
'''    

# CLOSE THE CAMERA
zed.close()


# TODO --> USE DATA TO STABILIZE LIDAR 
