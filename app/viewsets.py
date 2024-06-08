from rest_framework import viewsets
from .serializers import *
class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-id')
    serializer_class = ContactSerializer
