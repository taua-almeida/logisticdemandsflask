# Functions module
# Imports
import math


# SMA / MMS
def mms(value, base):
    totaldemand = 0
    print(value)
    for (period, demand) in value[-base:]:
        totaldemand = float(totaldemand) + float(demand)

    # round the result down or if you want up use math.ceil
    return math.floor(totaldemand / base)

