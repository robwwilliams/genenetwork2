from __future__ import print_function, division

import operator

import simplejson as json

#import xlwt
from pprint import pformat as pf

def export_sample_table(targs):
    #print("* keys0 args is:", targs[0].keys())
    
    
    #test_export_file = open("/home/zas1024/gene/wqflask/wqflask/show_trait/export_test.txt", "w")
    #
    #for key, item in targs.iteritems():
    #    print("[arrow] key is:", key)
    
    sample_data = json.loads(targs['export_data'])
    final_sample_data = []
    
    for sample_group in ['primary_samples', 'other_samples']:
        for row in sample_data[sample_group]:
            sorted_row = dict_to_sorted_list(row)
            print("sorted_row is:", pf(sorted_row))
            final_sample_data.append(sorted_row)
            
    return final_sample_data
     
def dict_to_sorted_list(dictionary):
    sorted_list = [item for item in dictionary.iteritems()]
    sorted_list = sorted(sorted_list, key=operator.itemgetter(0))
    sorted_values = [item[1] for item in sorted_list]
    return sorted_values    