from rest_framework import serializers
from .models import Task, Tweets, Tweets_L1, Tweets_L2, Tweets_L3, entaildata, entail_dli, fact_amd, fact_amr, fact_blr, fact_chn, fact_dli, fact_gwt, fact_hbd, fact_idr, fact_jpr, fact_kpr, fact_kta, fact_lko, fact_mbi, fact_pne, fact_rch, fact_snr, fact_vns

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

class TweetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tweets
		fields = '__all__'

class Tweets_L1_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Tweets_L1
		fields = '__all__'

class Tweets_L2_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Tweets_L2
		fields = '__all__'

class Tweets_L3_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Tweets_L3
		fields = '__all__'

class fact_amd_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_amd
		fields = '__all__'

class fact_amr_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_amr
		fields = '__all__'

class fact_blr_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_blr
		fields = '__all__'


class fact_chn_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_chn
		fields = '__all__'


class fact_dli_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_dli
		fields = '__all__'


class fact_gwt_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_gwt
		fields = '__all__'


class fact_hbd_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_hbd
		fields = '__all__'


class fact_idr_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_idr
		fields = '__all__'


class fact_jpr_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_jpr
		fields = '__all__'


class fact_kpr_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_kpr
		fields = '__all__'

class fact_kta_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_kta
		fields = '__all__'


class fact_lko_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_lko
		fields = '__all__'


class fact_mbi_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_mbi
		fields = '__all__'


class fact_pne_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_pne
		fields = '__all__'


class fact_rch_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_rch
		fields = '__all__'


class fact_snr_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_snr
		fields = '__all__'

class fact_vns_Serializer(serializers.ModelSerializer):
	class Meta:
		model = fact_vns
		fields = '__all__'




class entaildata_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entaildata
		fields = '__all__'

class entail_dli_data_Serializer(serializers.ModelSerializer):
	class Meta:
		model = entail_dli
		fields = '__all__'