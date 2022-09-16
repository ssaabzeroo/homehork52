from django.shortcuts import render

from webapp.views.cat import Cat
from django.core.handlers.wsgi import WSGIRequest
cat = Cat('ВАся')


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        match request.GET.get("actions"):
            case 'play':
                cat.happiness += 15
                cat.satiety -= 10
                if cat.happiness > 100:
                    cat.happiness = 100
            case 'sleep':
                cat.satiety -= 10
                cat.happiness += 15
                if cat.happiness > 100:
                    cat.happiness = 100
            case 'eat':
                cat.satiety += 15
                cat.happiness += 5
                if cat.satiety > 100:
                    cat.happiness -= 30
                    cat.satiety = 100
                if cat.happiness > 100:
                    cat.happiness = 100
        if 30 < cat.happiness < 60:
            cat.photo = "https://memepedia.ru/wp-content/uploads/2018/07/cover-3-1.jpg"
        elif cat.happiness >= 60 <= 100:
            cat.photo = "https://st.depositphotos.com/2756082/3215/i/600/depositphotos_32152243-stock-photo-smiling-cat.jpg"
        else:
            cat.photo = "https://ru.meming.world/images/ru/thumb/7/78/%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BA%D0%BE%D1%82_3.jpg/300px-%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BA%D0%BE%D1%82_3.jpg"
        context = {
            "name": cat.name,
            "age": cat.age,
            "satiety": cat.satiety,
            "happiness": cat.happiness,
            "photo": cat.photo
        }
        return render(request, 'article_create.html', context=context)
    else:
        if request.POST.get('name') is None:
            cat.name = cat.name
        else:
            cat.name= request.POST.get('name')
        context = {
            "name": cat.name,
            "age": cat.age,
            "satiety": cat.satiety,
            "happiness": cat.happiness,
            "photo": cat.photo
        }
        return render(request, 'article_create.html', context=context)
