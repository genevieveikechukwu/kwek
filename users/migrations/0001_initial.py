# Generated by Django 3.1.7 on 2021-07-19 13:22

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('full_name', models.CharField(max_length=255, verbose_name='full_name')),
                ('is_verified', models.BooleanField(default=False, verbose_name='is_verified')),
                ('is_seller', models.BooleanField(default=False, verbose_name='is_seller')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255, null=True)),
                ('lastname', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('shop_name', models.CharField(max_length=255, null=True)),
                ('shop_url', models.CharField(max_length=255, null=True)),
                ('shop_address', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('lga', models.CharField(max_length=255, null=True)),
                ('landmark', models.CharField(max_length=255, null=True)),
                ('how_you_heard_about_us', models.CharField(max_length=255, null=True)),
                ('accepted_policy', models.BooleanField()),
                ('store_banner_url', models.CharField(blank=True, max_length=255, null=True)),
                ('store_description', models.CharField(blank=True, max_length=255, null=True)),
                ('prefered_id', models.CharField(blank=True, max_length=255, null=True)),
                ('prefered_id_url', models.CharField(blank=True, max_length=255, null=True)),
                ('bvn', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account_name', models.CharField(blank=True, max_length=255, null=True)),
                ('seller_is_verified', models.BooleanField(default=False, verbose_name='seller_is_verified')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
