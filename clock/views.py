from django.shortcuts import render

def clock(requests):
    return render(requests,"index.html")
