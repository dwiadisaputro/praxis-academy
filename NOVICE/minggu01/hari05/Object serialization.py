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
# #Picle.dumps()
# import pickle

# data = [ {'a':'A', 'b':2, 'c':3.0}]
# data_string = pickle.dumps(data)
# print('PICKLE:', data_string)




##Python program to illustrate
##pickle.load()
# import pickle
# import io

# class SimpleObject(object):

#     def __init__(self, name):
#         self.name = name
#         l = list(name)
#         l.reverse()
#         self.name_backwards = ''.join(l)

# data = []
# data.append(SimpleObject('pickle'))
# data.append(SimpleObject('cPickle'))
# data.append(SimpleObject('lest'))

# # ##Simulate a file with StringIO
# out_s = io.StringIO()

# # ##Write to the stream
# for o in data:
#     print ('WRITING: %s (%s)' % (o.name, o.name_backwards))
    # print(pickle.dump(o, out_s))
    # print(out_s.flush())

# ##Set up a read-able stream
# in_s = io.StringIo(out_s.getvalue())

# ##Read the data
# while True:
#     try:
#         o = pickle.load(in_s)
#     except EOFError:
#         break
#     else:
#         print ('READ: %s (%s)' % (o.name, o.name_backwards))




###Python program to illustrate
###pickle.loads()
# import pickle
# import pprint

# data1 = [ { 'a':'A', 'b':2, 'c':3.0} ]
# print ('BEFORE:',)
# pprint.pprint(data1)

# data1_string = pickle.dumps(data1)

# data2 = pickle.loads(data1_string)
# print ('AFTER:',)
# pprint.pprint(data2)

# print ('SAME?:', (data1 is data2))
# print ('EQUAL?:', (data1 == data2))



# import pickle

# class TextReader:
#     """Print and number lines in a text file"""

#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename)
#         self.lineno = 0

#     def readline(self):
#         self.lineno + 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#         return "%i: %s" % (self.lineno, line)

#     def __getstate__(self):
#         # Copy the object's state from self.__dict__ which contains
#         # all our instance attributes. Always use the dict.copy()
#         # method to avoid modifying the original state.
#         state = self.__dict__.copy()
#         # Remove the unpicklable entries.
#         del state['file']
#         return state

#     def __setstate__(self, state):
#         #Restore instance attributes (i.e., filename and lineno).
#         self.__dict__.update(state)
#         #Restore the previously opened file's state. To do so, we need to
#         # reopen it and read from it until the line count is restored.
#         file = open(self.filename)
#         for _ in range(self.lineno):
#             file.readline()
#         #finnally, save the file.
#         self.file = file

# reader = TextReader("Geeksforgeeks.txt")
# print(reader.readline())
# print(reader.readline())
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.readline())