import requests

ip = input("ip:")
mess = input("command:")
data = input("data:")
url = f'http://{ip}:5000'
message = {
    "message": mess,
    "data": data
}

response = requests.post(url, data=message)

