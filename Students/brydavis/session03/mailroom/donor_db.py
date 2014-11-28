#!/usr/bin/env python

donor_list = {
	'Dummy Smith': [100,200,499],
	'Michael Something': [175,325,1000],
	'Diane Unknown': [550,275,850,1500],
	'Dude McGee': [900,100],
	'Stacy WhoMe': [350],
}


new_donor_list = {
	'Diane Unknown': {
		'don_num': 4,
		'don_amount': [550, 275, 850, 1500]
		},
	'Dude McGee': {
		'don_num': 2,
		'don_amount': [900, 100]
		},
	'Dummy Smith': {
		'don_num': 3,
		'don_amount': [100, 200, 499]
		},
	'Michael Something': {
		'don_num': 3,
		'don_amount': [175, 325, 1000]
		},
	'Stacy WhoMe': {
		'don_num': 3,
		'don_amount': [897, 453, 543]
		}
	}