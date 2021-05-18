from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
# TaskSerializer, TweetSerializer, Tweets_L1_Serializer, Tweets_L2_Serializer, Tweets_L3_Serializer, entaildata_Serializer, entail_dli_data_Serializer, fact_amd_Serializer, fact_amr_Serializer, fact_blr_Serializer, fact_chn_Serializer, fact_dli_Serializer, fact_gwt_Serializer, fact_hbd_Serializer, fact_idr_Serializer, fact_jpr_Serializer, fact_kpr_Serializer, fact_kta_Serializer, fact_lko_Serializer, fact_mbi_Serializer, fact_pne_Serializer, fact_rch_Serializer, fact_snr_Serializer, fact_vns_Serializer
from .models import *
# Task, Tweets, Tweets_L1, Tweets_L2, Tweets_L3, entaildata, entail_dli, fact_amd, fact_amr, fact_blr, fact_chn, fact_dli, fact_gwt, fact_hbd, fact_idr, fact_jpr, fact_kpr, fact_kta, fact_lko, fact_mbi, fact_pne, fact_rch, fact_snr, fact_vns
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

# @api_view(['GET'])
# def taskList(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	# serializer = CommonSerializer(tasks, many=True)
# 	tasks = Tweets.objects.all()
# 	# print("==============> tasks: ", tasks)
# 	serializer = TweetSerializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def taskL1List(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	# serializer = CommonSerializer(tasks, many=True)
# 	tasks = Tweets_L1.objects.all()
# 	# print("==============> tasks: ", tasks)
# 	serializer = Tweets_L1_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def taskL2List(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	# serializer = CommonSerializer(tasks, many=True)
# 	tasks = Tweets_L2.objects.all()
# 	print("==============> L2 tasks: ", tasks)
# 	serializer = Tweets_L2_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def taskL3List(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	# serializer = CommonSerializer(tasks, many=True)
# 	tasks = Tweets_L3.objects.all()
# 	# print("==============> tasks: ", tasks)
# 	serializer = Tweets_L3_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_amd_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("AMD"))
# 	tasks = fact_amd.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_amd_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
#
# @api_view(['GET'])
# def data_amr_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("AMR"))
# 	tasks = fact_amr.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_amr_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_blr_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("BLR"))
# 	tasks = fact_blr.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_blr_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_chn_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("CHN"))
# 	tasks = fact_chn.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_chn_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_dli_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	# print("=============>Inside {} API View: ".format("DLI"))
# 	tasks = fact_dli.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_dli_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_gwt_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("GWT"))
# 	tasks = fact_gwt.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_gwt_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_hbd_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("HBD"))
# 	tasks = fact_hbd.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_hbd_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_idr_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("IDR"))
# 	tasks = fact_idr.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_idr_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_jpr_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("JPR"))
# 	tasks = fact_jpr.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_jpr_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
#
# @api_view(['GET'])
# def data_kpr_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("KPR"))
# 	tasks = fact_kpr.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_kpr_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_kta_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("KTA"))
# 	tasks = fact_kta.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_kta_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_lko_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("LKO"))
# 	tasks = fact_lko.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_lko_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_mbi_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("MBI"))
# 	tasks = fact_mbi.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_mbi_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_pne_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("PNE"))
# 	tasks = fact_pne.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_pne_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_rch_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("RCH"))
# 	tasks = fact_rch.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_rch_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_snr_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("SNR"))
# 	tasks = fact_snr.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_snr_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def data_vns_list(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	print("=============>Inside {} API View: ".format("VNS"))
# 	tasks = fact_vns.objects.all()
# 	#print("==============> New tasks: ", tasks)
# 	serializer = fact_vns_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
#
# @api_view(['GET'])
# def entaillist(request):
# 	# tasks = open('CAA_23012020123524_token.csv', 'r').read().split('\n')
# 	# serializer = CommonSerializer(tasks, many=True)
# 	tasks = entaildata.objects.all()
# 	# print("==============> tasks: ", tasks)
# 	serializer = entaildata_Serializer(tasks, many=True)
# 	# print("==============> serializer.data: ", serializer.data)
# 	return Response(serializer.data)
#
#
# @api_view(['GET'])
# def taskDetail(request, pk):
# 	tasks = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(tasks, many=False)
# 	return Response(serializer.data)
#
#
# @api_view(['POST'])
# def taskCreate(request):
# 	serializer = TaskSerializer(data=request.data)
#
# 	if serializer.is_valid():
# 		serializer.save()
#
# 	return Response(serializer.data)
#
# @api_view(['POST'])
# def taskUpdate(request, pk):
# 	task = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(instance=task, data=request.data)
#
# 	if serializer.is_valid():
# 		serializer.save()
#
# 	return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def taskDelete(request, pk):
# 	task = Task.objects.get(id=pk)
# 	task.delete()
#
# 	return Response('Item succsesfully delete!')

