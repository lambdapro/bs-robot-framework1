import http.client

conn = http.client.HTTPSConnection("api.lambdatest.com")
payload = ''
headers = {
  'Authorization': 'Basic ZGVla3NoYXNhbHVndTp0RlU2ZzBjcmJHSjg1V0tDR3U0V1ZTNnJyUGxYOXdRdGM1U29KeG1rNDBvaVNWY0FjVQ=='
}
conn.request("GET", "/automation/api/v1/sessions", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))