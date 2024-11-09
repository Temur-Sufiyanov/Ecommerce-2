from django.urls import path
from .views import home, category_view, productDetail, about, contact, all_products,search_bar, customRegister, terms, customLogin, customLogout
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView, CustomPasswordResetConfirmView, profile_view, MyPasswordChangeDoneView, MyPasswordChangeView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('all-products/', all_products, name='all_products'),
    path('search/',search_bar, name='search'),
    path('category/<slug:slug>/', category_view, name='category_view'),
    path('product-detail/<slug:product_slug>/', productDetail, name='product_detail'),
    
    
    path('registration/', customRegister, name='register'),
    path('login/', customLogin, name='login'),
    path('logout/', customLogout, name='logout'),
    path('terms/', terms, name='conditions'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='app/registration/password_reset_complete.html'),name='password_reset_complete'),
    path('passwordchange/', ),
    
    path('profile/', profile_view, name='profile'),
]
