from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# Create your models here.

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class Item(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)

class Register(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=True)
    verify_password = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=30, null=False)
    nickname = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=30, null=False)

    @classmethod
    def register_user(cls, username, password):
        # Validate username and password
        if not username or not password:
            response_data = {"response": "Username and password are required"}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        # Check if the username already exists
        if cls.objects.filter(username=username).exists():
            response_data = {"response": "Username already exists"}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        cls.objects.create(username=username, password=password)

        response_data = {"response": "User registered successfully"}
        return Response(response_data, status=status.HTTP_201_CREATED)


class sport_news(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=50, null=True)
    old_new = models.CharField(max_length=4, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class lab_analysis(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    old_new = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class free_analysis(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    old_new = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class verification_center(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class site_db(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class confirmed(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    old_new = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class report_scam(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    old_new = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class malicious_report(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    old_new = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class report_scammer(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    old_new = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class new_post(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    old_new = models.CharField(max_length=100, null=True)
    date_and_time = models.DateTimeField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class popularity(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class notification(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=100, null=True)
    time = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class advertise(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class banner(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class scam_site(models.Model): 
    id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class fraud_report(models.Model):
#     id = models.AutoField(primary_key=True)
#     number = models.CharField(max_length=100, null=True)
#     title = models.CharField(max_length=100, null=True)
#     date = models.CharField(max_length=100, null=True)
#     check = models.CharField(max_length=100, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title


