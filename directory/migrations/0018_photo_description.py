# Generated by Django 3.0.5 on 2020-07-03 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0017_auto_20200703_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]