# --------AJAX APIs for 34 state data----------------
# ---------------------------------------------------


# Puducherry
@api_view(['GET'])
def entail_py_list_res(request, in_tid):
	out_obj = entail_py.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls_cls}
	return Response(context)
@api_view(['GET'])
def entail_py_list(request):
	tasks = entail_py.objects.all()
	serializer = entail_py_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Lakshadweep
@api_view(['GET'])
def entail_ld_list_res(request, in_tid):
	out_obj = entail_ld.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_ld_list(request):
	tasks = entail_ld.objects.all()
	serializer = entail_ld_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# West_Bengal
@api_view(['GET'])
def entail_wb_list_res(request, in_tid):
	out_obj = entail_wb.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_wb_list(request):
	tasks = entail_wb.objects.all()
	serializer = entail_wb_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Orissa
@api_view(['GET'])
def entail_or_list_res(request, in_tid):
	out_obj = entail_or.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_or_list(request):
	tasks = entail_or.objects.all()
	serializer = entail_or_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Bihar
@api_view(['GET'])
def entail_br_list_res(request, in_tid):
	out_obj = entail_br.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_br_list(request):
	tasks = entail_br.objects.all()
	serializer = entail_br_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Sikkim
@api_view(['GET'])
def entail_sk_list_res(request, in_tid):
	out_obj = entail_sk.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_sk_list(request):
	tasks = entail_sk.objects.all()
	serializer = entail_sk_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Chattisgarh
@api_view(['GET'])
def entail_ct_list_res(request, in_tid):
	out_obj = entail_ct.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_ct_list(request):
	tasks = entail_ct.objects.all()
	serializer = entail_ct_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# TN
@api_view(['GET'])
def entail_tn_list_res(request, in_tid):
	out_obj = entail_tn.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_tn_list(request):
	tasks = entail_tn.objects.all()
	serializer = entail_tn_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# MP
@api_view(['GET'])
def entail_mp_list_res(request, in_tid):
	out_obj = entail_mp.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_mp_list(request):
	tasks = entail_mp.objects.all()
	serializer = entail_mp_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Gujrat
@api_view(['GET'])
def entail_gj_list_res(request, in_tid):
	out_obj = entail_gj.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_gj_list(request):
	tasks = entail_gj.objects.all()
	serializer = entail_gj_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Goa
@api_view(['GET'])
def entail_ga_list_res(request, in_tid):
	out_obj = entail_ga.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_ga_list(request):
	tasks = entail_ga.objects.all()
	serializer = entail_ga_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Nagaland
@api_view(['GET'])
def entail_nl_list_res(request, in_tid):
	out_obj = entail_nl.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_nl_list(request):
	tasks = entail_nl.objects.all()
	serializer = entail_nl_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Manipur
@api_view(['GET'])
def entail_mn_list_res(request, in_tid):
	out_obj = entail_mn.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_mn_list(request):
	tasks = entail_mn.objects.all()
	serializer = entail_mn_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Arunachal_Pradesh
@api_view(['GET'])
def entail_ar_list_res(request, in_tid):
	out_obj = entail_ar.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_ar_list(request):
	tasks = entail_ar.objects.all()
	serializer = entail_ar_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Mizoram
@api_view(['GET'])
def entail_mz_list_res(request, in_tid):
	out_obj = entail_mz.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_mz_list(request):
	tasks = entail_mz.objects.all()
	serializer = entail_mz_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Tripura
@api_view(['GET'])
def entail_tr_list_res(request, in_tid):
	out_obj = entail_tr.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_tr_list(request):
	tasks = entail_tr.objects.all()
	serializer = entail_tr_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Daman_and_Diu
@api_view(['GET'])
def entail_dd_list_res(request, in_tid):
	out_obj = entail_dd.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_dd_list(request):
	tasks = entail_dd.objects.all()
	serializer = entail_dd_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Delhi
