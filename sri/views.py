from django.shortcuts import render,redirect
from .models import Details
def home(request):
    return render(request,'step.html')
def save(request):
    hide1=request.POST.get('hide')
    bodytype2=request.POST.get('bodytype')
    weight2=request.POST.get('weight')
    education2=request.POST.get('education')
    occupation2=request.POST.get('occupation')
    eating2=request.POST.get('eating')
    drinking2=request.POST.get('drinking')
    smoking2=request.POST.get('smoking')
    star2=request.POST.get('star')
    raasi2=request.POST.get('raasi')
    dob2=request.POST.get('dob')
    country2=request.POST.get('country')
    state2=request.POST.get('state')
    city2=request.POST.get('city')
    father2=request.POST.get('father')
    mother2=request.POST.get('mother')
    bno2=request.POST.get('bno')
    bma2=request.POST.get('bma')
    sno2=request.POST.get('sno')
    sma2=request.POST.get('sma')
    location2=request.POST.get('location')
    contact2=request.POST.get('contact')
    mobile2=request.POST.get('mobile')
    ao2=request.POST.get('ao')
    if hide1 == '':
        key=Details(bodytype1=bodytype2,weight1=weight2,education1=education2,occupation1=occupation2,eating1=eating2,drinking1=drinking2,smoking1=smoking2,
                   star1=star2,raasi1=raasi2,dob1=dob2,country1=country2,state1=state2,city1=city2,father1=father2,mother1=mother2,bno1=bno2,bma1=bma2,
                   sno1=sno2,sma1=sma2,location1=location2,contact1=contact2,mobile1=mobile2,ao1 =ao2)
        key.save()
        return redirect(retrive)
    else:
        updates=Details.objects.filter(id=hide1).update(bodytype1=bodytype2,weight1=weight2,education1=education2,occupation1=occupation2,eating1=eating2,drinking1=drinking2,smoking1=smoking2,
                   star1=star2,raasi1=raasi2,dob1=dob2,country1=country2,state1=state2,city1=city2,father1=father2,mother1=mother2,bno1=bno2,bma1=bma2,
                   sno1=sno2,sma1=sma2,location1=location2,contact1=contact2,mobile1=mobile2,ao1 =ao2)
        # return render(request,'retrive1.html',{'key':updates})
        return redirect(retrive)
def retrive(request):
    values=Details.objects.all()
    return render(request,'retrive1.html',{'keys':values})
def edit(request,id):
    value=Details.objects.get(id=id)
    return render(request,'step.html',{'key':value})
def deletes(request,id):
    delet=Details.objects.get(id=id)
    delet.delete()
    return redirect(retrive)