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

# Initialize session state for click data
if "click_data" not in st.session_state:
    st.session_state["click_data"] = None

# Streamlit App
st.title("Interactive Line, Bar, and Clickable Pie Chart")

# Sidebar for Bar Chart Selection
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
    marker=dict(size=10),
    customdata=df[["v1", "v2", "v3"]].values,  # Pass additional data for pie chart
    hovertemplate="Date: %{x}<br>Y: %{y}<br>v1: %{customdata[0]}<br>v2: %{customdata[1]}<br>v3: %{customdata[2]}"
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
    title="Line and Bar Chart with Clickable Pie Chart",
    xaxis_title="Date",
    yaxis_title="Values",
    barmode="overlay",  # Bar graph overlay
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)

# Render Plotly Figure in Streamlit
click_event = st.plotly_chart(fig, use_container_width=True)

# Capture Click Event
if click_event is not None:
    st.session_state["click_data"] = click_event["points"][0]

# Process Click Event for Pie Chart
st.subheader("Pie Chart for Selected Point")
if st.session_state["click_data"]:
    click_data = st.session_state["click_data"]
    customdata = click_data.get("customdata", [])
    if customdata:
        values = customdata
        labels = ["v1", "v2", "v3"]

        # Create Pie Chart
        pie_fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo="label+percent")])
        pie_fig.update_layout(title=f"Distribution of v1, v2, v3 on {click_data['x']}")
        st.plotly_chart(pie_fig, use_container_width=True)
else:
    st.write("Click on a point on the Y line chart to display its corresponding pie chart.")
