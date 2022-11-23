# Security-Device

## Project Description

IIT CS330 Project - Building a security device using Finite Automata 

This repository is for the security device build using the concepts of Finite Automata or Finite State Machine.
* The first file 'main.py' implements the Security device using FSM. The unlock code is "883371", while the locking code is "883374".
To properly run the code one needs to press enter after each correct value. All the numbers except 0...9 and strings are discarded.

* The second file 'SD2.py' guesses the password 10 times randomly. It also gives the minimum, maximum and average number of tries that can be randomly generated unitl the password is guessed.

## How to set up?
The instructions below are for a Linux environment (Ubuntu 22.04).

### Instruction to set up:
1. To install python and get Git:
```
$ sudo su
$ apt update && apt install python3
$ apt install git-all
```

2. Install the `coverage` module, run the following command:
```
$ pip install coverage
```

### Setup ###

1. Clone the repository:
```
$ git clone https://github.com/Spopli08/Security-Device.git
```

2. Run the unit tests located in SD2.py:
```
$ python3 -m coverage run -m unittest
```
3. To view the coverage report:
```
$ python3 -m coverage report
```
4. To run the exxecuatble:
For the first part of the project, run `main.py`, the Security Device simulator:
```
$ ./main.py
```
The unlock code is "883371", while the locking code is "883374".
To properly run the code one needs to press enter after each correct value. All the numbers except 0...9 and strings are discarded.

The second part can be run by:
```
$ ./SD2.py
```

## Author
Sanchit Popli
## Contact
spopli@hawk.iit.edu

