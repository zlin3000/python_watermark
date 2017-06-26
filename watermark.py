from PIL import Image, ImageDraw, ImageFont, ImageEnhance

# open image
img = Image.open("test.jpg")
img = img.convert("RGBA")

# open watermark image
# logo1.png is an normal image file without any transparent background
# logo2.png is an image with transparent background 
logo_img = Image.open("logo1.png")
#logo_img = Image.open("logo2.png")
logo_img = logo_img.convert("RGBA")

mask = Image.new("RGBA", logo_img.size, (0,0,0,0))
# change the alpha of the img logo
logo_img = Image.blend(mask, logo_img, 0.8)

# text watermark
content = "Test Watermark!"
font_file = 'carbon_bl.ttf'
font_size = 100 

color = (0,0,0, 100)

font = ImageFont.truetype(font_file, font_size)
t_w, w_h = font.getsize(content)
textlayer = Image.new("RGBA", img.size, (0,0,0,0))
textdraw = ImageDraw.Draw(textlayer, 'RGBA')
textpos = (-50,0)

#textlayer.paste(logo_img, (0,30), mask = logo_img)
textdraw.text(textpos, content, font=font, fill=color)

# put text watermark
output = Image.alpha_composite(img, textlayer)
# put image watermark
output.paste(logo_img, (0,30), mask = logo_img)

output.save("output.jpg", 'JPEG')
