from django.shortcuts import render

from versements.models import Versements


# Create your views here.
def listadmin(request):
    versements = Versements.objects.all()
    context = {"services": versements}
    return render(request, "html/list-admin.html", context=context)
