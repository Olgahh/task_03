from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list":[
    {"restaurant_name":"Rustic","food_type":"Mexican"},
    {"restaurant_name":"Bellariva","food_type":"Italian"},
    {"restaurant_name":"Rozana","food_type": "Lebanese"},
    ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object": {"restaurant_name": "Arriba","food_type": "Mexican"}

    }
    return render(request, 'detail.html', context)
