import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.write("""
# Multi sensor Synthetic data generation using Carla and Scenic """)
# Mapping dictionary for behaviors
behavior_mapping = {
    "Ego lane changing behavior": "Lane_Change_behavior_with_brake",
    "Ego accelerating backward behavior": "accelerate_backward",
    "Pedestrian walking through the sidewalk as ego passes behavior": "pedestrian_on_side",
    "Ego applies breaks when pedestrian crosses the road behavior": "PedestrianCrossingBehaviour",
    "Ego waiting for the pedestrian while taking reverse behavior": "scene_egoWaiting_for_ped_while_moving_frontandback",
    "Pedestrian crossing before lane change behavior": "Scene_Pedestrian_crossing_before_lane_change"
}
scenicBehavior = st.selectbox("Pick a SCENIC behavior", list(behavior_mapping.keys()))


SensorNumber=st.selectbox("Number of sensors?", [1,2,3,4,5,6,7,8,9,10])


saveFlag = st.selectbox('Do you want to save generated data?', ["Yes","No"])
# Map 'Yes' to 'y' and 'No' to 'n'
saveFlag = 'y' if saveFlag == 'Yes' else 'n'
sensor_locations = []
for i in range(SensorNumber):
    sensor = st.radio(
    "Pick a Sensor ",
    ["Camera RGB","Camera Depth(Raw)"," Camera Depth (Gray Scale)"," Camera Depth (Logarithmic Gray Scale)","Camera Semantic Segmentation (Raw)","Camera Semantic Segmentation(CityScapes Palette)","Lidar (Ray-Cast)"],key=f"sensor_{i}")
    st.header(f"Location of Sensor {i+1}")
    xvalue = st.number_input("Enter the x value", value=None, placeholder="Type a number...", key=f"x_{i}")
    
    
    yvalue = st.number_input("Enter the y value", value=None, placeholder="Type a number...", key=f"y_{i}")
    
    
    zvalue = st.number_input("Enter the z value", value=None, placeholder="Type a number...", key=f"z_{i}")
    
    
    st.header(f"Enter the Rotation values for the Sensor {i+1}")
    
    pitchValue = st.number_input("Enter the Pitch value", value=None, placeholder="Type a number...", key=f"pitch_{i}")
    
    
    yawValue = st.number_input("Enter the Yaw value", value=None, placeholder="Type a number...", key=f"yaw_{i}")
    sensor_locations.append((xvalue, yvalue, zvalue, pitchValue, yawValue))
# Format the command
command = f"python Scenic_behaviour\\generate_data.py D:\\Scenic\\Scenic_behaviour\\behaviours\\{scenicBehavior}.scenic vehicle.lincoln.mkz_2020 D:\\Scenic\\Scenic_behaviour\\output {saveFlag} 0 0"

for i, location in enumerate(sensor_locations, start=1):
    xvalue, yvalue, zvalue, pitchValue, yawValue = location
    command += f" {xvalue} {yvalue} {zvalue} {pitchValue} {yawValue}"

st.write(f"Generated Command: {command}")


