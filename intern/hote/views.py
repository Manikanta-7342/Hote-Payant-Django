from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    # dest1 = {'name':"Hyderabad",'price':400,'img':'static/images/Hyderabad.jpg'}
    # dest2 = {'name':"Bangalore",'price':500,'img':'static/images/Bengaluru.jpg'}
    # dest3 = {'name':"Mumbai",'price':600,'img':'static/images/Mumbai.jpg'}
    # dests=[dest1,dest2,dest3]

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})


    #media/pics/Bengaluru.jpg