import streamlit as st

import matplotlib.pyplot as plt
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
