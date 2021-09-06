import time
from plyer import notification

if __name__ == "__main__":
    title_input = input("What is your reminder? : ")
    time_input = float(input("time(in Seconds): "))
    while(True):
        time.sleep(time_input)
        notification.notify(
            title=title_input,
            message="Have Your Task Completed?",
            timeout=2
        )
        break
