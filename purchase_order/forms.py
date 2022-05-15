from django import forms

from purchase_order.models import PurchaseOrder

CURRENCY_CHOICES = [
    ('RUB', 'RUB'),
    ('USD', 'USD'),
    ('EUR', 'EUR')
]

STATUS_CHOICES = [
    ('review', 'рассмотрение заявки'),
    ('rework', 'на доработкуе у инициатора'),
    ('reparation_documentation', 'подготовка документации'),
    ('agreement_documentation', 'согласование документации'),
    ('rework_documentation', 'доработка документации'),
    ('approval', 'рассмотрение на КпЗ'),
    ('negotiation', 'проведение переговоров'),
    ('signing_contract', 'подписание договора'),
    ('signed_contract', 'договор подписан'),
    ('canceled', 'закупка отменена')
]

FORMAT_CHOICES = [
    ('contest', 'конкурс'),
    ('auction', 'аукцион'),
    ('rfp', 'запрос предложений'),
    ('rfq', 'запрос котировок'),
    ('sq', 'закупка у единственного контрагента')
]


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['number', 'date', 'date_in_dkz', 'subject', 'format', 'amount', 'currency', 'department_initiator',
                  'employee_initiator', 'status', 'comment', 'contract_number', 'contract_date', 'contractor',
                  'contract_price', 'rate', 'contract_price_rub']

        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(
                attrs={'class': 'input-group date', 'data-date-format': 'mm/dd/yyyy', 'id': 'datetimepicker2',
                       'size': '10'}),
            'date_in_dkz': forms.DateInput(
                attrs={'class': 'form-control pull-right', 'data-date-format': 'mm/dd/yyyy', 'id': 'date_dkz',
                       'size': '10'}),
            'subject': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'format': forms.Select(attrs={'class': 'form-control custom-select'}, choices=FORMAT_CHOICES),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'currency': forms.Select(attrs={'class': 'form-control custom-select'}, choices=CURRENCY_CHOICES),
            'department_initiator': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_initiator': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control custom-select'}, choices=STATUS_CHOICES),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'contract_number': forms.TextInput(attrs={'class': 'form-control'}),
            'contract_date': forms.TextInput(attrs={'class': 'form-control'}),
            'contractor': forms.TextInput(attrs={'class': 'form-control'}),
            'contract_price': forms.TextInput(attrs={'class': 'form-control'}),
            'rate': forms.TextInput(attrs={'class': 'form-control'}),
            'contract_price_rub': forms.TextInput(attrs={'class': 'form-control'}),

        }
