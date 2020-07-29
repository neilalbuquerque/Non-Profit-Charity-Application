from django.db import models

# Create your models here.
#Donation Form Model
class DonationForm(models.Model):
    #Total Fields : 5
    #------Donation form Table Fields------

    #This field store Full Name 
    full_name = models.CharField(max_length=300,blank=True)
    #This field store Email ID
    email_id = models.CharField(max_length=300,blank=True)
    #This field store Contact Number 
    contact_number = models.CharField(max_length=300,blank=True)
    #This field store Donation Amount 
    donation = models.CharField(max_length=300,blank=True)
    #This field store Message 
    message = models.TextField(max_length=3000,blank=True)
    #This field store Date & Time at which form is submitted
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) #Return Primary Key

    class Meta:
        verbose_name_plural = "Donation Form Data"
        verbose_name = "Donation Form"
