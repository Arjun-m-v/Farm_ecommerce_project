# Generated by Django 5.0.3 on 2024-03-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='product_images')),
                ('categories', models.CharField(choices=[('kg', 'kg'), ('Number', 'Number'), ('Litre', 'Litre'), ('Packet', 'Packet')], max_length=200)),
            ],
        ),
    ]