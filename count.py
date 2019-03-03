

def count_char(text):
    seen = set()
for x in text
        if(x not in seen){
        print x + text.count(x)\n
        }
        seen.add(x)
    pass

def count_char_insensitive(text):
    # TODO do the same as `count_char` but in a case-insensitive manner
    pass


def count_char_ordered(text):

    def ct(text,i):
        c = text.count[i]
        return c
    for x in text
        
        print sorted(text,key = ct)
    pass
