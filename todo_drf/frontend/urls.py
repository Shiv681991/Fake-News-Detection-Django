from django.urls import path
# from django.conf import settings
from . import views
import sys
app_name = 'frontend'

urlpatterns = [
	path('', views.index, name="index"),
	path('dashboard_index', views.dashboard_index, name="dashboard_index"),
	path('selectState',views.drillDownAState,name='drillDown'),
	path('about', views.about, name="aboutus"),
	# path('top_img/', settings.STATIC+'/frontend/factdemic_img_V1.png', name="top_img"),
	path('start_disp', views.start_disp, name='start_disp'),
	path('frame_1/<str:uri>', views.frame_1, name='frame_1'),
	path('frame_1_blank/<int:cnt>', views.frame_1_blank, name="frame_1_blank"),
	path('frame_2/<str:uri>', views.frame_2, name="frame_2"),
	path('frame_2_blank/<int:cnt>', views.frame_2_blank, name="frame_2_blank"),
	path('frame_3/<str:uri>', views.frame_3, name="frame_3"),
	path('frame_3_blank/<int:cnt>', views.frame_3_blank, name="frame_3_blank"),
	# path('frame_4/<str:uri>', views.frame_4, name="frame_4"),
	path('frame_4', views.frame_4, name="frame_4"),
	path('frame_4_blank/<int:cnt>', views.frame_4_blank, name="frame_4_blank"),
	path('frame_5/<str:uri>', views.frame_5, name="frame_5"),
	path('frame_5_blank/<int:cnt>', views.frame_5_blank, name="frame_5_blank"),
	path('frontend/contact_F2B_CLS/<str:in_text>', views.contact_F2B_CLS, name="contact_F2B_CLS"),
	path('frontend/contact_F2B_ENT/<str:in_text>', views.contact_F2B_ENT, name="contact_F2B_ENT"),
	# path('frontend/contact_F2B/', views.contact_F2B, name="contact_F2B")

]
