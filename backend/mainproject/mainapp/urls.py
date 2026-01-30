# from django.urls import path
# from mainapp.views import upload_with_ai_view, preprocess_view, download_view,health_check_view,advanced_analysis_view,analyze_with_mode_view

# urlpatterns = [
#     path('upload/', upload_with_ai_view, name='upload_with_ai'),
#     path('preprocess/', preprocess_view, name='preprocess'),
#     path('download/<str:filename>/', download_view, name='download_file'),
#     path('health/', health_check_view, name='health_check'),
#     path('upload/advanced/', advanced_analysis_view, name='upload_advanced'),  # Column-wise
#     path('upload/custom/', analyze_with_mode_view, name='upload_custom'),
# ]









from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_with_ai_view, name='upload_with_ai'),
    path('download/<str:filename>/', views.download_view, name='download_file'),
    path('preprocess/', views.preprocess_view, name='preprocess'),
   
    path('health/', views.health_check_view, name='health_check'),
    path('analyze-with-mode/', views.analyze_with_mode_view, name='analyze_with_mode'),
]