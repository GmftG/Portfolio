from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe, Product, Enrollment
from .forms import Addproducrtorecipe

def index(request):
    if request.method == "POST":

        form = Addproducrtorecipe(request.POST)
        
        if form.is_valid():
        
            recipe  = form.cleaned_data['recipe']
            product  = form.cleaned_data['product']
            weight = form.cleaned_data['weight']
            
            if product not in [q.name for q in Enrollment.objects.filter(recipe__name = recipe)]:
                new_product = Product.objects.create(name = product, timescooked = 1)
                current_recipe = Recipe.objects.get(name = recipe)
                Enrollment.objects.create(product = new_product, recipe = current_recipe, weight= weight)
            
            else:
                current_product = Product.objects.get(name = product)
                recipe = Recipe.objects.get(name = recipe)
                Enrollment.objects.update(recipe = recipe, product = current_product, weight = weight)
            
            return render(request,'books/thanks.html')
        
    form = Addproducrtorecipe()
    return render(request, "books/form.html", {"form": form})
   
    
