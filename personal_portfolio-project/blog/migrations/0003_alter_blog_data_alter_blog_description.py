# Generated by Django 4.1.6 on 2023-02-17 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
