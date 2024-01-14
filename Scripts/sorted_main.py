black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"

semnad = []
vosem = []
gelb = []

import json
import subprocess
import os
from time import sleep

try:
    import plyer
except:
   os.system('pip install plyer')
   import plyer

def cls():
  try:
    subprocess.call("clear")
  except:
    subprocess.call("cls", shell=True)

cls()

print(f'┌{"-"*10} Sorting starting \n╎')



try:
  
  ee = '├ Module: one.py'
  try:
    import one
    ee = ee + f'\n╎ StatusModule: one.py - {green}OK{white}'
  except:
    ee = ee + f'\n╎ StatusModule: one.py - {red}Error{white}'
  try:
    from one import imgs as imgs_1
    ee = ee + f'\n╎ IMGS_1: {green}OK{white}'

    for url in imgs_1:
      if type(url) != dict:
        if 'gelbooru.com' in url:
          gelb.append(url)
        if url not in semnad:
            semnad.append(url)
  except ImportError:
    ee = ee + f'\n╎ IMGS_1: {red}ImportError{white}'

  try:
    from one import imgs18 as imgs18_1
    ee = ee + f'\n╎ Status: IMGS18_1  ─ {green}OK{white}'

    for url in imgs18_1:
      if type(url) != dict:
        if 'gelbooru.com' in url:
          gelb.append(url)
        if url not in vosem:
            vosem.append(url)
  except ImportError:
    ee = ee + f'\n╎ IMGS18_1: {red}ImportError{white}'
  print(ee)

except Exception:
  pass

try:
  ee = '╎\n├ Module: two.py'
  try:
    import two
    ee = ee + f'\n╎ StatusModule: two.py - {green}OK{white}'
  except ModuleNotFoundError:
    ee = ee + f'\n╎ StatusModule: two.py - {red}ModuleNotFoundError{white}'
  except ImportError:
    ee = ee + f'\n╎ StatusModule: two.py - {red}ImportError{white}'
  
  try:
    from two import imgs as imgs_2

    ee = ee + f'\n╎ Status: IMGS_2  ─ {green}OK{white}'
    
    for url in imgs_2:
      if type(url) != dict:
        if 'gelbooru.com' in url:
          gelb.append(url)

        if url not in semnad:
            semnad.append(url)
  except ImportError:
    ee = ee + f"\n╎ IMGS_2: {red}ImportError{white}"
    pass


  try:

    from two import imgs18 as imgs18_2
    ee = ee + f'\n╎ Status: IMGS18_2  ─ {green}OK{white}'

    for url in imgs18_2:
      if type(url) != dict:
        if 'gelbooru.com' in url:gelb.append(url)
        if url not in vosem:vosem.append(url)
  except ImportError:
    ee = ee + f'\n╎ IMGS18_2: {red}ImportError{white}'

    pass
  print(ee)
except Exception as err:
  print(err)


try:
  ee = '╎\n├ Module: tree.py'
  try:
    import tree
    ee = ee + f'\n╎ StatusModule: tree.py - {green}OK{white}'
  except:
    ee = ee + f'\n╎ StatusModule: tree.py - {red}Error{white}'

  try:
    from tree import imgs as imgs_3
    ee = ee + f'\n╎ Status: IMGS_3  ─ {green}OK{white}'
    for url in imgs_3:
      if type(url) != dict:
        if 'gelbooru.com' in url:gelb.append(url)
        if url not in semnad:semnad.append(url)
  except ImportError:
    ee = ee + f'\n╎ Status: IMGS_3  ─ {red}Error{white}'

    pass

  try:
    from tree import imgs18 as imgs18_3
    ee = ee + f'\n╎ Status: IMGS18_3  ─ {green}OK{white}'
    for url in imgs18_3:
      if type(url) != dict:
        if 'gelbooru.com' in url:gelb.append(url)
        if url not in vosem:vosem.append(url)

  except ImportError:
     ee = ee + f'\n╎ Status: IMGS18_3  ─ {red}Error{white}'
  print(ee)

except Exception:
  pass


try:
  ee = '╎\n├ Module: four.py'
  try:
    import four
    ee = ee + f'\n╎ StatusModule: four.py - {green}OK{white}'
  except:
    ee = ee + f'\n╎ StatusModule: four.py - {red}Error{white}'

  try:
    from four import imgs as imgs_4
    ee = ee + f'\n╎ Status: IMGS_4  ─ {green}OK{white}'
    for url in imgs_4:
      if type(url) != dict:
        if 'gelbooru.com' in url:gelb.append(url)
        if url not in semnad:semnad.append(url)
  except ImportError:
    ee = ee + f'\n╎ Status: IMGS_4  ─ {red}ImportError{white}'

    pass

  try:
    from four import imgs18 as imgs18_4
    ee = ee + f'\n╎ Status: IMGS18_4  ─ {green}OK{white}'
    for url in imgs18_4:
      if type(url) != dict:
        if 'gelbooru.com' in url:gelb.append(url)
        if url not in vosem:vosem.append(url)

  except ImportError:
     ee = ee + f'\n╎ Status: IMGS18_4  ─ {red}ImportError{white}'
  print(ee)

except Exception:
  pass




try:
  ee = '╎\n├ Module: five.py'
  try:
    import five
    ee = ee + f'\n╎ StatusModule: five.py - {green}OK{white}'
  except:
    ee = ee + f'\n╎ StatusModule: five.py - {red}Error{white}'

  try:
    from five import imgs as imgs_5
    ee = ee + f'\n╎ Status: IMGS_5  ─ {green}OK{white}'
    for url in imgs_5:
      if type(url) != dict:
        if 'gelbooru.com' in url:gelb.append(url)
        if url not in semnad:semnad.append(url)
  except ImportError:
    ee = ee + f'\n╎ Status: IMGS_5  ─ {red}Error{white}'
    pass

  try:
    from five import imgs18 as imgs18_5
    ee = ee + f'\n╎ Status: IMGS18_5  ─ {green}OK{white}'
    for url in imgs18_5:
      if type(url) != dict:
        if 'gelbooru.com' in url:gelb.append(url)
        if url not in vosem:vosem.append(url)
  except ImportError:
     ee = ee + f'\n╎ Status: IMGS18_5  ─ {red}Error{white}'
  print(ee)

except Exception:
  pass

print(f'╎\n├-{"-"*10} Sorting finished {"-"*10}')



semnad = list(sorted(set(semnad)))
vosem = list(sorted(set(vosem)))
gelb = list(sorted(set(gelb)))

print(f'╎ semnad = {len(semnad)}, vosem = {len(vosem)}, gelb = {len(gelb)}')

if len(semnad) != 0:
  with open("17.json", "w") as outfile:
    json.dump(semnad, outfile, indent=4)

if len(vosem) != 0:
  with open("18.json", "w") as outfile:
    json.dump(vosem, outfile, indent=4)

if len(gelb) != 0:
  with open("gelb.json", "w") as outfile:
    json.dump(gelb, outfile, indent=4)

plyer.notification.notify(title = f"{'Sorting finished'.upper()}",message="Sorting finished!" ,timeout=2)


sleep(15)