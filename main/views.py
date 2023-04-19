from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import *
# Create your views here.


class IndexView(TemplateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        context = {}
        categories = Category.objects.all()
        context['categories'] = categories
        context['active_category'] = None
        return render(self.request, self.template_name, context)


class CategoryView(TemplateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        category = kwargs.get('category')
        context = {}
        categories = Category.objects.all()
        context['categories'] = categories
        context['active_category'] = category
        return render(self.request, self.template_name, context)
