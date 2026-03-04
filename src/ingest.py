import pandas as pd

def loadData(fileName):

    try:
        data = pd.read_csv(fileName)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("File was not found. Please check the file path and try again.")