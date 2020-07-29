#/------Django Internal Packages-----
from django.contrib import admin
# Register your models here.
#------Django Importing Models-----
from my_donation_data.models import DonationForm
#/------Django Importing Models-----
 
#Register your models here.
 
#-----Django Admin View for ----
 
#Django Admin View for Contact Form Model
class DonationFormkAdmin(admin.ModelAdmin):
    search_fields = ["pk","full_name"]
    list_filter = ["full_name"]
    list_display = [
        "pk",
        'created_at',
        "full_name",
        "email_id",
        "contact_number",
        "donation",
        "message",
    ]
    list_editable = ["full_name"]
 
#Register DonationForm in Admin view 
admin.site.register(DonationForm,DonationFormkAdmin)
