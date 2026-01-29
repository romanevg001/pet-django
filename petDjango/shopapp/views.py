from timeit import default_timer

from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProductForm, GroupsForm
from .models import Product,Order

class ShopIndexView(View):
    def get(self, request) -> HttpResponse:
        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Mouse', 999),
        ]
        context = {
            "time_running": default_timer(),
            "products": products
        }
        return render(request, "shopapp/shop-index.html", context=context)

# Create your views here.
# def shop_index(request: HttpRequest) -> HttpResponse:
#     products = [
#         ('Laptop', 1999),
#         ('Desktop', 2999),
#         ('Mouse', 999),
#     ]
#     context = {
#         "time_running": default_timer(),
#         "products": products
#     }
#     return render(request, "shopapp/shop-index.html", context = context)
    #print(request)
    #return HttpResponse("Hello, world. You're at the shop index.")

class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": GroupsForm(),
            "groups": Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, "shopapp/groups-list.html", context = context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = GroupsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)


# def groups_list(request: HttpRequest) -> HttpResponse:
#     context = {
#        #"groups": Group.objects.all(),
#        "groups": Group.objects.prefetch_related('permissions').all(),
#     }
#     return render(request, "shopapp/groups-list.html", context = context)

# class ProductDetailView(View):
#     def get(self, request: HttpRequest, pk: int) -> HttpResponse:
#         print('pk= ',pk)
#         # product = Product.objects.get(pk=pk)
#         product = get_object_or_404(Product, pk=pk)
#         context = {
#             "product": product,
#         }
#         return render(request, "shopapp/product-details.html", context=context)

class ProductDetailView(DetailView):
    template_name = "shopapp/product-details.html"
    model = Product
    context_object_name = "product"


class ProductListView(ListView):
    template_name = "shopapp/products-list.html"
    # model = Product
    context_object_name = "products"
    queryset = (Product.objects.filter(archived=False) )



# class ProductListView(TemplateView):
#     template_name = "shopapp/products-list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["products"] = Product.objects.all()
#         return context




# def products_list(request: HttpRequest) -> HttpResponse:
#     context = {
#        "products": Product.objects.all(),
#     }
#     return render(request, "shopapp/products-list.html", context = context)

class OrderListView(ListView):
    queryset = (Order.objects.select_related('user').prefetch_related('products') )


# def orders_list(request: HttpRequest) -> HttpResponse:
#     context = {
#        "orders": Order.objects.select_related('user').prefetch_related('products').all(),
#     }
#     return render(request, "shopapp/order_list.html", context = context)

class OrderDetailsView(DetailView):
    queryset = (Order.objects.select_related('user').prefetch_related('products') )

class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description", "price", "discount"]
    #form_class = ProductForm
    success_url = reverse_lazy("shopapp:products_list")

#
# def create_product(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             # name = form.cleaned_data['name']
#             # price = form.cleaned_data['price']
#             # Product.objects.create(**form.cleaned_data)
#             form.save()
#             url = reverse('shopapp:products_list')
#             return redirect(url)
#     else:
#         form = ProductForm()
#     context = {
#         "form": form
#     }
#     return render(request, "shopapp/product_form.html", context = context)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "description", "price", "discount"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("shopapp:product_details", kwargs={"pk": self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)