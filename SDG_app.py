import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


# Change your path to the file  
df = pd.read_csv('sdg_index_2000-2022.csv')


# Start visualization
tab1, tab2, tab3 = st.tabs(['SDGs', 'France an Ranking', 'Wordldwide'])
with tab1:
    st.markdown("<h2>Sustainable Development Report 2023</h2>", unsafe_allow_html=True)
    st.write(
    "The Sustainable Development Report (SDR) reviews progress made each year on the Sustainable Development Goals "
    "since their adoption by the 193 UN Member States in 2015. At the halfway mark to 2030, the Sustainable Development "
    "Report 2023 takes stock of progress made and discusses priorities to restore and accelerate SDG progress. Published "
    "on the eve of the 2023 Paris Summit for a New Global Financial Pact, this year’s edition focuses specifically on the "
    "need to scale up development finance and reform the global financial architecture to support the SDGs."
)
    st.markdown(
    "Database retrieved from Kaggle: "
    "[Sustainable Development Report on Kaggle](https://www.kaggle.com/datasets/sazidthe1/sustainable-development-report/data?select=sdg_index_2000-2022.csv)",
    unsafe_allow_html=True
)

    st.write("This app is a summary of the SDG scores for 180 countries worldwide from the year 2000 to 2022. Below is a summary of each goal.")
    data = {
    '#' : ['Explanation'],
    'Goal 1': ['No Poverty'],
    'Goal 2': ['Zero Hunger'],
    'Goal 3': ['Good Health and Wellbeing'],
    'Goal 4': ['Quality Education'],
    'Goal 5': ['Gender Equality'],
    'Goal 6': ['Clean Water and Sanitation'],
    'Goal 7': ['Affordable and Clean Energy'],
    'Goal 8': ['Decent Work and Economic Growth'],
    'Goal 9': ['Industry, Innovation and Infrastructure'],
    'Goal 10': ['Reduced Inequalities'],
    'Goal 11': ['Sustainable Cities and Communities'],
    'Goal 12': ['Responsible Consumption and Production'],
    'Goal 13': ['Climate Action'],
    'Goal 14': ['Life Below Water'],
    'Goal 15': ['Life on Land'],
    'Goal 16': ['Peace, Justice and Strong Institutions'],
    'Goal 17': ['Partnerships for the Goals'],
    }

    df_goals = pd.DataFrame(data).set_index('#').T
    st.table(df_goals)

    st.write('Our database retrived from Kaggle: https://www.kaggle.com/datasets/sazidthe1/sustainable-development-report/data?select=sdg_index_2000-2022.csv')

    st.header('Ranking of countries by SDG Index Score')
    grouped_df = df.groupby('year').apply(lambda x: x.sort_values('sdg_index_score', ascending=False).reset_index(drop=True))
    grouped_df_dropped = grouped_df.drop('country_code', axis=1)
    # Create a dropdown list for selecting the year
    selected_year = st.selectbox('Select a year', sorted(df['year'].unique()))
    # Display ranking for the selected year
    st.dataframe(grouped_df_dropped.loc[grouped_df_dropped['year'] == selected_year].reset_index(drop=True))


with tab2:
    st.header("France's overall SDG score over the years")
    st.write("We have not modified the dataset apart from creating a 'continent' column by creating a dictionnary with each country and its respective continent, and adding that in our original dataframe.")

    df_france = df.loc[df['country'] == 'France']
    fig = px.line(df_france, x='year', y='sdg_index_score', title = "Evolution of French SDG score (over 100)")
    st.plotly_chart(fig)

with tab3:
     st.header('Overall SDG score map of all continents')
     fig2= px.scatter_geo(df,locations='country',locationmode='country names',color='sdg_index_score',
         hover_name='country',
         size='sdg_index_score',
         projection='natural earth')
     st.plotly_chart(fig2)
     
     countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
    'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
    'Comoros', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia',
    'Denmark', 'Djibouti', 'Dominican Republic', 'East and South Asia', 'Eastern Europe and Central Asia', 'Ecuador',
    'Egypt, Arab Rep.', 'El Salvador', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon',
    'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Guyana', 'Haiti',
    'High-income Countries', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Rep.', 'Iraq',
    'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea, Rep.', 'Kuwait',
    'Kyrgyz Republic', 'Lao PDR', 'Latin America and the Caribbean', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
    'Lithuania', 'Lower & Lower-middle Income', 'Lower-middle-income Countries', 'Low-income Countries', 'Luxembourg',
    'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico',
    'Middle East and North Africa', 'Moldova', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
    'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oceania',
    'OECD members', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland',
    'Portugal', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
    'Serbia', 'Sierra Leone', 'Singapore', 'Slovak Republic', 'Slovenia', 'Small Island Developing States', 'Somalia',
    'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sub-Saharan Africa', 'Sudan', 'Suriname', 'Sweden',
    'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia',
    'Türkiye', 'Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
    'Upper-middle-income Countries', 'Uruguay', 'Uzbekistan', 'Venezuela, RB', 'Vietnam', 'World', 'Yemen, Rep.', 'Zambia',
    'Zimbabwe']
     
     st.header('Comparison of SDG scores for selected countries over the years')
     selected_countries = st.multiselect('Select countries', countries)
     df_selected = df[df['country'].isin(selected_countries)]
     fig = px.line(df_selected, x='year', y='sdg_index_score', color='country')
     st.plotly_chart(fig)
