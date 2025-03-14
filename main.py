import requests
from send_email import send_email


api_key = "cc327becc996435bbed5c238ec32c485"
url = str("https://newsapi.org/v2/top-headlines?country=us&category=business&a"\
          "piKey=cc327becc996435bbed5c238ec32c485")  # define url as str

request = requests.get(url) # make request
content = request.json() # convert the content into a json format dictionary


# access titles of articles

body = ""

for article in content["articles"]:

    body = body + str(article["title"]) + "\n" + str(article["description"]) + 2*"\n"

print(body)

body = body.encode("utf-8")
send_email(message=body)
