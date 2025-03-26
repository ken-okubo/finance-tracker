from datetime import date
from decimal import Decimal
from finance.models import Category, Expense
import uuid

# Limpando registros anteriores
Expense.objects.all().delete()
Category.objects.all().delete()

# Criando categorias
categories = [
    Category(name='Energy', is_fixed=True),
    Category(name='Water', is_fixed=True),
    Category(name='Supplies', is_fixed=False),
    Category(name='Maintenance', is_fixed=False),
    Category(name='Labor', is_fixed=True),
]
Category.objects.bulk_create(categories)

# Recapturando com IDs atualizados
categories = {cat.name: cat for cat in Category.objects.all()}

# Criando despesas
Expense.objects.bulk_create([
    Expense(
        id=uuid.uuid4(),
        description='Electricity Bill - March',
        value=Decimal('350.00'),
        category=categories['Energy'],
        supplier='Enel',
        competence_month=date(2025, 3, 1),
        payment_date=date(2025, 3, 10),
        has_invoice=True,
        invoice_downloaded=True,
        notes='Paid via Pix'
    ),
    Expense(
        id=uuid.uuid4(),
        description='Water Bill - March',
        value=Decimal('110.50'),
        category=categories['Water'],
        supplier='Sabesp',
        competence_month=date(2025, 3, 1),
        payment_date=date(2025, 3, 12),
        has_invoice=True,
        invoice_downloaded=False,
        notes=''
    ),
    Expense(
        id=uuid.uuid4(),
        description='Weekly vegetables',
        value=Decimal('480.00'),
        category=categories['Supplies'],
        supplier='Ceasa',
        competence_month=date(2025, 3, 1),
        payment_date=date(2025, 3, 15),
        has_invoice=False,
        invoice_downloaded=False,
        notes='Bought in cash'
    ),
    Expense(
        id=uuid.uuid4(),
        description='Air conditioner repair',
        value=Decimal('200.00'),
        category=categories['Maintenance'],
        supplier='ClimaTech',
        competence_month=date(2025, 3, 1),
        payment_date=date(2025, 3, 18),
        has_invoice=True,
        invoice_downloaded=True,
        notes='Invoice in .xml'
    ),
    Expense(
        id=uuid.uuid4(),
        description='Staff payment - March',
        value=Decimal('4000.00'),
        category=categories['Labor'],
        supplier='Ken',
        competence_month=date(2025, 3, 1),
        payment_date=date(2025, 3, 31),
        has_invoice=False,
        invoice_downloaded=False,
        notes='Paid in cash'
    )
])
