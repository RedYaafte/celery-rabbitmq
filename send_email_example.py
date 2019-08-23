import asyncio
import mandrill


mandrill_client = mandrill.Mandrill('yNwq2t49hMT6t4U32skWYA')

message = {'from_email': 'redyafte@gmail.com',
           'from_name': 'Yafté',
           'to': [{
               'email': 'yafte@bedu.com',
               'name': 'Yafé Bedu',
               'type': 'to'
           }],
           'subject': "Testing out Mandrill",
           'text': 'This is a message from Mandrill'
           }

send = mandrill_client.messages.send(message=message)

# send = mandrill_client.messages.send_at(message=message)
print(send)
