import ingest

def main():
    
    fileName = "sample_lightcurve.csv"
    data = ingest.loadData("data/raw/" + fileName)
    print("Data loaded: \n" + str(data))

if __name__ == "__main__":
    main()