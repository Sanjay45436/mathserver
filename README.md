# Ex.05 Design a Website for Server Side Processing
# Date:01/10/2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
maths.html

<!DOCTYPE html>
<html>
<head>
    <center>
    <title>Lamp Filament Power Calculator</title>
</head>
<body>
   <style>
    body {
        background-color: lightblue;
    }
    </style>
    <h1>Lamp Filament Power Calculator</h1>
    <div style="background-color: white; padding: 20px; border-radius: 10px; width: 300px;">
    <form method="post">
        {% csrf_token %}
        <label>Intensity (I in Amperes):</label>
        <input type="text" name="intensity" required><br><br>

        <label>Resistance (R in Ohms):</label>
        <input type="text" name="resistance" required><br><br>

        <button type="submit">Calculate Power</button>
    </form>

    {% if power != None %}
        <h2>Power (P) = {{ power }}</h2>
    {% endif %}
    </div>
</center>
</body>
</html>

views.py

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

    urls.py

    from django.urls import path
from mathapp.views import power_calculator

urlpatterns = [
    path('', power_calculator, name='power_calculator'),
]

```
# SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-10-01 230619.png>)

# HOMEPAGE:

![alt text](<Screenshot 2025-10-01 225529.png>)

# RESULT:
The program for performing server side processing is completed successfully.
