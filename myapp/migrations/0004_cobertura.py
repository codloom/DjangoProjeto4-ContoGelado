# Generated by Django 4.1.4 on 2024-03-18 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_sabor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cobertura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ativo', models.BooleanField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': '4 - Cobertura',
                'verbose_name_plural': '4 - Cobertura',
            },
        ),
    ]
