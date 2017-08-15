from api_calls import *

#groups = [("580502@N21","FIRE_FIRE_FIRE"),
#          ("81994094@N00", "Forest_Fires"),
#          ("422461@N23", "Burned_Forests")]

groups = ("82643161@N00", "youtube/crops")

#save_images_from_group(groups[0][0], "images/" + groups[0][1], quality=-2)
#save_images_from_group(groups[1][0], "images/" + groups[1][1], quality=-2)
#save_images_from_group(groups[2][0], groups[2][1])
save_images_from_group(groups[0], groups[1], -2)

#save_images_from_id_list('images/FireIds/Flamesid.txt', "images/FireIds/fire/", -2)
#save_images_from_id_list('images/FireIds/notFlamesid.txt', "images/FireIds/not_fire/", -2)

