

def showOptions(**arg_dict):
    print 'List of available {name}: '.format(**arg_dict)
    o_list = arg_dict.get('o_list')
    
    for i, sid in enumerate(o_list):
        kwargs = {'i': i, 'sid': sid}
        print '{i: >2}. {sid: >10}'.format(**kwargs)


two_dict = {'name': 'methods', 
            'o_list': ['Method A', 'Method B', 'Method C']}


showOptions(**two_dict)