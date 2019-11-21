#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Docstring."""

import utils.mesure as ms
import utils.file as fl

TEMPLATE_CONF_TAB = """
\\begin{{center}}
 \\begin{{tabular}}{{ r | c c c c | c }}
 {}
 \\end{{tabular}}
 \\captionof{{table}}{{}}
\\end{{center}}
"""
TEMPLATE_MESURE = """
\\begin{{center}}
 \\begin{{tabular}}{{ r | c c c c }}
 {}
 \\end{{tabular}}
 \\captionof{{table}}{{}}
\\end{{center}}
"""

TEMPLATE_COURSE = """
\\begin{{center}}
 \\begin{{tabular}}{{ r | c || c c c }}
 n\\textsuperscript{{o}} & points & Solat & Athene & UCLMR \\\\ \\hline
 {}
 \\end{{tabular}}
 \\captionof{{table}}{{{}}}
\\end{{center}}
"""

LABEL = fl.open_yml(
    '../config/constants.yml')['labels']


def get_sorted_list_max(tab):
    result = []
    for _ in range(len(tab)):
        indice_max = tab.index(max(tab))
        result.append(indice_max)
        tab[indice_max] = 0
    return result


def color_line_mesure(line):
    color_percent = 30
    max_index = get_sorted_list_max(copy.deepcopy(line))
    for m in max_index:
        number = round(line[m], 2)
        line[m] = "\\cellcolor{{white!{}}}{}".format(
            color_percent, number)
        color_percent -= 10
    return line


def round_line_mesure(line):
    return [str(round(elt, 2)) for elt in line]


def latex_table(table):
    return '\\\\\n'.join([' & '.join(line) for line in table])


def latex_all_mesure(count, score, who):
    name_line = ['Précision', 'Rappel', 'F1score',
                 '\\hline\n\\hline\nExactitude', 'Score FNC', 'Pourcentage FNC']
    name_column = ['Mesure'] + LABEL
    hline = [["\\hline"]]
    table = [round_line_mesure(line)
             for line in ms.all_mesure(count, score, who)]
    table[-1][0] = "\\multicolumn{{{}}}{{{}}}{{{}}}".format(
        "4", "c", table[-1][0])
    table[-2][0] = "\\multicolumn{{{}}}{{{}}}{{{}}}".format(
        "4", "c", table[-2][0])
    table[-3][0] = "\\multicolumn{{{}}}{{{}}}{{{}}}".format(
        "4", "c", table[-3][0])
    table = [[name] + line for line, name in zip(table, name_line)]
    table = [name_column] + hline + table
    table = "\\multicolumn{{{}}}{{{}}}{{{}}}".format(
        "5", "c", who) + '\\\\\n' + latex_table(table) + "\\\\"
    return TEMPLATE_MESURE.format(table).replace('hline\\\\', 'hline')


def latex_conf_tab(count, who):
    conf_tab = ms.get_full_conf_tab(count, who)
    name_line = LABEL + ['Somme']
    name_column = [""] + name_line
    hline = [["\\hline"]]
    conf_tab = [[str(elt) for elt in line] for line in conf_tab]
    conf_tab = [[lab] + line for line, lab in zip(conf_tab, name_line)]
    conf_tab = [["\\multicolumn{{{}}}{{{}}}{{{}}}".format(
        "6", "c", who)]] + hline + [name_column] + hline + conf_tab[:-1] + hline + [conf_tab[-1]]
    conf_tab = latex_table(conf_tab).replace('hline\\\\', 'hline') + "\\\\"
    conf_tab = TEMPLATE_CONF_TAB.format(conf_tab)
    return conf_tab
