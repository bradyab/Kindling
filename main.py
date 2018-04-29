# coding=utf-8

from datetime import date, datetime
from random import random
from time import sleep

import config
import tinder_api as api
import features as feat

'''
This file collects important data on your matches,
allows you to sort them by last_activity_date, age,
gender, message count, and their average successRate.
'''

mydata = feat.api.get_self()
# print(get_photos(mydata))
# myself