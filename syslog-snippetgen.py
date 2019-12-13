import json

# input as a list

def create_snippet_entry(snippetname, prefix, body):
    return { snippetname: { "prefix": prefix, "body": [ body ] } }

filename = "It_s_a_snippet"
fullname = filename + ".code-snippets"
options = [
    ("destination", "kafka-c", "bootstrap-servers", ["<string>"]),
    ("destination", "kafka-c", "client-lib-dir", ["<string>"]),
    ("destination", "kafka-c", "flush-timeout-on-reload", ["<number>"]),
    ("destination", "kafka-c", "flush-timeout-on-shutdown", ["<number>"])
]

def create_snippet_entries():
    entries = []
    for context, driver, keyword, arguments in options:
        # Refine these, build up the body in the correct way, add the hint for all the other options etc...
        # See https://github.com/DONSOC/Vscode_snippets/blob/master/kafka.code-snippets#L49
        snippetname = keyword.replace("-", "")
        prefix = context + "-" + driver + "::" + keyword
        body = keyword + "(" + " ".join(arguments) + ")"
        entries.append(create_snippet_entry(snippetname, prefix, body))
    return entries

with open(fullname, "w") as f: # write snippet to file
    json.dump(create_snippet_entries(), f, indent=4)
    f.close()
