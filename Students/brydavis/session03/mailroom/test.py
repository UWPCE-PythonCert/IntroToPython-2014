from donor_db import new_donor_list

donate_freq = []

def set_don_num():
	for k in new_donor_list.keys():
		# donate_freq.append(len(d))
		new_donor_list[k]['don_num'] = len(new_donor_list[k]['don_amount']) 
