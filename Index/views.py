from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def donor_view(request):
    return render(request, "donor.html")


def receiver_view(request):
    return render(request, 'receiver.html')
