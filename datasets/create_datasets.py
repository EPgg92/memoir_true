import pandas as pd
import numpy as np
import itertools
from pprint import pprint

RELATED = ['agree', 'disagree', 'discuss']
LABEL = RELATED + ['unrelated']


def open_csv(file):
    return pd.read_csv(file, encoding='ISO-8859-1')


def suffle_dataframe(dataframe):
    return dataframe.sample(frac=1, random_state=42).reset_index(drop=True)


def create_dev_train(dataframe, percent=10):
    number_dev = int(percent * len(dataframe) / 100)
    return dataframe.head(n=number_dev), dataframe.tail(
        n=len(dataframe) - number_dev).reset_index(drop=True)


def x_subtrain(dataframe, x=4):
    return [pd.DataFrame(data=df).reset_index(drop=True)
            for df in np.array_split(dataframe, x)]


def labels_subtrain(df, labels):
    return df.loc[df['Stance'].isin(labels)].reset_index(drop=True)


def combine_labels():
    return {tuple(sorted([x, y]))
            for x, y in itertools.product(LABEL, LABEL) if x != y}


def main():
    pass


if __name__ == '__main__':
    dataframe = open_csv('train/train_stances.csv')
    df_train = suffle_dataframe(dataframe)
    # df_dev, df_train = create_dev_train(df_train)
    # df_dev.to_csv('dev_test.csv')
    x_train = x_subtrain(df_train)
    comb_lab_train = {"_".join(key): labels_subtrain(
        df_train, key) for key in combine_labels()}

    [df.to_csv('subtrain{}.csv'.format(i + 1)) for i, df in enumerate(x_train)]
    [comb_lab_train[key].to_csv('subtrain_{}.csv'.format(key))
     for key in comb_lab_train]
