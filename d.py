import re
def a(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'match!'
        else:
                return('Not matched!')


import re
def a(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'match!'
        else:
                return('Not matched!')
        

import re
def a(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'match!'
        else:
                return('Not matched!')
        


import re
def a(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'match!'
        else:
                return('Not matched!')


import re
def a(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'match!'
        else:
                return('Not matched!')
        

import re
text = input()
print(re.sub("[ ,.]", ":", text))


def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))
a = input()
print(snake_to_camel(a))


import re
text = input()
print(re.findall('[A-Z][^A-Z]*', text))

import re
def capital(str1):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)


def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

