"""Osef on s'en branle."""

import utils.mesure as ms
import utils.dataframe as df
import utils.file as futils
from pprint import pprint


def main():
    """Blablabla Docstring blablabla."""
    a = df.open_csv(
        '/home/poggioe0/github/fnc-1/datasets/'
        + 'competition_test/competition_test_bodies.csv')
    dict_of_path = futils.open_yml(
        "/home/poggioe0/github/fnc-1/config/paths.yml")
    results_test_fnc = df.transfrom_dictpath_into_dictdataframe(
        dict_of_path['results_test_fnc'])
    pprint(results_test_fnc)


if __name__ == '__main__':
    main()
