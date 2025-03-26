from rest_framework import serializers

from .models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    
    class Meta:
        model = Expense
        fields = [
            'id', 'description', 'value', 'category', 'category_id', 'supplier',
            'competence_month', 'payment_date', 'has_invoice', 'invoice_downloaded',
            'notes', 'created_at', 'updated_at'
        ]