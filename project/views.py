from django.shortcuts import render
from django.http import HttpResponse
from .models import userdetails,impdetails,hospital_list,history,relativedetails
from twilio.rest import Client 
from datetime import date

# Create your views here.
def home(request):
    return render(request,'index1.html')
def login(request):
    return render(request,'login.html')
def dashboard(request):
    return render(request,'dashboard.html')
def register(request):
    return render(request,'register.html')

def authenticate_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        auth=userdetails.objects.all().filter(username=username)
        print(auth)
        for i in range(len(auth)):
            userid=auth[i].id
            user_name=auth[i].username
            password1=auth[i].password
            name=auth[i].name
            emailid=auth[i].emailid
            status=auth[i].status
            mobile=auth[i].mobile
            
            
            
        request.session['member_name'] = name
        request.session['member_email'] = emailid
        request.session['member_id']=userid
        request.session['member_mobile']=mobile

           
            
        if(username==user_name):
            if(password==password1):
                if(status==1):
                    c=impdetails.objects.all().filter(userdetails_id=userid)
                    print(c)
                    for i in range(len(c)):
                        age=c[i].age
                        bldgrp=c[i].Bldgrp
                        aptname=c[i].apartment
                        landmark=c[i].landmark
                        locality=c[i].locality
                        city=c[i].City
                    
                    request.session['age']=age
                    request.session['bldgrp']=bldgrp
                    request.session['aptname']=aptname
                    request.session['landmark']=landmark
                    request.session['locality']=locality
                    request.session['city']=city
                    



                return render(request,'index.html')
            else:
                return render(request,'invalidcredential.html')
        
    else:
        return redirect(login)         

