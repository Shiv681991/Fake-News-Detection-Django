from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, TweetSerializer, Tweets_L1_Serializer, Tweets_L2_Serializer, Tweets_L3_Serializer, entaildata_Serializer, entail_dli_data_Serializer, fact_amd_Serializer, fact_amr_Serializer, fact_blr_Serializer, fact_chn_Serializer, fact_dli_Serializer, fact_gwt_Serializer, fact_hbd_Serializer, fact_idr_Serializer, fact_jpr_Serializer, fact_kpr_Serializer, fact_kta_Serializer, fact_lko_Serializer, fact_mbi_Serializer, fact_pne_Serializer, fact_rch_Serializer, fact_snr_Serializer, fact_vns_Serializer
from .models import Task, Tweets, Tweets_L1, Tweets_L2, Tweets_L3, entaildata, entail_dli, fact_amd, fact_amr, fact_blr, fact_chn, fact_dli, fact_gwt, fact_hbd, fact_idr, fact_jpr, fact_kpr, fact_kta, fact_lko, fact_mbi, fact_pne, fact_rch, fact_snr, fact_vns
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	# serializer = CommonSerializer(tasks, many=True)
	tasks = Tweets.objects.all()
	# print("==============> tasks: ", tasks)
	serializer = TweetSerializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def taskL1List(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	# serializer = CommonSerializer(tasks, many=True)
	tasks = Tweets_L1.objects.all()
	# print("==============> tasks: ", tasks)
	serializer = Tweets_L1_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def taskL2List(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	# serializer = CommonSerializer(tasks, many=True)
	tasks = Tweets_L2.objects.all()
	print("==============> L2 tasks: ", tasks)
	serializer = Tweets_L2_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def taskL3List(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	# serializer = CommonSerializer(tasks, many=True)
	tasks = Tweets_L3.objects.all()
	# print("==============> tasks: ", tasks)
	serializer = Tweets_L3_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_amd_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("AMD"))
	tasks = fact_amd.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_amd_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)


@api_view(['GET'])
def data_amr_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("AMR"))
	tasks = fact_amr.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_amr_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_blr_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("BLR"))
	tasks = fact_blr.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_blr_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_chn_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("CHN"))
	tasks = fact_chn.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_chn_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_dli_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	# print("=============>Inside {} API View: ".format("DLI"))
	tasks = fact_dli.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_dli_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_gwt_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("GWT"))
	tasks = fact_gwt.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_gwt_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_hbd_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("HBD"))
	tasks = fact_hbd.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_hbd_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_idr_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("IDR"))
	tasks = fact_idr.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_idr_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_jpr_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("JPR"))
	tasks = fact_jpr.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_jpr_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)


@api_view(['GET'])
def data_kpr_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("KPR"))
	tasks = fact_kpr.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_kpr_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_kta_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("KTA"))
	tasks = fact_kta.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_kta_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_lko_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("LKO"))
	tasks = fact_lko.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_lko_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_mbi_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("MBI"))
	tasks = fact_mbi.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_mbi_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_pne_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("PNE"))
	tasks = fact_pne.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_pne_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_rch_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("RCH"))
	tasks = fact_rch.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_rch_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_snr_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("SNR"))
	tasks = fact_snr.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_snr_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def data_vns_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	print("=============>Inside {} API View: ".format("VNS"))
	tasks = fact_vns.objects.all()
	#print("==============> New tasks: ", tasks)
	serializer = fact_vns_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)


@api_view(['GET'])
def entaillist(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	# serializer = CommonSerializer(tasks, many=True)
	tasks = entaildata.objects.all()
	# print("==============> tasks: ", tasks)
	serializer = entaildata_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def entail_dli_list(request):
	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
	# serializer = CommonSerializer(tasks, many=True)
	tasks = entail_dli.objects.all()
	# print("==============> tasks: ", tasks)
	serializer = entail_dli_data_Serializer(tasks, many=True)
	# print("==============> serializer.data: ", serializer.data)
	return Response(serializer.data)



@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')



