
from ast import If
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from .models import Chat, Message, Token
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core import serializers
from django.db.models import Q
# Create your views here.
def testHtml(request):
    return render(request, "test.html")


@csrf_exempt
def register(request):
    if request.method == "POST":

        first_name=request.POST.get("first_name")
        username=request.POST.get("username")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        password_repeat=request.POST.get("password_repeat")
        email=request.POST.get("email")

        if password == password_repeat:
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                token = Token.objects.get(user=user).key

                return JsonResponse({"token": token}, safe=False)
            except IntegrityError:
                return JsonResponse({"errorMessage": "Username already exists" }, safe=False)
        else:
            return JsonResponse({"errorMessage": "Passwords don't match" }, safe=False)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_chats(request):
    user = request.user

    chats = Chat.objects.filter(Q(user_1=user) | Q(user_2=user))

    chats_json = serializers.serialize("json", chats)

    manipulatedChats = chats_json[:len(chats_json) - 3]
    add = ', "user_id": ' + str(user.pk) + '}}]'
    chats_json_with_user_id = manipulatedChats + add
    print(chats_json_with_user_id)
    return HttpResponse(chats_json_with_user_id, content_type='application/json')


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_messages(request):
    user = request.user
    chat_id = request.GET.get("chat_id")
    messages = Message.objects.filter(chat=chat_id)
    messages_json = serializers.serialize("json", messages)

    return HttpResponse(messages_json, content_type='application/json')


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_users_without_chat(request):
    user = request.user
    chats = Chat.objects.filter(Q(user_1=user) | Q(user_2=user))
    added_users = []
    for chat in chats:
        if chat.user_1 == user:
            added_users.append(chat.user_2)
        elif chat.user_2 == user:
            added_users.append(chat.user_1)

    not_added_users = User.objects.filter(~Q(username__in=added_users) & ~Q(username=user) )
    not_added_users_json = serializers.serialize("json", not_added_users)



    return HttpResponse(not_added_users_json, content_type='application/json')


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def post_chat(request):

    if request.method == "POST":
        user = request.user
        user_id = request.POST.get("user_id")
        second_user = User.objects.get(pk=user_id)
        chat = Chat.objects.create(user_1=user, user_2=second_user)

        chat_json = serializers.serialize("json", [chat])
        return HttpResponse(chat_json, content_type='application/json')


    return


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def post_message(request):

    if request.method == "POST":
        user = request.user
        chat_id = request.POST.get("chat_id")
        chat = Chat.objects.get(pk=chat_id)
        text = request.POST.get("text")
        message = Message.objects.create(sender=user, chat=chat, text=text)

        message_json = serializers.serialize("json", [message])
        return HttpResponse(message_json, content_type='application/json')

    return

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_users(request):
    user = request.user
    user_ids = request.GET.get("user_ids")
    user_ids = list(user_ids.split(","))
    users = []
    for user_id in user_ids:
        user = User.objects.get(pk=user_id)
        users.append(user)


    users_json = serializers.serialize("json", users)
    return HttpResponse(users_json, content_type='application/json')

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_last_message(request):
    user = request.user
    chat_ids = request.GET.get("chat_ids")
    chat_ids = list(chat_ids.split(","))
    lastMessages = []
    dummyMessage = Message.objects.create(text="", sender=user)
    for chat_id in chat_ids:
        messages = Message.objects.filter(chat=chat_id)
        if messages:
            lastMessages.append(messages.last())
        else:
            lastMessages.append(dummyMessage)

    messages_json = serializers.serialize("json", lastMessages)

    return HttpResponse(messages_json, content_type='application/json')

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_user_id(request):
    user = request.user
    user_id = user.pk

    return HttpResponse(user_id, content_type='application/json')


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@csrf_exempt
def create_guest_chats(request):




    if request.method == "POST":
        
        user = request.user

        second_user1 = User.objects.get(pk=1)
        chat = Chat.objects.create(user_1=user, user_2=second_user1)
        message = Message.objects.create(sender=user, chat=chat, text="Hallo")
        message = Message.objects.create(sender=second_user1, chat=chat, text="Hi")
        message = Message.objects.create(sender=second_user1, chat=chat, text="Wie geht es dir?")

        second_user2 = User.objects.get(pk=2)
        chat = Chat.objects.create(user_1=user, user_2=second_user2)
        message = Message.objects.create(sender=second_user1, chat=chat, text="Wer bist du?")

        second_user3 = User.objects.get(pk=3)
        chat = Chat.objects.create(user_1=user, user_2=second_user3)
        message = Message.objects.create(sender=second_user3, chat=chat, text="Schönen guten Tag")
        message = Message.objects.create(sender=user, chat=chat, text="Hallo")

        second_user4 = User.objects.get(pk=4)
        chat = Chat.objects.create(user_1=user, user_2=second_user4)
        message = Message.objects.create(sender=second_user4, chat=chat, text="Hallo!")
        message = Message.objects.create(sender=second_user4, chat=chat, text="Hast du das Fussballspiel gestern gesehen?")
        
        
        
        
        
        
        chat_json = serializers.serialize("json", [chat])
        return HttpResponse(chat_json, content_type='application/json')


    return
