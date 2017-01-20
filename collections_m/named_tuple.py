# tuple with named fields :) namedtuple() returns a subclass of a tuple, with
# named fields.

from collections import namedtuple 


partsz = namedtuple('parts', 'id_num desc cost amount')
auto_parts = partsz(id_num='1234', desc='Ford', cost=1200, amount=10)
# print(dir(parts))

print(partsz)

print(auto_parts.id_num)

# my_tuple = ('1234', 'ford', 1200, 10)
# print(my_tuple)
# print(my_tuple[0])

# var_a, var_b, var_c, var_d = my_tuple

# print(var_a, var_b, var_c, var_d)

# print(dir(my_tuple))
# print(my_tuple.__repr__())


my_keys_dict = {'id_num':'1234', 'desc':'ford'}
call_ntuple = namedtuple('shays_named_tuple',my_keys_dict.keys())


