import platform
import psutil
import time
import RPi.GPIO as GPIO


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 1000)
    try:
        pwm.start(0)
        while True:
            pwm.ChangeDutyCycle(max(min(psutil.cpu_percent(), 10), 80)+20) # 10-80 + 20 => (30%-100%)
            time.sleep(5)
    except:
        pass
    pwm.stop()