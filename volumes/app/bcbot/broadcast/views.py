from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect

from .models import Register
from .forms import CreateRecord


def index(request):

    params = {
        'msg': 'Set Broadcast Messeages and Times',
        'create': CreateRecord(),
        'data': Register.objects.all()
    }

    return render(request, 'broadcast.html', params)


def about(request):
    return render(request, 'about.html')


def broadcast(request):

    params = {
        'msg': 'Set Broadcast Messeages and Times',
        'create': CreateRecord(),
        'data': Register.objects.all()
    }

    if request.method == 'POST':
        obj = Register()
        record = CreateRecord(request.POST, instance=obj)
        record.save()
        return redirect(to='/broadcast')
    return render(request, 'broadcast.html', params)
