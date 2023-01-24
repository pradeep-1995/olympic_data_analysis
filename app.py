import pandas as pd
import streamlit as st 
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import scipy 

df = pd.read_csv('Olympic\events.csv',encoding='utf-8')
region_df = pd.read_csv('Olympic\egions.csv',encoding='utf-8')

df = preprocessor.preprocess(df,region_df)
st.sidebar.image('https://cdn.pixabay.com/photo/2016/02/03/20/43/rio-de-janeiro-2016-1177950_960_720.png')

user_menu = st.sidebar.radio("**Select an Option :**",('Medal Tally','Overall Analysis','Country Wise Analysis','Athelet wise Analysis'))
col1,col2 = st.columns(2)
with col1:
    st.subheader('Olympic Analysis')
    ''' Olympic Analysis contain  Medal Analysis, Overall Analysis (Cities,Event,Sports,Atheletic,Participating Nation),
     Countrywise like medaltally and Most Succesful Atheletic  and Qtheletics Analysis Accordinf to there height and weight and sex :'''
with col2:
    st.image('https://cdn.pixabay.com/photo/2014/04/02/10/56/runners-304972_960_720.png')
# Medal Tally
if user_menu == 'Medal Tally':
    st.sidebar.subheader('Medal Tally :')
    years_select,country_select = helper.country_year_list(df)

    year_selected = st.sidebar.selectbox('Select Year',years_select)
    country_selected = st.sidebar.selectbox('Select Country',country_select)

    medal_tally = helper.fetch_medal(df,year_selected,country_selected)
    # For Overall 
    if year_selected == 'Overall' and country_selected == 'Overall':
        st.subheader('Overall Medal Tally :') 
    # For Specific Country   
    if year_selected == 'Overall' and country_selected != 'Overall':
        st.subheader(str(country_selected) + " Overall Medal Tally")
    # For specific Year
    if year_selected != 'Overall' and country_selected == 'Overall':
        st.subheader("Medall Tally in : " + str(year_selected))
    # For Specific Country and Year    
    if year_selected != 'Overall' and country_selected != 'Overall':
        st.subheader("Medall Tally of " + str(country_selected) +" in Year " + str(year_selected))
    
    st.table(medal_tally)

# Overal Analysis
if user_menu == 'Overall Analysis':

    editions = df['Year'].unique().shape[0]
    cities = df['City'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.subheader('Overall Analysis :')
    st.subheader('Top Statistics :')
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader("Editions :")
        st.subheader(editions)
    with col2:
        st.subheader("Host :")
        st.subheader(cities)
    with col3:
        st.subheader("Events :")
        st.subheader(events)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader('Sports :')
        st.subheader(sports)
    with col2:
        st.subheader('Athletes :')
        st.subheader(athletes)
    with col3:
        st.subheader('Nations :')
        st.subheader(nations)
    
    
    nation_overtime = helper.data_over_time(df,'region')
    # Graph of Nation and year
    st.subheader('Participating Nation Over the Years :')
    ''' In this chart we represent number of countries join in the Olympic with Time passed.'''
    fig = px.line(nation_overtime,x='Edition',y='region')
    st.plotly_chart(fig)

    event_overtime = helper.data_over_time(df,'Event')
    # Graph of Events and year
    st.subheader('Events Over the Years :')
    '''Number of Event organiesd and also removed from schedule through out year passed. '''
    fig = px.line(event_overtime,x='Edition',y='Event')
    st.plotly_chart(fig)

    atheletic_overtime = helper.data_over_time(df,'Name')
    # Graph of Atheletic and year
    st.subheader("Athletes over the years")
    '''Popular increase with time with Number of Atheletic joining in Events'''
    fig = px.line(atheletic_overtime,x='Edition',y='Name')
    st.plotly_chart(fig)

    # Sports wise top Atheletic
    st.subheader('Most Successful Atheletics :')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sports = st.selectbox('Select Sports',sport_list)
    x = helper.most_successful(df,selected_sports)
    st.table(x)

    # Heat Map(Sports Wise)
    st.subheader("No. of Events over time(Every Sport)")
    fig,ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
                annot=True)
    st.pyplot(fig)
 
# Countrywise Analysis
if user_menu == 'Country Wise Analysis':

    st.subheader('Country Wise Analysis')
    # Countrywise Analysis
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.selectbox('Select Country',country_list)

    # Countrywise medaltally per year(lineplot)
    country_df = helper.yearwise_medal_tally(df,selected_country)
    st.subheader(selected_country + ' Medal Tally over Years :')
    fig = px.line(country_df,x='Year',y='Medal')
    st.plotly_chart(fig)

    # Countrywise event heatmap
    pt = helper.country_event_heatmap(df,selected_country)
    st.subheader(selected_country + " excels in the following sports :")
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    # Most Succesfull Atheletic( TOP 10 )
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.subheader('Top 10 Atheletics of ' + selected_country)
    st.table(top10_df)

# Atheletic Wise Analysis
if user_menu == 'Athelet wise Analysis':

    # Age wise atheletics win medal
    athlete_df = df.drop_duplicates(subset=['Name','region'])

    # Age of All Athelet 
    x1 = athlete_df['Age'].dropna()
    # Age of Athelete have Gold 
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    # Age of Athelete have Silver
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    # Age of Athelete have Bronze
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    st.subheader('Distribution of Age :')
    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.plotly_chart(fig)

    # Sport Wise Age analysis
    x = []
    name = []
    # Top popular Sports 
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.subheader("Distribution of Age with respect Sports(Gold Medalist) :")
    st.plotly_chart(fig)

    # Sports Wise Height, weight and man, women analysis 
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    st.subheader('Height vs Weight :')
    selected_sport = st.selectbox('Select Sports',sport_list)
    hw_df = helper.weight_v_height(df,selected_sport)

    fig,ax = plt.subplots()
    ax = sns.scatterplot(hw_df['Weight'],hw_df['Height'],hue=hw_df['Medal'],style=hw_df['Sex'],s=60)
    st.pyplot(fig)

    # Man Vs Women Participation over the years
    st.subheader("Men Vs Women Participation Over the Years")
    final = helper.men_v_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)



