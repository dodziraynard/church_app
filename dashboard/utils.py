from pusher_push_notifications import PushNotifications
from church_app import local_settings

def send_notification(title, message, topic="notifications"):
    beams_client = PushNotifications(
        instance_id = local_settings.instance_id,
        secret_key = local_settings.secret_key,
    )
    try:
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
    except Exception as e:
        print(e)