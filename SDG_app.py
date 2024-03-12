import streamlit as st
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import matplotlib.pyplot as plt



# Change your path to the file  
df = pd.read_csv('sdg_index_2000-2022.csv')



# Adding continent column
country_to_continent = {
    'Afghanistan': 'Asia',
    'Albania': 'Europe',
    'Algeria': 'Africa',
    'Angola': 'Africa',
    'Argentina': 'South America',
    'Armenia': 'Asia',
    'Australia': 'Oceania',
    'Austria': 'Europe',
    'Azerbaijan': 'Asia',
    'Bahamas, The': 'North America',
    'Bahrain': 'Asia',
    'Bangladesh': 'Asia',
    'Barbados': 'North America',
    'Belarus': 'Europe',
    'Belgium': 'Europe',
    'Belize': 'North America',
    'Benin': 'Africa',
    'Bhutan': 'Asia',
    'Bolivia': 'South America',
    'Bosnia and Herzegovina': 'Europe',
    'Botswana': 'Africa',
    'Brazil': 'South America',
    'Brunei Darussalam': 'Asia',
    'Bulgaria': 'Europe',
    'Burkina Faso': 'Africa',
    'Burundi': 'Africa',
    'Cabo Verde': 'Africa',
    'Cambodia': 'Asia',
    'Cameroon': 'Africa',
    'Canada': 'North America',
    'Central African Republic': 'Africa',
    'Chad': 'Africa',
    'Chile': 'South America',
    'China': 'Asia',
    'Colombia': 'South America',
    'Comoros': 'Africa',
    'Congo, Dem. Rep.': 'Africa',
    'Congo, Rep.': 'Africa',
    'Costa Rica': 'North America',
    "Cote d'Ivoire": 'Africa',
    'Croatia': 'Europe',
    'Cuba': 'North America',
    'Cyprus': 'Asia',
    'Czechia': 'Europe',
    'Denmark': 'Europe',
    'Djibouti': 'Africa',
    'Dominican Republic': 'North America',
    'East and South Asia': 'Asia',
    'Eastern Europe and Central Asia': 'Europe',
    'Ecuador': 'South America',
    'Egypt, Arab Rep.': 'Africa',
    'El Salvador': 'North America',
    'Estonia': 'Europe',
    'Eswatini': 'Africa',
    'Ethiopia': 'Africa',
    'Fiji': 'Oceania',
    'Finland': 'Europe',
    'France': 'Europe',
    'Gabon': 'Africa',
    'Gambia, The': 'Africa',
    'Georgia': 'Asia',
    'Germany': 'Europe',
    'Ghana': 'Africa',
    'Greece': 'Europe',
    'Guatemala': 'North America',
    'Guinea': 'Africa',
    'Guyana': 'South America',
    'Haiti': 'North America',
    'High-income Countries': 'Unknown',
    'Honduras': 'North America',
    'Hungary': 'Europe',
    'Iceland': 'Europe',
    'India': 'Asia',
    'Indonesia': 'Asia',
    'Iran, Islamic Rep.': 'Asia',
    'Iraq': 'Asia',
    'Ireland': 'Europe',
    'Israel': 'Asia',
    'Italy': 'Europe',
    'Jamaica': 'North America',
    'Japan': 'Asia',
    'Jordan': 'Asia',
    'Kazakhstan': 'Asia',
    'Kenya': 'Africa',
    'Korea, Rep.': 'Asia',
    'Kuwait': 'Asia',
    'Kyrgyz Republic': 'Asia',
    'Lao PDR': 'Asia',
    'Latin America and the Caribbean': 'South America',
    'Latvia': 'Europe',
    'Lebanon': 'Asia',
    'Lesotho': 'Africa',
    'Liberia': 'Africa',
    'Lithuania': 'Europe',
    'Lower & Lower-middle Income': 'Unknown',
    'Lower-middle-income Countries': 'Unknown',
    'Low-income Countries': 'Unknown',
    'Luxembourg': 'Europe',
    'Madagascar': 'Africa',
    'Malawi': 'Africa',
    'Malaysia': 'Asia',
    'Maldives': 'Asia',
    'Mali': 'Africa',
    'Malta': 'Europe',
    'Mauritania': 'Africa',
    'Mauritius': 'Africa',
    'Mexico': 'North America',
    'Middle East and North Africa': 'Asia',
    'Moldova': 'Europe',
    'Mongolia': 'Asia',
    'Montenegro': 'Europe',
    'Morocco': 'Africa',
    'Mozambique': 'Africa',
    'Myanmar': 'Asia',
    'Namibia': 'Africa',
    'Nepal': 'Asia',
    'Netherlands': 'Europe',
    'New Zealand': 'Oceania',
    'Nicaragua': 'North America',
    'Niger': 'Africa',
    'Nigeria': 'Africa',
    'North Macedonia': 'Europe',
    'Norway': 'Europe',
    'Oceania': 'Oceania',
    'OECD members': 'Unknown',
    'Oman': 'Asia',
    'Pakistan': 'Asia',
    'Panama': 'North America',
    'Papua New Guinea': 'Oceania',
    'Paraguay': 'South America',
    'Peru': 'South America',
    'Philippines': 'Asia',
    'Poland': 'Europe',
    'Portugal': 'Europe',
    'Qatar': 'Asia',
    'Romania': 'Europe',
    'Russian Federation': 'Europe',
    'Rwanda': 'Africa',
    'Sao Tome and Principe': 'Africa',
    'Saudi Arabia': 'Asia',
    'Senegal': 'Africa',
    'Serbia': 'Europe',
    'Sierra Leone': 'Africa',
    'Singapore': 'Asia',
    'Slovak Republic': 'Europe',
    'Slovenia': 'Europe',
    'Small Island Developing States': 'Unknown',
    'Somalia': 'Africa',
    'South Africa': 'Africa',
    'South Sudan': 'Africa',
    'Spain': 'Europe',
    'Sri Lanka': 'Asia',
    'Sub-Saharan Africa': 'Africa',
    'Sudan': 'Africa',
    'Suriname': 'South America',
    'Sweden': 'Europe',
    'Switzerland': 'Europe',
    'Syrian Arab Republic': 'Asia',
    'Tajikistan': 'Asia',
    'Tanzania': 'Africa',
    'Thailand': 'Asia',
    'Togo': 'Africa',
    'Trinidad and Tobago': 'North America',
    'Tunisia': 'Africa',
    'Türkiye': 'Asia',
    'Turkmenistan': 'Asia',
    'Uganda': 'Africa',
    'Ukraine': 'Europe',
    'United Arab Emirates': 'Asia',
    'United Kingdom': 'Europe',
    'United States': 'North America',
    'Upper-middle-income Countries': 'Unknown',
    'Uruguay': 'South America',
    'Uzbekistan': 'Asia',
    'Venezuela, RB': 'South America',
    'Vietnam': 'Asia',
    'World': 'Unknown',
    'Yemen, Rep.': 'Asia',
    'Zambia': 'Africa',
    'Zimbabwe': 'Africa'
}
def map_country_to_continent(country):
    return country_to_continent.get(country, 'Unknown')

# Apply the mapping to create a new 'Continent' column
df['continent'] = df['country'].apply(map_country_to_continent)





# Start visualization
tab1, tab2, tab3, tab4 = st.tabs(['SDGs', 'France', 'Europe', 'Wordldwide'])
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
    st.header('Overall SDG scores of European countries over time')
    selected_year2 = st.selectbox("All the SDGs scores for Europe over the years compared to France", (2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022), index=None)
    df_europe = df.loc[df['continent'] == 'Europe']
    fig3 = px.bar(df_europe.loc[df_europe['year'] == selected_year2], x='country', y='sdg_index_score')
    df_selected_year = df_europe[df_europe['year'] == selected_year2]
    fig3.update_traces(marker_color=['red' if country == 'France' else 'blue' for country in df_selected_year['country']])
    st.plotly_chart(fig3)


with tab4:
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