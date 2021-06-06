# Generated by Django 3.0.8 on 2020-11-07 06:21

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
            name="contact",
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank= True,max_length=254)),
                ('relation', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Husband', 'Husband'), ('Friend', 'Friend'), ('Relative', 'Relative'), ('Other', 'Other')], default='Other', max_length=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact', to=settings.AUTH_USER_MODEL)),
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                (
                    "relation",
                    models.CharField(
                        choices=[
                            ("Father", "Father"),
                            ("Mother", "Mother"),
                            ("Brother", "Brother"),
                            ("Sister", "Sister"),
                            ("Husband", "Husband"),
                            ("Friend", "Friend"),
                            ("Relative", "Relative"),
                            ("Other", "Other"),
                        ],
                        default="Other",
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
