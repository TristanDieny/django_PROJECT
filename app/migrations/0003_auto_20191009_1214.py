# Generated by Django 2.2.1 on 2019-10-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191009_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pval',
            name='PVALUE',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=7, max_length=100, null=True),
        ),
    ]
