# Generated by Django 2.1.1 on 2018-12-12 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('user_completed', models.BooleanField(default=False)),
                ('content', models.TextField(blank=True, default='')),
                ('order', models.IntegerField(default=0)),
                ('step_number', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_completed', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('category', models.CharField(choices=[('traffic', 'TRAFFIC'), ('conversion_rate', 'CONVERSION RATE'), ('marketing', 'MARKETING')], default='traffic', max_length=255)),
                ('done_message', models.TextField(default='', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='step',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailytask.Task'),
        ),
    ]