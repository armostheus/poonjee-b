from django.db import models

class Poonjee_Users(models.Model):
    email = models.CharField(max_length=200, primary_key = True)
    user_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=1)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    updatedAt = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return (self.email + '<>' + self.user_id)


class User_Credentials(models.Model):
    email = models.ForeignKey(Poonjee_Users, on_delete=models.CASCADE)
    password = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    updatedAt = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return (self.password)

