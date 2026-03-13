# Fixing a broken keyboard
#
# Filename: broken_keyboard_1.py
# Author:   YOUR_NAME
 
# fixing: ## in place of an a

my_original_text = "B##n##n##"

def fix_keyboard(the_text, find_this, replace_with):
    while the_text.find(find_this) != -1:
        position = the_text.find(find_this)
        the_text = the_text[:position] + "a" + the_text[position+2:]
    return the_text


correct_text = fix_keyboard(my_original_text,"==","u")
correct_text = fix_keyboard(correct_text,"###","i")
correct_text = fix_keyboard(correct_text,"##","a")
correct_text = fix_keyboard(correct_text,"???","e")
correct_text = fix_keyboard(correct_text,"??","u")

print('Original: ', my_original_text)
print('Fixed   : ', correct_text)
