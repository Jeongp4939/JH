from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':    # POST CREATE DATA

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))  # accountapp 의 hello_world 라는 앱으로 가라는 뜻

    else:
        hello_world_list = HelloWorld.objects.all()    # sql의 셀렉트문 # GET VIEW DATA
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})
