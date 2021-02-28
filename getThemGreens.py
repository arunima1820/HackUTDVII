# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 03:39:31 2021

@author: vjm180001
"""


from pathlib import Path
import streamlit as st
import numpy as np
import pandas as pd



df2 = pd.read_csv('./querytodo.csv', sep = ',')
st.title('My first app')
st.write(df2.head())

import zipfinder
zip_input = st.text_input(" ")
button_clicked = st.button("Enter ZIP code!")
[city, zone] = zipfinder.search_zip(zip_input)
st.write("Based on your Zip Code, we found that you live in " + city.title() + " and your USDA Plant Hardiness Zone is " + str(zone) + '.')

#chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
#st.line_chart(chart_data)
option = st.selectbox('Which number do you like best?',df2['Name'])

'You selected: ', option