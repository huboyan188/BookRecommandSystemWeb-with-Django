# Generated by Django 2.0.5 on 2018-05-16 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookRecommand', '0007_auto_20180516_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookIndex',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='douBanId',
            field=models.CharField(default='0', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='systemNumber',
            field=models.CharField(default='0', max_length=50, null=True),
        ),
    ]