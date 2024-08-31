from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description')


class ProductPositionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = StockProduct
        fields = ('product', 'quantity', 'price')


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ('id', 'address', 'positions')

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            product_data = position.pop('product')
            product, created = Product.objects.get_or_create(**product_data)
            StockProduct.objects.create(stock=stock, product=product, **position)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        # Удаляем старые позиции
        stock.positions.all().delete()

        for position in positions:
            product_data = position.pop('product')
            product, created = Product.objects.get_or_create(**product_data)
            StockProduct.objects.create(stock=stock, product=product, **position)

        return stock
