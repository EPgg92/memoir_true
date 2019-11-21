from pprint import pprint
import pandas as pd


def open_csv(file):
    return pd.read_csv(file, encoding='ISO-8859-1')


def get_majority_vote(dataframe, selected):
    dic_lab = {"solat": ("athene", "uclmr"), "uclmr": (
        "athene", "solat"), "athene": ("solat", "uclmr")}
    values = dataframe[["solat", "athene", "uclmr"]]
    values = {key: values[[key]].values.tolist() for key in values}
    values = {key: [elt[0] for elt in values[key]] for key in values}
    temp = []
    for i, lab in enumerate(values[selected]):
        v = lab
        if values[dic_lab[selected][0]][i] == values[dic_lab[selected][1]][i]:
            v = values[dic_lab[selected][0]][i]
        temp.append(v)
    values = temp
    return values


def main():
    pass


if __name__ == '__main__':
    dataframe = open_csv("all.csv")
    mv_solat = get_majority_vote(dataframe, 'solat')
    mv_athene = get_majority_vote(dataframe, 'athene')
    mv_uclmr = get_majority_vote(dataframe, 'uclmr')
    dataframe["mv_solat"] = mv_solat
    dataframe["mv_athene"] = mv_athene
    dataframe["mv_uclmr"] = mv_uclmr
    dataframe.to_csv("all.csv")
