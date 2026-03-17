def clean_lightkurve(data, save_path=None):
    # Remove rows with quality flags
    cleaned_data = data[data['quality'] == 0].copy()

    if save_path:
        cleaned_data.to_csv(save_path)

    return cleaned_data