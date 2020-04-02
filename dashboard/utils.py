from pusher_push_notifications import PushNotifications

def send_notification(title, message, topic="notifications"):
    beams_client = PushNotifications(
        instance_id='e07bd2ab-31f4-4600-b28d-546ec7d29fa2',
        secret_key='0AE36DFFBD13C5D71EC40B3F26818C992493D2C19FC272C6A5D3B2E890DF5952',
    )
    response = beams_client.publish_to_interests(
        interests=[topic],
        publish_body={
            'apns': {
                'aps': {
                    'alert': title
                }
            },
            'fcm': {
                'notification': {
                    'title': title,
                    'body': message
                }
            }
        }
    )
    print(response['publishId'])