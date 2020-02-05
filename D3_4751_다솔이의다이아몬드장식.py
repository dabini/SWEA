T = int(input())

for t in range(T):
    word = input()
    res = ''
    print("..#."*len(word)+".")
    print(".#.#"*len(word)+".")
    for i in range(len(word)):
        res += "#.{}.".format(word[i])
    print(res + "#")
    print(".#.#" * len(word) + ".")
    print("..#." * len(word) + ".")