import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.write("""
# Multi sensor Synthetic data generation using Carla and Scenic """)






st.selectbox("Pick a SCENIC behavior", ["Ego lane changing behavior", "Pedestrian walking through the sidewalk as ego passes behavior", "Ego applies breaks when pedestrian crosses the road behavior","Ego waiting for the pedestrian while taking reverse behavior","Pedestrian crossing before lane change behavior","Ego Accelerating backward behaviour"])

SensorNumber=st.selectbox("Number of sensors?", [1,2,3,4,5,6,7,8,9,10])
sensor = st.radio(
 "Pick a Sensor",
 ["Camera RGB","Camera Depth(Raw)"," Camera Depth (Gray Scale)"," Camera Depth (Logarithmic Gray Scale)","Camera Semantic Segmentation (Raw)","Camera Semantic Segmentation(CityScapes Palette)","Lidar (Ray-Cast)"])

st.selectbox('Do you want to save generated data?', ["Yes","No"])


for i in range(SensorNumber):

    st.header(f"Location of Sensor {i+1}")
    xvalue = st.number_input("Enter the x value {i+1}", value=None, placeholder="Type a number...", key=f"x_{i}")
    
    
    yvalue = st.number_input("Enter the y value {i+1}", value=None, placeholder="Type a number...", key=f"y_{i}")
    
    
    zvalue = st.number_input("Enter the z value {i+1}", value=None, placeholder="Type a number...", key=f"z_{i}")
    
    
    st.header(f"Enter the Rotation values for the Sensor {i+1}")
    
    ptchValue = st.number_input("Enter the Pitch value {i+1}", value=None, placeholder="Type a number...", key=f"pitch_{i}")
    
    
    yawValue = st.number_input("Enter the Yaw value {i+1}", value=None, placeholder="Type a number...", key=f"yaw_{i}")



