from django.shortcuts import render,get_object_or_404,redirect
from .models import Hood,Business,User
from django.views.generic import ListView,DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    context = {
        'hoods':Hood.objects.all()
    }
    return render(request,'index.html',context)

class HomePageView(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = Hood
    context_object_name ='hoods'
    
    # def get_queryset(self):
    #     contacts = super().get_queryset()
    #     return contacts.filter(manager = self.request.user)
        
    
class HoodDetailView(LoginRequiredMixin,DetailView):
    template_name = 'detail.html'
    model = Hood
    context_object_name = 'hood'
    
@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Hood.objects.filter(
            Q(name__icontains=search_term)|
            Q(location__icontains=search_term)|
            Q(count__icontains=search_term)
            )
        context = {
             'search_term': search_term,
             'hoods':search_results
    }
        return render(request,'search.html',context)
    else:
        return redirect('home')
def business(request):
    context = {
        'businesses':Business.objects.all()
    }
    return render(request,'business.html',context)
   
class BusinessDetailView(LoginRequiredMixin,DetailView):
    template_name = 'business_detail.html'
    model = Business
    context_object_name = 'business' 
 
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url =reverse_lazy( 'home')