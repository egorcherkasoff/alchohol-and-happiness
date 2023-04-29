import pandas as pd


def get_data():
    df = pd.read_csv("data\HappinessAlcoholConsumption.csv", sep=",")
    return df


if __name__ == "__main__":
    print(get_data())
