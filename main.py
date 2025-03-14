import requests

api_key = "cc327becc996435bbed5c238ec32c485"
url = str("https://newsapi.org/v2/top-headlines?country=us&category=business&a"\
          "piKey=cc327becc996435bbed5c238ec32c485")  # define url as str

request = requests.get(url) # make request
content = request.json() # convert the content into a json format dictionary


# access titles of articles
for index, article in enumerate(content["articles"]):

    print(index+1, article["title"])
