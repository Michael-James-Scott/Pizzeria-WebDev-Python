# Generated by Django 3.0.5 on 2020-04-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_auto_20200428_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='top_choice',
            field=models.CharField(choices=[('B', 'Bacon'), ('S', 'Sausage'), ('P', 'Pepperoni')], default='B', max_length=1),
            preserve_default=False,
        ),
    ]
