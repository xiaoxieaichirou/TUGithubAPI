from core.rest_client import RestClient

'''封装第一个接口, https://developer.github.com/v3/repos/'''
class Repos(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Repos, self).__init__(api_root_url, **kwargs)

    def list_you_repos(self):
        return self.get('/user/repos')