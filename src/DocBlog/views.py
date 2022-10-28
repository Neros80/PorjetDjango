from datetime import datetime
from django.shortcuts import render


def index(request):

    date = datetime.today()
    print(date)
    print(type(date))

    return render(request, "docBlog/index.html", context={"date": date})
