import requests
from datetime import datetime

response1 = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response1.json()
iss_position  = (float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])) 
print (iss_position)


parameters = {
    "lat": iss_position[0],
    "lng": iss_position[1],
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

data_data = response.json()
sunrise = data_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data_data["results"]["sunset"].split("T")[1].split(":")[0]
now = datetime.now().hour

print (f"Sunrise: {float(sunrise)}\nSunset: {float(sunset)}\nNow: {float(now)}")


