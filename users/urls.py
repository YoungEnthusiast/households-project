from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.create, name='account'),
    path('<ref>-invites-you-to-join-the-QwikGas-train-and-enjoy-amazing-offers', views.createFR, name='accountFR'),
    path('where-next/', views.loginTo),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/home.html'), name='logout'),
    # path('a---n-edit-profile', views.editProfileAdminFirst, name='profile_admin_first'),
    # path('staff-edit-profile', views.editProfileStaffFirst, name='profile_staff_first'),
    path('qwikcustomer-dashboard/edit-profile', views.editQwikCust, name='qwikcust_profile'),
    path('qwikvendor-dashboard/edit-profile', views.editQwikVendor, name='qwikvendor_profile'),
    path('qwikpartner-dashboard/edit-profile', views.editQwikPartner, name='qwikpartner_profile'),
    path('qwika-dashboard/edit-profile', views.editQwikAdmin, name='qwikadmin_profile'),
    path('qwika-dashboard/all-users', views.showQwikAdminPeople, name='qwikadmin_people'),
    path('qwikcustomer-dashboard/edit-profile/change-password', views.changePasswordQwikCust, name='qwikcust_change_password'),
    path('qwikvendor-dashboard/edit-profile/change-password', views.changePasswordQwikVendor, name='qwikvendor_change_password'),
    path('qwikpartner-dashboard/edit-profile/change-password', views.changePasswordQwikPartner, name='qwikpartner_change_password'),
    path('qwika-dashboard/edit-profile/change-password', views.changePasswordQwikAdmin, name='qwikadmin_change_password'),
    path('reset-password', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html'), name='reset_password'),
    path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'), name='password_reset_done'),
    path('reset-password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'), name='password_reset_confirm'),
    path('reset-password-complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'), name='password_reset_complete'),
    path('qwikcustomer-dashboard', views.showQwikCustBoard, name='qwikcust_board'),
    path('qwikcustomer_dashboard', views.showFirstLogin, name='first_login'),
    path('qwikvendor-dashboard', views.showQwikVendorBoard, name='qwikvendor_board'),
    path('qwikpartner-dashboard', views.showQwikPartnerBoard, name='qwikpartner_board'),
    path('qwika-dashboard', views.showQwikAdminBoard, name='qwikadmin_board'),
    path('qwika-dashboard/user/update/<int:id>', views.updatePerson, name='person_update'),
    path('qwika-dashboard/user/delete/<int:id>', views.deletePerson),
    path('qwika-dashboard/outlets', views.showQwikAdminOutlets, name='qwikadmin_outlets'),
    path('qwika-dashboard/outlet/update/<int:id>', views.updateOutlet, name='outlet_update'),
    path('qwika-dashboard/outlet/add-new', views.addOutlet, name='qwikadmin_outlet'),
    path('qwika-dashboard/outlet/delete/<int:id>', views.deleteOutlet),
    path('qwikcustomer-dashboard/wallet-histories', views.showQwikCustWallets, name='qwikcust_wallets'),
    # path('qwikcustomer-dashboard/wallet-histories/request-credit', views.requestCredit, name='bb'),

    path('qwika-dashboard/wallet-histories', views.showQwikAdminWallets, name='qwikadmin_wallets'),
    path('qwika-dashboard/credit-wallet', views.creditWallet, name='wallet_credit'),
    path('reg-gas-ister', views.createUser, name='qwikadmin_account'),
]
