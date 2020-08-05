import pickle
import datetime
import io
from io import BytesIO

my_object = {'kv1': 'keyvalue1', 'kv2': 2, 'kv3': [(1, 2), (3, 4)], 'kv4': {'kv5': [7.0, 8.0, 9.0], 'kv6': datetime.datetime(2020, 7, 8, 13, 4, 40, 178976)}, '_args': (True, False, 'Test')}

import pickle
f = BytesIO()
pickler = pickle.Pickler(f)
pickler.dump({"a".encode("utf-8"): str(1).encode("utf-8"), "b".encode("utf-8"): str(2).encode("utf-8")})
# assume bytes_io is a `BytesIO` object

wrapper = io.TextIOWrapper(f, encoding='utf-8')
# Read from the buffer
print(wrapper.read())
print(f.getvalue().decode('utf-8', errors="ignore"))
f.close()

# unpickler = pickle.Unpickler(open("sample.pkl"))
# print unpickler.load()