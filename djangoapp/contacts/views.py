from contacts.models import Contact
from contacts.serializers import ContactSerializer
from rest_framework import generics

# Create your views here.
class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetailCreate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
