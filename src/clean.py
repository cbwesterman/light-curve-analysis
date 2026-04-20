import numpy as np

def remove_bad_quality_flags(data):
    return data[data['quality'] == 0].copy()

def normalize_flux(data):
    flux_median = data['flux'].median()
    data['flux'] = data['flux'] / flux_median
    data['flux_err'] = data['flux_err'] / flux_median
    return data

def remove_outliers_mad(data, threshold = 5):
    flux = data['flux']
    flux_median = flux.median()
    mad = (flux - flux_median).abs().median()
    if mad == 0:
        return data
    
    modified_z = 0.6745 * (flux - flux_median) / mad
    mask = modified_z.abs() < threshold

    return data[mask]
    

def clean_lightkurve(data, save_path=None):
    # Remove rows with quality flags
    cd = remove_bad_quality_flags(data)
    cd = normalize_flux(cd)
    cd = remove_outliers_mad(cd)

    if save_path:
        cd.to_csv(save_path)

    return cd