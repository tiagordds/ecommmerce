# Generated by Django 4.2.7 on 2023-12-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='qtd_total',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
