from django.shortcuts import render

def power_calculator(request):
    power = None
    if request.method == 'POST':
        intensity = request.POST.get('intensity')
        resistance = request.POST.get('resistance')
        if intensity and resistance:
            try:
                I = float(intensity)
                R = float(resistance)
                power = I**2 * R
            except ValueError:
                power = "Invalid input. Please enter numeric values."
    return render(request, 'mathapp/maths.html', {'power': power})