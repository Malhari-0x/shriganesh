from django.db.models import Q
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()

        search_query = self.request.GET.get('q', '').strip()
        brand = self.request.GET.get('brand', '').strip()
        category = self.request.GET.get('category', '').strip()

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query)
                | Q(description__icontains=search_query)
                | Q(category__icontains=search_query)
                | Q(brand__icontains=search_query)
            )

        if brand:
            queryset = queryset.filter(brand=brand)

        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '').strip()
        context['selected_brand'] = self.request.GET.get('brand', '').strip()
        context['selected_category'] = self.request.GET.get('category', '').strip()
        context['brand_choices'] = Product.BRAND_CHOICES
        context['category_choices'] = Product.CATEGORY_CHOICES
        return context
