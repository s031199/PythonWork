import re
from requests_html import HTMLSession
import string

from VilniausMonmartas import *

def to_r_without_s(r):
    r_without_s = re.sub(r"\s+", "", r.text)
    return r_without_s

def to_results_link(rg_link, r_without_s):
    results_link = rg_link.findall(to_r_without_s(r))
    return results_link

def to_results_without_link(rg_without_link, r_without_s):
    results_without_link = rg_without_link.findall(to_r_without_s(r))
    return results_without_link

def to_status(raw_status):
    status = raw_status.upper().strip()
    if 'PARDUOTAS' in status:
        return 2
    elif 'PARDUOTA' in status:
        return 2
    elif 'LAISVAS' in status:
        return 0
    elif 'LAISVA' in status:
        return 0
    elif 'IETAPAS' in status:
        return 0
    elif 'IIETAPAS' in status:
        return 0
    elif 'IIIETAPAS' in status:
        return 0
    elif 'REZERVUOTAS' in status:
        return 1
    elif 'REZERVUOTA' in status:
        return 1 
    else:
        raise Exception('Nesupratau statuso')

# class AreaColumn(Column): 
#   def from_string(s):
#     return float(s.replace(',', '.'))
#   def get_key(self):
#      return 'area'

def to_price(raw_price):
    raw_price = raw_price.upper().strip()
    if raw_price is None:
        return None
    else:
        price = raw_price.replace('&EURO;', '')
        price = price.replace('EUR', '')
        price = price.replace('.', '')
        return price

