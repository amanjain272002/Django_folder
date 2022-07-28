from django.shortcuts import HttpResponse

# def index(request):
#     #query parameters
#     name  = request.GET['fname']
#     print(name)
#     return HttpResponse(f'<h1> hello {name} </h1>')
    # return HttpResponse('<h1>hello world </h1>')

def add(request):
    power = request.GET['number']
    power = int(power)**2
    print(power)
    return HttpResponse(f'{power}' )
    # return HttpResponse(2 + 3 )