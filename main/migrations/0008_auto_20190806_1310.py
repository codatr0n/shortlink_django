# Generated by Django 2.2.3 on 2019-08-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190806_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='main.Tag'),
        ),
    ]
