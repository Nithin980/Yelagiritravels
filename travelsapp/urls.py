from django.urls import path
from . import views

urlpatterns = [
    path('yelagiritravels/',views.Travels),
    path('about/',views.About),
    path('yelagiritravels/signup',views.Signup),
    path('yelagiritravels/signin',views.Signin),
    path('signout/',views.Signout),
    path('yelagiritravels/dashboard/',views.Dashboard),
    path('yelagiritravels/otp',views.forgotpass),
    path('yelagiritravels/triggerotp',views.Triggerotp),
    path('yelagiritravels/dashboard/book',views.Book),
    path('yelagiritravels/newpassword',views.change_password),
    path('yelagiritravels/book/success',views.success),
    path('yelagiritravels/dashboard/mybookings',views.Mybookings),
    
    
    

]