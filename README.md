# BP Take-Home Project

Hello! This is the project skeleton to use for your take-home project.

## Schema

![bp](https://user-images.githubusercontent.com/96007/85434011-39c27f80-b53a-11ea-9e02-2ce84c2cb0b2.png)


## Populating sample data

After setting up your environment, run migrations. Then, create sample data to develop against using this command:

```shell script
python manage.py create_player_data
```

This will insert three years of sample data for a configurable number (default: 100) of players.
Some players will have multiple stints in a single year, as if they've been traded.

If you feel doing so suits your demo, feel free to change or extend the models. 

(The models and generated data are purposefully contrived, don't get too hung up on that.)

Enjoy!