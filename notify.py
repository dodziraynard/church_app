# from firebase_admin import messaging
# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate('fire2.json')
# firebase_admin.initialize_app(cred)

# # # The topic name can be optionally prefixed with "/topics/".
topic = 'notifications'

# # These registration tokens come from the client FCM SDKs.
# registration_tokens = [
#     'd97qDIjVub8:APA91bGv6FsXKxu3eMxAWB5BZkzPQKYu3tADthLR6CbXA9dG0NnLfL2SE8xTY9eEUpvLGGLJMm0h43zeXExTHmbXjViVzPErBpJ_W4MNnbS_a8IAkqr0iHsqBvhb5OvU_MoIpDV4SyyA',
# ]

# # Subscribe the devices corresponding to the registration tokens to the
# # topic.
# response = messaging.subscribe_to_topic(registration_tokens, topic)
# # See the TopicManagementResponse reference documentation
# # for the contents of response.
# print(response.success_count, 'tokens were subscribed successfully')




# # See documentation on defining a message payload.
# message = messaging.Message(
#     data={
#         'score': '850',
#         'time': '2:45',
#     },
#     topic=topic,
# )

# # Send a message to the devices subscribed to the provided topic.
# response = messaging.send(message)
# # Response is a message ID string.
# print('Successfully sent message:', response)













from pusher_push_notifications import PushNotifications

beams_client = PushNotifications(
    instance_id='e07bd2ab-31f4-4600-b28d-546ec7d29fa2',
    secret_key='0AE36DFFBD13C5D71EC40B3F26818C992493D2C19FC272C6A5D3B2E890DF5952',
)

response = beams_client.publish_to_interests(
    interests=[topic],
    publish_body={
        'apns': {
            'aps': {
                'alert': 'Hello!'
            }
        },
        'fcm': {
            'notification': {
                'title': 'Hello',
                'body': 'Hello, World!'
            }
        }
    }
)

print(response['publishId'])