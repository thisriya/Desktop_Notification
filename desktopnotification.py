from plyer import notification
import time
if __name__=='__main__':
    while True:
        notification.notify(
            title="***Please Drink Water***",
            message="We should always be hydrated as it helps us being healthy and fresh.",
            timeout=5)
        time.sleep(3600)
