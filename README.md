# collatz-problem
this script (currently only python, possibly adding more some time) tests the collatz-problem for every natural number (starting from 1 counting up).
Currently there is no good indication wether or not the 4-2-1 loop is reached other than an output of the first number that appears a second time in the sequence (basically if it tells you 4 than the 4-2-1 loop is reached, if it tells you anything else you broken the collatz-problem and disproven it.. like if thats ever gonna happen lol)

use this command to build your docker container:
 > docker build --tag collatz-problem/python:latest https://github.com/mrJogurt13/collatz-problem.git#main:collatzPython
