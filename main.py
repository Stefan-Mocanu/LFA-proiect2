with open("input.txt", "r") as f:
    trz = f.readline().strip().split()
    tranzitii = {x: {} for x in trz}
    alfabet = [x for x in f.readline().split()]
    for (i, j) in enumerate(alfabet):
        if j == 'lb':
            alfabet[i] = 'λ'
    initiala = f.readline().strip()
    finale = [x for x in f.readline().strip().split()]
    x = f.readline().split()
    while x:
        for (i, j) in enumerate(x):
            if j == 'lb':
                x[i] = 'λ'
        if x[2] in tranzitii[x[0]].keys():
            tranzitii[x[0]][x[2]].append(str(x[1]))
        else:
            tranzitii[x[0]][x[2]] = [str(x[1])]
        x = f.readline().split()
ok = 1
print(tranzitii)
for key, item in tranzitii.items():
    for key1, item1 in item.items():
        tranzitii[key][key1] = "+".join(tranzitii[key][key1])
    if initiala not in tranzitii[key].keys():
        ok = 0

if initiala in finale or not ok:
    tranzitii["new_initiala"] = {}
    tranzitii["new_initiala"][initiala] = "λ"
    initiala = "new_initiala"

if len(finale) == 1 and tranzitii[finale[0]] == {}:
    finale = finale[0]
else:
    tranzitii["new_finala"] = {}
    for x in finale:
        tranzitii[x]["new_finala"] = "λ"
    finale = "new_finala"

for key in tranzitii.keys():
    if key not in tranzitii[key].keys() and key != initiala and key != finale:
        tranzitii[key][key] = "λ"

for key in tranzitii.keys():
    for key1 in tranzitii.keys():
        if key1 not in tranzitii[key].keys():
            tranzitii[key][key1] = ""

keys = list(tranzitii)
for key in keys:
    if key in (initiala, finale):
        continue
    for key1 in tranzitii.keys():
        if key1 == key:
            continue
        for key2 in tranzitii.keys():
            if key2 == key:
                continue
            if tranzitii[key1][key] and tranzitii[key][key2]:
                strs = [tranzitii[key1][key2], tranzitii[key1][key], tranzitii[key][key], tranzitii[key][key2]]
                ok = False
                if strs[1] == "λ" and strs[2] == "λ" and strs[3] == "λ":
                    ok = True
                if strs[2] == "λ":
                    strs[2] = ""
                else:
                    if len(strs[2]) > 1:
                        strs[2] = "(" + strs[2] + ")*"
                    else:
                        strs[2] = strs[2] + "*"
                for i in range(len(strs)):
                    if i == 1:
                        if ok:
                            continue
                    if i != 2:
                        if strs[i] == "λ":
                            strs[i] = ""
                        elif i == 0 and strs[i]:
                            if strs[i][-1] == "*":
                                strs[i] = "(" + strs[i] + ")"
                            strs[i] += "+"
                        if "+" in strs[i] and i != 0:
                            strs[i] = "(" + strs[i] + ")"
                tranzitii[key1][key2] = "".join(strs)
    for key1 in tranzitii.keys():
        tranzitii[key1].pop(key)
    print(tranzitii)
    tranzitii.pop(key)
print(tranzitii[initiala][finale])
