import streamlit as st

col1, col2, col3 , col4 = st.columns(4)

with col1:
    st.header("Water Signs")
    st.image("water.jpg")
    water=['Scorpio','Pisces','Cancer']
    st.radio('what is your zodiac',(water))


with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
    fire=['Aries','Leoi','Sagittarius']
    st.radio('what is your zodiac',(fire))


with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    air=['Libra', 'Aquarius', 'Gemini']
    st.radio('what is your zodiac',(air))


with col4:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    earth=['Capricorn','Taurus', 'Virgo']
    st.radio('what is your zodiac',(earth))
