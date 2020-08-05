import pickle
import datetime

my_object = {'kv1': 'keyvalue1', 'kv2': 2, 'kv3': [(1, 2), (3, 4)], 'kv4': {'kv5': [7.0, 8.0, 9.0], 'kv6': datetime.datetime(2020, 7, 8, 13, 4, 40, 178976)}, '_args': (True, False, 'Test')}


my_pickled_object = pickle.dumps(my_object)  # Pickling the object
print(f"This is my pickled object:\n{my_pickled_object}\n")

my_unpickled_object = pickle.loads(my_pickled_object)  # Unpickling the object
print(f"This is a_dict of the unpickled object:\n{my_unpickled_object}\n")