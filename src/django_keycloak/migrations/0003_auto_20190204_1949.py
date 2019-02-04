# Generated by Django 2.1.5 on 2019-02-04 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_keycloak', '0002_auto_20180322_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteUserOpenIdConnectProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.TextField(null=True)),
                ('expires_before', models.DateTimeField(null=True)),
                ('refresh_token', models.TextField(null=True)),
                ('refresh_expires_before', models.DateTimeField(null=True)),
                ('sub', models.CharField(max_length=255, unique=True)),
                ('realm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='openid_profiles', to='django_keycloak.Realm')),
            ],
            options={
                'abstract': False,
                'swappable': 'KEYCLOAK_OIDC_PROFILE_MODEL',
            },
        ),
        migrations.AlterField(
            model_name='exchangedtoken',
            name='oidc_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KEYCLOAK_OIDC_PROFILE_MODEL),
        ),
    ]
