# input as a list

filename = "It's_a_snippet"
fullname = filename + ".code-snippets"
snippetname = "snippetname"
prefix = "prefix"
body = "body"










# format the snippet to snippet filetype standards.
snippet = "\t\"" + snippetname +"\" :{\n "+\
"\t"*2 + "\"prefix\": \"" + prefix +"\",\n" +\
"\t"*2 + "\"body\": [\n\t\"" + body +"\",\n\t]\n\t},"

framed = "{\n"+ snippet + "\n}" # make the 2 main brackets

# print(framed) #control of output in console if needed

with open(fullname, "w") as f: # write snippet to file
    f.write(framed)
    f.close()
