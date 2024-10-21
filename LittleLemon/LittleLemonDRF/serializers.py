from rest_framework import serializers
from .models import MenuItem
import bleach
class MenuItemSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        return bleach.clean(value)
    class Meta:
        model = MenuItem
        fields = [
            'id', 'title', 'price', 'inventory'
        ]
        extra_kwargs = {
            'price':{'min_value': 2},
            'inventory':{'min_value': 0}
        }