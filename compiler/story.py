import yaml

__author__ = 'japaz'

def process_head(head=None):
    if head:
        return None,head
    else:
        return None,None



def compile(file=None):
    result = []
    if file:
        source = file.read()
        story = yaml.load(source)
        for head in story:
            type,identifier = process_head(head)
            print type,identifier
        return story

    return result
