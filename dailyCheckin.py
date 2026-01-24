moods = ["good", "ok", "bad"]

# _________Mood_____________
while True:
    my_mood = input("how are you feeling today? (good / ok / bad) : ")
    if my_mood in moods:
        break
    else:
        print("what is your mood today? only good, ok or bad please: ")

#       Productivity

while True:
    try:
        productivity = int(input("how productive was your day? (1 to 5): "))
        if productivity in range(1, 6):
           break
        else:
            print("enter only numbers between 1 and 5: ")
    except ValueError:
        print("only numbers")

#       Note for the day
note = input("any short note about the day? : (press Enter to skip): ")

#       Print all
print("\n Daily Check-In Summary")
print(f"Mood: {my_mood}")
print(f"Productivity: {productivity}/5 ")

if note:
    print(f"Your note for the day: {note}")
else:
    print("No note for the day")


