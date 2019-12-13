import json

# input as a list

def create_snippet_entry(snippetname, prefix, body):
    return { snippetname: { "prefix": prefix, "body": [ body ] } }

filename = "It_s_a_snippet"
fullname = filename + ".code-snippets"
snippetname = "snippetname"
prefix = "prefix"
body = "body"

snippet = create_snippet_entry(snippetname, prefix, body)

with open(fullname, "w") as f: # write snippet to file
    json.dump(snippet, f, indent=4)
    f.close()
