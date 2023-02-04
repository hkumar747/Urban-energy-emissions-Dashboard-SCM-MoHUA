
import streamlit as st

st.sidebar.markdown('# Energy Usage by Category')

from datetime import date, datetime
import csv

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#plt.style.use('seaborn-v0_8')

import pandas as pd


@st.cache
def load_category_energy_usage_data():
    # Category
    CATEGORY_DAY_PATH = 'data/dfc_day.csv'

    CATEGORY_DF = pd.read_csv(CATEGORY_DAY_PATH).drop('Unnamed: 0', axis=1)

    CATEGORIES = CATEGORY_DF['CATEGORY'].unique()

    CATEGORY_DATA = [
        CATEGORY_DF.loc[CATEGORY_DF['CATEGORY'] == c]
        for c in CATEGORIES   
    ]

    return CATEGORY_DATA, CATEGORIES

CATEGORY_DATA, CATEGORIES = load_category_energy_usage_data()
fig = plt.figure()
ax = plt.axes()

x = [datetime.strptime(d, '%Y-%m-%d').date() for d in CATEGORY_DATA[0].date]

for i in range(len(CATEGORIES)):
    cat = CATEGORY_DATA[i]
    ax.plot(x, cat.imp, label=CATEGORIES[i])

plt.legend(loc='upper right')

ax.set_ylabel('Energy Usage')
ax.set_xlabel('Date')
ax.set_title('Consumer Energy Usage by Category')

st.title('Energy Usage by Category')

st.pyplot(fig)

# TODO allow filtering by date
# TODO allow filtering by category
