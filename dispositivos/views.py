from django.shortcuts import render
from user_agents import parse

def home(request):
    device_type = 'Desconocido'
    # Asegurarnos de que 'HTTP_USER_AGENT' está presente
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    
    # Solo analizamos si hay un user_agent
    if user_agent:
        user_agent_parsed = parse(user_agent)
        if user_agent_parsed.is_mobile:
            device_type = 'Móvil'
        elif user_agent_parsed.is_tablet:
            device_type = 'Tablet'
        else:
            device_type = 'Escritorio'
    
    return render(request, 'home.html', {'device_type': device_type})
