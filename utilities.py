import getopt

# extract cmd arguments into a map
def extractArgs(argv: list) -> dict:
  argMap = {}
  opts, args = getopt.getopt(argv, "", ["alpha=", "beta=", "evp=", "q="])
  for opt, arg in opts:
    argMap[opt] = arg
  return argMap
