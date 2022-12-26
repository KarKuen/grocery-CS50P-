grocery = {}
def main():
    while True:
        try:
            items = input().upper()
            list(items)
        except EOFError:
            print()
            break
    for i in sorted(grocery.keys()):
        print(grocery[i], i)

def list(items):
    if items in grocery:
        grocery[items] += 1
    else:
        grocery[items] = 1

main()