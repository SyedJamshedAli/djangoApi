from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("Home page request")
    friends = ['Jam', 'Ali', 'Shah']
    return JsonResponse(friends, safe=False)
