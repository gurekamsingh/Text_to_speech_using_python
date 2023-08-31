import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

list1 = ["Gurekam", "Rohan", "Lilly", "Jovan", "Samaiyra", "Roohani", "Sam"]

for i in list1:
    if i == "Gurekam":
        print(f"Shoutout to {i}, he is an extraordinary student, he will reach to greater heights! well done!!")
        s = f"Shoutout to {i}, he is an extraordinary student, he will reach to greater heights! well done!!"
        speaker.Speak(s)
    else:
        print(f"Shoutout to {i}, Well done!!")
        s = f"Shoutout to {i}, Well done!!"
        speaker.Speak(s)
