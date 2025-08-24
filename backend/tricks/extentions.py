from games.models import Game

def game_choise_field():
    all_games = Game.objects.all()
    cleaned_games = []

    for game in all_games:
        cleaned_games.append((game.id , game.title))
    
    return cleaned_games


if __name__ == "__main__":
    try:
        game_choise_field()
    except:
        pass