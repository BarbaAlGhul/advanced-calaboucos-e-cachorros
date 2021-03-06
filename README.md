# Calabouços & Cachorros Avançado
Calabouços & Cachorros Avançado (Advanced Dungeons & Dogs, in English) is a roguelike demo game, created for my own learning purposes, using python and the [tcod](https://github.com/libtcod/python-tcod) library.<br><br>

![](https://lh3.googleusercontent.com/qpJqzioQVlAoIiZigmiKuz75v3JKMQ6_Tcsw9xly6FB7w-zWVDiLuuZA6PdkRGmh6skIZ7ToxWEO6ihsDSLXpGTtdTou7bZEzOowb75_skm939wz_yNA_PfCNBa_IeOmJ3OylN9BareQFHWH_4CmTXIAzV7Tb43FJe9g189fjjnXCs7_filBlE-XzON-hQz1SoZEl9MIQYYgYELhIOIZfjanvro_jyMWKc0cMSJeHa40oVejoEYdpjHqHoI7WeFg2s0UF0m46XbdAcVdDwI2a5rKA7DuUdu2iyBYzPVSKRY7JIzigEvEehcqUU3Q1CU6Pruyy4yt8kLdI2yP3_fH7pUsCE4FPS3Fs4nafzMA-d77praDbEcFhT8jWNsvmIJKWwX1jmPk1HQHSRo7O2KkUKjCuE97ac8574rXqAOD8Tt7vXrOHOpBGIzVzApTtpgTzgOyLyC2ZpODqENSmmUj41p-f1fIZyLDVO-hZqmh7EU2P1OH7JXN_xFstrdiZ49euNTQ_5QQzQ7mAOTo0xacwMe8r_EPYUUqJG5Y-9_FUeP_HQop157e0MSxagNeuu88h9HvUsZX1iYNyMrf6fNLGAAe7ME_0EDRcyAK56wflb-z6yy0iS02W87daWWEW8YVvkpUtCEzglxEdPpYa_4jK85-K-R1ezFbAwXeZrGVCu6L0jcMCiRpNePY4KW0iNHXodl6gxtHWeYo781M0SWhhthH=w802-h532-no?authuser=0)

![](https://lh3.googleusercontent.com/i1GobJJqnFy4i1ZTEBpdwAkAtZ1jOUasnv4crczCgL3SDpOi3wco5Yun_NeCbBeBu9eQzll7N3Sn-hAqHKP-DWJ7pOVOzL2EkjK8daqT6auLU3aZbf-AkiKvVV3_nFJAlK0sB3QzPmT8M_kPypTEEHTkGtyzXHRCYwRAmQDV0RDDoc6034KUJXAFWJ9CQl5DMe5JpBHJXbFugCjjOkuPNau8_2lBP67XtmlLAaDuwGKjhRjcbZcl2YcQwFrDEEdsfuSH3SVPixMM_6Ow91fhouV2JJDboldEQmrJGu9sfIYlCQT0jnuZqx7upV4pEtaccRUGm4nYK6OwoIPjJNBIEtg-FD-HObDqzdtTNplvX5dc4dlr6uSMEhL67dmzMOA4xq-Zz6DSjzHrQdK8APcrJemtF25oeS6iCD7L5bMczoM2CeMlIOpqOtd-L50_f2idD9H2rHRlds6G2sZifa6YEG9WSF82cYsTIH3RTvtTCWjEF2r4e8IgeunMU7qwFx9KbVspbXBcrNpAk5NpWIV8RB_hsLAdHYV7YywfPPJ03NFym6ehSEeEafET50s6gaw8beht_VYppk2LUGABgjs1EKuRlpk7m8cTr44G525rh7e6W4yNrD09RkBY0cGWK9EduY08zDauA0wdDdLNaeo5VP8CRDhDQfGwESj-E8Nc6jksMbtCDL5t0ELRnw8S0QjyZH70y2Q26up2KKVhYuR_i0U3=w802-h532-no?authuser=0)

This code is based on the [Yet Another Roguelike Tutorial](http://rogueliketutorials.com/tutorials/tcod/v2/)

## Requirements
Python 3.7 or higher and the requirements on the Pipfile.

The project used Pipenv as the environment, but if you use another virtual environment, there is a *requirements.txt* file with the project.

To run it, just run the file *main.py* on the terminal.

##Commands
- Movement:
  - Cursor Keys: 
    -  up: :arrow_up:
    -  down::arrow_down:
    -  left: :arrow_left:
    -  right: :arrow_right:
    -  PageUp: :arrow_upper_right:
    -  PageDown: :arrow_lower_right:
    -  End: :arrow_lower_left:
    -  Home: :arrow_upper_left:
      
  - Numpad:
    -  8: :arrow_up:
    -  2::arrow_down:
    -  4: :arrow_left:
    -  6: :arrow_right:
    -  9: :arrow_upper_right:
    -  3: :arrow_lower_right:
    -  1: :arrow_lower_left:
    -  7: :arrow_upper_left:
    
- Action:
  - G: pick up item
  - I: open inventory - uses selected item
  - D: open inventory - drop selected item
  - C: open character information  
  - Enter: confirm action
  - /: enter cursor mode
  - Esc: quit

      
## Resources
Font: [REXPaint's 10x10 tweaked by qbicfeet](https://www.gridsagegames.com/rexpaint/resources.html)
