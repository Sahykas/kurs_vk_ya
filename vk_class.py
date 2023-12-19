import requests


def trans_name_id(token_vk, screen_name):
    API_BASE_URL = 'https://api.vk.com/method/utils.resolveScreenName'
    params = {
        'access_token': token_vk,
        'v': '5.154',
        'extended': 1,
        'screen_name': screen_name
    }
    response = requests.get(API_BASE_URL, params=params).json()
    if len(response['response']) == 0:
        return screen_name
    else:
        return response['response']['object_id']


class VK_API_PHOTOS:
    API_BASE_URL = 'https://api.vk.com/method/photos.get'

    def __init__(self, token_vk, owner_id):
        self.token_vk = token_vk
        self.owner_id = owner_id

    def get_params(self):
        params = {
            'access_token': self.token_vk,
            'v': '5.154',
            'extended': 1
        }
        return params

    def get_photos(self):
        params = self.get_params()
        params.update({'owner_id': self.owner_id, 'album_id': 'profile'})
        response = requests.get(self.API_BASE_URL, params=params).json()
        list_file_names = []
        photos_list = []
        for files in response['response']['items']:
            file_url = files['sizes'][-1]['url']
            file_name = str(files['likes']['count']) + '.jpg'
            for photo in photos_list:
                if file_name in photo.keys():
                    file_name = str(files['likes']['count']) + str(files['date']) + '.jpg'
            size = files['sizes'][-1]['type']
            photos_list.append({file_name: [file_url, size]})
        return photos_list
