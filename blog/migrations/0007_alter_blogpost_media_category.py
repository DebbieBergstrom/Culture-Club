# Generated by Django 3.2.23 on 2024-01-14 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpost_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='media_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_posts', to='blog.mediacategory'),
        ),
    ]