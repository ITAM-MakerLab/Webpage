# Generated by Django 2.0.1 on 2018-02-20 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180220_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredblogentry',
            name='featuredImage',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]