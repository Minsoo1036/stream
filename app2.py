## version 2
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
st.title("Interactive Line, Bar, and Pie Chart")

# Sidebar
st.sidebar.header("Controls")
selected_bar = st.sidebar.selectbox("Select Bar Graph Variable:", ["v1", "v2", "v3"])

# Create Plotly Figure
fig = go.Figure()

# Add Line Chart for Y
fig.add_trace(go.Scatter(
    x=df["date"], 
    y=df["Y"], 
    mode="lines+markers", 
    name="Y", 
    line=dict(color="blue"),
    hoverinfo="x+y+text",
    text=[f"v1: {row['v1']}, v2: {row['v2']}, v3: {row['v3']}" for _, row in df.iterrows()]
))

# Add Bar Chart for Selected Variable
fig.add_trace(go.Bar(
    x=df["date"], 
    y=df[selected_bar], 
    name=selected_bar, 
    marker=dict(color="orange"),
    opacity=0.6
))

# Update Layout
fig.update_layout(
    title="Line and Bar Chart with Hover Interaction",
    xaxis_title="Date",
    yaxis_title="Values",
    barmode="overlay",  # Bar graph overlay
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)

# Render Plotly Figure in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Interactive Pie Chart
st.subheader("Pie Chart on Hover")

# Add input to select a specific date (optional)
selected_date = st.selectbox("Select Date:", df["date"].astype(str))

# Filter data for the selected date
filtered_data = df[df["date"] == pd.to_datetime(selected_date)]
if not filtered_data.empty:
    row = filtered_data.iloc[0]
    values = [row["v1"], row["v2"], row["v3"]]
    labels = ["v1", "v2", "v3"]

    # Create Pie Chart
    pie_fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo="label+percent")])
    pie_fig.update_layout(title=f"Distribution of v1, v2, v3 on {selected_date}")
    st.plotly_chart(pie_fig, use_container_width=True)
else:
    st.write("No data available for the selected date.")