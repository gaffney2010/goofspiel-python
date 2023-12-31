import sys

sys.path.append("src")

import bot_namer
import breed_lib
import goofspiel
import mutation_lib
import player_lib
import scorer_lib


config = goofspiel.GameConfig(
    deck=[c for c in range(1, 20)],
    namer=bot_namer.NumberedNamer(),
    logger=goofspiel.GoofLogger(log_types=["HIGH_SCORE"]),
    scorer=scorer_lib.half_diff,
    breeder=breed_lib.geneless_breeding,
    mutator=mutation_lib.no_mutation,
    mutation_degree=0.0,
)
goofspiel.evolve_players(
    seed_players=[player_lib.BotPlayer(config, seed=_ * 11) for _ in range(10)],
    n_bots=25,
    survival_rate=10,
    config=config,
    generations=200,
)
