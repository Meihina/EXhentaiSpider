from random import *

head_arr = [  #请求头
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
]

def random_head() :
    head_roll = choice(head_arr)
    head = {'User-Agent':head_roll}
    return head