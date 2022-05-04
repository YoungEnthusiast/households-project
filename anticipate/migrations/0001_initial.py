# Generated by Django 3.2.4 on 2022-05-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AntiOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_Id', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=12, null=True)),
                ('outlet_static', models.CharField(blank=True, max_length=30, null=True)),
                ('who6_2', models.CharField(blank=True, max_length=9, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('payment_type1', models.CharField(blank=True, choices=[('Pay Now', 'Pay Now')], max_length=7, null=True, verbose_name='Payment Type')),
                ('payment_type2', models.CharField(blank=True, choices=[('Paylater', 'Paylater')], max_length=8, null=True, verbose_name='')),
                ('payment_type3', models.CharField(blank=True, choices=[('Pay Small Small', 'Pay Small Small')], max_length=15, null=True, verbose_name='')),
                ('payment_date_later', models.DateField(blank=True, null=True, verbose_name='Committed Payment Date')),
                ('payment_split', models.CharField(blank=True, max_length=40, null=True, verbose_name='Payment Split in Amount')),
                ('payment_choice', models.CharField(choices=[('Bank Transfer', 'Bank Transfer'), ('PoS', 'PoS'), ('Cash', 'Cash')], max_length=13, null=True, verbose_name='Payment Choice')),
                ('payment_ref', models.CharField(blank=True, max_length=40, null=True, verbose_name='Payment Reference')),
                ('payment1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='1st Payment')),
                ('payment1_date', models.DateField(blank=True, null=True, verbose_name='1st Payment Date')),
                ('payment2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='2nd Payment')),
                ('payment2_date', models.DateField(blank=True, null=True, verbose_name='2nd Payment Date')),
                ('payment3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='3rd Payment')),
                ('payment3_date', models.DateField(blank=True, null=True, verbose_name='3rd Payment Date')),
                ('payment_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('stage', models.CharField(blank=True, max_length=3, null=True)),
                ('transaction', models.CharField(blank=True, choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=12, null=True, verbose_name='Transaction Status')),
                ('static_price', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('static_total_cost', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=13, null=True)),
                ('static_price2', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('static_total_cost2', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]