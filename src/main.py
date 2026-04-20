import clean
import ingest
import visualize

def main():
    
    # Use lightkurve library
    raw_data = ingest.load_lightkurve("KIC 3733346")
    cleaned_data = clean.clean_lightkurve(raw_data, "data/raw/kic_3733346.csv")

    # Print the number of data points
    print(f"Data points: {len(cleaned_data)}\n")

    # Time range of data
    print(f"Time starts at: {cleaned_data.index.min()} days.")
    print(f"Time ends at: {cleaned_data.index.max()} days.")
    print(f"Total time range: {cleaned_data.index.max() - cleaned_data.index.min()} days.\n")

    # Flux data
    print(f"Min flux value: {cleaned_data['flux'].min()}")
    print(f"Max flux value: {cleaned_data['flux'].max()}")
    print(f"Mean flux value: {cleaned_data['flux'].mean()}")
    print(f"Median flux value: {cleaned_data['flux'].median()}")
    print(f"Standard deviation of flux: {cleaned_data['flux'].std()}\n")

    visualize.plot(raw_data, cleaned_data)

if __name__ == "__main__":
    main()