

def showOptions(**arg_dict):
    print 'List of available {name}: '.format(**arg_dict)
    o_list = arg_dict.get('o_list')
    
    for i, sid in enumerate(o_list):
        kwargs = {'i': i, 'sid': sid}
        print '{i: >2}. {sid: >10}'.format(**kwargs)


two_dict = {'name': 'methods', 
            'o_list': ['Method A', 'Method B', 'Method C']}


showOptions(**two_dict)

%matplotlib
p_test.plot_dict
import matplotlib.pyplot as plt
fig = plt.figure()
ax1=fig.add_subplot(1,1,1)
data=p_test.plot_dict['y_value']
ax1.bar((1,2), data_n, 0.35)
fig.canvas.draw()
%hist