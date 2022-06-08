import streamlit as st
import cherrypy as ch

import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
st.write("geeks for geeks example")
y=['one', 'two', 'three', 'four', 'five']
 
# getting values against each value of y
x=[5,24,35,67,12]
plt.barh(y, x)
 
# setting label of y-axis
plt.ylabel("pen sold")
 
# setting label of x-axis
plt.xlabel("price")
plt.title("Horizontal bar graph")
plt.show()



class HelloWorld():
    @cherrypy.expose
    def index(self):
        return st.write("Hello World!")

ch.quickstart(HelloWorld())
