from django.contrib.auth.models import User
from django.db import models


class Contractor(models.Model):
    CATEGORY_CHOICES = [
        ('it_equipment', 'ИТ оборудование'),
        ('software', 'программное обеспечение'),
        ('link', 'связь'),
        ('processing', 'процессинг и инкассация'),
        ('marketing', 'маркетинг'),
        ('hr', 'услуги для персонала'),
        ('security', 'безопасность')
    ]
    name = models.CharField('наименование', max_length=50, db_index=True)
    manager = models.CharField('контактное лицо', max_length=50, null=True, blank=True)
    contact_phone = models.CharField('контактный телефон', max_length=50, null=True, blank=True)
    email = models.CharField('email', max_length=50, null=True, blank=True)
    category = models.CharField('категория', max_length=15, choices=CATEGORY_CHOICES)
    comment = models.TextField('комментарий', blank=True, null=True)


class PurchaseOrder(models.Model):
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

    number = models.IntegerField('номер', unique=True, db_index=True)
    date = models.DateField('дата')
    date_in_dkz = models.DateField('дата поступления в ДКЗ')
    subject = models.TextField('предмет')
    format = models.CharField('форма закупки', max_length=12, choices=FORMAT_CHOICES, db_index=True)
    amount = models.DecimalField('сумма закупки', max_digits=12, decimal_places=2)
    currency = models.CharField('валюта', max_length=3, choices=CURRENCY_CHOICES, db_index=True)
    department_initiator = models.CharField('инициатор', max_length=50, db_index=True)
    employee_initiator = models.CharField('работник инициатора', max_length=50, db_index=True)
    employee_dkz = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='purchase_orders',
                                     verbose_name='категорийный менеджер', null=True, blank=True)
    status = models.CharField('статус', max_length=24, default='review', choices=STATUS_CHOICES, db_index=True)
    comment = models.TextField('комментарий', blank=True, null=True)
    contract_number = models.CharField('номер договора', max_length=20, blank=True, null=True, db_index=True)
    contract_date = models.DateField('дата', blank=True, null=True, db_index=True)
    contractor = models.ForeignKey(Contractor, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='contracts', verbose_name='контрагент')
    contract_price = models.DecimalField('цена договора', max_digits=12, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField('курс рубля', max_digits=6, decimal_places=2, blank=True, null=True)
    contract_price_rub = models.DecimalField('цена договора в рублях', max_digits=12, decimal_places=2, blank=True,
                                             null=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = 'Заявки на приобретение'
