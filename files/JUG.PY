def jug():
    jug1 = 0 
    jug2 = 0

    jug1_capacity = 4
    jug2_capacity = 3
    
    while jug1 != 2:
        print("jug1:", jug1, "jug2:", jug2)
        if jug1 == 0:
            jug1 = jug1_capacity
        elif jug2 == 0 or jug1 == jug1_capacity:
            transfer = min(jug1, jug2_capacity - jug2)
            jug1 -= transfer
            jug2 += transfer
        elif jug2 == jug2_capacity:
            jug2 = 0
            print("emptied jug 2")
    print("jug1:", jug1, "jug2:", jug2)
    
jug()