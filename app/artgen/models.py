from django.db import models

accessibility = { 
    "high-contrast": 1, 
}

class Art(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField('date published')
    # likes = models.IntegerField()
    image_1 = models.CharField(max_length=200)
    image_2 = models.CharField(max_length=200)
    filepath = models.CharField(max_length=200)

class User(models.Model):
    firstName = models.CharField(
        "First name", max_length=255, blank=True, null=True)
    lastName = models.CharField(
        "Last name", max_length=255, blank=True, null=True)
    email = models.EmailField()
    date_created = models.DateTimeField("Created At", auto_now_add=True)
    # last_login = models.DateTimeField("Last Seen", auto_now_add=True)
    preferences = models.CharField("Accessibility", blank=True, null=True)


    def __str__(self):
        return self.firstName
