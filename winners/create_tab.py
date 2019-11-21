"""Create a usable dataframe for an easy exploitation."""

import pandas as pd


def open_csv(file):
    return pd.read_csv(file, encoding='ISO-8859-1')


def main():
    """Test function."""
    solat = open_csv('solat/averaged.csv')
    solat_deep = open_csv('solat/deepoutput.csv')
    solat_tree = open_csv('solat/tree_pred.csv')
    athene = open_csv('athene/submission.csv')
    uclmr = open_csv('uclmr/predictions_test.csv')
    gold = open_csv('competition_test_stances.csv')[["Stance"]]

    for x, y in zip(
            [uclmr, athene, solat, solat_tree],
            ['uclmr', 'athene', 'solat', 'solat_tree']):
        values = x["Stance"].values
        gold[y] = values
    values = []
    tag = ["agree", "disagree", "discuss", "unrelated"]
    for line in solat_deep[["agree", "disagree", "discuss", "unrelated"]].values:
        line = line.tolist()
        values.append(tag[line.index(max(line))])
    gold["solat_deep"] = values

    gold.to_csv("all.csv")

    print(gold)


if __name__ == '__main__':
    main()
