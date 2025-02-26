import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def plot_gordon_sensitivity(D0, r, base_g):
    """3D surface plot for Gordon Growth sensitivity"""
    growth_rates = np.linspace(0, r*0.95, 50)
    required_returns = np.linspace(r*0.5, r*1.5, 50)
    
    X, Y = np.meshgrid(growth_rates, required_returns)
    Z = D0 * (1 + X) / (Y - X)
    
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('Growth Rate')
    ax.set_ylabel('Required Return')
    ax.set_zlabel('Stock Price')
    st.pyplot(fig)