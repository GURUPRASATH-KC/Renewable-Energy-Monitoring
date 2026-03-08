import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create folders if they don't exist
os.makedirs('reports', exist_ok=True)
os.makedirs('plots', exist_ok=True)

# Simulate 30 days
days = np.arange(1, 31)
wind_speed = np.random.uniform(4, 15, size=30)  # m/s
turbine_efficiency = 0.35  # 35%
air_density = 1.225  # kg/m3
rotor_area = 10  # m2

# Power formula: 0.5 * rho * A * v^3 * efficiency
wind_energy = 0.5 * air_density * rotor_area * wind_speed**3 * turbine_efficiency / 1000  # kWh approx

# Create DataFrame
df = pd.DataFrame({
    'Day': days,
    'Wind_Speed(m/s)': wind_speed,
    'Wind_Energy(kWh)': wind_energy
})

# Save CSV
df.to_csv('reports/monthly_wind_report.csv', index=False)

# Plot
plt.figure(figsize=(10,5))
plt.plot(df['Day'], df['Wind_Energy(kWh)'], marker='o', color='blue')
plt.title('Daily Wind Energy Output')
plt.xlabel('Day')
plt.ylabel('Energy (kWh)')
plt.grid(True)
plt.savefig('plots/wind_energy_plot.png')
plt.show()