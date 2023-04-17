import speech_recognition as sr
import re
import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()

r = sr.Recognizer()

def use_skill(btn):
    gamepad.right_trigger_float(value_float=1.0)
    gamepad.update()
    time.sleep(0.1)
    gamepad.press_button(button=btn)
    gamepad.update()
    time.sleep(1)
    gamepad.right_trigger_float(value_float=0.0)
    gamepad.release_button(button=btn)
    gamepad.update()

with sr.Microphone() as source:                
    while True:
        audio = r.listen(source)
        try:
            # result = r.recognize_sphinx(audio, keyword_entries=[("one",1),("two",1)])
            result = r.recognize_google(audio, language="th-TH")
            print("Said: " + result)
            if re.search('ระเบิด', result, re.IGNORECASE):
                print("Confringo")
                use_skill(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            elif re.search('ดึง', result, re.IGNORECASE):
                print("Accio")
                use_skill(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            elif re.search('ลอย', result, re.IGNORECASE) or re.search('ยก', result, re.IGNORECASE):
                print("Levioso")
                use_skill(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            elif re.search('ปลด', result, re.IGNORECASE):
                print("Expelliarmus")
                use_skill(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            elif re.search('ค้นหา', result, re.IGNORECASE):
                print("Revelio")
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                gamepad.update()
                time.sleep(1)
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                gamepad.update()
            else:
                print("What?")

        except LookupError:
            print("LookupError")
        except sr.UnknownValueError:
            print("UnknownValueError")
