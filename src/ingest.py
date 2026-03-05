import pandas as pd

def loadData(fileName):

    try:
        data = pd.read_csv(fileName)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        raise FileNotFoundError("File not found. Please check the file path and try again.")