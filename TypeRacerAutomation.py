from PIL import Image
import pytesseract
import pyautogui


typeboxlist = []
regionlist = []
typebox = pyautogui.locateOnScreen('TyperacerTypeBox.jpg', confidence=0.8)  # region of typing box
typeboxcenter = pyautogui.locateCenterOnScreen('TyperacerTypeBox.jpg', confidence=0.8)  # coordinates of type box
yellowlines = list(pyautogui.locateAllOnScreen('yellowdottedline.jpg', confidence=0.95))  # finding all yellow lines

for set in yellowlines:  # organizing data so that it can be manipulated
    regionlist.append([coordinate for coordinate in set])

for coordinate in typebox:
    typeboxlist.append(coordinate)

# finding region values for screenshot
TopofLine = regionlist[-1][1] + 10
TopofText = typeboxlist[1]
HeightSS = TopofText - TopofLine + 10

textSS = pyautogui.screenshot('textSS.jpg', region=(591, TopofLine, 620, HeightSS))
towrite = pytesseract.image_to_string('textSS.jpg')

# manipulating output to be more accurate
cleantext = towrite.lstrip('> ')
cleantext = cleantext.replace('|', 'I')
cleantext = cleantext.replace('\n', ' ')

if cleantext.startswith('[') or cleantext.startswith('('):
    cleantext = cleantext.lstrip('[')
    cleantext = cleantext.lstrip('(')

# moving cursor to type box
pyautogui.click(pyautogui.moveTo(typeboxcenter, duration=1))
pyautogui.typewrite(cleantext, interval=.05)

