class TrieNode:
    def __init__(self):
 

        self.key = None
        self.count = 0
        self.character = {}
 
#string in tree
def insert(head, s):
 
    curr = head
 
    for c in s:

        curr = curr.character.setdefault(c, TrieNode())
 
    curr.key = s
    curr.count += 1
 

def preorder(curr, key='', max_count=0):
 
    if curr is None:
        return key, max_count
 
    for (k, v) in curr.character.items():
 
        if max_count < v.count:
            key = v.key
            max_count = v.count
 
        key, max_count = preorder(v, key, max_count)
 
    return key, max_count
 
 
if __name__ == '__main__':
 
    words = [
        'code', 'coder', 'coding', 'codable', 'codec', 'codecs', 'coded',
        'codeless', 'codec', 'codecs', 'codependence', 'codex', 'codify',
        'codependents', 'codes', 'code', 'coder', 'codesign', 'codec',
        'codeveloper', 'codrive', 'codec', 'codecs', 'codiscovered'
    ]
 
    head = TrieNode()
    for word in words:
        insert(head, word)
 
    key, count = preorder(head)
 
    print('Word :', key)
    print('Count:', count)