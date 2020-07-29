from django.urls import include, path
from my_donation_data import views

app_name = 'my_donation_data'
 
urlpatterns = [
	path('',views.home,name='home'),
	path('ourwork',views.ourwork,name='ourwork'),
	path('donateus',views.donateus,name='donateus'),
	path('donation_form_submit',views.donation_form_submit,name='donation_form_submit'),
]
