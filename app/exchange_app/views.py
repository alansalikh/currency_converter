from django.shortcuts import render
import requests

def exchange(request):
    response =  requests.get(url="https://v6.exchangerate-api.com/v6/ede514c9f12b3319f29d49c3/latest/USD").json()
    currencies = response.get('conversion_rates')
    if request.method == 'GET':
        context = {
            'currencies':currencies
        }
        return render(request=request, template_name='exchange_app/index.html', context=context)
    
    if request.method == 'POST':
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr') 
        converted_amount = round((currencies[from_curr] / currencies[to_curr] * float(from_amount)),2)

        context = {
            'currencies': currencies,
            'converted_amount': converted_amount,
            'from_curr': from_curr,
            'from_amount': from_amount,
            'from_amount': from_amount,
        }

        return render(request=request, template_name='exchange_app/index.html', context=context)