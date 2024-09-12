from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message, decrypt_message

@login_required
def send(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            # The plaintext_message is set by the form and will be encrypted in save()
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messaging/send.html', {'form': form})

@login_required
def list_message(request):
    received_messages = Message.objects.filter(receiver=request.user)
    for msg in received_messages:
        msg.encrypted_message = decrypt_message(msg.encrypted_message, msg.encryption_key)
    return render(request, 'messaging/list_message.html', {'messages': received_messages})
