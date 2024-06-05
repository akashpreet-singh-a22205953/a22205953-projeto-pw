from django.shortcuts import render
import requests


urlLisbon = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
urlDescricaoClima = "https://api.ipma.pt/open-data/weather-type-classe.json"




def weather(request):





    urlLisbon = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    urlDescricaoClima = "https://api.ipma.pt/open-data/weather-type-classe.json"






    ficheiroSvg = "w_ic_d_"
    response = requests.get(urlLisbon)
    response2 = requests.get(urlDescricaoClima)


    if response.status_code == 200:
        data = response.json()
    else:
        print("Erro ao acessar a API:", response.status_code)


    if response2.status_code == 200:
        dataDescricaoClima = response2.json()
    else:
        print("Erro ao acessar a API:", response2.status_code)

    idWeather = data['data'][0]['idWeatherType']
    if idWeather > 9:
            ficheiroSvg = ficheiroSvg + str(idWeather) + "anim.svg"
    else:
            ficheiroSvg = ficheiroSvg + "0" + str(idWeather) + "anim.svg"
    tempDesc = ""
    for item in dataDescricaoClima['data']:
        if item['idWeatherType'] == idWeather:
            tempDesc = item['descWeatherTypePT']
    context = {
        "dataHoje" : data['dataUpdate'].split('T')[0],
        "temperaturaMin" : data['data'][0]['tMin'] + "ºC",
        "temperaturaMax" : data['data'][0]['tMax'] + "ºC",
        "tempDesc" : tempDesc,
        "svgFile" : ficheiroSvg
    }

    return render(request, 'meteo/index.html', context)



urlLisbon = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
urlDescricaoClima = "https://api.ipma.pt/open-data/weather-type-classe.json"


def weather5days(request):
    ficheiroSvg = "w_ic_d_"
    response = requests.get(urlLisbon)
    response2 = requests.get(urlDescricaoClima)
    data = {}
    dataDescricaoClima = {}

    if response.status_code == 200:
        data = response.json()
    else:
        print("Erro ao acessar a API:", response.status_code)

    if response2.status_code == 200:
        dataDescricaoClima = response2.json()
    else:
        print("Erro ao acessar a API:", response2.status_code)

    allDesc = []
    for n in dataDescricaoClima['data']:
        if n['idWeatherType'] >= 0:
            allDesc.append(n['descWeatherTypePT'])


    list = []
    for n in data['data']:
        weatherDetails = {}
        weatherDetails["dataHoje"] = n['forecastDate']
        weatherDetails["temperaturaMin"] = n['tMin'] + "ºC"
        weatherDetails["temperaturaMax"] = n['tMax'] + "ºC"
        weatherDetails["tempDesc"] = allDesc[n['idWeatherType']]
        weatherDetails["svgFile"] = ficheiroSvg + (str(n['idWeatherType']) if n['idWeatherType'] > 9 else "0" + str(n['idWeatherType'])) + "anim.svg"
        list.append(weatherDetails)

    context = {
        "weatherDetailsList" : list
    }

    return render(request, 'meteo/weather5days.html', context)