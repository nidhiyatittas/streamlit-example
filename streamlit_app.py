import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.write("""
# Multi sensor Synthetic data generation using Carla and Scenic """)




genre = st.radio(
 "Pick a SCENIC behavior",
 ["Ego lane changing behavior", "Pedestrian walking through the sidewalk as ego passes behavior", "Ego applies breaks when pedestrian crosses the road behavior","Ego waiting for the pedestrian while taking reverse behavior","Pedestrian crossing before lane change behavior"])
st.write('The SCENIC behavior is ', genre)



sensor = st.radio(
 "Pick a Sensor",
 ["Camera RGB","Camera Depth(Raw)"," Camera Depth (Gray Scale)"," Camera Depth (Logarithmic Gray Scale)","Camera Semantic Segmentation (Raw)","Camera Semantic Segmentation(CityScapes Palette)","Lidar (Ray-Cast)"])
st.write('The Sensor is ', sensor)



st.header(f"Location of the Sensor")
number = st.number_input("Enter the x value", value=None, placeholder="Type a number...")
st.write('The x value is ', number)

number = st.number_input("Enter the y value", value=None, placeholder="Type a number...")
st.write('The y value is ', number)

number = st.number_input("Enter the z value", value=None, placeholder="Type a number...")
st.write('The z value is ', number)


