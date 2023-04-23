import pytesseract
from PIL import Image

# Open the image using PIL
image = Image.open('merci_full.jpg')

# Use pytesseract to convert the image into text
text = pytesseract.image_to_string(image)

# Print the text
print(text)

