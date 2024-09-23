import RPi.GPIO as GPIO
import tkinter as tk

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
Red_led = 35
Green_led = 38
Blue_led = 40

# Set up GPIO pins for PWM
GPIO.setup(Red_led, GPIO.OUT)
GPIO.setup(Green_led, GPIO.OUT)
GPIO.setup(Blue_led, GPIO.OUT)

# Set PWM frequency to 100Hz
red_pwm = GPIO.PWM(Red_led, 100)
green_pwm = GPIO.PWM(Green_led, 100)
blue_pwm = GPIO.PWM(Blue_led, 100)

# Start PWM with 0% duty cycle (LEDs off)
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

# Function to adjust the LED brightness
def adjust_brightness():
    red_pwm.ChangeDutyCycle(red_slider.get())
    green_pwm.ChangeDutyCycle(green_slider.get())
    blue_pwm.ChangeDutyCycle(blue_slider.get())

# Exit and clean up GPIO
def end_app():
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()
    window.quit()

# Create the Tkinter window
window = tk.Tk()
window.title("LED Intensity Controller")

# Create sliders for LED intensity
red_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Red LED", command=lambda x: adjust_brightness())
red_slider.pack(padx=20, pady=10)

green_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Green LED", command=lambda x: adjust_brightness())
green_slider.pack(padx=20, pady=10)

blue_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Blue LED", command=lambda x: adjust_brightness())
blue_slider.pack(padx=20, pady=10)

# Create Exit button
exit_button = tk.Button(window, text="Exit", command=end_app)
exit_button.pack(pady=20)

# Run the Tkinter main loop
window.mainloop()
