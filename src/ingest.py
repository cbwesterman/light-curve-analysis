import pandas as pd
import lightkurve as lk
    
def load_lightkurve(target):
    search_result = lk.search_lightcurve(target)[0].download()
    if len(search_result) == 0:
        raise ValueError("No light curve data found for the specified target.")
    
    data = search_result.to_pandas()
    flux_median = data['flux'].median()
    data['flux'] = data['flux'] / flux_median
    data['flux_err'] = data['flux_err'] / flux_median

    return data