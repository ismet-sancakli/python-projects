import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


api_key = os.environ.get("OWN_API_KEY")
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "Your Account SID"
auth_token = os.environ.get("OWN_AUTH_TOKEN")


MY_LAT = 51.507351
MY_LON = -0.127758

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWN_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hourly_data in weather_slice:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella.",
            from_="Your Twilio trial number",
            to="The number of the person you want to send."
        )
    print(message.status)

# print(weather_data["hourly"][0]["weather"][0]["id"])




