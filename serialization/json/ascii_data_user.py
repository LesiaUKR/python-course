from __future__ import annotations

import json

# ensure_ascii = False - дозволяє виводити кирилицю в файл

data = {"developer": {"name": "Юрій Кучма", "species": "програміст"}}

with open("data_user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

with open("data_user.json", "r", encoding="utf-8") as f:
    restore_data = json.load(f)
    print(restore_data)
