import os
import pyttsx3
print()
while True: 
  pyttsx3.speak("ENTER YOUR REQUIREMENTS FOR CHATTING")
  print("Enter Your Requirement For Chatting: ", end = "")
  Cmnd = input().lower()

  if ( ("not" not in Cmnd) and ("donot" not in Cmnd) and ("don't" not in Cmnd) and ("doesn't" not in Cmnd) and ("doesnot" not in Cmnd) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("chrome" in Cmnd) or ("google" in Cmnd)) ):
    pyttsx3.speak("Wait, Chrome is Opening")
    os.system("chrome")

  elif ( (("not" in Cmnd) or ("donot" in Cmnd) or ("don't" in Cmnd) or ("doesn't" in Cmnd) or ("doesnot" in Cmnd)) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("google" in Cmnd) or ("chrome" in Cmnd)) ):   
    pyttsx3.speak("As Per Your Request, We Are Not Opening the Chrome!!")
    print("As Per Your Request, We Are Not Opening the Chrome!!")

  elif ( ("not" not in Cmnd) and ("donot" not in Cmnd) and ("don't" not in Cmnd) and ("doesn't" not in Cmnd) and ("doesnot" not in Cmnd) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("notepad" in Cmnd) or ("texteditor" in Cmnd)) ):
    pyttsx3.speak("Wait, NotePad is Opening")
    os.system("notepad")
  
  elif ( (("not" in Cmnd) or ("donot" in Cmnd) or ("don't" in Cmnd) or ("doesn't" in Cmnd) or ("doesnot" in Cmnd)) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("notepad" in Cmnd) or ("texteditor" in Cmnd)) ):   
    pyttsx3.speak("As Per Your Request, We Are Not Opening the NotePad!!")
    print("As Per Your Request, We Are Not Opening the NotePad!!")
 
  elif ( ("not" not in Cmnd) and ("donot" not in Cmnd) and ("don't" not in Cmnd) and ("doesn't" not in Cmnd) and ("doesnot" not in Cmnd) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("vlcplayer" in Cmnd) or ("vlc" in Cmnd)) ):
    pyttsx3.speak("Wait, VLC Media Player is Opening")
    os.system("vlc")
  
  elif ( (("not" in Cmnd) or ("donot" in Cmnd) or ("don't" in Cmnd) or ("doesn't" in Cmnd) or ("doesnot" in Cmnd)) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("vlcplayer" in Cmnd) or ("vlc" in Cmnd)) ):   
    pyttsx3.speak("As Per Your Request, We Are Not Opening the VLC Media Player!!")
    print("As Per Your Request, We Are Not Opening the VLC Media Player!!")

  elif ( ("not" not in Cmnd) and ("donot" not in Cmnd) and ("don't" not in Cmnd) and ("doesn't" not in Cmnd) and ("doesnot" not in Cmnd) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("wmplayer" in Cmnd) or ("wmplyr" in Cmnd) or ("windows media player" in Cmnd)) ):
    pyttsx3.speak("Wait, Windows Media Player is Opening")
    os.system("wmplayer")
  
  elif ( (("not" in Cmnd) or ("donot" in Cmnd) or ("don't" in Cmnd) or ("doesn't" in Cmnd) or ("doesnot" in Cmnd)) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("wmplayer" in Cmnd) or ("wmplyr" in Cmnd) or ("windows media player" in Cmnd)) ):   
    pyttsx3.speak("As Per Your Request, We Are Not Opening the Windows Media Player!!")
    print("As Per Your Request, We Are Not Opening the Windows Media Player!!")

  elif ( ("not" not in Cmnd) and ("donot" not in Cmnd) and ("don't" not in Cmnd) and ("doesn't" not in Cmnd) and ("doesnot" not in Cmnd) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("control panel" in Cmnd) or ("controlpanel" in Cmnd) or ("cntrl pnl" in Cmnd)) ):
    pyttsx3.speak("Wait, Control Panel is Opening")
    os.system("control panel")
  
  elif ( (("not" in Cmnd) or ("donot" in Cmnd) or ("don't" in Cmnd) or ("doesn't" in Cmnd) or ("doesnot" in Cmnd)) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("control panel" in Cmnd) or ("controlpanel" in Cmnd) or ("cntrl pnl" in Cmnd)) ):   
    pyttsx3.speak("As Per Your Request, We Are Not Opening the Control Panel!!")   
    print("As Per Your Request, We Are Not Opening the Control Panel!!")
  
  elif ( ("not" not in Cmnd) and ("donot" not in Cmnd) and ("don't" not in Cmnd) and ("doesn't" not in Cmnd) and ("doesnot" not in Cmnd) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("powershell" in Cmnd) or ("power shell" in Cmnd) or ("windows powershell" in Cmnd)) ):     
    pyttsx3.speak("Wait, PowerShell is Opening")
    os.system("Powershell")
  
  elif ( (("not" in Cmnd) or ("donot" in Cmnd) or ("don't" in Cmnd) or ("doesn't" in Cmnd) or ("doesnot" in Cmnd)) and (("run" in Cmnd) or ("open" in Cmnd) or ("launch" in Cmnd) or ("execute" in Cmnd) or ("create" in Cmnd)) and (("powershell" in Cmnd) or ("power shell" in Cmnd) or ("windows powershell" in Cmnd)) ):   
    pyttsx3.speak("As Per Your Request, We Are Not Opening the PowerShell!!")
    print("As Per Your Request, We Are Not Opening the Windows PowerShell!!")

  elif (("exit" in Cmnd) or ("close" in Cmnd) or ("stop" in Cmnd) or ("quit" in Cmnd) or ("finish" in Cmnd)):
    pyttsx3.speak("Exit The Program")
    break 

  else:
    pyttsx3.speak("Oops! Command Not Found")
    print("Oops! Command is not found")
  print()
