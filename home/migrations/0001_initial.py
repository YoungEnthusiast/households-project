# Generated by Django 3.2.4 on 2022-05-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField(max_length=500, null=True)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Treated', 'Treated'), ('New', 'New'), ('Pending', 'Pending')], default='New', max_length=9, null=True)),
            ],
            options={
                'verbose_name': 'Contact us Message',
                'verbose_name_plural': 'Contact us Messages',
                'ordering': ('-date_submitted',),
            },
        ),
    ]
