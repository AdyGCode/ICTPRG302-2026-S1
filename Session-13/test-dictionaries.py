ingredients = {
    'cinnamon': {'amount':3,'unit':'tsp'},
    'sugar': {'amount':3,'unit':'tbsp'},
}

use_get_method = ingredients.get('cinnamon')
use_array_index = ingredients['cinnamon']

print (use_array_index)
print (use_get_method)
