#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 10:40:27 2018

@author: zhouheyu
"""

import sys
import os
import ComputeScore


def main():
    print 'main function begin.'
    if len(sys.argv) != 4:
        print 'parameter is incorrect!'
        print 'Usage: python check.py inputFile predictData TestFile'
        exit(1)
    # Read the input files
    inputFilePath = sys.argv[1]
    predictDataPath = sys.argv[2]
    TestFilePath = sys.argv[3]
    
    predict_infor_array = read_lines(predictDataPath)
    input_file_array = read_lines(inputFilePath)
    Test_file_array=read_lines(TestFilePath)
    # implementation the function predictVm
    Score=ComputeScore.getScore(predict_infor_array,input_file_array,Test_file_array)
    print Score
    print 'main function end.'


def write_result(array, outpuFilePath):
    with open(outpuFilePath, 'w') as output_file:
        for item in array:
            output_file.write("%s\n" % item)


def read_lines(file_path):
    if os.path.exists(file_path):
        array = []
        with open(file_path, 'r') as lines:
            for line in lines:
                array.append(line)
        return array
    else:
        print 'file not exist: ' + file_path
        return None


if __name__ == "__main__":
    main()
