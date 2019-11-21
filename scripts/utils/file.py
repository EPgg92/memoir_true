#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utility function module to do operations on YAML file."""

import yaml


def open_yml(path):
    """Return a dict form a yml file.

    :param path: path to a yml file
    :type path: str
    :return: dictionnary corresponding at yml file
    :rtype: dict
    """
    returned_dic = {}
    with open(path, 'r') as stream:
        returned_dic = yaml.load(stream)
    return returned_dic
