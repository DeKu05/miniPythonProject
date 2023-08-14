import os
if __name__ == '__main__':
  print("Konichiwa everyone, Welcome to Robospeaker created bty Gaurav")
  while True:
      x =  input("What do you want me to speak : ")
      if x == "q":
          break
      command = f'''PowerShell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).speak('{x}');"'''
      os.system(command)
#PowerShell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).speak('hello');"