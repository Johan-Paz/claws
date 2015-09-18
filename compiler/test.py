# @Author: japaz
import yaml
from os import path

__author__ = 'japaz'

story_file = path.join(path.dirname(__file__),"..","stories","tests.sto")
with open(story_file) as story_desc:
    story_source = story_desc.read()
    story = yaml.load(story_source)
    print story
    print yaml.dump(story,allow_unicode=True)