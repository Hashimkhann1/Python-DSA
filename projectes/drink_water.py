import time
from plyer import notification

while True:
    notification.notify(
        title="Take Rest",
        message="Drink water and play Table Tennis to refresh.",
        timeout=10,
        app_icon='takeRest.png'
    )
    time.sleep(10)
