from django.urls import path 

from . import views

urlpatterns = [
    path("get_event/",views.get_event_view,name="get_event"),
    path("add_event/",views.add_event_view,name="add_event"),
    path("edit_event/",views.edit_event_view,name="edit_event"),
    path("delete_event/",views.delete_event_view,name="delete_event"),
]