def rot13(s):
	print s
	from codecs import encode
	return s.encode('rot13')
  

if __name__ == '__main__':

    assert rot13('ZNTARGVP SEBZ BHGFVQR ARNE PBEARE') == 'MAGNETIC FROM OUTSIDE NEAR CORNER'
    print "All Tests Pass"

