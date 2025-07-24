print('''
A Gentle Whisper
The wind whispers secrets to the trees,
A gentle breeze, carrying ease.
Sunlight paints the leaves with gold,
Stories of summer, bravely told.
A quiet moment, calm and deep,
Where peaceful thoughts begin to sleep''')
# to print something multilined we can use single triple and double triple
# external module example
# as we have used the midule named pyttsx whcih means text to speak it we speak what we have written in the print section
import pyttsx3
engine = pyttsx3.init()

engine.say('''
A Gentle Whisper
The wind whispers secrets to the trees,
A gentle breeze, carrying ease.
Sunlight paints the leaves with gold,
Stories of summer, bravely told.
A quiet moment, calm and deep,
Where peaceful thoughts begin to sleep''')
engine.runAndWait()
