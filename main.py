import re
from requests_html import HTMLSession
from checker import *

apartments = []
def update_status():
	apartments.append({
	'flat_id': flat_id,
 	'status': to_status(raw_status),
  	'rooms': int(rooms),
  	'area': AreaColumn(raw_area),
	'floor': floor,
  	'www': www,
  	'price': to_price(raw_price),
})

# # ('https://zverynoparkas.lt/butai/1-01/', '1-01', '45.05', '2', '1', 'ŠV', Laisvas, 160.000 Eur)
# for flat_id , rooms, raw_area, floor, orientation, raw_price, raw_status, www in to_results_link(rg_link, to_r_without_s(r)):
# 	price = None
# 	try:
# 		update_status()
# 	except:
# 		pass
# 		update_status()

# print(apartments)

##############################################################################################################################

# print(to_results_link(rg_link, to_r_without_s(r)))

def from_columns(item, keys):
	result = []
	for (s, item_key) in zip (item, keys):
		result[item_key] = get_column_by_key(item_key).from_string(s)

# class FlatIdColumn(object): 
# 	def __init__(self, name):
# 		self.name = name
# 	def from_string(self, name):
# 		return 45
# 	def get_key(self):
# 		return 'flat_id'

# flat_id_alone = [item[0] for item in to_results_link(rg_link, to_r_without_s(r))]
# flat_id = FlatIdColumn(flat_id_alone)
# flat_id.get_key()

# print(flat_id.from_string())

class AreaColumn(object):
	def __init__(self, name):
		self.name = name
	def from_string(self, s):
		return float(s.replace(',', '.'))
	def get_key(self):
		return 'area'

raw_area_alone =[item[2] for item in to_results_link(rg_link, to_r_without_s(r))]
raw_area = AreaColumn(raw_area_alone)
raw_area.get_key()

print(raw_area.from_string())


results = rg_link.findall(to_r_without_s(r)); 
for results in to_results_link(rg_link, to_r_without_s(r)): 
	apartments.append(from_columns(['flat_id', 'area']))

print(apartments)


# def area(raw_area):
#     area = float(raw_area.replace(',', '.'))
#     return area