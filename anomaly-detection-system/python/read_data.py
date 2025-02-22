import numpy as np
import matplotlib.pyplot as plt

file_path = "C:\\Users\\mahee\\Downloads\\DASHlink_full_fourclass_raw_comp.npz"
full_data = np.load(file_path)
data = full_data['data']
label = full_data['label']
print(f"Data shape: {data.shape}")
print(f"Label shape: {label.shape}")
instance_index = 0
instance_data = data[instance_index]
instance_label = label[instance_index]

print(f"Instance {instance_index} Label: {instance_label}")
print(f"Instance Shape: {instance_data.shape}")

# Plot a specific variable over time (e.g., Altitude at index 3)
time_steps = range(instance_data.shape[0])
plt.plot(time_steps, instance_data[:, 4])  # Altitude
plt.title("Altitude Over Time")
plt.xlabel("Time Steps (seconds)")
plt.ylabel("Altitude (Feet)")
plt.show()