import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

model = LinearRegression()
x = df[["diameter"]]
y = df[["price"]]

model.fit(x, y)

st.title("Predicting the price of a pizza")
st.divider()
diameter = st.number_input("Enter the diameter of the pizza:")

if diameter:
  predicted_price = model.predict([[diameter]])[0][0]
  st.write(f"The price of a pizza with diameter of {diameter:.2f}cm is ${predicted_price:.2f}.")
  st.balloons()
