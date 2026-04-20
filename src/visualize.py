import matplotlib.pyplot as plt
import numpy as np

def plot(raw_data, cleaned_data):
    plt.figure(figsize=(10, 5))

    removed = raw_data[~raw_data.index.isin(cleaned_data.index)]

    plt.plot(raw_data.index, raw_data['flux'], '.', alpha=0.2, label="Raw Data")
    plt.plot(cleaned_data.index, cleaned_data['flux'], '.', label="Kept Data")
    plt.plot(removed.index, removed['flux'], 'r.', label="Removed Outliers")

    plt.title("Light Curve Cleaning")
    plt.xlabel("Time")
    plt.ylabel("Flux")
    plt.legend()

    plt.show()