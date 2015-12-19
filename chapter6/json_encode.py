def json_encode(data):
    if isinstance(data, bool):
       if data:
          return "true"
       else:
          return "false"
    elif isinstance(data, (int, float)):
       return str(data)
    elif isinstance(data, str):
       return '"' + escape_string(data) + '"'
    elif isinstance(data, list):
       return "[" + ",".join(json_encode(d) for d in data) + "]"
    elif isinstance(data, dict):
        return "{" + ", ".join(json_encode(x) + ":" + json_encode(y) for x,y in
                data.items()) + "}"
    else:
       raise TypeError("%s is not JSON serializable"% repr(data))
def escape_string(s):
    """Escapes double-quote,
    tab new line characters
    in a string."""
    s = s.replace('"','\\"')
    s = s.replace("\t","\\t")
    s = s.replace("\n","\\n")
    return s
print json_encode({1:'one', 2:'two'})
