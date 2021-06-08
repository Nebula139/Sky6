#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    dict1 = {1: "one", 2: "two", 3: "three"}
    print(dict1.items())
    dict2 = dict()
    for key, value in dict1.items():
        dict2[value] = key
    print(dict2.items())
