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




st.header(f"Location of the Sensor")
xvalue = st.number_input("Enter the x value", value=None, placeholder="Type a number...")


yvalue = st.number_input("Enter the y value", value=None, placeholder="Type a number...")


zvalue = st.number_input("Enter the z value", value=None, placeholder="Type a number...")


st.header(f"Enter the Rotation values for the Sensor")

ptchValue = st.number_input("Enter the Pitch value", value=None, placeholder="Type a number...")


yawValue = st.number_input("Enter the Yaw value", value=None, placeholder="Type a number...")

# Creating lists to store start and end dates
lista_dt_inicio = []
lista_dt_fim = []

# Pegando os ativos do usuário e populando as listas
for i in range(int(qtd_ativo)):
    lista_ativos.append(st.text_input("Nome do ativo + .SA: ", key=str(i)))
    dt_inicio = st.date_input("Data de início: ", key="start_date_" + str(i))
    dt_fim = st.date_input("Data de fim: ", key="end_date_" + str(i))
    
    # Storing start and end dates
    lista_dt_inicio.append(dt_inicio)
    lista_dt_fim.append(dt_fim)

