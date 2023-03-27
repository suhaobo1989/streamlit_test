import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
#simple stock app
"""
)

tickerSymbol='GOOGL'
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d',start='2020-04-30',end='2020-5-31')
tickerDf

st.line_chart(tickerDf[['Open','Close']])
st.line_chart(tickerDf.Volume)