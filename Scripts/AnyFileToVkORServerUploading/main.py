import os
import json
import time
from modules.random_neko_list import imgs, imgs18
from py_upload import upload_to_server
from vk_upload import vk_uploader
from downloader import DDF

w_dir = os.getcwd()
with open('data.json', "r+") as f:data = json.load(f)


print(f'''
Count Imgs: {len(imgs)}
Count Imgs18: {len(imgs18)}
''')

VK_folder    = 'VK_'
Other_folder = 'PY_'


append_ = []
not_append_ = []

access_image_list = ['jpg', 'png', 'jpeg']
block__image_list = ['mp4', 'gif', 'webm']
NewVKLinks = []

o = 0
print(f'''┌{"―"*15} Start:''')
try:
    for link in imgs:
        
        if type(link) == dict:pass
        else:
            if link not in ['imgs', 'imgs18']:

                if str(link.split('/')[2]) not in  ['i.pinimg.com','i.pximg.net']:
                    if 'https://sun' not in str(link):
                        # print(str(link.split('/')[2]))

                        if list(link.split('.'))[-1] in access_image_list:
                            if not os.path.exists(VK_folder):
                                os.mkdir(VK_folder)
                            os.chdir(VK_folder)
                            name_file = DDF(link, o)
                            per_link = link
                            
                            os.chdir(w_dir)
                            link = vk_uploader(name_file, VK_folder) 
                            NewVKLinks.append(link)
                            
                            print(f'''
├{"―"*10} NEXT LINK:
┊ Pervious LINK: {per_link}
┊ VK link: {link}
''')

                        elif list(link.split('.'))[-1] in block__image_list:
                            if not os.path.exists(Other_folder):os.mkdir(Other_folder)
                            os.chdir(Other_folder)
                            name_file = DDF(link, o)
                            # print(os.getcwd())
                            
                            upload_to_server(name_file)
                            print(f'''
├{"―"*10} NEXT LINK:
┊ Pervious LINK: {per_link}
┊ UPLOADED TO SERVER
''')
                        o = o + 1
                        os.chdir(w_dir)
                    else:
                        NewVKLinks.append(link)
                        pass
            
            
            if 'imgs' == link: append_.append(link)
            if 'imgs18' == link: append_.append(link)
        
        time.sleep(10)
except:
    with open("NewVKLinks.json", "w") as outfile:json.dump(NewVKLinks, outfile, indent=4)

        
print(f'''└{"―"*15}''')


with open("NewVKLinks.json", "w") as outfile:json.dump(NewVKLinks, outfile, indent=4)