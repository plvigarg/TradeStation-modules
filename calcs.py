import pickle
import operator

from sentiment import get_predictions

get_predictions()
pickle_file = open("dictionary.pkl", "rb")
objects = pickle.load(pickle_file)
pickle_file.close()
print(type(objects))
sorted_d = dict(
    sorted(objects.items(), key=operator.itemgetter(1), reverse=True))

for obj in sorted_d:
    print(obj, '---->', sorted_d[obj])
