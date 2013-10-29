#!/usr/bin/python
import math
#生成Pi，保留指定小数位。
n = int( raw_input('How long? ') )
print( '{0:.%df}' % min(20,n) ).format( 4 * math.atan(1.) )
