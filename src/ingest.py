import pandas as pd
import lightkurve as lk

def load_csv(file_name):
    try:
        data = pd.read_csv(file_name)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        raise FileNotFoundError("File not found. Please check the file path and try again.")
    
def load_lightkurve(target, save_path=None):
    search_result = lk.search_lightcurve(target)[0].download()
    if len(search_result) == 0:
        raise ValueError("No light curve data found for the specified target.")
    if save_path:
        search_result.to_csv(save_path)
    return search_result.to_pandas()