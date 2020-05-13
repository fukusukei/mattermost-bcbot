from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404

from .models import Register
from .forms import CreateRecord
from logging import getLogger
from .tasks import Broadcast_Entrytasks

logger = getLogger(__name__)

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
    if request.method == 'POST':
        logger.debug(request.POST["func"])
        if request.POST["func"] == "create":
            obj = Register()
            record = CreateRecord(request.POST, instance=obj)
            record.save()
            Broadcast_Entrytasks(obj.Years, obj.Months, obj.Days, obj.Hours, obj.Minutes)
            return redirect(to='/broadcast')
        elif request.POST["func"] == "delete":
            book = get_object_or_404(Register, pk=request.POST["sub"])
            book.delete()
            return redirect(to='/broadcast')

    params = {
        'msg': 'Set Broadcast Messeages and Times',
        'create': CreateRecord(),
        'data': Register.objects.all()
    }

    return render(request, 'broadcast.html', params)

