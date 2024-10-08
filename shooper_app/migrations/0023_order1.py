# Generated by Django 4.2.10 on 2024-03-06 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0022_rename_address_address_address0'),
    ]

    operations = [
        migrations.CreateModel(
            name='order1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('img', models.ImageField(upload_to='image')),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shooper_app.user')),
            ],
        ),
    ]
