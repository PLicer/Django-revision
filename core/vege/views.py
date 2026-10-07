from django.shortcuts import redirect, render

from vege.models import Receipe

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")
        print(receipe_name,receipe_description,receipe_image)

        Receipe.objects.create(receipe_name=receipe_name,receipe_description=receipe_description,receipe_image=receipe_image)
        return redirect("receipes")

    qs = Receipe.objects.all()

    if request.GET.get("search"):
        qs = qs.filter(receipe_name__icontains=request.GET.get("search"))

    context = {
        "receipes":qs
    }

    return render(request,"receipes.html",context)

def delete(request,id):
    Receipe.objects.get(id=id).delete()
    return redirect("receipes")

def update(request,id):
    qs = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")
        qs.receipe_name = receipe_name
        qs.receipe_description = receipe_description

        if receipe_image:
            qs.receipe_image = receipe_image

        qs.save()

        return redirect("receipes")

    context = {"receipe":qs}

    return render(request,"update_receipe.html",context)