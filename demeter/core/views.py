from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Good

# Create your views here.
def index(request):
    num_goods = Good.objects.all().count()
    return render(
            request,
            'index.html',
            context={'num_goods':num_goods}
    )

def change(request):
    idG = int(request.GET['id'])
    print(idG)
    valG = int(request.GET['value'])
    t = Good.objects.get(id=idG)
    t.value = valG  # change field
    t.save()
    return HttpResponse(request)

class GoodListView(generic.ListView):
    model = Good

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context