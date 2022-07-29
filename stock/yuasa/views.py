from datetime import datetime, timedelta

from django.shortcuts import render, redirect

from .models import PaletteSauron, PalettePicard

from .forms import PaletteSauronForm, PalettePicardForm


def nbre_jours_max_stockage_avant_sulfatation(technologie, tension):
    if technologie == 'Industrielle':
        self_discharge = 0.001          # 0.03V/month
        min_voltage = 12.45
    elif technologie == 'Auto standard':
        self_discharge = 0.0012        # 0.035V/month
        min_voltage = 12.36
    elif technologie == 'Auto AGM':
        self_discharge = 0.001         # 0.03V/month
        min_voltage = 12.45
    elif technologie == 'Moto Wet':
        self_discharge = 0.0024       # 0.07V/month
        min_voltage = 12.30
    else:
        return 1

    days = 0
    for i in range(1000):
        tension -= self_discharge
        days += 1
        if tension <= min_voltage:
            return days


def main(request):
    return render(request, "yuasa/main.html")


def palettesSauron(request):
    palettes = PaletteSauron.objects.all()
    for f in palettes:
        max_days = nbre_jours_max_stockage_avant_sulfatation(f.type, f.voltage)
        date_limite = f.dateTransfert + timedelta(days=max_days)
        f.date_limite = date_limite
        f.save()
    palettes = PaletteSauron.objects.all().order_by('date_limite')
    return render(request, "yuasa/sauron.html", {"palettes": palettes})


def sauron_new(request):
    palette = PaletteSauronForm()
    if request.method == "POST":
        form = PaletteSauronForm(request.POST)
        if form.is_valid():
            palette = form.save()
            return redirect('sauron-detail', palette.id)
    else:
        palette = PaletteSauronForm()
    return render(request, "yuasa/sauron-new.html", {"palette": palette})


def sauron_detail(request, id):
    palette = PaletteSauron.objects.get(id=id)
    return render(request, 'yuasa/sauron-detail.html', {"palette": palette})


def sauron_delete(request, id):
    palette = PaletteSauron.objects.get(id=id)
    if request.method == 'POST':
        palette.delete()
        return redirect('sauron')
    return render(request, 'yuasa/sauron-delete.html', {"palette": palette})


def sauron_change(request, id):
    palette = PaletteSauron.objects.get(id=id)

    if request.method == "POST":
        form = PaletteSauronForm(request.POST, instance=palette)
        if form.is_valid():
            form.save()
            return redirect('sauron-detail', palette.id)
    else:
        form = PaletteSauronForm(instance=palette)

    return render(request, 'yuasa/sauron-change.html', {"form": form})









def palettesPicard(request):
    palettes = PalettePicard.objects.all()
    for f in palettes:
        max_days = nbre_jours_max_stockage_avant_sulfatation(f.type, f.voltage)
        date_limite = f.dateTransfert + timedelta(days=max_days)
        f.date_limite = date_limite
        f.save()
    palettes = PalettePicard.objects.all().order_by('date_limite')
    return render(request, "yuasa/picard.html", {"palettes": palettes})


def picard_new(request):
    palette = PalettePicardForm()
    if request.method == "POST":
        form = PalettePicardForm(request.POST)
        if form.is_valid():
            palette = form.save()
            return redirect('picard-detail', palette.id)
    else:
        palette = PalettePicardForm()
    return render(request, "yuasa/picard-new.html", {"palette": palette})


def picard_detail(request, id):
    palette = PalettePicard.objects.get(id=id)
    return render(request, 'yuasa/picard-detail.html', {"palette": palette})


def picard_delete(request, id):
    palette = PalettePicard.objects.get(id=id)
    if request.method == 'POST':
        palette.delete()
        return redirect('picard')
    return render(request, 'yuasa/picard-delete.html', {"palette": palette})


def picard_change(request, id):
    palette = PalettePicard.objects.get(id=id)

    if request.method == "POST":
        form = PalettePicardForm(request.POST, instance=palette)
        if form.is_valid():
            form.save()
            return redirect('picard-detail', palette.id)
    else:
        form = PalettePicardForm(instance=palette)

    return render(request, 'yuasa/picard-change.html', {"form": form})