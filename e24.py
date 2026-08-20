
def join(arr):
    s = ""
    for c in arr:
        s+=c
    return s

perms = []
for zero in range(10):
    options = [0,1,2,3,4,5,6,7,8,9]
    s = ['0','1','2','3','4','5','6','7','8','9']

    s[zero] = '0'
    options.remove(zero)
    for one in range(9):
        oneIndex = options[one]
        s[oneIndex] = '1'
        options.remove(oneIndex)

        for two in range(8):
            twoIndex = options[two]
            s[options[two]] = '2'
            options.remove(options[two])

            for three in range(7):
                threeIndex = options[three]
                s[options[three]] = '3'
                options.remove(options[three])

                for four in range(6):
                    fourIndex = options[four]
                    s[options[four]] = '4'
                    options.remove(options[four])

                    for five in range(5):
                        fiveIndex = options[five]
                        s[options[five]] = '5'
                        options.remove(options[five])

                        for six in range(4):
                            sixIndex = options[six]
                            s[options[six]] = '6'
                            options.remove(options[six])

                            for seven in range(3):
                                sevenIndex = options[seven]
                                s[options[seven]] = '7'
                                options.remove(options[seven])

                                for eight in range(2):
                                    eightIndex = options[eight]
                                    s[options[eight]] = '8'
                                    options.remove(options[eight])
                                    nineIndex = options[0]
                                    s[options[0]] = '9'
                                    perms.append(join(s))
                                    print(join(s))
                                    options.append(eightIndex)
                                    options.sort()
                                options.append(sevenIndex)
                                options.sort()
                            options.append(sixIndex)
                            options.sort()
                        options.append(fiveIndex)
                        options.sort()
                    options.append(fourIndex)
                    options.sort()
                options.append(threeIndex)
                options.sort()
            options.append(twoIndex)
            options.sort()
        options.append(oneIndex)
        options.sort()
    options.append(zero)
    options.sort()


perms.sort()
print(perms[1_000_000 - 1])