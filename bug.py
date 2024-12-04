def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some code that might raise an exception ...
    # f.close()  # Missing file closure
    return

function_with_unclosed_file("myFile.txt")