@api_view(['GET'])
def entail_dl_list_res(request, in_tid):
	print("====================> inside the delhi module Success!")
	print(type(in_tid))
	print(in_tid)
	print(type(int(in_tid)))
	print(int(in_tid))

	out_obj = entail_dl.objects.get(id__exact=int(in_tid))
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_dl_list(request):
	tasks = entail_dl.objects.all()
	serializer = entail_dl_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Haryana
@api_view(['GET'])
def entail_hr_list_res(request, in_tid):
	out_obj = entail_hr.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_hr_list(request):
	tasks = entail_hr.objects.all()
	serializer = entail_hr_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Chandigarh
@api_view(['GET'])
def entail_ch_list_res(request, in_tid):
	out_obj = entail_ch.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_ch_list(request):
	tasks = entail_ch.objects.all()
	serializer = entail_ch_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# HP
@api_view(['GET'])
def entail_hp_list_res(request, in_tid):
	out_obj = entail_hp.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_hp_list(request):
	tasks = entail_hp.objects.all()
	serializer = entail_hp_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# J&K
@api_view(['GET'])
def entail_jk_list_res(request, in_tid):
	out_obj = entail_jk.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_jk_list(request):
	tasks = entail_jk.objects.all()
	serializer = entail_jk_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Kerela
@api_view(['GET'])
def entail_kl_list_res(request, in_tid):
	out_obj = entail_kl.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_kl_list(request):
	tasks = entail_kl.objects.all()
	serializer = entail_kl_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Karnataka
@api_view(['GET'])
def entail_ka_list_res(request, in_tid):
	out_obj = entail_ka.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_ka_list(request):
	tasks = entail_ka.objects.all()
	serializer = entail_ka_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Dadra_and_Nagar_Haveli
@api_view(['GET'])
def entail_dn_list_res(request, in_tid):
	out_obj = entail_dn.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_dn_list(request):
	tasks = entail_dn.objects.all()
	serializer = entail_dn_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Maharashtra
@api_view(['GET'])
def entail_mh_list_res(request, in_tid):
	out_obj = entail_mh.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_mh_list(request):
	tasks = entail_mh.objects.all()
	serializer = entail_mh_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Assam
@api_view(['GET'])
def entail_as_list_res(request, in_tid):
	out_obj = entail_as.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_as_list(request):
	tasks = entail_as.objects.all()
	serializer = entail_as_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# AP
@api_view(['GET'])
def entail_ap_list_res(request, in_tid):
	out_obj = entail_ap.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_ap_list(request):
	tasks = entail_ap.objects.all()
	serializer = entail_ap_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Meghalaya
@api_view(['GET'])
def entail_ml_list_res(request, in_tid):
	out_obj = entail_ml.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_ml_list(request):
	tasks = entail_ml.objects.all()
	serializer = entail_ml_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Punjab
@api_view(['GET'])
def entail_pb_list_res(request, in_tid):
	out_obj = entail_pb.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_pb_list(request):
	tasks = entail_pb.objects.all()
	serializer = entail_pb_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Rajasthan
@api_view(['GET'])
def entail_rj_list_res(request, in_tid):
	out_obj = entail_rj.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_rj_list(request):
	tasks = entail_rj.objects.all()
	serializer = entail_rj_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# UP
@api_view(['GET'])
def entail_up_list_res(request, in_tid):
	out_obj = entail_up.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_up_list(request):
	tasks = entail_up.objects.all()
	serializer = entail_up_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Uttaranchal
@api_view(['GET'])
def entail_ut_list_res(request, in_tid):
	out_obj = entail_ut.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_ut_list(request):
	tasks = entail_ut.objects.all()
	serializer = entail_ut_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------
# ---------------------------------------------------
# Jharkhand
@api_view(['GET'])
def entail_jh_list_res(request, in_tid):
	out_obj = entail_jh.objects.get(id__exact=in_tid)
	print(f"=======>Returned item from DB: {out_obj.res_cls}")
	context = {'Tweet': out_obj.tweet, 'Result': out_obj.res_cls, 'prob': out_obj.prob_cls}
	return Response(context)
@api_view(['GET'])
def entail_jh_list(request):
	tasks = entail_jh.objects.all()
	serializer = entail_jh_data_Serializer(tasks, many=True)
	return Response(serializer.data)
# ---------------------------------------------------

