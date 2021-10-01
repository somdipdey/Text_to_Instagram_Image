# Install Pillow package
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def getSize(txt, font):
  testImg = Image.new('RGB', (1, 1))
  testDraw = ImageDraw.Draw(testImg)
  return testDraw.textsize(txt, font)

if __name__ == '__main__':
  fontname = "OpenSans-Bold.ttf"
  fontsize = 31
  username = "somdipdey"
  text = "Does anyone know how to convert/transfer the DeSo from here (Bitclout.com) to DeSo in Blockchain.com?!\nI am curious to learn how that process works.\nCorrect answer will get diamonds."
  print("Total character: " + str(len(text)))
  text_lines = text.split("\n")

  colorText = "black"
  colorOutline = "#439bfe"
  colorBackground = "white"


  font = ImageFont.truetype(fontname, fontsize)
  username_font = ImageFont.truetype(fontname, fontsize+7)
  width, height = getSize(text, font)
  height = width
  img_width = width + 31
  img_height = height + 31
  img = Image.new('RGB', (img_width, img_height), colorBackground)
  d = ImageDraw.Draw(img)
  d.text((15, height/2 - (21*len(text_lines))), "@" + username, fill=colorOutline, font=username_font)
  d.multiline_text((15, height/2), text, fill=colorText, font=font)
  d.rectangle((0, 0, img_width-3, img_height-3), outline=colorOutline, width=9)

  img.save("output_image.png")
