import speech_recognition as sr
import os
from gtts import gTTS
import playsound
import webbrowser as web
import datetime
import time
import tkinter

def microphone_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        playsound.playsound("start.mp3")
        print("say something!")
        audio = recognizer.listen(source)
        #audio = recognizer.record(source, duration=4)
    try:
        user_input = recognizer.recognize_google(audio, language="th")
        print("คุณพูดว่า :" + user_input)
        text_user.configure(text=user_input, bg="#afeeee", bd=3)
        label_user.configure(text="user", bd=3)
    except:
        user_input = "try again"
        print("ขอโทษค่ะ กรุณาลองใหม่อีกครั้ง")
        label_bob.configure(text="bob", bd=3)
        text_bob.configure(text="ขอโทษค่ะ กรุณาลองใหม่อีกครั้ง", bg="#afeeee", bd=3)
    return user_input

def bob_speak(text):
    print(text)
    sound_bob = gTTS(text=text, lang='th')
    sound_bob.save("sound_file.mp3")
    playsound.playsound("sound_file.mp3")
    os.remove("sound_file.mp3")
    text_bob.configure(text = text, bg="#afeeee", bd=3)
    label_bob.configure(text="bob", bd=3)

def bob_check(text_speak):
    if"try again" in text_speak:
        pass
    elif "สวัสดี" in text_speak or "Hello" in text_speak:
        bob_speak("สวัสดีค่ะ มีอะไรให้ช่วยไหมคะ")
    #elif "" in text_speak:
    elif "เวลาเท่าไหร่แล้ว" in text_speak or "กี่โมงแล้ว" in text_speak:
        now = datetime.datetime.now()
        hour = int(now.strftime("%H"))
        minute = int(now.strftime("%M"))
        if hour >= 6 and hour <=11:#โมงเช้า
            text_time = str(hour) + "โมง"+str(minute) + "นาที"
        if hour == 12:#เที่ยง
            text_time = "เที่ยง" + str(minute) + "นาที"
        if hour >= 13 and hour <= 15:#บ่ายโมง
            text_time = "บ่าย" + str(hour - 12) + str(minute) + "นาที"
        if hour >= 16 and hour <= 18:#โมงเย็น
            text_time = str(hour - 12) + "โมงเย็น" + str(minute) + "นาที"
        if hour >= 19 and hour <= 23:#ทุ่ม
            text_time = str(hour - 18) + "ทุ่ม" + str(minute) + "นาที"
        if hour == 0:#เที่ยงคืน
            text_time = "เที่ยงคืน" + str(minute) + "นาที"
        if hour >= 1 and hour <= 5:#ตี
            text_time = "ตี" + str(hour) + str(minute) + "นาที"
        bob_speak(text_time + "ค่ะ")
    elif "เปิด Google" in text_speak:
        web.open("www.google.com")
        bob_speak("เปิด Google")
    elif "เปิด YouTube" in text_speak:
        bob_speak("เปิดคลิปอะไรคะ")
        search = microphone_input()
        if "try again" in search or "เปิดเฉยๆ" in search:
            web.open("www.youtube.com")
        else:
            web.open("www.youtube.com/results?search_query="+search)
        bob_speak("เปิด youtube")
    elif "เปิด Facebook" in text_speak:
        web.open("www.facebook.com")
        bob_speak("เปิด facebook")
    elif "เปิด IG" in text_speak:
        web.open("www.instragram.com")
        bob_speak("เปิด instragram")
    elif "เปิด Word" in text_speak:
        wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(wordPath)
        bob_speak("เปิด word")
    elif "เปิด Excel" in text_speak:
        execelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(execelPath)
        bob_speak("เปิด excel")
    elif "เปิด Powerpoint" in text_speak:
        pointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(pointPath)
        bob_speak("เปิด powerpoint")
    elif "ปิดเครื่อง" in text_speak or "Shut Down" in text_speak:
        bob_speak("บ๊ายบายค่ะ")
        os.system("shutdown /s /t 1")

def main_program():
    #while True:
    text_bob.configure(text="", bg="white")
    text_user.configure(text="", bg="white")
    user_speak=microphone_input()
    bob_check(user_speak)
    if "บ่าย" in user_speak or "บาย" in user_speak or "บ๊าย" in user_speak:
        bob_speak("บ๊ายบายค่ะ")
        quit(window)
        #break

window = tkinter.Tk()
window.title("bob")
window.geometry("500x250")
window.configure(bg="white")
button = tkinter.Button(window, text = "start", command = main_program, font = "times 16")
text_bob = tkinter.Label(window, text = "", font = "tahoma 16", bg = "white")
text_user = tkinter.Label(window, text = "", font = "tahoma 16", bg = "white")
label_user =tkinter.Label(window, text = "", font = "tahoma 20", bg = "white")
label_bob =tkinter.Label(window, text = "", font = "tahoma 20", bg = "white")
developer =tkinter.Label(window, text = "developer : krit taochoo", font = "tahoma 10", fg = "gray")

button.pack(ipadx=10)
label_user.pack(anchor = "e")
text_user.pack(anchor = "e", ipadx=10, ipady=5)
label_bob.pack(anchor = "w")
text_bob.pack(anchor = "w", ipadx=10, ipady=5)
developer.pack(side = "bottom")
window.mainloop()


