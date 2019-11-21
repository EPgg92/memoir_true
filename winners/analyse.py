'''Analyse all.csv.'''

import pandas as pd
from collections import defaultdict as dd
from collections import Counter as cnt
from pprint import pprint
import copy

RELATED = ['agree', 'disagree', 'discuss']
LABEL = RELATED + ['unrelated']
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


def get_useful_var(result):
    count = dd(int)
    score = dd(int)
    score_rel = dd(lambda: dd(int))
    same = dd(int)
    difference = []
    for line in result:
        gold, uclmr, athene, solat = line[:4]
        for i, elt in enumerate(line):
            count[(tag[i], gold, elt)] += 1
            s_fnc = score_fnc(gold, elt)
            score_rel[tag[i]][elt] += s_fnc
            score[tag[i]] += s_fnc
        if gold == uclmr and gold == athene and gold == solat:
            same[gold] += 1
        else:
            difference.append(tuple(line[:4]))
    difference = cnt(difference)
    return count, score, score_rel, same, difference


def open_csv(file):
    return pd.read_csv(file, encoding='ISO-8859-1')


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
    table = [round_line_mesure(line) for line in all_mesure(count, score, who)]
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
    conf_tab = get_full_conf_tab(count, who)
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


def what(g, v, n):
    str0 = ''
    s = score_fnc(g, v)
    if s == 0:
        return '\\textcolor{{red}}{{{} {}}}'.format(n * 0, v)
    if s == 1:
        return '\\textcolor{{green}}{{{}}}'.format(n)
    if s == 0.25:
        return '{} {}'.format(0.25 * n, v)


def how_many(g, v, n):
    str0 = ''
    s = score_fnc(g, v)
    if s == 0:
        return n * 0
    if s == 1:
        return n
    if s == 0.25:
        return 0.25 * n


def all_conf_mesure(count, score, participants):
    str0 = ''
    for p in participants:
        str0 = '{}\n{}\n{}\n'.format(str0, latex_conf_tab(
            count, p), latex_all_mesure(count, score, p))
    return str0


def main():
    pass


if __name__ == '__main__':
    all = open_csv('all.csv')

    tag = ['Stance',  'solat', 'athene', 'uclmr',
           'solat_tree', 'solat_deep', 'mix_solat_uclmr', 'mv_solat',
           'mv_athene', 'mv_uclmr']
    participants = tag[1:]
    result_only = all[tag].values
    count, score, score_rel, same, difference = get_useful_var(result_only)

    print(all_conf_mesure(count, score, ['mv_solat',
                                         'mv_athene', 'mv_uclmr']))
    # pprint(same)
    # print(sum([same[lab]for lab in same]))
    # print([(lab, count[("Stance", lab, lab)] - same[lab])for lab in same])
    # print(sum([count[("Stance", lab, lab)] - same[lab]for lab in same]))
"""    number_errors = dd(lambda: dd(lambda: dd(int)))
    for key in difference:
        errors = 0
        for x in range(1, 4):
            if key[0] != key[x]:
                errors += 1
        number_errors[key[0]][errors][(difference[key], key)] = key
    # pprint(number_errors)
    str0 = ""
    for l in ['agree', 'disagree', 'discuss', 'unrelated']:
        for error in number_errors[l]:
            name_tab = 'Tableau pour le label {} pour {} erreurs dans les participants.'.format(
                l, error)
            tab = []
            yy = []
            for i, n in enumerate(reversed(sorted(number_errors[l][error]))):
                # print(l, error, n, number_errors[l][error][n])
                values = number_errors[l][error][n]
                n = n[0]
                point = n
                if l == 'unrelated':
                    point = n / 4
                x = [str(i + 1), str(point)]
                y = [point]

                gold = values[0]
                values = values[1:]
                for v in values:
                    x.append(what(gold, v, n))
                    y.append(how_many(gold, v, n))
                tab.append(x)
                yy.append(y)
            y = [str(sum(s)) for s in zip(*yy)]
            tab = latex_table(tab)
            tab = '{}\\\\ \\hline\n{}\\\\'.format(tab, ' & '.join([''] + y))
            tab = TEMPLATE_COURSE.format(tab, name_tab)
            str0 = '{}\n{}'.format(str0, tab)
    print(str0)
"""
