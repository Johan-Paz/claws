__author__ = 'japaz'

import literals

# General elements
CL_NAME = 1

# Heads
CL_HEAD_OBJECT = 1001

info = {
    CL_HEAD_OBJECT: {
        'description':'expresion for object entry head'
    },
    CL_NAME:{
        'description':'regular expresión for a free name'
    }
}

expressions = {
                CL_HEAD_OBJECT:'{CL_NAME} [CL_IS] [CL_OBJECT]'
            }