# Generated by Django 5.1 on 2024-09-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoiceId', models.AutoField(primary_key=True, serialize=False)),
                ('ordId', models.IntegerField()),
                ('pdf', models.FileField(blank=True, null=True, upload_to='shop/invoice')),
            ],
        ),
    ]
