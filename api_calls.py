import json, flickrapi, csv
from urllib import urlretrieve

api_key = u'e70e36089197fa4ad763fb6f779fbf5b'
api_secret = u'844e2f498155f238'

flickr = flickrapi.FlickrAPI(api_key, api_secret)


def get_id_list(group_id):
	response = json.loads(flickr.groups.pools.getPhotos(group_id=group_id, format='json'))

	pages = response['photos']['pages']
	print 'Pages founded: ' + str(pages)
	ids = list()

	for page in range(2, pages):
		list_of_images = response['photos']['photo']

		for image in list_of_images:
			ids.append(image['id'])

		response = json.loads(flickr.groups.pools.getPhotos(group_id=group_id, format='json', page=str(page)))

	print "Download of " + str(len(ids)) + " images."
	return ids


def save_images_from_group(group_id, path, quality):
	id_list = get_id_list(group_id)

	for i, image_id in enumerate(id_list):
		save_image(image_id, path + "/img" + str(i) + ".jpg", quality)


def save_images_from_id_list(file, path, quality):
	file = open(file, 'r')
	reader = csv.reader(file)
	for row in reader:
		path_name = path + row[0].strip() + ".jpg"
		save_image(row[0].strip(), path_name, quality)
		#print(path_name, "saved")


def save_image(image_id, path_name, quality):
	urls = get_image_url(image_id)
	if len(urls) > 0:
		url = urls[quality]  # Seleciona o tamanho da imagem
		urlretrieve(url, path_name)
		print('Saved:', image_id)
	else:
		print('Not saved:', image_id)


def get_image_url(image_id):
	image = json.loads(flickr.photos.getSizes(photo_id=image_id, format='json'))
	urls = list()

	if image['stat'] == 'ok':
		for line in image['sizes']['size']:
			urls.append(line["source"])

	return urls
