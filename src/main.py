import ingest

def main():
    
    fileName = "sample_lightcurve.csv"
    data = None
    try:
        data = ingest.loadData("data/raw/" + fileName)
    except FileNotFoundError as e:
        print(e)
        return
    
    print("Data loaded: \n" + str(data))
    print("Mean of data: \n" + str(data.mean()))
    print("Min of data: \n" + str(data.min()))
    print("Max of data: \n" + str(data.max()))
    print("Std of data: \n" + str(data.std()))

if __name__ == "__main__":
    main()