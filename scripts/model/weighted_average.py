"""This module permit to calculate the weighted average between two system.
"""


def weighted_average50(x, y):
    """
    Return the 50/50 average between x and y.

    :param x: first entry for the average
    :type x: float
    :param y: second entry for the average
    :type y: float
    :return: 50/50 weighted average of x and y
    :rtype: float
    """
    return (50 * x + 50 * y) / (50 + 50)


def weighted_average(list_of_values, list_of_weight=[]):
    """
    Return the weighted average between a list of values.

    If list_of_weight is just an empty list, list_of_weight begin a list of an
    equal pourcent of lenght list_of_values

    :param list_of_value: ordonned list of values
    :type list_of_value: list
    :param list_of_weight: ordonned list of weights
    :type list_of_weight: list
    :return: return weighted average
    :rtype: float
    """
    if list_of_weight == []:
        list_of_weight = [100 / len(list_of_values) for _ in list_of_values]
    return sum([v * w for v, w in zip(
        list_of_values, list_of_weight)]) / sum(list_of_weight)


def _calculate_all(sublist1, sublist2):
    return [weighted_average([elt1, elt2])
            for elt1, elt2 in zip(sublist1, sublist2)]


def calculate_all(list1, list2):
    return [_calculate_all(sublist1, sublist2)
            for sublist1, sublist2 in zip(list1, list2)]


def asign_label(mix,  LABELS):
    return [LABELS[m.index(max(m))] for m in mix]


def main():
    pass


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    c = [7, 8, 9, 2, 1]
    d1 = [a, b, c]
    d2 = [c, b, a]
    from pprint import pprint
    pprint(calculate_all(d1, d2))
    pprint(weighted_average(a))
