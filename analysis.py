
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Step 1: Load the dataset
file_path = 'C:/Users/skkha/Desktop/my_project/my_project/data/metadata.csv'
data = pd.read_csv(file_path)

# Step 2: Inspect dataset structur e
print(data.info())  # Check columns and data types
print(data.head())  


# Drop rows with NaN values in Re and Rct columns
data = data.dropna(subset=['Re', 'Rct'])

data.head()

re_data = data['Re']
rct_data = data['Rct']


import plotly.graph_objects as go

figur = go.Figure()
figur.add_trace(go.Scatter(x=data.index, y=re_data, mode='lines', name='Re'))
figur.add_trace(go.Scatter(x=data.index, y=rct_data, mode='lines', name='Rct'))

figur.update_layout(
    title='Battery Impedance Parameters over Aging',
    xaxis_title='Cycle Number',
    yaxis_title='Impedance (Ohms)',
    legend_title='Parameter'
)

figur.show()