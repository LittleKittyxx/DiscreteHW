import time
import random
import pandas as pd


def measure_function_performance(target_function):
    performance_data = {"Число вызовов": [], "Затраченное время (с)": []}

    NUM_TRIALS_RANGE = range(50, 1001, 50)

    num_args = target_function.__code__.co_argcount

    for current_num_calls in NUM_TRIALS_RANGE:

        start_time_seconds = time.time()

        for _ in range(current_num_calls):
            if num_args == 1:
                input_val = random.randint(1, 1000)
                target_function(input_val)
            elif num_args == 2:
                input_val_a = random.randint(1, 1000)
                input_val_b = random.randint(1, 1000)
                target_function(input_val_a, input_val_b)
            else:
                pass

        end_time_seconds = time.time()

        elapsed_time = end_time_seconds - start_time_seconds

        performance_data["Число вызовов"].append(float(current_num_calls))
        performance_data["Затраченное время (с)"].append(elapsed_time)

    results_df = pd.DataFrame(performance_data)
    return results_df