def registeruser(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        register=userdetails(name=name,mobile=mobile,emailid=email,username=username,password=password,status=0)
        register.save()
        return render(request,'registersuccess.html')
    else:
        return redirect('register')    

def getstart(request):
    name=request.session['member_name']
    user=userdetails.objects.filter(name=name)
    print(user)
    for i in range(len(user)):
        status=user[i].status
    if(status==1):
        del request.session['member_name']
        del request.session['member_email']
        del request.session['age']
        del request.session['bldgrp']
        del request.session['aptname']
        del request.session['landmark']
        del request.session['locality']
        del request.session['city']
    else:
        del request.session['member_name']
        del request.session['member_email']

    return render(request,'index1.html')  

def index(request):
    return render(request,'index.html') 

def completeprofile(request):
    if request.method=='POST':
        
        userid=request.session['member_id']
        age=request.POST['age']
        bldgrp=request.POST['bldgrp']
        aptname=request.POST['aptname']
        landmark=request.POST['landmark']
        locality=request.POST['locality']
        city=request.POST['city']
        c=impdetails(userdetails_id=userid,age=age,Bldgrp=bldgrp,apartment=aptname,landmark=landmark,locality=locality,City=city)
        c.save()

        auth=userdetails.objects.get(id=userid)
        print(auth)
        auth.status=1
        print(auth.status)
        auth.save()

        request.session['age']=age
        request.session['bldgrp']=bldgrp
        request.session['aptname']=aptname
        request.session['landmark']=landmark
        request.session['locality']=locality
        request.session['city']=city

        return render(request,'index.html')
    else:
        return redirect('register')

def selfhelp(request):
    return render(request,'selfhelp.html')

def selfhelpmessage(request):
    if request.method=='POST':
        hname=request.POST['hname']
        hcontact=request.POST['hcontact']
        hlocality=request.POST['hlocality']
        hcity=request.POST['hcity']

        userid=request.session['member_id']
        name=request.session['member_name']
        age=request.session['age']
        bldgrp=request.session['bldgrp']

        hlist=hospital_list.objects.all().filter(hospital_name=hname,userdetails_id=userid)
        count=0
        for i in range(len(hlist)):
            if(hname==hlist[i].hospital_name):
                count=1
                break


        if (count==0):
            hl=hospital_list(userdetails_id=userid,hospital_name=hname,locality=hlocality,City=hcity,contact=hcontact)
            hl.save()
        
        getall=impdetails.objects.all().filter(Bldgrp=bldgrp,locality=hlocality,City=hcity).exclude(userdetails_id=userid)
        print(getall)
        users=[]
        for i in range(len(getall)):
            users.append(i)
            users[i]=getall[i].userdetails_id
            print(users[i])

        mobile_no_of_users=[]   
        for i in range(len(users)):
            mobile_no_of_users.append(users[i])
            getall1=userdetails.objects.filter(id=users[i])
            mobile_no_of_users[i]=getall1[0].mobile
            print(mobile_no_of_users[i])

            account_sid = 'ACe2f3de774c3cde2525633814fd418c46'
            auth_token = '54c2e6968e16b49679e0323873b15ab1'

            client = Client(account_sid, auth_token) 
            
            regcode=str(mobile_no_of_users[i])
            

            ''' Change the value of 'from' with the number 
            received from Twilio and the value of 'to' 
            with the number in which you want to send message.'''
            message = client.messages.create( 
							from_='+12058393422', 
							body ='\nDear User 1 RaktaSeva member has requested for your help.'
                            'Bring you steps ahead and help him in his need.\nPatient name='+name+'\nPatient Age='+str(age)+''
                            '\nAdmitted Hospital='+hname+'\nHospital Contact='+str(hcontact)+'\nHospital locality='+hlocality+''
                            '\nHospital City='+hcity+'',
							to ='+91'+ regcode
						) 

            print(message.sid) 


        today = date.today()
        today=str(today)
        length=len(mobile_no_of_users)
        if(length!=0):
            hist=history(userdetails_id=userid,no_of_persons=length,patient_type='selfpatient',date=today)
            hist.save()


        return render(request,'messagesuccess.html',{'length':length})
    else:
        return redirect('index')


def viewhospitals(request):
    userid=request.session['member_id']
    hlist=hospital_list.objects.all().filter(userdetails_id=userid)
    print(hlist)
    
    return render(request,'viewhospitallist.html',
    {"query_results":hlist})    

def backtodashboard(request):
    return render(request,'index.html')

def viewhistory(request):
    userid=request.session['member_id']
    hist=history.objects.all().filter(userdetails_id=userid)
    return render(request,'viewhistory.html',{"query_results":hist})

        
def relativehelp(request):
    return render(request,'relativehelp.html')

def relativehelpmessage(request):
    if request.method=='POST':
        hname=request.POST['hname']
        hcontact=request.POST['hcontact']
        hlocality=request.POST['hlocality']
        hcity=request.POST['hcity']
        r_name=request.POST['r_name']
        r_age=request.POST['r_age']
        r_bldgrp=request.POST['r_bldgrp']


        userid=request.session['member_id']
        name=request.session['member_name']
        age=request.session['age']
        bldgrp=request.session['bldgrp']

        relative=relativedetails(userdetails_id=userid,rname=r_name,age=r_age,Bldgrp=r_bldgrp)
        relative.save()

        hlist=hospital_list.objects.all().filter(hospital_name=hname,userdetails_id=userid)
        count=0
        for i in range(len(hlist)):
            if(hname==hlist[i].hospital_name):
                count=1
                break


        if (count==0):
            hl=hospital_list(userdetails_id=userid,hospital_name=hname,locality=hlocality,City=hcity,contact=hcontact)
            hl.save()
        
        getall=impdetails.objects.all().filter(Bldgrp=r_bldgrp,locality=hlocality,City=hcity).exclude(userdetails_id=userid)
        print(getall)
        users=[]
        for i in range(len(getall)):
            users.append(i)
            users[i]=getall[i].userdetails_id
            print(users[i])

        mobile_no_of_users=[]   
        for i in range(len(users)):
            mobile_no_of_users.append(users[i])
            getall1=userdetails.objects.filter(id=users[i])
            mobile_no_of_users[i]=getall1[0].mobile
            print(mobile_no_of_users[i])

            account_sid = 'ACe2f3de774c3cde2525633814fd418c46'
            auth_token = '54c2e6968e16b49679e0323873b15ab1'

            client = Client(account_sid, auth_token) 
            
            regcode=str(mobile_no_of_users[i])
            

            ''' Change the value of 'from' with the number 
            received from Twilio and the value of 'to' 
            with the number in which you want to send message.'''
            message = client.messages.create( 
							from_='+12058393422', 
							body ='\n\nDear User 1 RaktaSeva member has requested for your help.'
                            'Bring you steps ahead and help him in his need.\nPatient name='+r_name+'\nPatient Age='+str(age)+''
                            '\nAdmitted Hospital='+hname+'\nHospital Contact='+str(hcontact)+'\nHospital locality='+hlocality+''
                            '\nHospital City='+hcity+'',
							to ='+91'+ regcode
						) 

            print(message.sid) 


        today = date.today()
        today=str(today)
        length=len(mobile_no_of_users)
        if(length!=0):
            hist=history(userdetails_id=userid,no_of_persons=length,patient_type='relative',date=today)
            hist.save()


        return render(request,'messagesuccess.html',{'length':length})
    else:
        return redirect('index')
