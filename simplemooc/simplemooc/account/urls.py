from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from account.views import register, dashboard, edit

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^entrar/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^cadastre-se/$', register, name='register'),
    url(r'^editar/$', edit, name='editar'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout')

]