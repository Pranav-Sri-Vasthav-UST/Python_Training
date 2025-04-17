from django.shortcuts import render
from .models import TimerHistory

# Exchange rate (1 USD = 83 INR)
USD_TO_INR = 83.0

def converter(request):
    context = {}
    if request.method == "POST":
        amount = float(request.POST.get("amount", 0))
        direction = request.POST.get("direction")

        if direction == "usd_to_inr":
            converted = round(amount * USD_TO_INR, 2)
            context["result"] = f"{amount} USD = {converted} INR"
        elif direction == "inr_to_usd":
            converted = round(amount / USD_TO_INR, 2)
            context["result"] = f"{amount} INR = {converted} USD"
    return render(request, r"D:\Python Training\Python_Training\04_17\converterproj\convertapp\templates\converter.html", context)

def timer(request):
    if request.method == 'POST':
        minutes = int(request.POST.get('minutes', 0))
        seconds = int(request.POST.get('seconds', 0))
        total_seconds = minutes * 60 + seconds

        TimerHistory.objects.create(duration=total_seconds)

        return render(request, r'D:\Python Training\Python_Training\04_17\converterproj\convertapp\templates\timer.html', {'saved': True, 'duration': total_seconds})

    return render(request, r'D:\Python Training\Python_Training\04_17\converterproj\convertapp\templates\timer.html')
