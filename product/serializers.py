from django.db.models import Avg
from rest_framework import serializers
from product.models import Product, Category, Review, Tag


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = 'id name products_count'.split()

    def get_products_count(self, obj):
        return obj.products.count()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    title = serializers.CharField(min_length=3)
    description = serializers.CharField(max_length=200)
    tag = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def validate_tag(self, attrs):
        for tag_id in attrs:
            try:
                Tag.objects.get(id=tag_id)
            except Tag.DoesNotExist as e:
                return serializers.ValidationError(str(e))
        return attrs


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'reviews', 'average_rating']

    def get_average_rating(self, obj):
        average_rating = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        return average_rating
