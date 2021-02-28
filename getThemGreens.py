# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 03:39:31 2021

@author: vjm180001
"""


from pathlib import Path
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64


df2 = pd.read_csv('./querytodo.csv', sep = ',')
del df2 ["freezeproof"]

import zipfinder
import googlemaps
import ebaysearch


#st.sidebar.image("https://github.com/arunima1820/HackUTDVII/blob/main/getthemgreens.PNG")
#st.sidebar.image("https://github.com/arunima1820/HackUTDVII/blob/main/get-them-greens/public/favicon.png")
favi = Image.open("./getthemgreens.png")
temoc = Image.open("./temochome.gif")
st.image(favi)
st.sidebar.image(temoc)


my_table = st.empty()

zip_input = st.text_input(" ")
button_clicked = st.button("Enter ZIP code!")
[city, zone] = zipfinder.search_zip(zip_input)
st.write("Based on your Zip Code, we found that you live in " + city.title() + " and your USDA Plant Hardiness Zone is " + str(zone) + '.')

df3 = zipfinder.parseZone(str(zone))
st.write("Here is a list of plants that you can grow in your zone!")

st.sidebar.subheader("What skillset do you have with gardening?")
skill = st.sidebar.radio(label="Select a skill level", options=["Beginner", "Advanced"], key=[0,1])
df3 = zipfinder.parseSkillLevel(skill, df3)

st.sidebar.subheader("Display only freeze-resistant plants?")
freezeproof = 1 if st.sidebar.checkbox('Yes!') else 0
df3 = zipfinder.parseFreezeLevel(freezeproof, df3)

st.sidebar.subheader("Where will you be growing the plants?")
locations = st.sidebar.multiselect(label="Select location", options=["Indoors", "Outdoors"])
#locations
df3 = zipfinder.parseIndoors(locations, df3)

st.sidebar.subheader("How much space do you have?")
space_select = st.sidebar.radio("Please specify", ('Not much', 'Decent', 'Tons'))
df3 = zipfinder.parseSpace(space_select, df3)

st.sidebar.subheader("Select the max number of months you are willing to wait until harvest")
harvest_time = st.sidebar.select_slider(label="Slide to select",value=2, options=[1,2,3,4,5,6,7,8,9,10,11,12])
df3 = zipfinder.parseHarvest(harvest_time, df3)

submit_status = st.sidebar.button(label="Submit")
if submit_status:
    st.write(df3)
opts = np.asarray(df3["Name"])
user_selected_plants = st.multiselect(label="Select the plants you'd be interested in harvesting", options=opts)
#user_selected_plants
check_conflict_status = st.button(label="Check Conflicts")
if check_conflict_status:
    conflict_list = zipfinder.checkEnemies(user_selected_plants)
    conflict_list
    
food_bank_status = st.button(label="Check out nearby food banks")
if food_bank_status:
    food_banks = googlemaps.returnplaces(zip_input)
    food_banks
      
ebay_status = st.button(label="Check out eBay products that will help you harvest these plants")
if ebay_status:
    for plant in user_selected_plants:
        ebay_prods = ebaysearch.returnebay(plant)
        ebay_prods
