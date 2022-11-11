# Import the required module for text 
# to speech conversion

from PIL import Image
from pytesseract import pytesseract
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r""

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract


# Passing the image object to image_to_string() function
# This function will extract the text from the image


  
# Language in which you want to convert
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
  
# Saving the converted audio in a mp3 file named
# welcome 


  
# Playing the converted file
#os.system("mpg321 welcome.mp3")