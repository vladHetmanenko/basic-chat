from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from django.middleware.csrf import get_token

from messenger.constants import WAIT_MESSAGE, NGROK_SERVER2_URL

def index(request):
    return render(request, 'messenger/index.html', {
        'message': WAIT_MESSAGE,
        'post_message_url': NGROK_SERVER2_URL,
        'csrf_token': get_token(request),
    })

@csrf_exempt
def update_message(request):
    if request.method == 'POST':
        new_message = request.POST.get('message', '')
        if new_message:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'messenger_group',
                {
                    'type': 'send_message',
                    'message': new_message,
                }
            )
            return JsonResponse({'status': 'success', 'message': new_message}, status=200)
    return JsonResponse({'status': 'failed'}, status=400)
