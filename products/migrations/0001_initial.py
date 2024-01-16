# Generated by Django 5.0.1 on 2024-01-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(blank=True, choices=[('HEAT SHIELD', 'HEAT SHIELD'), ('BRACKET', 'BRACKET'), ('EXHAUST VALVE', 'EXHAUST VALVE')], max_length=20)),
                ('price', models.FloatField(help_text='euros each')),
                ('image', models.ImageField(default='default.png', upload_to='products')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
