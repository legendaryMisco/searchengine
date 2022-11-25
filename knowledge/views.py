from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
import requests
# Create your views here.
def Home(request):
    results = []
    query=''
    if request.method == "POST":
        query = request.POST.get('search')
        if query == "":
            return redirect('home')
        else:
            web = requests.get('https://search17.lycos.com/web/?q='+query).text
            scrap = BeautifulSoup(web, 'lxml')
            listings = scrap.find_all(class_="result-item")
            for content in listings:
                title = content.find(class_='result-title').text
                description = content.find(class_='result-description').text
                link = content.find(class_='result-link').text
                url = content.find(class_='result-url').text
                results.append((title,description,url))

    context= {'results':results,'query':query}
    return render(request, 'index.html',context)