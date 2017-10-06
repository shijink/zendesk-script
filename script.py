creds = {
    'email' : 'k.shijin95@gmail.com',
    'token' : '9KtDcFzd1lWBfURpeG0NXU9mjSZp7JLCYLcZ3afG',
    'subdomain': 'test3015'
}


# Import the Zenpy Class
from zenpy import Zenpy


def remove_tags(tickets=[], tags_to_remove=[], creds={}):
    """Function to remove tags from zendesk ticket
    Args:
        param1 (list): List of tickets.
        param2 (list): List of tags to remove.
        param3 (dict): Credentials to access the zendesk.

    Returns:
        list: List of ticket ids that has updated
    """
    zenpy_client = Zenpy(**creds)
    changed_tickets = []
    for ticket in zenpy_client.tickets():
        # checking ticket id is in specified list if list is empty checking all tickets in zendesk
        if not tickets or ticket.id in tickets:
            common_tags = list(set(tags_to_remove).intersection(ticket.tags))
            if common_tags:
                zenpy_client.tickets.delete_tags(ticket.id, common_tags)
                changed_tickets.append(ticket.id)
                print('removed ', common_tags, ' from ', ticket)
    return changed_tickets


if __name__ == '__main__':
    tickets = []
    tags = ["comment:threshold:exceeded", "comment:threshold:exceeded:2",
            "comment:threshold:exceeded:3", "comment:threshold:exceeded:alert1",
            "comment:threshold:exceeded:alert2", "comment:threshold:exceeded:alert3"]
    effected_tickets = remove_tags(tickets, tags, creds)
    print(effected_tickets)
