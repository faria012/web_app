import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""Simple Stoke Price App""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)

tickerDataframe = tickerData.history(period='1d', start='2010-05-31', end='2020-05-31')

st.write(""" 
# Closing Price
""")
st.line_chart(tickerDataframe.Close)
st.write("""
# Volume Price
""")
st.line_chart(tickerDataframe.Volume)

