import json
import sys
import pandas as pd
import os
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

#root_url = 'https://www.athlinks.com/Athletes/Api/ + %s + /Races'

def get_racer_results(root_url):
    '''Retrieve results data for a given racer'''
    userid = 77065418
    race_lst = requests.get(root_url).text
    filename = str(userid) + '.csv'
    f = open(filename, 'w')
    f.write(race_lst)
    f.close()

if __name__ == '__main__':
    root_url = 'https://www.athlinks.com/Athletes/Api/77065418/Races'
    get_racer_results(root_url)
