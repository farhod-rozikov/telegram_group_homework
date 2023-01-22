from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    u_msg = [msg['text'] for msg in data['messages'] if msg['type'] == "message" and msg['from_id'] == users_id]
    return len(u_msg)

data = read_data('data/result.json')
any_id = find_all_users_id(data)[5]
if __name__ == '__main__':
    print(find_user_message_count(data, any_id))