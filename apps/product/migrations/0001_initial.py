# Generated by Django 4.2 on 2023-05-14 19:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('icon', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='brand/', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='FeatureName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Feature Name',
                'verbose_name_plural': 'Feature Names',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Discounted Price')),
                ('is_discount', models.BooleanField(default=False, verbose_name='Is Discounted')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand', verbose_name='Brand')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('icon', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='section/', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('comment', models.TextField(verbose_name='Text')),
                ('rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Rating')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.section', verbose_name='Section'),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
                ('feature_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.featurename', verbose_name='Feature Name')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]