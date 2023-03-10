# Generated by Django 4.1.3 on 2023-02-14 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishna', '0006_auto_20200808_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='hotels',
            name='country',
            field=models.CharField(default='Canada', max_length=50),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='name',
            field=models.CharField(default='Last Booking', max_length=30),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
