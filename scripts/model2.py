#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Docstring.'''

import sys
import pandas as pd
import model.weighted_average as wa
import utils.file as fl
import utils.mesure as ms
import utils.mesure2 as ms2
import utils.dataframe as df
from collections import Counter as cnt
import utils.functions as fun
from collections import defaultdict as dd
import utils.code_latex as ltx

tag_vec = ['solat_agree', 'solat_disagree', 'solat_discuss',
           'solat_unrelated', 'uclmr_agree', 'uclmr_disagree',
           'uclmr_discuss', 'uclmr_unrelated', ]
tag_lab = ['Stance']

rln = fl.open_yml(
    '../config/constants.yml')['revert_labels_number']


def main():
    if 'dev' in sys.argv:
        test_vectors = df.open_csv(
            'vectors/dev_test_vectors.csv')[tag_vec].as_matrix()
        test_labels = df.open_csv(
            'vectors/dev_test_labels.csv')[tag_lab].as_matrix()
    else:
        test_vectors = df.open_csv(
            'vectors/test_vectors.csv')[tag_vec].as_matrix()
        test_labels = df.open_csv(
            'vectors/test_labels.csv')[tag_lab].as_matrix()
    tuples_group_label = [(0, 4), (1, 5), (2, 6), (3, 7)]
    pred_label = []
    for vec, label in zip(test_vectors, test_labels):
        pred = [wa.weighted_average50(vec[x], vec[y])
                for x, y in tuples_group_label]
        pred = pred.index(max(pred))
        pred_label.append((pred, label[0]))
    pred_label = [(rln[x], rln[y]) for x, y in pred_label]
    print(ms2.all_mesure(pred_label))
    score_pred = sum([fun.score_fnc(label, pred)
                      for pred, label in pred_label])
    score_max = sum([fun.score_fnc(label, label)
                     for pred, label in pred_label])
    score_fnc_pourcent = score_pred / score_max * 100
    print("Score FNC:", score_pred, " / ", score_max)
    print('Pourcentage:', score_fnc_pourcent)

    score = {"Stance": score_max, "model": score_pred}
    count = dd(int)
    for pred, label in pred_label:
        count[("model", label, pred)] += 1
        count[("Stance", label, label)] += 1
    with open('res_model2.txt', 'w+') as stream:
        stream.write(ltx.latex_conf_tab(count, 'model'))
        stream.write('\n')
        stream.write(ltx.latex_all_mesure(count, score, 'model'))


if __name__ == '__main__':
    main()
