import ingest
import visualize

def main():
    
    # Use lightkurve library
    data = ingest.load_lightkurve("KIC 3733346", "data/raw/kic_3733346.csv")

    # Print the number of data points
    print(f"Data points: {len(data)}\n")

    # Time range of data
    print(f"Time starts at: {data.index.min()} days.")
    print(f"Time ends at: {data.index.max()} days.")
    print(f"Total time range: {data.index.max() - data.index.min()} days.\n")

    # Flux data
    print(f"Min flux value: {data['flux'].min()}")
    print(f"Max flux value: {data['flux'].max()}")
    print(f"Mean flux value: {data['flux'].mean()}")
    print(f"Median flux value: {data['flux'].median()}")
    print(f"Standard deviation of flux: {data['flux'].std()}\n")

    visualize.plot(data)

if __name__ == "__main__":
    main()