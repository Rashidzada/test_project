from django.urls import path,include
from rest_framework import routers
from .viewsets import ContactViewset
router = routers.DefaultRouter()
router.register(r'contact',ContactViewset)
from .import views
urlpatterns = [
    path('api_contact/',views.api_contact,name='api_contact'),
    path('api/',include(router.urls)),
    path('',views.IndexView.as_view(),name='index'),
    path('contact/',views.contact,name='contact'),
    path('edit_contact/<int:pk>/',views.EditContact.as_view(),name='edit_contact'),
    # path('delete_contact/<int:pk>/',views.DeleteContact.as_view(),name='delete_contact'),
    path('delete_contact/<int:contact_id>/',views.delete_contact, name='delete_contact'),
    path('update_contact/<int:contact_id>/',views.update_contact, name='update_contact'),
]