import configparser
import json
import logging

import vk_class
import yandex_class

if __name__ == '__main__':
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    token_vk = parser.get('Settings', 'token_vk')
    token_yandex = parser.get('Settings', 'token_yandex')
    print('Start programs')
    print("Введите id или screen_name страницы")
    screen_name = input()
    owner_id = vk_class.trans_name_id(token_vk, screen_name)
    # 76879487
    # 'y0_AgAAAAAFmdz2AArRrwAAAADx_0S8TuTq6oibSaCtNNXm5Cx94MDHHBs'
    logging.basicConfig(filename='log_file.log', filemode='w',
                        encoding='utf-8', level='INFO', format='%(asctime)s, %(levelname)s, %(message)s')
    logger = logging.getLogger()
    logger.info('Входные данные о странице пользователя введены')
    vk_page = vk_class.VK_API_PHOTOS(token_vk, owner_id)
    length = len(vk_page.get_photos())
    print(f'Введите количество фото, но не более', length,
          ', поскольку у пользователя столько фотографий в профиле')
    count = int(input())
    if count <= length:
        logger.info('Пользователь вверно ввёл количество фото')
        class1 = yandex_class.YANDEX_DISK_API(token_yandex, vk_page.get_photos())
        photos_list = class1.save_photos(count)
        logger.info('Фотографии загружены на Яндекс диск')
        with open('data_file.json', "w") as f:
            json.dump(photos_list, f)
        logger.info('Сформирован итоговый json файл')
    else:
        print('Пользователь неверно ввёл количество фото')
        logger.info('Пользователь неверно ввёл количество фото')
