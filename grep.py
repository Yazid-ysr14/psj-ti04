import sys 
script = sys.argv[0]

def print_usage():
  sys.exit(f'Usage: python {script} pattern [FILE]')
def main(argv):

  if len(argv) < 1:
    print_usage()
    
   pattern = argv[0]
   lines = sys.stdin
   if len(argv) > 1:
    try:
      lines = open(argv[1])
    except:
      sys.exit("FILE NOT FOUND")
    for line in lines:
      if pattern in line:
        print(line.strip())
if_name_ == '_main_':
    main(sys.argv[1:])