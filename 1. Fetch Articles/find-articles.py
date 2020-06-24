import pymongo
from pymongo import MongoClient
from collections import Counter

# ---------- Fixed Params ------------
art_client = MongoClient('mongodb://10.237.26.159:27017/')
client = MongoClient('mongodb://10.237.26.159:27017/')
art_db = art_client['media-db']
my_db = client['media-db']
# -----------------------------------

print("Finding articles...")

# Enter the base set of keywords in the regex below, separated by |

#x = art_db.articles.find({'$and':[{'text': {'$regex': ' Aadhar|Aadhaar|Adhar|Adharcard|Aadharcard|Aadhaarcard|UIDAI|Aadhar Card ', '$options': 'i'}}]},
#                     no_cursor_timeout=True)

#x = art_db.articles.find({'$and':[{'text': {'$regex': ' GST|Goods and Services Tax|Goods & Services Tax|Excise Duty ', '$options': 'i'}}]},
#                     no_cursor_timeout=True)

#x = art_db.articles.find({'$and':[{'text': {'$regex': ' demonetis|demonetiz|demonitis|demonitiz|denomination note|cash withdrawal|swipe machine|\
#	unaccounted money|withdrawal limit|pos machine|fake currency|digital payment|digital transaction|cash transaction|cashless economy|black money|\
#	cash crunch|currency switch|long queue|demonetised note|cashless transaction|note ban|currency switch ', '$options': 'i'}}]},
#                     no_cursor_timeout=True)

x = art_db.articles.find({'$and':[{'text': {'$regex': ' loan waiver|farmer loan|farmer suicide|pest infestation|Swaminathan Commission|National Commission on Farmer, \
	kisan|monsoon failure|crop failure|fertilizers|Seeds Corporation|farmer|agricultural ', '$options': 'i'}}]},
                     no_cursor_timeout=True)

#articles = input('Enter name of collection to store resultant articles: ')
articles = "farmers-all"

print("Storing articles now...")
coll = my_db[articles]
art_map = {}
count = 0

for art in x:
	count+=1
	print('Doing for '+str(count)+' relevant article')
	url = art['articleUrl']
	if url not in art_map:
		art_map[url] = 1
		coll.insert_one(art)
	# try:
	# 	cat = str(art['category'])
	# 	print('category attribute found')
	# 	if url not in art_map:
	# 		art_map[url] = 1
	# 		coll.insert_one(art)
	# except KeyError as err1:
	# 	print('category attribute not found')
		
	# try:
	# 	lis = art['categories']
	# 	print('categories attribute found')
	# 	if url not in art_map and 'OPINION' in lis:
	# 		art_map[url] = 1
	# 		coll.insert_one(art)
	# except KeyError as err2:
	# 	print('categories attribute not found')
	# 