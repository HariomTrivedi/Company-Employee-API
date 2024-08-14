from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home")
    Friends = [
        'Raj'
        'Sunil'
        'parth'
        'chaitanya'
    ]
    return JsonResponse(Friends, safe=False)