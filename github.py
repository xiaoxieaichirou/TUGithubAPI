from api.repositories.repos import Repos

class Github():
    def __init__(self, **kwargs):
        self.api_root_url = 'http://api.github.com'
        self.repos = Repos(self.api_root_url, **kwargs)

if __name__ == '__main__':
    r = Github(token = '')
    x = r.repos.list_you_repos()
    print(x.text)

    r = Github(username = '', password = '')
    x = r.repos.list_you_repos()
    print(x.text)