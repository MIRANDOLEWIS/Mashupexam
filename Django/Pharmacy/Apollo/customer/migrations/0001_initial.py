# Generated by Django 2.2.28 on 2023-02-12 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='diseases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your diseases', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medic_name', models.CharField(help_text='Enter your medicine', max_length=200)),
                ('medic_type', models.CharField(choices=[('t', 'tablet'), ('s', 'syrup')], default='t', help_text='Select your medicine type', max_length=1)),
                ('diseases_name', models.ManyToManyField(help_text='Select your diseases', to='customer.diseases')),
            ],
        ),
        migrations.CreateModel(
            name='medic_copy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='medicine main id', primary_key=True, serialize=False)),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('medname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.medicine')),
            ],
        ),
    ]
