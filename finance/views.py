from datetime import datetime

from django.db.models import Count, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('-payment_date')
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'supplier', 'competence_month', 'has_invoice']

    @action(detail=False, methods=['get'], url_path='summary')
    def summary(self, request):
        month_str = request.query_params.get('month')
        if not month_str:
            return Response(
                {"error": "You must provide the 'month' parameter in the format YYYY-MM."},
                status=400
            )

        try:
            month = datetime.strptime(month_str, "%Y-%m")
        except ValueError:
            return Response(
                {"error": "Invalid format. Use YYYY-MM, e.g. 2025-03."},
                status=400
            )

        expenses = Expense.objects.filter(competence_month=month.replace(day=1))

        total = expenses.aggregate(total=Sum('value'))['total'] or 0
        total_by_category = expenses.values('category__name').annotate(
            total=Sum('value'),
            count=Count('id')
        )

        total_with_invoice = expenses.filter(has_invoice=True).aggregate(total=Sum('value'))['total'] or 0
        total_without_invoice = expenses.filter(has_invoice=False).aggregate(total=Sum('value'))['total'] or 0

        return Response({
            "month": month.strftime("%Y-%m"),
            "total": total,
            "total_with_invoice": total_with_invoice,
            "total_without_invoice": total_without_invoice,
            "expenses_count": expenses.count(),
            "by_category": list(total_by_category),
        })
