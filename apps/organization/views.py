from django.shortcuts import render
from django.views import View


class OrgView(View):
    def get(self, request):
        return render(request, 'org-list.html')
