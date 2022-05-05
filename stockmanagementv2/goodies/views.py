from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from xhtml2pdf import pisa


from .models import Catergory, Product
from .forms import AddProduct, GeeksForm


class CategoryList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Catergory
    context_object_name = "category_data"
    template_name = 'goodies/categories.html'


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Catergory
    fields = '__all__'
    success_url = "/"
    template_name = 'goodies/form.html'


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Catergory
    fields = '__all__'
    success_url = "/"
    template_name = 'goodies/form.html'


class DeleteCategory(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Catergory
    success_url = "/"
    template_name = 'goodies/delete-categories.html'


class ProductList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Product
    context_object_name = "data"
    template_name = 'goodies/product.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'home page'
        return data


class ProductCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Product
    fields = '__all__'
    success_url = "/"
    template_name = 'goodies/form.html'


class ProductUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Product
    fields = '__all__'
    success_url = "/"
    template_name = 'goodies/form.html'


class DeleteProduct(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Product
    success_url = "/"
    template_name = 'goodies/delete-product.html'


class AddProductQuantity(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    form_class = AddProduct
    success_url = '/'
    template_name = 'goodies/form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = Product.objects.get(id=pk)
            add = int(request.POST.get('add_quantity'))
            obj.quantity += add
            obj.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


class HighStockProduct(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    queryset = Product.quantify.all()
    context_object_name = "data"
    template_name = 'goodies/product.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'High stock'
        return data


class LowStockProduct(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    queryset = Product.lessquantity.all()
    context_object_name = "data"
    template_name = 'goodies/product.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'low stock'
        return data


class SalePdfView(FormView):
    form_class = GeeksForm
    template_name = "goodies/form.html"
    success_url = 'SaleList'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            return redirect('render_pdf_view', start_date, end_date)

        return render(request, self.template_name, {'form': form})


def render_pdf_view(request, start_date, end_date):
    queryset = Product.objects.filter(date_created__range=(start_date, end_date))
    template_path = 'goodies/salepdf.html'
    context = {'data': queryset}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'sale.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
