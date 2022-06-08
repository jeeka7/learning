import streamlit as st

col1, col2, col3 , col4 = st.columns(4)

with col1:
    st.header("Water Signs")
    st.image("water.jpg")
    water='Scorpio\n','Pisces\n','Cancer'
    st.write(water)


with col2:
    st.header("Fire Signs")
    st.image("fire.jpg")
    fire=['Aries','Leo','Sagittarius']
    st.write(fire)


with col3:
    st.header("Air Signs")
    st.image("air.jpg")
    air=['Libra', 'Aquarius', 'Gemini']
    st.write(air)


with col4:
    st.header("Earth Signs")
    st.image("earth.jpg")
    earth=['Capricorn','Taurus', 'Virgo']
    st.write(earth)

zodiac=['Scorpio','Pisces','Cancer','Aries','Leo','Sagittarius','Libra', 'Aquarius', 'Gemini','Capricorn','Taurus', 'Virgo']
with st.sidebar:
    add_radio = st.radio(
        "Choose your Zodiac",
        (zodiac)
    )
