# Generated by Django 3.2.7 on 2022-05-19 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='id_Brend_and_id_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Brend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.brand')),
            ],
        ),
    ]
