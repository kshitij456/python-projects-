# Extract digit string from a given string

test_string = "hfhsh63GGJHJYUUYYufhjfljufji7376nfjfhuijf9rmfie894mf8GGFHDdopokPOfhjfTFYHUYTYGVHGYTYTriu438FHGHF475834ut834t"
print("The original string: " + test_string)

res = ''.join(filter(lambda i: i.isdigit(), test_string))
rev = ''.join(filter(lambda i: i.isupper(), test_string))
reu = ''.join(filter(lambda i: i.islower(), test_string))
print("The digit string: " + str(res))
print("The upper alphabet string: " + str(rev))
print("The lower alphabet string: " + str(reu))

