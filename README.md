# Dividend Discount Model (DDM) Valuation App

![DDM App Screenshot](./images/app-screenshot.png) <!-- Add actual screenshot later -->

A modular Streamlit application for stock valuation using Dividend Discount Models (DDM) with real-time data integration, sensitivity analysis, and interactive tutorial.

## Features

- 🎓 Built-in interactive tutorial
- 📈 Multiple DDM variants (Zero-Growth, Gordon Growth, Multi-Stage)
- 🌐 Yahoo Finance API integration
- 📊 Sensitivity analysis visualizations
- 🧩 Modular architecture
- 📱 Responsive web interface

## Project Structure
ddm-valuation-app/
├── main_app.py # Core application logic
├── data_fetcher.py # Financial data operations
├── tutorial.py # Interactive learning system
├── sensitivity.py # Analysis visualizations
├── requirements.txt # Dependency list
├── .gitignore
└── README.md # This documentation


## Script Documentation

### 1. `main_app.py`
**Core Application Controller**
- Manages user interface and workflow
- Integrates all modules
- Handles model selection and calculations
- Displays results and visualizations

**Key Features:**
- Model selection dropdown
- Dynamic input fields
- Real-time valuation calculations
- Integrated visualizations
- Error handling and validation

### 2. `data_fetcher.py`
**Financial Data Module**
- Interfaces with Yahoo Finance API
- Retrieves historical dividend data
- Calculates growth metrics

**Key Features:**
- Automatic dividend history fetching
- Historical CAGR calculation
- Data caching for performance
- Error handling for API failures

### 3. `tutorial.py`
**Interactive Learning System**
- Step-by-step DDM tutorial
- Formula explanations
- Interactive examples

**Key Features:**
- Progressive disclosure of concepts
- Integrated LaTeX formulas
- Interactive walkthrough
- Session state management

### 4. `sensitivity.py`
**Visual Analysis Module**
- Generates sensitivity plots
- Creates 3D surface visualizations
- Produces growth timelines

**Key Features:**
- Gordon Growth 3D surface plots
- Dividend projection charts
- Matplotlib integration
- Dynamic axis scaling

## Installation & Setup

### Prerequisites
- Python 3.9+
- pip package manager
- Internet connection (for Yahoo Finance API)

### Quick Start
1. Clone repository:
   ```bash
   git clone https://github.com/siddley1001/ddm-valuation-app.git
   cd ddm-valuation-app

2. Install dependencies:
pip install -r requirements.txt

3. Run the application:
streamlit run main_app.py

4. Access in Browser at http://localhost:8501


### Usage Guide
1. Start with Tutorial
Click the "Interactive Tutorial" expander to learn DDM basics

2. Fetch Real Data
Enter a stock ticker (e.g., AAPL) in the sidebar to load dividend history

3. Select Model
Choose from three valuation models using the dropdown

4. Adjust Parameters
Modify inputs using number fields and sliders

5. Analyze Results
View valuations and explore sensitivity plots

6. Save Scenarios
Use browser's bookmark feature to save parameter sets