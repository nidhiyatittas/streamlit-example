import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.write("""
# Multi sensor Synthetic data generation using Carla and Scenic """)

st.image('Ego_waiting_for_pedestrian_on_reverse.jpg', caption='Sunrise by the mountains')
# Mapping dictionary for behaviors
behavior_mapping = {
    "Ego lane changing behavior": "Lane_Change_behavior_with_brake",
    "Ego accelerating backward behavior": "accelerate_backward",
    "Pedestrian walking through the sidewalk as ego passes behavior": "pedestrian_on_side",
    "Ego applies breaks when pedestrian crosses the road behavior": "PedestrianCrossingBehaviour",
    "Ego waiting for the pedestrian while taking reverse behavior": "scene_egoWaiting_for_ped_while_moving_frontandback",
    "Pedestrian crossing before lane change behavior": "Scene_Pedestrian_crossing_before_lane_change"
}
# Mapping dictionary for sensors
sensor_mapping = {
    "Camera RGB": 0,
    "Camera Depth(Raw)": 1,
    "Camera Depth (Gray Scale)": 2,
    "Camera Depth (Logarithmic Gray Scale)": 3,
    "Camera Semantic Segmentation (Raw)": 4,
    "Camera Semantic Segmentation(CityScapes Palette)": 5,
    "Lidar (Ray-Cast)": 6
}

scenicBehavior = st.selectbox("Pick a SCENIC behavior", list(behavior_mapping.keys()))
vehicleType = st.selectbox("Pick type of ego vehicle", [
    "vehicle.audi.a2",
    "vehicle.audi.etron",
    "vehicle.audi.tt",
    "vehicle.bmw.grandtourer",
    "vehicle.chevrolet.impala",
    "vehicle.citroen.c3",
    "vehicle.dodge.charger_police",
    "vehicle.jeep.wrangler_rubicon",
    "vehicle.lincoln.mkz_2017",
    "vehicle.mercedes.coupe",
    "vehicle.mini.cooper_s",
    "vehicle.ford.mustang",
    "vehicle.nissan.micra",
    "vehicle.nissan.patrol",
    "vehicle.seat.leon",
    "vehicle.tesla.model3",
    "vehicle.toyota.prius",
    "vehicle.volkswagen.t2",
])
sensor_values = []
SensorNumber=st.selectbox("Number of sensors?", [1,2,3,4,5,6,7,8,9,10])


saveFlag = st.selectbox('Do you want to save generated data?', ["Yes","No"])
# Map 'Yes' to 'y' and 'No' to 'n'
saveFlag = 'y' if saveFlag == 'Yes' else 'n'
sensor_locations = []
for i in range(SensorNumber):
    sensor = st.radio(
    "Pick a Sensor ",
    list(sensor_mapping.keys()),key=f"sensor_{i}")
    sensor_values.append(sensor_mapping[sensor])  # Map the sensor value to integer
    
    st.header(f"Location of Sensor {i+1}")
    xvalue = st.number_input("Enter the x value", value=None, placeholder="Type a number...", key=f"x_{i}")
    
    
    yvalue = st.number_input("Enter the y value", value=None, placeholder="Type a number...", key=f"y_{i}")
    
    
    zvalue = st.number_input("Enter the z value", value=None, placeholder="Type a number...", key=f"z_{i}")
    
    
    st.header(f"Enter the Rotation values for the Sensor {i+1}")
    
    pitchValue = st.number_input("Enter the Pitch value", value=None, placeholder="Type a number...", key=f"pitch_{i}")
    
    
    yawValue = st.number_input("Enter the Yaw value", value=None, placeholder="Type a number...", key=f"yaw_{i}")
    sensor_locations.append((xvalue, yvalue, zvalue, pitchValue, yawValue))

# Get the mapped behavior
mapped_behavior = behavior_mapping[scenicBehavior]

# Format the command
command = f"python Scenic_behaviour\\generate_data.py D:\\Scenic\\Scenic_behaviour\\behaviours\\{mapped_behavior}.scenic {vehicleType} D:\\Scenic\\Scenic_behaviour\\output {saveFlag} "

for i, location in enumerate(sensor_locations, start=1):
    xvalue, yvalue, zvalue, pitchValue, yawValue = location
    sensor_value = sensor_values[i-1]  # Get sensor value for this iteration
    transform_index = i-1
    command += f" {transform_index} {sensor_value} {xvalue} {yvalue} {zvalue} {pitchValue} {yawValue}"

st.write(f"Generated Command: {command}")
