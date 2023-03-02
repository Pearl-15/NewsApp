from django.shortcuts import render
import requests
API_KEY = 'aa2585274c0349358a2ed7dfc43bd589'


# Create your views here.
def home(request):

    country = request.GET.get('country')

    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()

        articles = data['articles']  #data['keyFromAPIJson']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()

        articles = data['articles']  #data['keyFromAPIJson']

    context = {
            'articles': articles
    }

    return render(request,'news_api/home.html',context)