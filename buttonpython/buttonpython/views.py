from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):
    return render(request, 'home.html')

def output(request):

    data = requests.get("https://www.google.com/")
    print(data.text)
    data = data.text
    return render(request, 'home.html', {'data':data})


def external(request):
    inp = request.POST.get('param')
    out = run([sys.executable, 'D://Temp//IR-PROJECT-CODE-SEARCH//main.py',inp],shell=False, stdout=PIPE)
    str1 = out.stdout.decode('utf-8').splitlines()
    
    # divide str1 into parts when you get -----------
    def  partition(lst, condition):
        result = []
        current = []
        def send(request):
            print("send")
        for item in lst:
            if condition(item):
                if current:
                    result.append(current)
                    current = []
            else:
                current.append(item)
        if current:
            result.append(current)
        return result
    
            


    #str1 = str1.splitlines()
    str1 = partition(str1, lambda x: x == '--------------------------------------------------')

    return render(request, 'home.html', {'data1':str1})