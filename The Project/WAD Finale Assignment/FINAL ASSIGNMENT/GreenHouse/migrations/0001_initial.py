# Generated by Django 4.1 on 2022-11-02 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prodid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('prodname', models.TextField(max_length=60)),
                ('prodprice', models.IntegerField()),
                ('prodcategory', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SignIn',
            fields=[
                ('Name', models.TextField(max_length=100)),
                ('Birth_Date', models.DateField(null=True)),
                ('Email_Id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Mobile_Number', models.CharField(max_length=20)),
                ('Gender', models.TextField(max_length=10)),
                ('Address', models.CharField(max_length=100)),
                ('City', models.TextField(max_length=20, null=True)),
                ('Pin_Code', models.IntegerField()),
                ('State', models.TextField(max_length=20)),
                ('Country', models.TextField(max_length=20)),
                ('password', models.CharField(max_length=50, null=True)),
                ('retype_password', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GreenHouse.signin')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custname', models.TextField(max_length=100)),
                ('custphone', models.CharField(max_length=11)),
                ('custstate', models.TextField(max_length=20)),
                ('custaddress', models.CharField(max_length=100)),
                ('custZIP', models.IntegerField()),
                ('date', models.DateField()),
                ('custemail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GreenHouse.signin')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('prodid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GreenHouse.product')),
            ],
        ),
    ]
