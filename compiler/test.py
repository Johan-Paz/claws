# @Author: japaz
import yaml
from os import path
import story

__author__ = 'japaz'

story_file = path.join(path.dirname(__file__),"..","stories","tests.sto")
with open(story_file) as story_desc:
    sto = story.compile(story_desc)
    print sto
    print yaml.dump(sto,allow_unicode=True)