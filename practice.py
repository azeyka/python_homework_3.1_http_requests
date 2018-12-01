import requests
import os

  
def translate_it(text, lang):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    
    return ' '.join(response.get('text', []))
    
def main():
  
  def get_files_list_to_translate():
    files_list = os.listdir(current_dir)
    files_list_to_translate = []
    for file_name in files_list:
      if file_name.split('.')[-1] == 'txt':
        files_list_to_translate.append(file_name)
    
    return files_list_to_translate

  def make_result_dir():
    result_dir = os.path.join(current_dir, 'Translated_files')
    if 'Translated_files' not in os.listdir(current_dir):
      os.mkdir(result_dir)
    
    return result_dir

  def open_and_translate(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as f:
      text = f.read()
      
    lang = (file_name.strip('.txt') + '-' + translate_to).lower()
    translated_text = translate_it(text, lang)

    return translated_text
  
  def write_translate(file_name, result_dir, translated_text):
    translated_file_name = file_name.strip('.txt') + '-' + translate_to.upper() + '.txt'
    translated_file_path = os.path.join(result_dir, translated_file_name)
    with open(translated_file_path, 'tw', encoding = 'utf-8') as f:
      f.write(translated_text)
      
  current_dir = os.path.dirname(os.path.abspath(__file__))
  files_list = get_files_list_to_translate()
  if files_list:
    translate_to = input('Введите язык перевода: ')
    result_dir = make_result_dir()
    for file_name in files_list:
      try:
        translated_text = open_and_translate(file_name)
        write_translate(file_name, result_dir, translated_text)
        print('Перевод файла {} выполнен успешно.'.format(file_name))
      except:
        print('Ошибка перевода файла {}!'.format(file_name)) 

    print('Перевод файлов завершен.')
    print('Результаты в папке {}'.format(result_dir))
  else:
    print('В папке нет ни одного доступного для перевода файла.')
  
main()