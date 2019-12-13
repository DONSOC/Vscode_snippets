import json

# input as a list

filename = "It's_a_snippet"
fullname = filename + ".code-snippets"
snippetname = "snippetname"
prefix = "prefix"
body = "body"


snippet = { snippetname: { "prefix": prefix, "body": [ body ] } }


with open(fullname, "w") as f: # write snippet to file
    json.dump(snippet, f, indent=4)
    f.close()
