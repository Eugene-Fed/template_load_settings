# -*- coding: UTF-8 -*-

import requests
import json
import sys
from pathlib import Path
from datetime import datetime, timedelta, date, time

# Это единственные 'данные/настройки' в коде. Все остальное вынесено в файл settings.json
TEMPLATES_DIR = 'templates'
SETTINGS_FILE = 'settings.json'

templates_dir = Path(TEMPLATES_DIR)
settings_file = Path(SETTINGS_FILE)
settings = {}
api_keys = {}


def load_settings(templates_dir=templates_dir, settings_file=settings_file, settings=settings):
    if settings_file.exists():
        with settings_file.open() as f:
            settings = json.load(f)
    else:
        settings_template = templates_dir / settings_file
        if settings_template.exists():
            with settings_template.open() as f:
                settings = json.load(f)
                # TODO: добавить интерактивный вввод параметров с дальнейшим сохранением в файл settings.json
            with settings_file.open("w", encoding="utf-8") as f:
                json.dump(settings, f, indent=4, ensure_ascii=False)

        else:
            print('Files "settings.json" and "templates/settings.json" do not exists')
            sys.exit(1)


if __name__ == '__main__':
    load_settings(settings=settings)
    print(settings)
