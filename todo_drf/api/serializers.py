from rest_framework import serializers
from .models import *


# class TaskSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Task
# 		fields ='__all__'
#
# class TweetSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Tweets
# 		fields = '__all__'
#
# class Tweets_L1_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Tweets_L1
# 		fields = '__all__'
#
# class Tweets_L2_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Tweets_L2
# 		fields = '__all__'
#
# class Tweets_L3_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Tweets_L3
# 		fields = '__all__'
#
# class fact_amd_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_amd
# 		fields = '__all__'
#
# class fact_amr_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_amr
# 		fields = '__all__'
#
# class fact_blr_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_blr
# 		fields = '__all__'
#
#
# class fact_chn_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_chn
# 		fields = '__all__'
#
#
# class fact_dli_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_dli
# 		fields = '__all__'
#
#
# class fact_gwt_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_gwt
# 		fields = '__all__'
#
#
# class fact_hbd_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_hbd
# 		fields = '__all__'
#
#
# class fact_idr_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_idr
# 		fields = '__all__'
#
#
# class fact_jpr_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_jpr
# 		fields = '__all__'
#
#
# class fact_kpr_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_kpr
# 		fields = '__all__'
#
# class fact_kta_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_kta
# 		fields = '__all__'
#
#
# class fact_lko_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_lko
# 		fields = '__all__'
#
#
# class fact_mbi_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_mbi
# 		fields = '__all__'
#
#
# class fact_pne_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_pne
# 		fields = '__all__'
#
#
# class fact_rch_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_rch
# 		fields = '__all__'
#
#
# class fact_snr_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_snr
# 		fields = '__all__'
#
# class fact_vns_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = fact_vns
# 		fields = '__all__'
#
#
#
#
# class entaildata_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = entaildata
# 		fields = '__all__'

# class entail_dli_data_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = entail_dli
# 		fields = '__all__'


class entail_py_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_py
		fields = '__all__'
class entail_ld_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_ld
		fields = '__all__'
class entail_wb_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_wb
		fields = '__all__'
class entail_or_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_or
		fields = '__all__'
class entail_br_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_br
		fields = '__all__'
class entail_sk_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_sk
		fields = '__all__'
class entail_ct_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_ct
		fields = '__all__'
class entail_tn_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_tn
		fields = '__all__'
class entail_mp_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_mp
		fields = '__all__'
class entail_gj_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_gj
		fields = '__all__'
class entail_ga_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_ga
		fields = '__all__'
class entail_nl_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_nl
		fields = '__all__'
class entail_mn_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_mn
		fields = '__all__'
class entail_ar_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_ar
		fields = '__all__'
class entail_mz_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_mz
		fields = '__all__'
class entail_tr_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_tr
		fields = '__all__'
class entail_dd_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_dd
		fields = '__all__'
class entail_dl_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_dl
		fields = '__all__'
class entail_hr_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_hr
		fields = '__all__'
class entail_ch_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_ch
		fields = '__all__'
class entail_hp_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_hp
		fields = '__all__'
class entail_jk_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_jk
		fields = '__all__'
class entail_kl_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_kl
		fields = '__all__'
class entail_ka_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_ka
		fields = '__all__'
class entail_dn_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_dn
		fields = '__all__'
class entail_mh_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_mh
		fields = '__all__'
class entail_as_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_as
		fields = '__all__'
class entail_ap_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_ap
		fields = '__all__'
class entail_ml_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_ml
		fields = '__all__'
class entail_pb_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_pb
		fields = '__all__'
class entail_rj_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_rj
		fields = '__all__'
class entail_up_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_up
		fields = '__all__'
class entail_ut_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_ut
		fields = '__all__'
class entail_jh_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_jh
		fields = '__all__'