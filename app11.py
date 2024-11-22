import pandas as pd
from glob import glob

path = './price_simulator_cmamba/'

simul_data = {
    f"simul_v{i}_{j}": pd.read_csv(path + f'simul_v{i}_{j}.csv').iloc[:, 1:]
    for i in range(1, 8) for j in range(8)
}


# Streamlit app
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Simulated example dataframes (replace these with your actual data)
import numpy as np
from datetime import datetime, timedelta

# Streamlit app
st.title("Interactive Time Series Plot")
st.sidebar.header("Select Configuration")

# Select version (v1 ~ v7)
version = st.sidebar.selectbox("Select Version", [f"v{i}" for i in range(1, 8)])

# Filter DataFrames based on version
filtered_keys = [key for key in simul_data.keys() if version in key]
filtered_data = {key: simul_data[key] for key in filtered_keys}

# Display line plots
st.header(f"Plots for {version}")
for name, df in filtered_data.items():
    st.subheader(name)
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot each column against "Date"
    for col in df.columns:
        if col != "Date":
            ax.plot(df["Date"], df[col], label=col)

    ax.set_xlabel("Date")
    ax.set_ylabel("Values")
    ax.legend()
    st.pyplot(fig)
