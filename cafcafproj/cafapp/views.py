from django.shortcuts import render
from django.views import View


class Dashboard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cafapp/dashboard.html')
