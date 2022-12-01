#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    lists = dir(hidden_4)
    for list_ in lists:
        if list_[:2] != "__":
            print(list_)
