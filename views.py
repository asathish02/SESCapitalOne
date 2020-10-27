from django.shortcuts import render


# Create your views here.
def home(request):
    import requests
    import json

    # Returns the top headlines in the US on the home page
    news_api_request = requests.get(
        "https://newsapi.org/v2/top-headlines?country=us&apiKey=070d778afff84c4491fc8f9e73055f24"
    )

    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api': api})


def sports(request):
    import requests
    import json

    # Returns the top headlines in the US on the home page
    news_api_request = requests.get(
        "http://newsapi.org/v2/top-headlines?category=sports&apiKey=070d778afff84c4491fc8f9e73055f24"
    )

    api = json.loads(news_api_request.content)
    return render(request, 'sports.html', {'api': api})


def entertainment(request):
    import requests
    import json

    # Returns the top headlines in the US on the home page
    news_api_request = requests.get(
        "http://newsapi.org/v2/top-headlines?category=entertainment&apiKey=070d778afff84c4491fc8f9e73055f24"
    )

    api = json.loads(news_api_request.content)
    return render(request, 'entertainment.html', {'api': api})


def technology(request):
    import requests
    import json

    # Returns the top headlines in the US on the home page
    news_api_request = requests.get(
        "http://newsapi.org/v2/top-headlines?category=technology&apiKey=070d778afff84c4491fc8f9e73055f24"
    )

    api = json.loads(news_api_request.content)
    return render(request, 'technology.html', {'api': api})
