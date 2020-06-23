# BP Take-Home Project

Hello! This is the project skeleton to use for your take-home project.

## Schema

![bp](https://user-images.githubusercontent.com/96007/85434011-39c27f80-b53a-11ea-9e02-2ce84c2cb0b2.png)


## Populate sample data, run app

Unzip the emailed `bp-project-master.zip` file. (If you attempt to download and run the GitHub `.zip` file it will fail as you will be missing `secret_key.txt` and `playerstats/local_settings.py` files.)

After setting up your environment and installing required packages, run migrations. Then, create sample data to develop against using this command:

```shell script
$ python manage.py create_player_data
```

This will insert three years of sample data for a configurable number (default: 100) of players.
Some players will have multiple stints in a single year, as if they've been traded.

Start the development server and go to the root URL (most likely http://127.0.0.1:8000/). To see the SQL queries, run the development server with the `local_settings`, i.e.:

```shell script
$ python manage.py runserver --settings=playerstats.local_settings
```

