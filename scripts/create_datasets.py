import utils.datasets as ds
import utils.dataframe as df


def datasets_for_ensemble_learning():
    train = df.open_csv('../datasets/train/train_stances.csv')
    train = df.suffle_dataframe(train)
    for x in range(2, 11):
        subtrain = ds.create_train_datasets_ssl(train, x)
        ds.save_list_couple_tt_subtrain(subtrain, "_{}".format(x))


def main():
    pass


if __name__ == '__main__':
    datasets_for_ensemble_learning()
    pass
