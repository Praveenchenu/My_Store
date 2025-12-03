from rest_framework import serializers
from app.models import Item,Category

class CategotySerialization(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerialization(serializers.ModelSerializer):
    category = CategotySerialization(read_only=True)
    class Meta:
        model = Item
        fields = '__all__'

    def validate_name(self,value):
        if Item.objects.filter(product__iexact=value).exists():
            raise serializers.ValidationError("Product with this name is already Exists.")
        return value
    
    def validate_price(self,value):
        if value <= 0 :
            raise serializers.ValidationError("Price must br Greater than 0.")
        return value
    


class CategoryHyperSerialization(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:item-detail',
        source='item_set'
    )

    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'items']
        extra_kwargs = {
            'url': {'view_name': 'api:category-detail'},
        }


class ItemHyperSerialization(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['url','id','product','price','image','is_available','description','category']
        extra_kwargs = {
            'url': {'view_name': 'api:item-detail'},
            'category': {'view_name': 'api:category-detail'}
        }