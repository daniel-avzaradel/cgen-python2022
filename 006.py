# Sets
## unordered collection

ob  = set('abcdefg')
print(ob)

basket_one = {'a', 'b', 'c'}
basket_two = {'a', 'd', 'g'}

print('a' in basket_one)          # checking the membership
print(basket_one - basket_two)    # difference between two sets
print(basket_one | basket_two)    # union of two sets
print(basket_one & basket_two)    # intersection between two sets
print(basket_one ^ basket_two)    # difference between two sets
print(set('bcd') < basket_one)    # subset of another set
print(set('abcde') > basket_one)  # superset of another set

x = {'dave','mike','jane'}        #creating new set
x.add('ron')                      #insert a new item
x.update({'shimrit','sandra'})    #merge with other set
x.remove('dave')                  #remove item

print(x)