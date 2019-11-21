#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Docstring."""
import utils.file as fl

LABEL = fl.open_yml(
    '../config/constants.yml')['labels']


def _straight_conf_tab(count, who):
    return [[count[(who, truth, pred)] for pred in LABEL] for truth in LABEL]


def _conf_tab_with_sum_truth(s_conf_tab):
    return [line + [sum(line)] for line in s_conf_tab]


def _get_list_sum_pred(s_t_conf_tab):
    return [sum(column) for column in zip(*s_t_conf_tab)]


def get_full_conf_tab(count, who):

    conf_tab = _conf_tab_with_sum_truth(_straight_conf_tab(count, who))
    conf_tab.append(_get_list_sum_pred(conf_tab))
    return conf_tab


def cal_acc(count, who):
    return sum([count[(who, l, l)] for l in LABEL]) / sum([count[
        ('Stance', l, l)] for l in LABEL]) * 100


def calculate_precision(count, who, label):
    return count[(who, label, label)] / sum([count[
        (who, label, l)] for l in LABEL])


def calculate_recall(count, who, label):
    return count[(who, label, label)] / sum([count[
        (who, l, label)] for l in LABEL])


def calculate_f1score(count, who, label):
    precision = calculate_precision(count, who, label)
    recall = calculate_recall(count, who, label)
    return 2 * precision * recall / (precision + recall)


def calculate_fonc_labels(count, who, fonc):
    return [fonc(count, who, l) for l in LABEL]


def get_fnc_score(score, who):
    return [[score[who]], [score[who] / score['Stance'] * 100]]


def all_mesure(count, score, who):
    return [calculate_fonc_labels(count, who, fonc)
            for fonc in [calculate_precision,
                         calculate_recall,
                         calculate_f1score]] + [[cal_acc(count, who)]] + get_fnc_score(score, who)
