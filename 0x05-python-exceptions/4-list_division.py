#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for p in range(list_length):
        try:
            result = my_list_1[p] / my_list_2[p]
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            div_list.append(result)
    return (div_list)
