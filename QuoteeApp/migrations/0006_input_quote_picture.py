# Generated by Django 2.1.1 on 2018-09-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteeApp', '0005_auto_20180929_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='input_quote',
            name='picture',
            field=models.ImageField(blank=True, default='images/no-image.png', upload_to='images'),
        ),
    ]