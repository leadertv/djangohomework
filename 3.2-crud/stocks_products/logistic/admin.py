from django.contrib import admin
from logistic.models import Product, Stock, StockProduct

# Регистрация моделей
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(StockProduct)