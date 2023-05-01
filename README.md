# FIT1045: Basic Algorithms/Data Structures, Debugging, Code Style in Python

[View the slides](https://www.canva.com/design/DAFg1vJXg7s/6-0FxSWMXRa86JW2km5cuA/view?utm_content=DAFg1vJXg7s&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)

This repo contains some code examples intended to teach beginner programming concepts in python, such as built in data structures, code style, debugging, and some basic algorithms.

## Run the Examples

All examples can be run just by calling `python <file_name>`. This repo requires python 3.10 or higher (just for the typing code). You can check your python version using `python --version`.

## Connect K Implementation

[./assignment_1/](./assignment_1/) contains two example implementations of how I would approach building connect K in the shell. It is not a complete implementation, and it doesn't follow the same code-structure rules as the assignment specification. Instead, the aim is to demonstrate my personal style of programming focusing on a procedural, top to bottom flow that hopefully simplifies the logic a bit. There are also two implementations, a [line by line](./assignment_1/line_by_line.py) implementation and a [neighbours](./assignment_1/neighbours.py) which demonstrate different ways of checking whether a player has won.

## Word Guessing Game

[./guess_word/](./guess_word/) contains another small python game meant to demonstrate how you can use datasets, and how to manipulate them to be able to run your queries efficiently. The game is similar to [Betweenle](https://betweenle.com/) and includes an AI player that tries to play using the "binary search" strategy.

## Debugging Examples

[./debugging/](./debugging/) contains examples of students' code I have debugged, broken into stages to show the process of how to identify what errors were made. To view these examples, I recommend using a "diff" tool to compare the files step by step and see what changes were made on the way to fixing each bug.

Note that the [Board Printing](./debugging/board_printing/) code never completely works. I fixed a few bugs, but there is quite a lot of code and even with my fixes there are more problems with the conditional statements in `end_of_game()`. Sometimes when everything seems difficult and fixing one issue just reveals more and more bugs, my advice is to throw it out and try again.

Don't do this if you can avoid it, but if you only develop a good mental model of what your code is supposed to do after writing an initial buggy implementation, you might be able to rewrite it in a more concise, or better laid out way that makes it easier to understand, and avoid those issues.