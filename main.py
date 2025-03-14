import requests
from send_email import send_email


api_key = "cc327becc996435bbed5c238ec32c485"

# define url as str
url = str("https://newsapi.org/v2/top-headlines?country=us"\
          "&category=business"\
          "&apiKey=cc327becc996435bbed5c238ec32c485"\
            "&language=en")  
        

request = requests.get(url) # make request
content = request.json() # convert the content into a json format dictionary


# access titles of articles

body = ""

for article in content["articles"][:10]:

    body = "Subject: Business News" + "\n" + body + str(article["title"]) + "\n" + str(article["description"])\
          + "\n" + f"Link: {article['url']}" + 2*"\n"

print(body)

body = body.encode("utf-8")
send_email(message=body)
