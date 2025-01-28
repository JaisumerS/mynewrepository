from github import Github
from secrets import auth

# or using an access token
g = Github(auth)
repo = g.get_repo("JaisumerS/mynewrepository")

print(list(repo.get_branches()))
pulls = repo.get_pulls(state='closed', sort='created', base='main')
for pr in pulls:
   print(pr)

commits = repo.get_commits()
for commit in commits:
    print(commit.commit.message)