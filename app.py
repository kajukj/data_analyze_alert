import streamlit as st
import plotly.graph_objects as go
import numpy as np
from backend import db_connect as db
import pandas as pd

# Establish a connection to the database
cur = db.database()

# Execute the query to retrieve data
query = """ SELECT TO_CHAR(SAL_ORDER_DT,'YYYY') YEAR,SUM(SAL_PROFIT) INCOME,
            SUM(SAL_RATE) EXPENSE
            FROM SAM_SAL_DATA 
            GROUP BY TO_CHAR(SAL_ORDER_DT,'YYYY')
            ORDER BY 1 """

cur.execute(query)
data = cur.fetchall()

# Extract data from the result
years = [int(entry[0]) for entry in data]
income = [entry[1] for entry in data]
expense = [entry[2] for entry in data]

# Create a Streamlit app title
st.title('Plotly Dashboard')

# Add a range slider to filter the year range
max_year = st.slider('Max Year', min_value=min(years), max_value=max(years), value=max(years))

# Filter the data based on the selected year range
filtered_data = [(y, i, e) for y, i, e in zip(years, income, expense) if y <= max_year]

# Extract filtered data
years_filtered = [entry[0] for entry in filtered_data]
income_filtered = [entry[1] for entry in filtered_data]
expense_filtered = [entry[2] for entry in filtered_data]

# Create a bar chart using Plotly
fig = go.Figure(data=[
    go.Bar(name='Income', x=years_filtered, y=income_filtered),
    go.Bar(name='Expense', x=years_filtered, y=expense_filtered)
])

# Update the layout
fig.update_layout(
    title='Income vs Expense Over Years',
    xaxis_title='Year',
    yaxis_title='Amount',
    barmode='group'
)

# Display the bar chart
st.plotly_chart(fig)
filtered_df = pd.DataFrame({
    'Year': years_filtered,
    'Income': income_filtered,
    'Expense': expense_filtered
})


# Display a clickable link
if st.button('Show Data'):
    show_data = st.session_state.get('show_data', True)
    if show_data:
        print(show_data)
        st.dataframe(filtered_df)
    else:
        pass
    st.session_state['show_data'] = not show_data

# Create the second bar chart using Plotly
# Example data
categories = ['Category A', 'Category B', 'Category C']
values = [10, 20, 30]

fig2 = go.Figure(go.Bar(x=categories, y=values))

# Update the layout for the second chart
fig2.update_layout(
    title='Example Bar Chart',
    xaxis_title='Category',
    yaxis_title='Value'
)

# Display the bar charts side by side
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)

