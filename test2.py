from selenium import webdriver
import time
from selenium import *
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\driver\chromedriver.exe")



def get_ammo(calibre):
    driver.get("https://escapefromtarkov.gamepedia.com/Ballistics")
    table = driver.find_elements_by_class_name("wikitable.sortable.jquery-tablesorter")[1].find_element_by_tag_name(
        "tbody")
    bullet_prams = table.find_elements_by_tag_name("tr")

    bullet_dict = []
    bullet_list = []

    for i in bullet_prams:
        if len(i.find_elements_by_tag_name("td")) == 16 and i.find_element_by_tag_name("a").text == calibre:
            bullet_list.append(i)
        elif len(bullet_list) == 0:
            continue
        elif len(i.find_elements_by_tag_name("td")) == 15:
            bullet_list.append(i)
        else:
            break

    for i in bullet_list:
        par_list = i.find_elements_by_tag_name('td')
        if len(par_list) == 16:
            del par_list[0]
            
        bullet_dict.append({'Name': par_list[0].text, 'Damage': par_list[1].text, 'Penetration power': par_list[2].text, 'Armor damage': par_list[3].text, "Accuracy": par_list[4].text, "Recoil": par_list[5].text, "Frag.": par_list[6].text, '1': par_list[9].text, '2': par_list[10].text, '3': par_list[11].text, '4': par_list[12].text, '5': par_list[13].text, '6': par_list[14].text})

    return bullet_dict

for i in get_ammo("23x75mm"):
    print(i)