import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from api.models import Question

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        event = event['message']
        roomName = event['roomid']
        message = event['question']
        opt1 = event['option1']
        opt2 = event['option2']
        opt3 = event['option3']
        opt4 = event['option4']
        ans = event['answer']
        qid = event['qid']
        # print("QUESTION ID: ", qid)
        print(event)
        # Send message to WebSocket
        
        # creating a model instance
        question = Question.objects.create(roomname=roomName ,question=message, option1=opt1, option2=opt2, option3=opt3, option4=opt4,answer=int(ans), qid=qid)
        try:
            if(not Question.objects.get(message == question.message)):
                question.save()
                self.send(text_data=json.dumps({
                'message': "Quesition created! 😂", 
                }))
        except:
            self.send(text_data=json.dumps({
            'message': "Question not created! 😂", 
            }))

   