
# Create your views here.
from django.views import View
from django.shortcuts import render

class Navbar(View):
    def get(self, request):
        return render(request, 'navbar.html')
