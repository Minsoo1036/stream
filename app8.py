import pandas as pd

simul_v1_0 = pd.read_csv("./price_simulator/simul_v1_0.csv").iloc[:,1:]
simul_v1_1 = pd.read_csv("./price_simulator/simul_v1_1.csv").iloc[:,1:]
simul_v1_2 = pd.read_csv("./price_simulator/simul_v1_2.csv").iloc[:,1:]
simul_v1_3 = pd.read_csv("./price_simulator/simul_v1_3.csv").iloc[:,1:]
simul_v1_4 = pd.read_csv("./price_simulator/simul_v1_4.csv").iloc[:,1:]
simul_v1_5 = pd.read_csv("./price_simulator/simul_v1_5.csv").iloc[:,1:]
simul_v1_6 = pd.read_csv("./price_simulator/simul_v1_6.csv").iloc[:,1:]
simul_v1_7 = pd.read_csv("./price_simulator/simul_v1_7.csv").iloc[:,1:]

simul_v2_0 = pd.read_csv("./price_simulator/simul_v2_0.csv").iloc[:,1:]
simul_v2_1 = pd.read_csv("./price_simulator/simul_v2_1.csv").iloc[:,1:]
simul_v2_2 = pd.read_csv("./price_simulator/simul_v2_2.csv").iloc[:,1:]
simul_v2_3 = pd.read_csv("./price_simulator/simul_v2_3.csv").iloc[:,1:]
simul_v2_4 = pd.read_csv("./price_simulator/simul_v2_4.csv").iloc[:,1:]
simul_v2_5 = pd.read_csv("./price_simulator/simul_v2_5.csv").iloc[:,1:]
simul_v2_6 = pd.read_csv("./price_simulator/simul_v2_6.csv").iloc[:,1:]
simul_v2_7 = pd.read_csv("./price_simulator/simul_v2_7.csv").iloc[:,1:]

simul_v3_0 = pd.read_csv("./price_simulator/simul_v3_0.csv").iloc[:,1:]
simul_v3_1 = pd.read_csv("./price_simulator/simul_v3_1.csv").iloc[:,1:]
simul_v3_2 = pd.read_csv("./price_simulator/simul_v3_2.csv").iloc[:,1:]
simul_v3_3 = pd.read_csv("./price_simulator/simul_v3_3.csv").iloc[:,1:]
simul_v3_4 = pd.read_csv("./price_simulator/simul_v3_4.csv").iloc[:,1:]
simul_v3_5 = pd.read_csv("./price_simulator/simul_v3_5.csv").iloc[:,1:]
simul_v3_6 = pd.read_csv("./price_simulator/simul_v3_6.csv").iloc[:,1:]
simul_v3_7 = pd.read_csv("./price_simulator/simul_v3_7.csv").iloc[:,1:]

simul_v4_0 = pd.read_csv("./price_simulator/simul_v4_0.csv").iloc[:,1:]
simul_v4_1 = pd.read_csv("./price_simulator/simul_v4_1.csv").iloc[:,1:]
simul_v4_2 = pd.read_csv("./price_simulator/simul_v4_2.csv").iloc[:,1:]
simul_v4_3 = pd.read_csv("./price_simulator/simul_v4_3.csv").iloc[:,1:]
simul_v4_4 = pd.read_csv("./price_simulator/simul_v4_4.csv").iloc[:,1:]
simul_v4_5 = pd.read_csv("./price_simulator/simul_v4_5.csv").iloc[:,1:]
simul_v4_6 = pd.read_csv("./price_simulator/simul_v4_6.csv").iloc[:,1:]
simul_v4_7 = pd.read_csv("./price_simulator/simul_v4_7.csv").iloc[:,1:]

simul_v5_0 = pd.read_csv("./price_simulator/simul_v5_0.csv").iloc[:,1:]
simul_v5_1 = pd.read_csv("./price_simulator/simul_v5_1.csv").iloc[:,1:]
simul_v5_2 = pd.read_csv("./price_simulator/simul_v5_2.csv").iloc[:,1:]
simul_v5_3 = pd.read_csv("./price_simulator/simul_v5_3.csv").iloc[:,1:]
simul_v5_4 = pd.read_csv("./price_simulator/simul_v5_4.csv").iloc[:,1:]
simul_v5_5 = pd.read_csv("./price_simulator/simul_v5_5.csv").iloc[:,1:]
simul_v5_6 = pd.read_csv("./price_simulator/simul_v5_6.csv").iloc[:,1:]
simul_v5_7 = pd.read_csv("./price_simulator/simul_v5_7.csv").iloc[:,1:]

simul_v6_0 = pd.read_csv("./price_simulator/simul_v6_0.csv").iloc[:,1:]
simul_v6_1 = pd.read_csv("./price_simulator/simul_v6_1.csv").iloc[:,1:]
simul_v6_2 = pd.read_csv("./price_simulator/simul_v6_2.csv").iloc[:,1:]
simul_v6_3 = pd.read_csv("./price_simulator/simul_v6_3.csv").iloc[:,1:]
simul_v6_4 = pd.read_csv("./price_simulator/simul_v6_4.csv").iloc[:,1:]
simul_v6_5 = pd.read_csv("./price_simulator/simul_v6_5.csv").iloc[:,1:]
simul_v6_6 = pd.read_csv("./price_simulator/simul_v6_6.csv").iloc[:,1:]
simul_v6_7 = pd.read_csv("./price_simulator/simul_v6_7.csv").iloc[:,1:]

simul_v7_0 = pd.read_csv("./price_simulator/simul_v7_0.csv").iloc[:,1:]
simul_v7_1 = pd.read_csv("./price_simulator/simul_v7_1.csv").iloc[:,1:]
simul_v7_2 = pd.read_csv("./price_simulator/simul_v7_2.csv").iloc[:,1:]
simul_v7_3 = pd.read_csv("./price_simulator/simul_v7_3.csv").iloc[:,1:]
simul_v7_4 = pd.read_csv("./price_simulator/simul_v7_4.csv").iloc[:,1:]
simul_v7_5 = pd.read_csv("./price_simulator/simul_v7_5.csv").iloc[:,1:]
simul_v7_6 = pd.read_csv("./price_simulator/simul_v7_6.csv").iloc[:,1:]
simul_v7_7 = pd.read_csv("./price_simulator/simul_v7_7.csv").iloc[:,1:]

# Streamlit app
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Simulated example dataframes (replace these with your actual data)
import numpy as np
from datetime import datetime, timedelta

# Creating example dataframes
simul_data = {
    f"simul_v{i}_{j}": globals()[f"simul_v{i}_{j}"] 
    for i in range(1, 8) for j in range(8)
}

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
