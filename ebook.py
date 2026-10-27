import pyttsx3

engine = pyttsx3.init()

print("Welcome to Audio E-book Reader!")

file_path = input("Enter the text file path: ")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    if content.strip():
        print("\nBook content:")
        print(content)

        engine.save_to_file(content,"audio_book.wav")
        engine.runAndWait()

        print("\nReading completed!")

    else:
        print("The file is empty.")

except FileNotFoundError:
    print("Error: File not found. Please check the file path.")