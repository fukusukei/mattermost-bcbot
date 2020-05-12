from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404

from .models import Register
from .forms import CreateRecord
from logging import getLogger

from celery.result import AsyncResult

from .tasks import add

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

    task_id = add.delay(5, 5)
    result = AsyncResult(task_id)
    logger.error(result)
    logger.error(result.state)
    logger.error(result.ready())
    return render(request, 'broadcast.html', params)

