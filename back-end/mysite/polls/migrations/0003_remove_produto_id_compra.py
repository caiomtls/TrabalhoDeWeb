# Generated by Django 4.2.1 on 2023-05-09 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_cliente_compra_fornecedor_produto_venda_vendedor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='id_compra',
        ),
    ]
