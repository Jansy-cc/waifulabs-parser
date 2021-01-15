print('Loading all modules...')
import os
from selenium import webdriver
import time
import urllib.request
import random

class mainUtils:
    def genString(length : int): return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for i in range(length))

    def clear():os.system('cls') if os.name == 'nt' else os.system('clear')

    def checkFolder(folderName):#if not folder in this dir -> create folder
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)) + f'\\{folderName}')):
            os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)) + f'\\{folderName}'))
    def windowSize(width : int = 100, height : int = 100): os.system(f'mode con: cols={width} lines={height}') if os.name == 'nt' else ''

    def windowTitle(title): os.system(f'title {str(title)}') if os.name == 'nt' else ''
class waifuParser:
    def __init__(self, driver):
        self.driver = driver

    def visitSite(self):
        self.driver.get('https://waifulabs.com/')
        time.sleep(5)
        self.driver.find_element_by_class_name('button-content').click()
        time.sleep(5)

    def imagesFromCache(self):
        self.images = [self.driver.find_element_by_css_selector(f'#root > div > div > div.container > div > div > div:nth-child({count}) > div > div > div:nth-child(2) > div').get_attribute('style').split(' url("')[1].replace('");', '').split(' ')[0] for count in range(1, 17)]
        return self.images

    def saveImages(self, pathSave = 'images/'):
        for image in self.images:
            urllib.request.urlretrieve(image, f'{pathSave}{mainUtils.genString(36)}.png')

mainUtils.clear()
mainUtils.windowSize(60, 20)
print('''
        ██╗    ██╗ █████╗ ██╗███████╗██╗   ██╗
        ██║    ██║██╔══██╗██║██╔════╝██║   ██║
        ██║ █╗ ██║███████║██║█████╗  ██║   ██║
        ██║███╗██║██╔══██║██║██╔══╝  ██║   ██║
        ╚███╔███╔╝██║  ██║██║██║     ╚██████╔╝
        ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝

        ██████╗  █████╗ ██████╗ ███████╗███████╗██████╗
        ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
        ██████╔╝███████║██████╔╝███████╗█████╗  ██████╔╝
        ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝  ██╔══██╗
        ██║     ██║  ██║██║  ██║███████║███████╗██║  ██║
        ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
        (Download all images for https://waifulabs.com/)
            Press enter to start parser
''')

input()
mainUtils.checkFolder('driver')
mainUtils.checkFolder('images')
try:
    driver = webdriver.Chrome(executable_path=r'{0}'.format(os.path.join(os.path.dirname(os.path.abspath(__file__)) + f'\\driver\\chromedriver.exe')))
except Exception as error:
    print(error)
    input()

count = 0
while True:
    mainUtils.clear()
    print(f'{count} images downloaded...')
    mainUtils.windowTitle(f'{count} images downloaded')

    waifu = waifuParser(driver)
    waifu.visitSite()
    images = waifu.imagesFromCache()
    waifu.saveImages('images/')

    count += len(images)
    
    
