import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Example DataFrame
data = {
    "date": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "v1": [5, 7, 6, 4, 3, 8, 9, 6, 4, 7],
    "v2": [3, 8, 5, 7, 9, 4, 6, 5, 3, 7],
    "v3": [4, 6, 7, 5, 3, 9, 8, 6, 7, 5],
    "Y": [20, 25, 22, 28, 30, 35, 32, 34, 31, 29]
}
df = pd.DataFrame(data)

# Streamlit App
st.title("Interactive Line and Bar Chart with Streamlit")

# Sidebar
st.sidebar.header("Controls")
selected_bar = st.sidebar.selectbox("Select Bar Graph Variable:", ["v1", "v2", "v3"])

# Create Plotly Figure
fig = go.Figure()

# Add Line Chart for Y
fig.add_trace(go.Scatter(x=df["date"], y=df["Y"], mode="lines+markers", name="Y", line=dict(color="blue")))

# Add Bar Chart for Selected Variable
fig.add_trace(go.Bar(x=df["date"], y=df[selected_bar], name=selected_bar, marker=dict(color="orange")))

# Update Layout
fig.update_layout(
    title="Line and Bar Chart",
    xaxis_title="Date",
    yaxis_title="Values",
    barmode="overlay",  # Bar graph overlay
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)

# Render Plotly Figure in Streamlit
st.plotly_chart(fig, use_container_width=True)