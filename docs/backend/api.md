# API Endpoints
All apps and sections have a root url:
home: `/` 

games: `games/`

tricks: `tricks/`

authentication: `auth/`

dashboard: `dash/`
## Home
**Root url: `/`**

``` json
"Name": "home" ,
"Url": ''
"Summary": "home page (index.html)"
```

``` json
"Name": "show profile" ,
"Url": "profile/?user_id/"
"Summary": "render and show user profile"
```

## Authentication
**Root url: `auth/`**

``` json
"Name": "register",
"Url": "register/",
"Summary": "signup user to the system"
```

``` json
"Name": "login",
"Url": "login/",
"Summary": "log user in"
```

``` json
"Name": "logout",
"Url": "logout/",
"Summary": "log user out"
```

## Tricks
**Root url: `tricks/`**

``` json
"Name": "show trick",
"Url": "?trick_id/",
"Summary": "get and show specific trick info "
```

``` json
"Name": "get all tricks",
"Url": "all/",
"Summary": "get all tricks from database and render them"
```

``` json
"Name": "get tricks by game",
"Url": "game/?game_id/",
"Summary": "get tricks by a spesific game from database and render them"
```

``` json
"Name": "get tricks buy creator",
"Url": "user/?creator_id/",
"Summary": "get tricks by a specific user from database and render them"
```

``` json
"Name": "new trick",
"Url": "new/",
"Summary": "Create new trick"
```

``` json
"Name": "delete trick",
"Url": "delete/?trick_id/",
"Summary": "delete a specific trick by trick id"
```

``` json
"Name": "update trick",
"Url": "update/?trick_id/",
"Summary": "update a specific by trick id"
```


## Games
**Root url: `games/`**

``` json
"Name": "get all games",
"Url": "all/",
"Summary": "get all game from database"
```

``` json
"Name": "game info",
"Url": "info/?game_id/",
"Summary": "get and render a game info"
```

``` json
"Name": "game by genre",
"Url": "genre/?genre_id/",
"Summary": "get games by genre from database by genre id"
```

``` json
"Name": "games by publisher",
"Url": "publisher/?publisher_id/",
"Summary": "get games by publisher from database by pub id"
```

``` json
"Name": "games by ESRB",
"Url": "esrb/?esrb_sign/",
"Summary": "get games from database by ESRB sign like M,A,T,etc ..."
```


## Dashboard
**Root url: `dash/`**
``` json
"Name": "my profile",
"Url": "profile/",
"Summary": "show logined user information and actions (user panel)"
```

``` json
"Name": "add favorite game",
"Url": "add_favorite_game/?game_id/",
"Summary": "add a game to user favorite games "
```

``` json
"Name": "add saved trick",
"Url": "add_saved_trick/?trick_id/",
"Summary": "add a trick to user saved tricks"
```

``` json
"Name": "my favorite games",
"Url": "my_favorite_games/",
"Summary": "get and show user favorite games"
```

``` json
"Name": "my saved tricks",
"Url": "my_saved_tricks/",
"Summary": "get and show user saved tricks"
```
