import requests


class YANDEX_DISK_API:
    api_disk_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token_yandex, photos_list):
        self.token_yandex = token_yandex
        self.photos_list = photos_list

    def save_photos(self, count):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token_yandex}'
        }
        path = 'kurs_work'
        response = requests.put(f'{self.api_disk_url}?path={path}', headers=headers)
        params = {
            'path': '',
            'url': ''
        }
        for photo in self.photos_list[0:count]:
            for key in photo:
                params['path'] = 'kurs_work/' + key
                params['url'] = photo[key][0]
                photo[key].remove(params['url'])
            response = requests.post(f'{self.api_disk_url}/upload', params=params, headers=headers)
        result_json = []
        for photo in self.photos_list[0:5]:
            for k, v in photo.items():
                result_json.append({'file_name': k, 'size': v})
        return result_json
