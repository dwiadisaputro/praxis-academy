###---Output Formatting
# import reprlib
# print(reprlib.repr(set('supercalifragilisticexpialidocious')))

# import pprint
# t = [[[['black', 'cyan'], 'white',['green', 'red']],[['magenta', 'yellow'], 'blue']]]
# pprint.pprint(t, width=30)

# import textwrap
# doc = """The wrap() method is just like fill() except that it returns
# a list of strings instead of one big string with newlines to separate
# the wrapped lines."""

# print(textwrap.fill(doc, width=40))


##blm ketemu
# import locale
# locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# print(conv = locale.localeconv())
# print(locale.format("%s%.*f", (conv['currency_symbol'],
# conv['frac_digits'], x), grouping=True))

###---Templating
from string import Template
t = Template('${village}folk send $$10 to $cause')
print(t.substitute(village='Nottingham', cause='the ditch fund'))