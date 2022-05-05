from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Sale, Order
from goodies.models import Product


class SaleList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Sale
    context_object_name = 'saledata'
    template_name = 'sale/salelist.html'


class SaleCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Sale
    fields = ['buyer', 'buyercontact', 'clientemail', 'item', 'quantity']
    success_url = "/"
    template_name = 'goodies/form.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance.serverby=request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class SaleUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Sale
    fields = '__all__'
    success_url = "/"
    template_name = 'goodies/form.html'


class DeleteSale(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Sale
    success_url = "/"
    template_name = 'sale/delete-sale.html'


class OrderList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Order
    context_object_name = 'order_data'
    template_name = 'sale/order.html'


class OrderCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Order
    fields = '__all__'
    success_url = 'OrderList'
    template_name = 'goodies/form.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            orderquantity = int(request.POST.get('quantity'))
            d = request.POST.get('product')
            good = Product.objects.get(id=d)
            good.quantity -= orderquantity
            good.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class OrderDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Order
    success_url = '/'
    template_name = 'sale/delete_order.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        obj = Order.objects.get(id=self.object.id)
        productid = obj.product.id
        if form.is_valid():
            obj1 = Product.objects.get(id=productid)
            obj1.quantity += obj.quantity
            obj1.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
