from django.shortcuts import render, redirect
from .models import UserProfile, Organ

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_num = request.POST.get('mobnum')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        bloodgroup = request.POST.get('bloodgroup')
        birthdate = request.POST.get('birthdate')
        gender = request.POST.get('gender')
        disorder = request.POST.get('disorder')
        organs = request.POST.getlist('organs[]')

        # Check if 'identityproof' is present in the request.FILES dictionary
        if 'identityproof' in request.FILES:
            identityproof = request.FILES['identityproof']
        else:
            identityproof = None  # Set a default value if the key is not present

        user_profile = UserProfile.objects.create(
            name=name,
            email=email,
            phone_num=phone_num,
            address=address,
            city=city,
            state=state,
            bloodgroup=bloodgroup,
            identityproof=identityproof,
            birthdate=birthdate,
            gender=gender,
            disorder=disorder,
        )

        for organ_name in organs:
            organ, created = Organ.objects.get_or_create(name=organ_name)
            user_profile.organs.add(organ)

        return redirect('index:home')  # Redirect to a success page or any other page you prefer

    return render(request, 'register.html')
