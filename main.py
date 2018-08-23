import sqlite3

db = sqlite3.connect('tests/populated_gists_database.db')
db.row_factory = sqlite3.Row

cursor = db.execute('SELECT * FROM gists')

for gist in cursor:
    print('Github Id: ', gist['github_id'])
    print('Html Url: ', gist['html_url'])
    print('Git Pull Url: ', gist['git_pull_url'])
    print('Git Push Url: ', gist['git_push_url'])
    print('Commits Url: ', gist['commits_url'])
    print('Forks Url: ', gist['forks_url'])
    print('Public: ', gist['public'])
    print('Created At: ', gist['created_at'])
    print('Updated At: ', gist['updated_at'])
    print('Comments: ', gist['comments'])
    print('Comments Url: ', gist['comments_url'])
    print('=' * 60)
