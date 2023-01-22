from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    return list(set([_uid['from_id'] for _uid in data['messages'] if _uid['type'] == "message"]))

data = read_data('data/result.json')
if __name__ == '__main__':
    print(find_all_users_id(data))