import streamlit as st
from data_fetcher import get_dividend_history, calculate_historical_growth, get_company_name
from tutorial import show_ddm_tutorial
from sensitivity import plot_gordon_sensitivity

# Calculation Functions
def calculate_zero_growth(D, r):
    """Zero-growth dividend discount model calculation"""
    return D / r

def calculate_gordon(D0, r, g):
    """Gordon growth model calculation"""
    if g >= r:
        return None
    D1 = D0 * (1 + g)
    return D1 / (r - g)

def calculate_multistage(D0, r, g_initial, years, g_stable):
    """Multi-stage dividend discount model calculation"""
    try:
        present_value = 0
        # Initial growth phase
        for year in range(1, years + 1):
            dividend = D0 * (1 + g_initial) ** year
            present_value += dividend / ((1 + r) ** year)
        
        # Terminal value
        terminal_dividend = dividend * (1 + g_stable)
        terminal_value = terminal_dividend / (r - g_stable)
        present_value += terminal_value / ((1 + r) ** years)
        return present_value
    except:
        return None

# Main Application
def main():
    # Configure page
    st.set_page_config(
        page_title="DDM Valuation Suite",
        page_icon="📈",
        layout="wide"
    )
    
    # Show interactive tutorial
    show_ddm_tutorial()
    
    # Sidebar for data fetching
    st.sidebar.header("Real Data Integration")
    ticker = st.sidebar.text_input("Enter Stock Ticker (e.g. AAPL):", "AAPL")
    
    company_name = get_company_name(ticker)

    historical_data = None
    if ticker:
        with st.spinner("Fetching dividend history..."):
            historical_data = get_dividend_history(ticker)
            if historical_data is not None:

                # Title for chart in the sidebar            
                st.sidebar.subheader(f"{company_name} ({ticker}) Dividend History")

                # Display historical data in sidebar    
                st.sidebar.line_chart(historical_data.set_index('Date'))
                
                growth_rate = calculate_historical_growth(historical_data)
                if growth_rate:
                    st.sidebar.metric(
                        "5-Yr Historical Growth Rate", 
                        f"{growth_rate*100:.2f}%",
                        help="Compound Annual Growth Rate based on historical dividends"
                    )

    # Main interface
    st.header("DDM Valuation Calculator")
    
    # Model selection
    model = st.selectbox(
        "Select Valuation Model",
        ["Zero-Growth Model", "Gordon Growth Model", "Multi-Stage DDM"],
        index=1
    )
    
    # Input columns
    col1, col2 = st.columns(2)
    
    with col1:
        current_dividend = st.number_input(
            "Current Annual Dividend ($)", 
            min_value=0.0, 
            value=2.0, 
            step=0.1,
            help="Most recent annual dividend payment"
        )
        
    with col2:
        required_return = st.number_input(
            "Required Rate of Return (%)", 
            min_value=0.1, 
            value=10.0, 
            step=0.5,
            help="Investor's required return (discount rate)"
        ) / 100
    
    # Model-specific inputs
    if model == "Gordon Growth Model":
        growth_rate = st.number_input(
            "Dividend Growth Rate (%)", 
            min_value=0.0, 
            max_value=15.0, 
            value=5.0, 
            step=0.5,
            help="Expected constant growth rate"
        ) / 100
        
    elif model == "Multi-Stage DDM":
        st.subheader("Multi-Stage Parameters")
        col3, col4, col5 = st.columns(3)
        with col3:
            initial_growth = st.number_input(
                "Initial Growth Rate (%)", 
                min_value=0.0, 
                max_value=25.0, 
                value=10.0, 
                step=0.5
            ) / 100
        with col4:
            stable_growth = st.number_input(
                "Stable Growth Rate (%)", 
                min_value=0.0, 
                max_value=15.0, 
                value=5.0, 
                step=0.5
            ) / 100
        with col5:
            growth_years = st.number_input(
                "Years of Initial Growth", 
                min_value=1, 
                max_value=20, 
                value=5, 
                step=1
            )
    
    # Calculation and results
    if st.button("Calculate Stock Valuation", type="primary"):
        result = None
        error = None
        
        try:
            if model == "Zero-Growth Model":
                result = calculate_zero_growth(current_dividend, required_return)
                
            elif model == "Gordon Growth Model":
                if growth_rate >= required_return:
                    error = "Growth rate must be less than required return"
                else:
                    result = calculate_gordon(current_dividend, required_return, growth_rate)
                    
            elif model == "Multi-Stage DDM":
                if stable_growth >= required_return:
                    error = "Stable growth rate must be less than required return"
                else:
                    result = calculate_multistage(
                        current_dividend, 
                        required_return,
                        initial_growth, 
                        growth_years, 
                        stable_growth
                    )
            
            if error:
                st.error(error)
            elif result:
                st.success(f"**Calculated Stock Value ({model}):** ${result:,.2f}")
                
                # Show sensitivity analysis for Gordon model
                if model == "Gordon Growth Model":
                    with st.expander("Sensitivity Analysis", expanded=True):
                        plot_gordon_sensitivity(
                            current_dividend, 
                            required_return, 
                            growth_rate
                        )
                        
        except Exception as e:
            st.error(f"Calculation error: {str(e)}")
    
    # Disclaimer
    st.markdown("---")
    st.caption("""
    **Disclaimer:** This application provides theoretical valuations based on dividend discount models. 
    Actual stock prices may vary due to market conditions, risk factors, and other fundamental 
    considerations. Always conduct thorough research before making investment decisions.
               
    Data is taken from the Yahoo Finance API
    """)

    st.sidebar.caption("""
                       You can:
- Hover over the line chart for date information
- Can scroll to zoom in and out
- Use the mouse to drag the graph around

Enjoy!
                       """)

if __name__ == "__main__":
    main()