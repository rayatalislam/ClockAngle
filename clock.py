def clock():
    hour = int(input("Enter Hour: "))
    min = int(input("Enter Minute"))

    res = abs((hour*60)-(min*11))
    res2 = abs(res/2)

    result = abs(res2)
    result2 = abs(res2-360)

    print(f"The angles are **{result}°** & **{result2}°**")

    veri = abs(result + result2)
    if veri == 360:
        print(f"result verified. Cuz the sum is {veri}")
    else:
        print(f"Duhh!! It throwed some error {veri} ")

clock()


