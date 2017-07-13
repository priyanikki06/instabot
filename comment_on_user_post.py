# comment_on_user_post.py file created

import requests

from constants import APP_ACCESS_TOKEN, BASE_URL
from get_user_post_id import get_post_id


def comment_on_a_post(insta_username):
    # function logic
    media_id = get_post_id(insta_username)

    if media_id == None:
        print ('\nUsername does not exist')
        exit()
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)

    comment = raw_input('\n\nPlease enter your comment:-\t')
    payload = {'access_token': APP_ACCESS_TOKEN, 'text': comment}
    print ('\nPOST request url : %s' % (request_url))
    user_info = requests.post(request_url, payload).json()

    if user_info['meta']['code'] == 200:
        print ('\nComment posted  Successfully')
    else:
        print ('\n\nStatus code received is other than 200')
        print ('\nUnable to post the comment on the recent Post')
        exit()
