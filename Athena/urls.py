from django.urls import path
from Athena import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Dash.as_view(), name='home_page'),
    path('dash', views.Dash.as_view(), name='dash_page'),
    path('course', views.Courses.as_view(), name='course_page'),
    path('login', views.Login.as_view(), name='login_page'),
    path('course/<int:course_id>', views.CourseDetails.as_view(), name='course_details_page'),
    path('course/enrollment', views.EnrollCourse.as_view(), name='course_enrollment'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
