from django.db import models


class Request(models.Model):

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

    number = models.IntegerField('номер', unique=True, db_index=True)
    date = models.DateField('дата')
    date_in_dkz = models.DateField('дата поступления в ДКЗ')
    subject = models.TextField('предмет')
    format = models.CharField('форма закупки', max_length=20, db_index=True)
    amount = models.DecimalField('сумма закупки', max_digits=12, decimal_places=2)
    currency = models.CharField('валюта', max_length=3, choices=CURRENCY_CHOICES, db_index=True)
    amount_rub = models.DecimalField('сумма закупки в рублях', max_digits=12, decimal_places=2, null=True)
    department_initiator = models.CharField('инициатор', max_length=50, db_index=True)
    employee_initiator = models.CharField('работник инициатора', max_length=50, db_index=True)
    employee_dkz = models.CharField('категорийный менеджер', max_length=50, db_index=True)
    status = models.CharField('статус', max_length=24, default='review', choices=STATUS_CHOICES, db_index=True)
    comment = models.TextField('комментарий', blank=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = 'Заявки на приобретение'


