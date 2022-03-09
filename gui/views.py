from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
import subprocess
from .models import iptableRules


# Create your views here.
#shree ganeshay namah
#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

def sgn(request):
    return HttpResponse("sgnons jkh jbm jam jkh jcs jkb jjb jjb jsb jsd jam jom jsm jlm jsm jsm jkb jhd jgb jjb jd jd jd jmp jg")

def index(request):
    context={}
    return render(request, 'index.html', context)    



def setRules(request):
    if request.method == "GET":
        #request.session['msg']=""
        black_list_ips = iptableRules.objects.filter(rule="Black")
        print(black_list_ips)
        white_list_ips = iptableRules.objects.filter(rule="White")
        return render(request=request, template_name="setRules.html",context={ 
            'black_list_ips' :black_list_ips,
            'white_list_ips' :white_list_ips })	

    if request.method == "POST":
        try:
            if request.POST.get("black_list_ip"):    
                #add black list rule    
                p = subprocess.Popen(["bash","iptable-sgn.sh","1",request.POST['black_list_ip']])
                rule = iptableRules(project_name = "sgn",
                                    rule = "Black",
                                    ipaddr=request.POST['black_list_ip'])
                rule.save()                    
            elif request.POST.get("white_list_ip"):
                p = subprocess.Popen(["bash","iptable-sgn.sh","3",request.POST['white_list_ip']])               
                rule = iptableRules(project_name = "sgn",
                                    rule = "White",
                                    ipaddr=request.POST['white_list_ip'])
                rule.save()                    
            
            return redirect(setRules)
        except:
            request.session['msg']="Rule was not Created try again"
            return render(request=request, template_name="setRules.html",context={
                'msg': request.session['msg']
             })	

def BlackListRemove(request,black_list_ip):
    rule = iptableRules.objects.get(
                        id=black_list_ip)
    rule.delete()                    
    p = subprocess.Popen(["bash","iptable-sgn.sh","2",rule.ipaddr])    

    return redirect(setRules)


def WhiteListRemove(request,white_list_ip):
    rule = iptableRules.objects.get(
                        id=white_list_ip)
    rule.delete()                    
    p = subprocess.Popen(["bash","iptable-sgn.sh","9",rule.ipaddr])    

    return redirect(setRules)


def setWAF(request):
    if request.method == "GET":
        #request.session['msg']=""
        return render(request=request, template_name="setWAF.html",context={  })	

    if request.method == "POST":
        try:
            
            p = subprocess.Popen(["bash","iptable-sgn.sh","7",request.POST['black_list_ip'],])
            
            return redirect(setRules)
        except:
            request.session['msg']="Rule was not Created try again"
            return render(request=request, template_name="setRules.html",context={
                'msg': request.session['msg']
             })	
