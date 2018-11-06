from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("registro/crear_perro/",views.crear_perro,name = "crear_perro"),
    path("registro/crear/",views.crear,name = "crear"),
    path("index/",views.index, name="index"),
    path("registro_persona/",views.persona_form, name="registro_persona"),
    path("registro_perro/",views.perro_form, name="registro_perro"),
    path("login/",views.login, name="login"),
    path("login/iniciar/",views.login_iniciar,name="iniciar"),
    path("cerrarsesion/",views.cerrar_session,name="cerrar_session"),
    path("listado/",views.listado,name="listado"),
    path("contrasenia/",views.contrasenia,name="contrasenia"),
    path("contrasenia/",views.cambio_contrasenia,name="cambio"),
    path("password/recovery/",
        auth_views.PasswordResetView.as_view(
            template_name='password_reset_form.htm',
            html_email_template_name='password_reset_email.htm',
        ),
        name='passwordreset',
    ),
    url(
        r'^password/recovery/(?P<uidb64>[0-9A-Za-z-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            success_url='/login/',
            post_reset_login=True,
            template_name='password_reset_confirm.htm',
            post_reset_login_backend=(
                'django.contrib.auth.backends.AllowAllUsersModelBackend'
            ),
        ),
        name='password_reset_confirm',
    ),
    url(
        r'^password/recovery/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.htm',
        ),
        name='password_reset_done',
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
