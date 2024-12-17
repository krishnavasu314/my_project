
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re
import os

# Function to clean and extract datetime from the 'start_time' column
def clean_datetime(entry):
    """
    Extract datetime components from list-like or irregular 'start_time' values.
    Args:
        entry: Raw value from 'start_time' column.
    Returns:
        pd.Timestamp or None
    """
    try:
        # Extract numbers (regex) and ensure valid datetime format
        numbers = re.findall(r'\d+\.?\d*', str(entry))
        numbers = [int(float(n)) for n in numbers]
        if len(numbers) >= 6:  # Year, month, day, hour, minute, second
            return pd.Timestamp(*numbers[:6])
        elif len(numbers) >= 5:  # Year, month, day, hour, minute
            return pd.Timestamp(*numbers[:5])
        else:
            return None
    except:
        return None

# Main function to process the dataset and generate plots
def main():
    # File Path
    file_path = 'data/metadata.csv'  # Adjust to your dataset's location

    # Create 'plots' folder to save HTML files
    output_dir = "plots"
    os.makedirs(output_dir, exist_ok=True)

    # Step 1: Load Dataset
    print("Loading dataset...")
    df = pd.read_csv(file_path)

    # Step 2: Clean 'start_time' column
    print("Cleaning 'start_time' column...")
    df['start_time'] = df['start_time'].apply(clean_datetime)
    df = df.dropna(subset=['start_time'])  # Drop invalid rows

    # Step 3: Filter impedance measurements and calculate total impedance
    print("Filtering impedance data...")
    impedance_data = df[(df['type'] == 'impedance') & df[['Re', 'Rct']].notna().all(axis=1)]
    impedance_data = impedance_data.sort_values(by='start_time')
    impedance_data['Battery_Impedance'] = impedance_data['Re'] + impedance_data['Rct']

    # Step 4: Generate Plots and Save as HTML

    # Plot 1: Electrolyte Resistance (Re) vs Time
    print("Generating plot: Electrolyte Resistance vs Time...")
    fig1 = px.line(
        impedance_data, x='start_time', y='Re',
        title='Electrolyte Resistance (Re) vs Time',
        labels={'start_time': 'Time', 'Re': 'Electrolyte Resistance (Ohms)'}
    )
    fig1.write_html(os.path.join(output_dir, "electrolyte_resistance.html"))

    # Plot 2: Charge Transfer Resistance (Rct) vs Time
    print("Generating plot: Charge Transfer Resistance vs Time...")
    fig2 = px.line(
        impedance_data, x='start_time', y='Rct',
        title='Charge Transfer Resistance (Rct) vs Time',
        labels={'start_time': 'Time', 'Rct': 'Charge Transfer Resistance (Ohms)'}
    )
    fig2.write_html(os.path.join(output_dir, "charge_transfer_resistance.html"))

    # Plot 3: Battery Impedance (Re + Rct) vs Time
    print("Generating plot: Total Battery Impedance vs Time...")
    fig3 = px.line(
        impedance_data, x='start_time', y='Battery_Impedance',
        title='Total Battery Impedance (Re + Rct) vs Time',
        labels={'start_time': 'Time', 'Battery_Impedance': 'Battery Impedance (Ohms)'}
    )
    fig3.write_html(os.path.join(output_dir, "battery_impedance.html"))

    # Combined Plot: All Parameters vs Time
    print("Generating combined plot...")
    fig_combined = go.Figure()

    fig_combined.add_trace(go.Scatter(
        x=impedance_data['start_time'], y=impedance_data['Re'],
        mode='lines', name='Electrolyte Resistance (Re)'
    ))
    fig_combined.add_trace(go.Scatter(
        x=impedance_data['start_time'], y=impedance_data['Rct'],
        mode='lines', name='Charge Transfer Resistance (Rct)'
    ))
    fig_combined.add_trace(go.Scatter(
        x=impedance_data['start_time'], y=impedance_data['Battery_Impedance'],
        mode='lines', name='Battery Impedance (Re + Rct)'
    ))

    fig_combined.update_layout(
        title='Battery Parameters Over Time',
        xaxis_title='Time',
        yaxis_title='Resistance (Ohms)',
        legend=dict(x=0, y=1)
    )
    fig_combined.write_html(os.path.join(output_dir, "combined_plot.html"))

    print("All plots saved successfully in the 'plots' folder!")

if __name__ == "__main__":
    main()
