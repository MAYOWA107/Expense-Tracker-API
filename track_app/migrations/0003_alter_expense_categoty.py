# Generated by Django 5.0.6 on 2024-08-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track_app', '0002_alter_expense_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='categoty',
            field=models.CharField(choices=[('GROCERIES', 'groceries'), ('LEISURE', 'leisure'), ('ELECTRONICS', 'electronics'), ('UTILITIES', 'utilities'), ('CLOTHING', 'clothing'), ('HEALTH', 'health'), ('OTHERS', 'others')], default=None, max_length=50),
        ),
    ]
