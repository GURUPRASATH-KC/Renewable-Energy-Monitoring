import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create folders if they don't exist
os.makedirs('reports', exist_ok=True)
os.makedirs('plots', exist_ok=True)

# Simulate 30 days
days = np.arange(1, 31)
sunlight_intensity = np.random.uniform(3, 10, size=30)  # kWh/m2/day
panel_efficiency = 0.18  # 18%

# Calculate energy generated per day
solar_energy = sunlight_intensity * panel_efficiency * 1  # assume 1 m2 panel

# Create DataFrame
df = pd.DataFrame({
    'Day': days,
    'Sunlight(kWh/m2)': sunlight_intensity,
    'Solar_Energy(kWh)': solar_energy
})

# Save CSV
df.to_csv('reports/monthly_solar_report.csv', index=False)

# Plot
plt.figure(figsize=(10,5))
plt.plot(df['Day'], df['Solar_Energy(kWh)'], marker='o', color='orange')
plt.title('Daily Solar Energy Output')
plt.xlabel('Day')
plt.ylabel('Energy (kWh)')
plt.grid(True)
plt.savefig('plots/solar_energy_plot.png')
plt.show()