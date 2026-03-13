import pandas as pd
import lightkurve as lk
    
def load_lightkurve(target, save_path=None):
    search_result = lk.search_lightcurve(target)[0].download()
    if len(search_result) == 0:
        raise ValueError("No light curve data found for the specified target.")
    
    data = search_result.to_pandas()
    data['flux'] = data['flux'] / data['flux'].median()
    data['flux_err'] = data['flux_err'] / data['flux'].median()

    if save_path:
        data.to_csv(save_path)
    return data