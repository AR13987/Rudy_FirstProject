from django.urls import path
from .views import index, BBPasswordChangeView, profile_bb_add, profile_bb_change, profile_bb_delete
from .views import other_page
from .views import BBLoginView
from .views import profile
from .views import BBLogoutView
from .views import ChangeUserInfoView
from .views import RegisterDoneView, RegisterUserView
from .views import user_activate
from .views import DeleteUserView
from .views import by_rubric, detail

app_name = 'main'
urlpatterns = [
    path('<str:page>/', other_page, name='other'),
    path('rubric/<int:pk>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('account/login/', BBLoginView.as_view(),
         name='login'),
    path('account/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(),
         name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('rubric/<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
    path('accounts/profile/change/<int:pk>/', profile_bb_change, name='profile_bb_change'),
    path('accounts/profile/delete/<int:pk>/', profile_bb_delete, name='profile_bb_delete'),

]
