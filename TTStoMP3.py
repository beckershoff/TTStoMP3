import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

# List of insecure words
insecure_words = ["rm", "del", "shutdown", "format"]

# Dictionary of supported languages with language codes
languages = {"Dutch": "nl", "English": "en", "French": "fr", "German": "de", "Italian": "it", "Portuguese": "pt", "Spanish": "es"}

# Function to remove insecure words
def remove_insecure_words(text):
    for word in insecure_words:
        if word in text:
            text = text.replace(word, "")
    return text

# Function to handle TTS button press
def tts_button_pressed():
    text = text_input.get("1.0", "end-1c") # Get text from text input
    text = remove_insecure_words(text) # Remove insecure words
    if len(text) == 0:
        messagebox.showerror("Error", "Please enter some text.") # Show error message if no text entered
        return
    language = language_dropdown.get() # Get selected language
    if language not in languages:
        messagebox.showerror("Error", "Language not supported.") # Show error message if selected language not supported
        return
    lang_code = languages[language]
    tts = gTTS(text=text, lang=lang_code) # Create TTS object
    filename = text + ".mp3" # Create filename
    tts.save(filename) # Save MP3 file
    play_button.config(state="normal") # Enable play button

# Function to handle play button press
def play_button_pressed():
    filename = text_input.get("1.0", "end-1c") + ".mp3" # Get filename
    filepath = os.path.abspath(os.path.join(os.getcwd(), filename)) # Get absolute path of audio file
    audio = AudioSegment.from_file(filepath, format="mp3") # Load audio file
    play(audio) # Play audio file

# Function to handle exit button press
def exit_button_pressed():
    window.destroy()

# Create main window
window = tk.Tk()
window.title("Text-to-Speech")

# Create text input
text_input_label = tk.Label(window, text="Enter text:")
text_input_label.pack()
text_input = tk.Text(window, height=10, width=50)
text_input.pack()

# Create language dropdown
language_label = tk.Label(window, text="Select language:")
language_label.pack()
language_dropdown = ttk.Combobox(window, values=list(languages.keys()))
language_dropdown.current(1)
language_dropdown.pack()

# Create TTS button
tts_button = tk.Button(window, text="Create MP3", command=tts_button_pressed)
tts_button.pack()

# Create play button
play_button = tk.Button(window, text="Play MP3", state="disabled", command=play_button_pressed)
play_button.pack()

# Create exit button
exit_button = tk.Button(window, text="Exit", command=exit_button_pressed)
exit_button.pack()

# Run main loop
window.mainloop()
