# client Id = a395daa3b1f8c8e
# Client Secret = 0c8eb794b602bb3de7d39e20171794227bcfc205


from imgurpython import ImgurClient


class API:
    def __init__(self, _client_id, _client_secret):
        self.client_id = _client_id
        self.client_secret = _client_secret
        self.client = ImgurClient(_client_id, _client_secret)
        pass

    def get_album_image_urls(self, _album_id):
        images = self.client.get_album(_album_id).__dict__['images']
        links = []
        for image in images:
            links.append(image['link'])
            pass
        return links
        pass

    def get_favorites_image_urls(self, username):
        images = self.client.get_account_favorites(username)
        links = []
        for image in images:
            links.append(image.__dict__['link'])
            pass
        return links
        pass

    pass


if __name__ == '__main__':
    client_id = 'YOUR ID'
    client_secret = 'YOUR SECRET'
    api = API(client_id, client_secret)
    print(api.get_album_image_urls('Album ID'))
    print(api.get_favorites_image_urls("UserName"))
    pass
