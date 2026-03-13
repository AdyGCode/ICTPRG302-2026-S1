# Fixing a broken keyboard
#
# Filename: broken_keyboard_1.py
# Author:   YOUR_NAME
 
# fixing: ## in place of an a
my_text = "B##n##n##"
fixed_text = my_text

while fixed_text.find("##") != -1:
    first_hash = fixed_text.find("##")
    fixed_text = fixed_text[:first_hash] + "a" + fixed_text[first_hash+2:]

while fixed_text.find("??") != -1:
    first_hash = fixed_text.find("??")
    fixed_text = fixed_text[:first_hash] + "u" + fixed_text[first_hash+2:]
     
print('Original: ', my_text)
print('Fixed   : ', fixed_text)
