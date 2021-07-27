# Generated by Django 3.2.5 on 2021-07-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.IntegerField(choices=[(0, 'Unknown'), (1, 'processed'), (2, 'paid')], null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]