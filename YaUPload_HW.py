import os
import requests


class YaUploader:
    def __init__(self, token_: str):
        self.token = token_

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, path):
        URL = "https://cloud-api.yandex.net/v1/disk/resources"
        response = requests.put(f'{URL}?path={path}', headers=self.get_headers())
        if response.status_code == 201:
            print(f'Success. Create directory in YandexDisk: {path}')

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params, timeout=10)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self.get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()  # код ответа HTTP
        if response.status_code == 201:
            print(f'Successfully! The file was created on YandexDisk: {filename}')

    def upload(self, file_path: str):
        for f in os.listdir(f'{os.getcwd()}/{file_path}'):
            self.upload_file_to_disk(f'/{file_path}/{str(f)}', f'{file_path}/{str(f)}')


if __name__ == '__main__':
    path_to_file = "download"
    token = ""

    uploader = YaUploader(token)
    uploader.create_folder(path_to_file)
    uploader.upload(path_to_file)
