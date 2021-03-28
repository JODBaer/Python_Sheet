l1 = [1, 4, 3, 2]       # Listen erstellen
l2 = ["Panda", "Po"]
l2.append("Fu")         # l2 = ['Panda', 'Po', 'Fu']
l1 = l1 + [5]           # l1 = [1, 4, 3, 2, 5]
l1.extend(l2)           # l1 = [1, 4, 3, 2, 5, 'Panda', 'Po', 'Fu']
l1.remove("Po")         # l1 = [1, 4, 3, 2, 5, 'Panda', 'Fu']
l1.insert(5, 6)         # l1 = [1, 4, 3, 2, 5, 6, 'Panda', 'Fu']
l3 = l1[0:6:1]          # l3 = [1, 4, 3, 2, 5, 6] l1[0] exklusive l1[6]
l3.sort(reverse=False)  # l3 = [1, 2, 3, 4, 5, 6]
l4 = l3[::2]            # l4 = [1, 3, 5] ; jedes zweite Element auswaehlen
