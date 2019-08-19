from PIL import Image
import os

for pic in os.listdir('origin'):
	#print(pic)
	if pic.endswith('.jpg'):
		image_file = Image.open(os.path.join('origin',pic))
		image_file = image_file.convert('L')
		image_file = image_file.save(os.path.join('output',pic[:-4]+'_G.jpg'))
