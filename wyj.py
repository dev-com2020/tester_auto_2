def multi(a, b):
    count = 0
    try:
        suma = int(a) * int(b)
    except (TypeError, ValueError):
        count += 1
    else:
        return suma
    finally:
        print(count)


def multi2(a, b):
    return int(a) * int(b)

print(multi("a","b"))
print(multi(5,5))



try:
    multi2("a","b")
except TypeError:
    print("Błąd typu!")
except ValueError:
    print("Błąd wartości!")