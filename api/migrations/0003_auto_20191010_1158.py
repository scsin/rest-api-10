# Generated by Django 2.2.6 on 2019-10-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191010_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='api_lambdaf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lst', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LambdaF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lst', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='lambda_f',
        ),
    ]
