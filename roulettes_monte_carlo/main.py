# main.py
import random
from roulettes import FairRoulette, EuRoulette, AmRoulette
from statistics import get_mean_and_std, get_confidence_margin


#roulette_class: es la clase de la ruleta que vamos a usar (FairRoulette, EuRoulette o AmRoulette). Pasamos la clase como un molde para que la función pueda crear el objeto adentro.

#num_trials: es el número total de intentos o simulaciones independientes que haremos. En la vida real, equivale a la cantidad de jugadores distintos que mandamos al casino para luego poder calcular un promedio estadístico entre todos ellos.

#spins_per_trial: es la cantidad de lanzamientos (giros de rueda) que hará cada jugador. Representa el tamaño de la muestra. Modificar este número nos permite ver cómo funciona la "Ley de los Grandes Números" a medida que la muestra se hace más grande.

#bet_pocket: es la casilla o número específico al que el jugador decide apostar siempre (por ejemplo, el número entero 2, o el texto "00" si fuera la ruleta americana).

#bet_amount: es el monto o cantidad de dienero que el jugador va a arriesgar en cada uno de los lanzamientos (por ejemplo, apostar $1 dólar en cada giro).



def run_monte_carlo(roulette_class, num_trials, spins_per_trial, bet_pocket, bet_amount):
    """
    Orchestrates the Monte Carlo simulation.
    A 'trial' represents an independent group containing many consecutive 'spins'.
    """
    trial_returns = []
    game_instance = roulette_class()
    
    # bucle externo para cada trial (jugador independiente)
    for _ in range(num_trials):
        total_trial_payout = 0
        for _ in range(spins_per_trial): # Bucle para los lanzamientos de cada jugador
            game_instance.spin() # Gira la ruleta al azar
            total_trial_payout += game_instance.betPocket(bet_pocket, bet_amount) # Apuesta y acumula balance
        
        # The proportional return is the net payout divided by the total capital risked in this trial
        return_percentage = total_trial_payout / spins_per_trial #porcentaje de retorno dividiendo la ganancia neta entre el total apostado
        trial_returns.append(return_percentage)
        
    return trial_returns, str(game_instance)


def simulate_mit_experiment():
    #random.seed(0)
    trials = 20
    selected_pocket = 2 # El número favorito del jugador
    stake = 1 # Dinero apostado por lanzamiento ($1)
    
    roulette_types = [FairRoulette, EuRoulette, AmRoulette]
    # Scaling up the sample sizes to observe convergence (Regression to the mean)
    spin_scales = [100, 1000, 100000]
    
    print("=====================================================================")
    print("      MIT MONTE CARLO SIMULATION PROJECT (ROULETTE EXPERIMENT)       ")
    print("=====================================================================")
    
    # Este doble bucle (for) va a evaluar primero las 3 ruletas con $100$ giros, luego las 3 ruletas con $1,000$ giros, y finalmente las 3 con $100,000$ giros.
    for spins in spin_scales:
        print(f"\n>> Simulating {trials} trials with {spins:,} spins per trial:")
        print("-" * 75)
        
        for r_class in roulette_types:
            # 1. Harvest raw data utilizing stochastic sampling (Monte Carlo)
            # Correr simulación de los datos usando Monte Carlo
            returns, game_name = run_monte_carlo(
                roulette_class=r_class,
                num_trials=trials,
                spins_per_trial=spins,
                bet_pocket=selected_pocket,
                bet_amount=stake
            )
            
            # 2. Extract statistical metrics from collected sample sets
            mean, std = get_mean_and_std(returns)
            margin = get_confidence_margin(std, confidence_level=0.95)
            
            # Formating to human-readable percentages
            expected_return_pct = mean * 100
            margin_pct = margin * 100
            
            print(f"   Expected return for {game_name:<18} = {expected_return_pct:>7.3f}%, "
                  f"+/- {margin_pct:>6.3f}% (95% Confidence)")

if __name__ == "__main__":
    simulate_mit_experiment()