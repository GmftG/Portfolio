# Generated by Django 5.0.1 on 2024-02-07 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_product_remove_entry_authors_remove_entry_blog_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='products',
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
