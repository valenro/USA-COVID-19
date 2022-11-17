import streamlit as st
st.set_page_config(layout='centered')

st.markdown(
    '''
    In this project, I will analyze data from COVID-19 cases in the United States with a dataset provided by the CDC 
    from the United States which has records from the beginning of the pandemic in January 2020 until August 2022. 
    I will use data visualization to show how many people were affected by COVID-19, how many people had been 
    hospitalized and where they were located as well as how many of those people were admitted to hospitals. 
    This data will also be used to show how many people had died from COVID-19 and which states had the highest 
    number of deaths. 

    This project will provide an overview of the pandemic and patient records, also it will demonstrate graphics made
    using Python libraries, including Pandasql which allows you to query pandas DataFrames using SQL syntax and Plotly 
    for visualizations.

    You can consult the dataset information from the following source and below you can access to the github repository. 
    > * https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/g62h-syeh
    > * https://github.com/valenro/USA-COVID-19

    The results you will see on the next pages were obtained from the questionnaire below nevertheless I decided to group the different analytics by topic.

    > 1 - What were the 5 states with the highest hospital occupancy due to COVID? Occupancy criteria for common bed. Consider the number of beds occupied with confirmed patients and take the first 6 months of 2020 as a reference - remember to include the number of infected in those months (cumulative).
    > 
    > 2 - Analyze the occupancy of beds (Common) by COVID in the State of New York during the established quarantine and indicate:
    > - Intervals of growth and decline
    > - Critical points (minimum and maximum)
    > 
    > 3 - What were the five States that used the most ICU beds -Intensive Care Units- during the year 2020? The measurement must be made in absolute terms.
    > 
    > 4 - What number of beds were used, by State, for pediatric patients with COVID during 2020?
    > 
    > 5 - What percentage of ICU beds correspond to confirmed cases of COVID-19? Group by State.
    > 
    > 6 - How many deaths from covid were there, by State, during the year 2021?
    > 
    > 7 - What is the relationship between the lack of medical personnel and the number of deaths in 2021?
    > 
    > 8 - Following the previous answers, what was the worst month of the pandemic for the USA as a whole? You can use other measures that you deem necessary.
    '''
)