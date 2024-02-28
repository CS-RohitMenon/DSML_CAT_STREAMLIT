import datetime

import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf

stock = st.text_input("Enter a Stock", "MSFT")
data = yf.Ticker(stock)

st.write("Currently Analysing: ", stock)
# get historical market data

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Enter Start Date", datetime.date(2024, 1, 1))


with col2:
    end_date = st.date_input("Enter End Date", datetime.date(2024, 1, 31))

hist = data.history(period="1d", start=start_date, end=end_date)

st.dataframe(hist)

st.subheader("Trend in closing prices:")
st.line_chart(hist["Close"])

st.subheader("Trend in Volume:")
st.bar_chart(hist["Volume"])
