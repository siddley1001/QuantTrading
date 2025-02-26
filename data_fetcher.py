import yfinance as yf
import streamlit as st

@st.cache_data(ttl=3600)
def get_dividend_history(ticker):
    """Fetch dividend history from Yahoo Finance"""
    try:
        stock = yf.Ticker(ticker)
        div_history = stock.dividends
        if len(div_history) == 0:
            return None
        return div_history.reset_index()
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        return None

def calculate_historical_growth(div_history):
    """Calculate 5-year dividend growth rate"""
    if div_history is None:
        return None
        
    latest = div_history.iloc[-1]['Dividends']
    oldest = div_history.iloc[0]['Dividends']
    years = (div_history.iloc[-1]['Date'] - div_history.iloc[0]['Date']).days / 365.25
    
    if years == 0 or oldest == 0:
        return None
        
    cagr = (latest / oldest) ** (1/years) - 1
    return cagr

def get_company_name(ticker):
    """
    Fetches the full company name based on the stock ticker.
    
    Args:
        ticker (str): Stock ticker symbol.
    
    Returns:
        str: Full company name if found, otherwise returns the ticker.
    """
    try:
        stock_info = yf.Ticker(ticker)
        return stock_info.info.get("longName", ticker)  # Fallback to ticker if not found
    except Exception as e:
        print(f"Error fetching company name for {ticker}: {e}")
        return ticker
