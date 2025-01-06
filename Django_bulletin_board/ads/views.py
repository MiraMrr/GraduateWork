from django.shortcuts import render, redirect, get_object_or_404
from .models import Advertisement
from .forms import AdvertisementForm

def index(request):
    ads = Advertisement.objects.all()
    return render(request, 'ads/index.html', {'ads': ads})

def create_ad(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AdvertisementForm()
    return render(request, 'ads/create.html', {'form': form})

def delete_ad(request, ad_id):
    ad = get_object_or_404(Advertisement, id=ad_id)
    ad.delete()
    return redirect('index')
