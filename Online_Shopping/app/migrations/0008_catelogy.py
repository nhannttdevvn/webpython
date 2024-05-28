# Generated by Django 3.2 on 2024-05-23 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catelogy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sub', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('sub_catelory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_catelories', to='app.catelogy')),
            ],
        ),
    ]