import pandas as pd
import streamlit as st
import plotly.express as px

#Page Headers
st.set_page_config(page_title='My Dashboard')
st.header('Data Analysis Covid-19 India')
st.subheader('Confirmed Cases in India Till August 2021')

#Reading Dataset
df = pd.read_csv("covid_19_india.csv")

#Plotting Data Using different types of charts
pie_chart=px.pie(df,
                 values='Confirmed',
                 names='State/UnionTerritory')

st.plotly_chart(pie_chart)

bar_chart=px.bar(df,
                        x='State/UnionTerritory',
                        y='Confirmed',
                        color='State/UnionTerritory')

st.plotly_chart(bar_chart)

st.subheader('Vaccination Drive in India')

df1=pd.read_csv('covid_vaccine_statewise.csv')

bar1_chart=px.bar(df1,
                        x='Total Doses Administered',
                        y='State',
                        color='State',
                    )

st.plotly_chart(bar1_chart)

st.subheader('Vaccination Classification based on Gender')
line1=px.line(df1,
                 y='Updated On',
                 x='Male(Individuals Vaccinated)'
                )

line2=px.line(df1,
                 y='Updated On',
                 x='Female(Individuals Vaccinated)'
                )

line3=px.line(df1,
                 y='Updated On',
                 x='Transgender(Individuals Vaccinated)'
                )
left_column,middle_column, right_column = st.columns(3)
left_column.plotly_chart(line1, use_container_width=True)
middle_column.plotly_chart(line2, use_container_width=True)
right_column.plotly_chart(line3, use_container_width=True)


#Removing by default styling of streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
