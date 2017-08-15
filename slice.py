import image_slicer
import os

def slice_image(local_path,image_name,tiles_path):
	try:
		tiles = image_slicer.slice(image_name, 4)
		for t in tiles:
			tname = str(t)[11:][:-1]
			try:
				os.rename(tname, local_path + "/" + tiles_path + "/" + tname)
			except:
				print("Falha ao mover. "+tname)
				os.remove(tname)
	except:
		print("Falha ao fazer a divisão. "+image_name)

def slice_dirctory_image(image_path):
	image_names = os.listdir(image_path)
	tiles_path = image_path + "_sliced"

	if not os.path.exists(tiles_path):
		os.makedirs(tiles_path)

	local_path = os.getcwd()
	os.chdir(image_path)
	
	for image in image_names:
		slice_image(local_path,image,tiles_path)

	os.chdir(local_path)


#slice_dirctory_image("youtube/fire")
#slice_dirctory_image("youtube/not_fire")
slice_dirctory_image("youtube/crops")