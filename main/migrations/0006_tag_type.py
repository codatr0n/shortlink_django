# Generated by Django 2.2.3 on 2019-08-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='type',
            field=models.IntegerField(choices=[(1, 'Retargeting'), (2, 'Analytics'), (3, 'Tracking'), (4, 'Tag manager')], default=1),
        ),
    ]
