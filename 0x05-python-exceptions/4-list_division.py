#!/usr/bin/python3
# Write a function that divides element by element 2 lists.
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(0, list_length):
        try:
            new.append(my_list_1[i] / my_list_2[i])
        except ValueError:
            print("wrong type")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except Exception:
            new.append(0)
    return new
