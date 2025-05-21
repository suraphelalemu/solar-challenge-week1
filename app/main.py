import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, plot_ghi_boxplot


st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("🌞 Solar Potential Comparison Dashboard")

# Sidebar
st.sidebar.title("Controls")
countries = ["Benin", "Sierraleone", "Togo"]
selected = st.sidebar.multiselect("Select countries to compare:", countries, default=countries)

# Load and filter data
data = load_data(selected)

# GHI Boxplot
st.subheader("GHI Comparison")
fig = plot_ghi_boxplot(data)
st.pyplot(fig)

# Top Regions Table
# st.subheader("Top Regions by Average GHI")
# st.dataframe(top_regions_table(data))