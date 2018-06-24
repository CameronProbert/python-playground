#!/usr/bin/python
import maths

def increment (num):
  return maths.add(num, 1)

def square (num):
  return num * num

def power (num, power):
  endNum = num
  i = 1
  while i < power:
    endNum * num
    i = i + 1
  return endNum

print(increment(1))