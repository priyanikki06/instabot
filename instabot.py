# instabot.py file created
from self_info import self_info
from get_user_info import get_user_info
from get_own_post import get_own_post
from get_users_post import get_users_post
from like_user_post import like_a_post
from comment_on_user_post import comment_on_a_post


print ('\n\nYou want to see your own details\n')
self_info()
print '\n\n'

# fetching your recent post
print '\n\nYou want to see your recent post\n'
get_own_post()
print '\n\n'

# fetching other users detail
print ('\n\nYou want to see other users detail\n')
other_username = raw_input('Enter the username')
get_user_info(insta_username= other_username)

# fetching the other users recent post
print ('\n\nYou want to see other users recent post\n')
other_username = raw_input('Enter the username')
get_users_post(insta_username=other_username)

# like the other users recent post
print ('\n\nYou want to like the other users recent post\n')
other_username = raw_input('Enter the username')
like_a_post(insta_username= other_username)
print '\n\n'

# Post a comment on the other users recent post
print ('\n\nYou want to post a comment on the other users recent post\n')
other_username = raw_input('Enter the username')
comment_on_a_post(insta_username=other_username)
print '\n\n'

# you want to close the application
exit()
