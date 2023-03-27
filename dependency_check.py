import pandas as pd
import time


def dependency_check():
    i=[1,2,3,4,5,6]
    for x in i:
        if x<5:
            print(x)
            time.sleep(5)
        else:
            print("hello")

dependency_check()

