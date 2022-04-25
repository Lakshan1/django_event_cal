# Django_event_cal

Django_event_cal is a Django app to intergrate event calendar to your app. users can click a specific
date and see events and also can create, edit and delete events.

## Installation

Stable version:
pip install django_event_cal

## Documentation

Usage

#####

1. Add "django_event_cal" to your INSTALLED_APPS setting like this:

```
    INSTALLED_APPS = [
        ...
        'django_event_cal',
    ]
```

2. Include the django_event_cal URLconf in your project urls.py like this:

```
    path('', include("django_event_cal.urls")),
```

3. Run `python manage.py migrate` to create the events models.

4. run import inside views.py like this:

```
    from django_event_cal.functions import cal_context
```

5. call `cal_context` function inside desired view like this and pass your context dictionary, it will return a context with additional event calendar values dictionary:

```
    def index_view(request):
        context = {}
        context = cal_context(context) #add this line
        return render(request,"base/index.html",context)
```

6. add `{% include 'events_cal/event.html' %}` inside the template where you want the calendar and events:

```
    {% include 'events_cal/event.html' %}
```

7. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

8. Visit http://127.0.0.1:8000/polls/ to participate in the poll.

Month navigation

#####

1. accept two parameters in ur desired url:

```
    urlpatterns = [
        path("<int:year>/<str:month>/",views.index_view,name="index"),
    ]
```

2. receive them in your view and pass additional arguments to the cal_context function like this:

```
    def index_view(request,year,month):
        context = {}
        context = cal_context(context,year,month,True) #add this line
        return render(request,"base/index.html",context)
```
