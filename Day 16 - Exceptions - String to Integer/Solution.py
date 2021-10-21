#!/bin/python3

import math
import os
import random
import re
import sys


S = input().strip()
try:
  num = int(S)
  print(S)
except:
  print("Bad String") 