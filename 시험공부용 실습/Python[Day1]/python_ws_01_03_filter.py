def Adult(list):
    adult_list = [dict for dict in list if dict['age'] >= 18]
    print(adult_list)

def Is_active(list):
    is_active_list = [dict for dict in list if dict['is_active'] == True]
    print(is_active_list)

def Adult_and_Is_active(list):
    adult_and_is_active_list = [dict for dict in list if dict['age'] >= 18 and dict['is_active'] == True]
    print(adult_and_is_active_list)
