###--pickle.dump(obj, file, protocol = None, *, fix_imports = True)
# import pickle
# import io

# class SimpleObject(object):

#     def __init__(self, name):
#         self.name = name
#         l = list(name)
#         l.reverse()
#         self.name_backwards = ''.join(l)
#         return

# data = []
# print(data.append(SimpleObject('pickle')))
# print(data.append(SimpleObject('cPickle')))
# print(data.append(SimpleObject('last')))

# ##Simulate a file with StringIO
# # print(out_s = io.StringIO())

# ##Write to the stream
# for o in data:
#     print ('WRITING: %s (%s)' % (o.name, o.name_backwards))
#     pickle.dump(o, out_s)
#     out_s.flush()


## Python program to illustrate
##Picle.dumps()
# import pickle

# data = [ {'a':'A', 'b':2, 'c':3.0}]
# data_string = pickle.dumps(data)
# print('PICKLE:', data_string)

##