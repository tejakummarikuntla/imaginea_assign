input_curr = [int(x) for x in input().split()]
notes_given = sorted(input_curr, reverse=True)
input_val = int(input("Enter The value: "))
#notes_given = [500, 100, 50, 20, 10, 1]
#notes_given = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
#notes_given = [2000, 500, 100, 50, 20, 10, 5, 2, 1]
for nt in notes_given:
    notes = input_val // nt
    if notes:
        input_val = input_val % nt
        print(notes,"*", nt, "=", notes*nt)
