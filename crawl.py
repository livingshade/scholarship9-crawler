
import requests
import time
import os

# token should start with '.'
token = 'you need to fill up this!'

cookies = dict(session=token)


url = "https://scholarship.net9.org/publicity_data"


def get(x):
	return requests.get(url=url, params={"id": str(x)}, cookies=cookies)

os.system("rm -f output")

# 1000 should be enough
for i in range(0, 1000):
	print("crawling {}".format(i))
	res = get(i)
	if res.status_code != 200:
		print("error occured on {}".format(i))
	else:
		text = res.text.encode('utf-8').decode('unicode_escape')
		with open("./output", "a+") as f:
			f.write(text)
	time.sleep(1)
