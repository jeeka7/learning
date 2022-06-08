import streamlit as st

col1, col2, col3 , col4 = st.columns(4)

with col1:
    st.header("Water Signs")
    st.image("water.jpg")
    water=['Scorpio','Pisces','Cancer']
    x=st.radio('what is your zodiac',(water))


with col2:
    st.header("A dog")
    st.image("fire.jpg")
    fire=['Aries','Leoi','Sagittarius']
    x=st.radio('what is your zodiac',(fire))


with col3:
    st.header("An owl")
    st.image("air.jpg")
    air=['Libra', 'Aquarius', 'Gemini']
    x=st.radio('what is your zodiac',(air))


with col4:
    st.header("An owl")
    st.image("earth.jpg")
    earth=['Capricorn','Taurus', 'Virgo']
    x=st.radio('what is your zodiac',(earth))
st.write(x)
