#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def search_element(e):
        return (e if e != search else replace)
    return list(map(search_element, my_list))
