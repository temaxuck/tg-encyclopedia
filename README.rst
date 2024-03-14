===============
tg-encyclopedia
===============

A telegram bot for viewing and searching for **`Link Number Pyramid objects <https://oenp.tusur.ru/>`_**. Bot is available by this link: <https://t.me/oenp_bot>

The bot is written using aiogram package and is also able to load pyramid data to **`Link telegram channel <t.me/oenp_tusur>`_**.

To run bot that would post pyramids data to telegram channel run `python3 load_pyramids_to_channel`.

----------------------
**EXTRA-REQUIREMENTS**
----------------------
- texlive-latex-extra 
- dvipng


--------
**TODO**
--------
- [x] Refactor code and make python package from this repo;
- [x] Create proper CLI tool to run bot and to post pyramid data to channel;
- [x] Dockerize this package;
- [x] Add tests and CI;
