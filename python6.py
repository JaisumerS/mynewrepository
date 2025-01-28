from github import Github
from secrets import auth

print(auth)
# or using an access token
g = Github(auth)
repo = g.get_repo("JaisumerS/mynewrepository")