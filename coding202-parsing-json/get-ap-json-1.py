from urllib.request import Request, urlopen

req = Request('https://devnetapi.cisco.com/sandbox/mse/api/config/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
try:
    with urlopen(req) as response:
        response_string = response.read().decode('utf-8')
        print(response_string)
except Exception as e:
    print(str(e))
