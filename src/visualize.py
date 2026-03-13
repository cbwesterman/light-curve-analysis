import matplotlib.pyplot as plt
import numpy as np

def plot(data):
    data_array = data.to_numpy()
    plt.plot(data_array[:, 0]) # Plots the first column (flux)
    plt.title("Light Curve")
    plt.xlabel("Time")
    plt.ylabel("Brightness")
    plt.show()