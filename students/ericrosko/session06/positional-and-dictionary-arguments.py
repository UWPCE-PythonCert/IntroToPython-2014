'''
Nov. 10, 2015
In-class lab for session 6

Description:
	This shows how passing or using a positional or dictionary argument objects will expand to fill
	the necessary placeholders in a string.
'''

def foo(fore_color="Black", back_color="White", link_color="Blue", visited_color="Purple"):
	print("fore_color={}, back_color={}, link_color={}, visited_color={}".format(fore_color,back_color,link_color,visited_color))

def foo2(*pos):
	print("fore_color={}, back_color={}, link_color={}, visited_color={}".format(*pos))


def main():
	foo()

	pos=("Green","Red","Pink","Brown")
	foo(*pos)
	foo2(*pos)

	color_dict={"link_color":"Yellow"}
	foo (**color_dict)

	color_dict={"link_color":"Cyan", "fore_color":"Gray"}
	foo (**color_dict)

	color_dict={"link_color":"Cyan", "fore_color":"Gray", "visited_color":"aquamarine", "back_color":"chartreuse"}
	foo (**color_dict)

main()