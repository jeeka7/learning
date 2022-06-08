import streamlit as st

col1, col2, col3 , col4 = st.columns(4)

with col1:
    st.header("Water Signs")
    st.image("water.jpg")
    st.write('* Scorpio')
    st.write('* Pisces')
    st.write('* Cancer')

with col2:
    st.header("Fire Signs")
    st.image("fire.jpg")
    fire=['Aries','Leo','Sagittarius']
    st.write('* Aries')
    st.write('* Leo')
    st.write('* Sagittarius')
with col3:
    st.header("Air Signs")
    st.image("air.jpg")
    air=['Libra', 'Aquarius', 'Gemini']
    st.write('* Libra')
    st.write('* Aquarius')
    st.write('* Gemini')


with col4:
    st.header("Earth Signs")
    st.image("earth.jpg")
    st.write('* Capricorn')
    st.write('* Tauras')
    st.write('* Virgo')


zodiac=['Scorpio','Pisces','Cancer','Aries','Leo','Sagittarius','Libra', 'Aquarius', 'Gemini','Capricorn','Taurus', 'Virgo']
with st.sidebar:
    x = st.radio(
        "Choose your Zodiac",
        (zodiac)
    )
st.write('HOROSCOPE for 2022')

if (x=='Scorpio'):
    st.write('Scorpios are the dumbest people')
elif (x=='Capricorn'):
    st.write('Capricorns think they are very smart')
