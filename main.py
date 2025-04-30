from PIL import Image
from rembg import remove

#####################Start Code########################

#input Image
input_img = "media/input_img.png"

#Open Image
input_img_open = Image.open(input_img)

#BgRemove -> Output
output_img = remove(input_img_open)

#Save In Png
output_img.save("media/output_img.png")

print(f"Image saved to media/output_img.png")
