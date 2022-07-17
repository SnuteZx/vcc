import sys
import os
import argparse

def getparer():
    parser = argparse.ArgumentParser(description='get file')
    parser.add_argument('-v','--version')
    parser.add_argument('-o','--output')

    return parser


if __name__ == '__main__':
    parser = getparer()
    args = parser.parser_args()
    print ("xx")