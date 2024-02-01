# Generated by Django 5.0.1 on 2024-02-01 15:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_stages_password", "0008_replace_inbuilt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passwordstage",
            name="backends",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.TextField(
                    choices=[
                        ("authentik.core.auth.InbuiltBackend", "User database + standard password"),
                        ("authentik.core.auth.TokenBackend", "User database + app passwords"),
                        (
                            "authentik.sources.ldap.auth.LDAPBackend",
                            "User database + LDAP password",
                        ),
                        (
                            "authentik.sources.kerberos.auth.KerberosBackend",
                            "User database + Kerberos password",
                        ),
                    ]
                ),
                help_text="Selection of backends to test the password against.",
                size=None,
            ),
        ),
    ]
