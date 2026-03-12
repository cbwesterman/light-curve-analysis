import ingest
import visualize

def main():
    
    # Use local .csv
    # data = ingest.loadData("sample_lightcurve.csv")

    # Use lightkurve library
    # data = ingest.load_lightkurve("KIC 3733346", "data/raw/kic_3733346.csv")
    
    visualize.plot(data)

if __name__ == "__main__":
    main()