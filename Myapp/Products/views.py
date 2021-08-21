
from django.db.models.query import QuerySet
from .models import Product
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import DetailView,UpdateView,ListView,CreateView,DeleteView





class producList(ListView):
    model=Product
    template_name='products/l.html'
       


        #CRUD
class ProductCreat(CreateView):
    model=Product
    fields='__all__'
    template_name='products/c.html'
    success_url='/p/'
    




class ProductDetail(DetailView):
    model=Product
    template_name='products/d.html'
    success_url='/p/'   


class ProductUpdate(UpdateView):
    model=Product
    fields='__all__'
    template_name='products/u.html'
    success_url='/p/'     

class ProducttDel(DeleteView):
    model=Product
    template_name='products/dele.html'
    success_url='/p/'    

