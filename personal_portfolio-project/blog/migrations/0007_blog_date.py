# Generated by Django 4.1.6 on 2023-02-18 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_delete_blogss'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
