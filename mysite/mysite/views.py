from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
# listings/views.py



def gettingstarted(request):
    if request.method == 'POST':
        results = []
        selected_option_freqout = request.POST.get('freqout')
        results.append(selected_option_freqout)
        selected_option_durawork = request.POST.get('durawork')
        results.append(selected_option_durawork)
        selected_option_car = request.POST.get('car')
        results.append(selected_option_car)
        selected_option_energy = request.POST.get('energy')
        results.append(selected_option_energy)
        selected_option_devicestatus = request.POST.get('devicestatus')
        results.append(selected_option_devicestatus)
        selected_option_diet = request.POST.get('diet')
        results.append(selected_option_diet)
        selected_option_recycle = request.POST.get('recycle')
        results.append(selected_option_recycle)
        selected_option_travel = request.POST.get('travel')
        results.append(selected_option_travel)
        selected_option_hobbies = request.POST.get('hobbies')
        results.append(selected_option_hobbies)
        selected_option_readytochange = request.POST.get('readytochange')
        results.append(selected_option_readytochange)
        # Do something with the selected options, like saving them to the database
        print(results)
        options = {"Everyday":483,
                   "thrice":207,
                   "once":69,
                   "10":23,
                   "30":69,
                   "hour":138,
                   "electric":0,
                   "engine":2.3,
                   "nocar":0,
                   "solar":0,
                   "hybrid":175,
                   "grid":350,
                   "never":0,
                   "rarely":0.45,
                   "sometimes":0.96,
                   "vegan":3,
                   "half":2,
                   "full":0,
                   "does":0,
                   "try":2,
                   "dont":4,
                   "monthly":4.2,
                   "biyearly":2.1,
                   "yearly":0.4,
                   "impact":0,
                   "dontimpact":0,
                   "notsure":0,
                   "yessir":0,
                   "nosir":0,
                   "dontcare":0}
        b = 0
        for i in results:
            b += options[i]
        print(b)
        b = b
        d = b*7
        f = d*4
        e = f*12
        c = {"b":b,
            "d":d,
             "f":f,
             "e":e}
        template = loader.get_template('pages/results.html')
        return HttpResponse(template.render(c,request))
    else:
        selected_option_freqout = None
        selected_option_durawork = None
        selected_option_car = None
        selected_option_energy = None
        selected_option_devicestatus = None
        selected_option_diet = None
        selected_option_recycle = None
        selected_option_travel = None
        selected_option_hobbies = None
        selected_option_readytochange = None
        


    context = {
        'selected_option_freqout': selected_option_freqout,
        'selected_option_durawork': selected_option_durawork,
        'selected_option_car': selected_option_car,
        'selected_option_energy': selected_option_energy,
        'selected_option_devicestatus': selected_option_devicestatus,
        'selected_option_diet': selected_option_diet,
        'selected_option_recycle': selected_option_recycle,
        'selected_option_travel': selected_option_travel,
        'selected_option_hobbies': selected_option_hobbies,
        'selected_option_readytochange': selected_option_readytochange,
    }

    return render(request, 'pages/start.html', context)

def home_view(request):
    if request.method == 'POST':
        vil = request.POST.get("mail")
        print(vil)
        email_addresses = []
        email_addresses.append(vil)
        send_mail(
        "Thanks for subscribing to our mailing services",
        "You will be recieving weekly updates and information on the climate and much more",
        "imaadudeen111@gmail.com",
        [vil],
        fail_silently=False,
    )
        return render(request, "pages/home.html")
    
    return render(request, "pages/home.html")

def loggedin(request):
    if request.method == 'POST':
        results = []
        selected_option_freqout = request.POST.get('freqout')
        results.append(selected_option_freqout)
        selected_option_durawork = request.POST.get('durawork')
        results.append(selected_option_durawork)
        selected_option_car = request.POST.get('car')
        results.append(selected_option_car)
        selected_option_energy = request.POST.get('energy')
        results.append(selected_option_energy)
        selected_option_devicestatus = request.POST.get('devicestatus')
        results.append(selected_option_devicestatus)
        selected_option_diet = request.POST.get('diet')
        results.append(selected_option_diet)
        selected_option_recycle = request.POST.get('recycle')
        results.append(selected_option_recycle)
        selected_option_travel = request.POST.get('travel')
        results.append(selected_option_travel)
        selected_option_hobbies = request.POST.get('hobbies')
        results.append(selected_option_hobbies)
        selected_option_readytochange = request.POST.get('readytochange')
        results.append(selected_option_readytochange)
        # Do something with the selected options, like saving them to the database
        print(results)
        options = {"Everyday":483,
                   "thrice":207,
                   "once":69,
                   "10":23,
                   "30":69,
                   "hour":138,
                   "electric":0,
                   "engine":2.3,
                   "nocar":0,
                   "solar":0,
                   "hybrid":175,
                   "grid":350,
                   "never":0,
                   "rarely":0.45,
                   "sometimes":0.96,
                   "vegan":3,
                   "half":2,
                   "full":0,
                   "does":0,
                   "try":2,
                   "dont":4,
                   "monthly":4.2,
                   "biyearly":2.1,
                   "yearly":0.4,
                   "impact":0,
                   "dontimpact":0,
                   "notsure":0,
                   "yessir":0,
                   "nosir":0,
                   "dontcare":0}
        b = 0
        for i in results:
            b += options[i]
        print(b)
        b = b
        d = b*7
        f = d*4
        e = f*12
        c = {"b":b,
             "d":d,
             "f":f,
             "e":e}
        template = loader.get_template('pages/results.html')
        return HttpResponse(template.render(c,request))
    else:
        selected_option_freqout = None
        selected_option_durawork = None
        selected_option_car = None
        selected_option_energy = None
        selected_option_devicestatus = None
        selected_option_diet = None
        selected_option_recycle = None
        selected_option_travel = None
        selected_option_hobbies = None
        selected_option_readytochange = None


    context = {
        'selected_option_freqout': selected_option_freqout,
        'selected_option_durawork': selected_option_durawork,
        'selected_option_car': selected_option_car,
        'selected_option_energy': selected_option_energy,
        'selected_option_devicestatus': selected_option_devicestatus,
        'selected_option_diet': selected_option_diet,
        'selected_option_recycle': selected_option_recycle,
        'selected_option_travel': selected_option_travel,
        'selected_option_hobbies': selected_option_hobbies,
        'selected_option_readytochange': selected_option_readytochange,
    }
    return render(request, "registration/logged.html", context)

def login(request):
    return render(request, "pages/login.html", {})

def password_change(request):
    return render(request, "registration/password_change_form.html", {})

def password_change_done(request):
    return render(request, "registration/password_change_done.html", {})


 