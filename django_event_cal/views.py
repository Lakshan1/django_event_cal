from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

from .models import Events
from .forms import EventForm,AdEventForm
from .functions import cal_context


# Create your views here.

def get_event_view(request):
    if request.is_ajax():
        res = None
        date = request.POST.get("date")
        month = request.POST.get("month")
        year = request.POST.get("year")
        if Events.objects.all().filter(date=date,month__icontains=month,year=year).exists():
            objs = Events.objects.all().filter(date=date,month=month,year=year)
            data = []
            for obj in objs:
                item = {
                    'title':obj.event_name,
                    'description':obj.body,
                    'slug':obj.slug,
                }
                data.append(item)
            res = data
        else:
            res = 'No Events found...'
        return JsonResponse({'data':res})
    else:
        return JsonResponse({})

def add_event_view(request):
    if request.method == "POST":
        form = AdEventForm(request.POST)
        year = request.POST.get("year")
        month = request.POST.get("month")
        date = request.POST.get("date")
        if form.is_valid():
            form.save()

            objs = Events.objects.all().filter(date=date,month=month,year=year)
            data = []
            for obj in objs:
                item = {
                    'title':obj.event_name,
                    'description':obj.body,
                    'slug':obj.slug,
                }
                data.append(item)
            res = data
            return JsonResponse({'data':res})
        else:
            return JsonResponse({'data':"Please fill out all the fields"})
    form = AdEventForm()
    return HttpResponse(form.as_p())

def edit_event_view(request):
    if request.method == "POST":
        year = request.POST.get("year")
        month = request.POST.get("month")
        date = request.POST.get("date")
        slug = request.POST.get("slug")
        obj = Events.objects.get(slug=slug)
        form = EventForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()

            objs = Events.objects.all().filter(date=date,month=month,year=year)
            data = []
            for obj in objs:
                item = {
                    'title':obj.event_name,
                    'description':obj.body,
                    'slug':obj.slug,
                }
                data.append(item)
            res = data
            return JsonResponse({'data':res})
        else:
            return JsonResponse({'data':"Please fill out all the fields"})
    slug = request.GET.get("data")
    print("working")
    obj = Events.objects.get(slug=slug)
    form = EventForm(instance=obj)
    return HttpResponse(form.as_p())

def delete_event_view(request):
    slug = request.GET.get("data")
    obj = Events.objects.get(slug=slug)
    year = obj.year
    month = obj.month
    date = obj.date
    obj.delete()
    if Events.objects.all().filter(date=date,month__icontains=month,year=year).exists():
        objs = Events.objects.all().filter(date=date,month=month,year=year)
        data = []
        for obj in objs:
            item = {
                'title':obj.event_name,
                'description':obj.body,
                'slug':obj.slug,
            }
            data.append(item)
        res = data
        return JsonResponse({'data':res})
    else:
        res = 'No Events found...'
        return JsonResponse({'data':res})