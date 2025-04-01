def water_jug():
    jug1_capacity = 4  
    jug2_capacity = 3  
    jug1, jug2 = 0, 0  
    target = (2, 0)  

    print(f"Jug1: {jug1_capacity} gallons, Jug2: {jug2_capacity} gallons\n")

    while (jug1, jug2) != target:
        if jug2 == 0:
            jug2 = 3
            print("Jug2 Filled →", f"({jug1}, {jug2})")

        elif jug1 < 4:
            pour_amount = min(jug2, 4 - jug1)
            jug1 += pour_amount
            jug2 -= pour_amount
            print("Jug2 Poured into Jug1 →", f"({jug1}, {jug2})")

        elif jug1 == 4:
            jug1 = 0
            print("Jug1 Emptied →", f"({jug1}, {jug2})")

    print(f"\nGoal state reached: ({jug1}, {jug2})")

water_jug()
