# Generated by Django 4.1.5 on 2023-03-29 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Kategori')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Renkler')),
                ('styletitle', models.CharField(max_length=50, null=True, verbose_name='Renk class')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug Renk')),
            ],
        ),
        migrations.CreateModel(
            name='Gander',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Cinsiyet')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Resim')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('brand', models.CharField(max_length=50, verbose_name='Marka')),
                ('price', models.FloatField(null=True, verbose_name='Ortalama Fiyat')),
                ('text', models.TextField(max_length=1000, verbose_name='Açıklama')),
                ('detail', models.TextField(max_length=800, verbose_name='Özellikler')),
                ('stars', models.FloatField(default=0, verbose_name='Puan')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug Title')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.category', verbose_name='Kategori')),
                ('colors', models.ManyToManyField(to='appMy.color', verbose_name='Renkler')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product', verbose_name='Resim')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Beden')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug Beden')),
            ],
        ),
        migrations.CreateModel(
            name='Size2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Beden')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug Beden')),
            ],
        ),
        migrations.CreateModel(
            name='SizeNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='Fiyat')),
                ('stok', models.IntegerField(default=0, verbose_name='Stok sayısı')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.color', verbose_name='Renk')),
                ('gander', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.gander', verbose_name='Cinsiyet')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.size', verbose_name='Beden Numarası')),
            ],
        ),
        migrations.CreateModel(
            name='SizeLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='Fiyat')),
                ('stok', models.IntegerField(default=0, verbose_name='Stok')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.color', verbose_name='Renk')),
                ('gander', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.gander', verbose_name='Cinsiyet')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.size2', verbose_name='Beden')),
            ],
        ),
        migrations.CreateModel(
            name='Shopbasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_all', models.FloatField(default=0, verbose_name='Toplam Fiyat')),
                ('count', models.IntegerField(default=0, verbose_name='Adet')),
                ('product_letter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.sizeletter', verbose_name='Ürün Giysi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ManyToManyField(to='appMy.productimg', verbose_name='Ürün Fotoğrafları')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
                ('sizeletter', models.ManyToManyField(blank=True, to='appMy.sizeletter', verbose_name='Kıyafet beden ve stok')),
                ('sizenumber', models.ManyToManyField(blank=True, to='appMy.sizenumber', verbose_name='Ayyakkabı beden ve stok')),
            ],
        ),
    ]
