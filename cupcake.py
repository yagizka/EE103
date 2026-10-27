total = 28
found = False   # çözüm bulundu mu?

for david in range(0, total + 1):
    for emma in range(0, total + 1):
        for frank in range(0, total + 1):
            if emma == david + 3 and frank == 3 * david and david + emma + frank == total:
                print("David packed", david, "cupcakes!")
                print("Emma packed", emma, "cupcakes!")
                print("Frank packed", frank, "cupcakes!")
                found = True
                break          # frank döngüsünden çık
        if found:
            break              # emma döngüsünden çık
    if found:
        break                  # david döngüsünden çık
            