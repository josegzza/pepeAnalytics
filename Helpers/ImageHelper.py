from PIL import Image, ImageDraw, ImageFont

class ImageHelper():

    def __init__(self):
        self.img = None

    def createImg(self, templateFileName, frontFileName, fontFileName, text):
        ## Background Template
        # Open an image
        im = Image.open('./sources/img/'+templateFileName)
        draw = ImageDraw.Draw(im)
        ## Insert image
        front_img = Image.open('./sources/img/'+frontFileName)
        #Resize front img
        img_width, img_height = front_img.size
        front_img = front_img.resize((int(img_width*5), int(img_height*5)))
        front_img.thumbnail((950, 800))
        img_width, img_height = front_img.size
        #center align
        front_x = (im.width - img_width) / 2
        front_y = ((im.height+45) - img_height) / 2
        im.paste(front_img, (int(front_x), int(front_y)))

        # # Get a font object
        font = ImageFont.truetype("./sources/fonts/"+fontFileName, 50)
        text_width = draw.textlength(text, font=font)
        # Align center
        text_x = (im.width - text_width) / 2
        draw.text((text_x, 50), text, font=font, fill=(0,0,0), align='center')
        self.img = im        
    
    #Save img
    def saveImg(self):
        # # # Save the image
        self.img.save("./outputs/img/output.png")