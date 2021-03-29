from django.urls import path
from . import views
app_name = 'api'
urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-L1-list/', views.taskL1List, name="task-L1-list"),
	path('task-L2-list/', views.taskL2List, name="task-L2-list"),
	path('entaillist/', views.entaillist, name="entaillist"),
	path('entail_dli_list/', views.entail_dli_list, name="entail_dli_list"),
	path('task-L3-list/', views.taskL3List, name="task-L3-list"),
	path('data_amd_list/', views.data_amd_list, name="data_amd_list"),
	path('data_amr_list/', views.data_amr_list, name="data_amr_list"),
	path('data_blr_list/', views.data_blr_list, name="data_blr_list"),
	path('data_chn_list/', views.data_chn_list, name="data_chn_list"),
	path('data_dli_list/', views.data_dli_list, name="data_dli_list"),
	path('data_gwt_list/', views.data_gwt_list, name="data_gwt_list"),
	path('data_hbd_list/', views.data_hbd_list, name="data_hbd_list"),
	path('data_idr_list/', views.data_idr_list, name="data_idr_list"),
	path('data_jpr_list/', views.data_jpr_list, name="data_jpr_list"),
	path('data_kpr_list/', views.data_kpr_list, name="data_kpr_list"),
	path('data_kta_list/', views.data_kta_list, name="data_kta_list"),
	path('data_lko_list/', views.data_lko_list, name="data_lko_list"),
	path('data_mbi_list/', views.data_mbi_list, name="data_mbi_list"),
	path('data_pne_list/', views.data_pne_list, name="data_pne_list"),
	path('data_rch_list/', views.data_rch_list, name="data_rch_list"),
	path('data_snr_list/', views.data_snr_list, name="data_snr_list"),
	path('data_vns_list/', views.data_vns_list, name="data_vns_list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
