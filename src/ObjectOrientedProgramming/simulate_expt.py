import argparse
from src.ObjectOrientedProgramming.models import SimpleMemoryModel, InterferenceMemoryModel


def run(all_my_arguments):
    someones_memory = SimpleMemoryModel()  # Individual 1's memory instance
    someone_elses_memory = InterferenceMemoryModel(
        seed=32)  # Individual 2's memory instance

    # print(type(someone_elses_memory.rng))

    for trial in range(all_my_arguments.num_trials):
        p1, acc1 = someones_memory.simulate_trial(
            all_my_arguments.list_of_letters)
        print(f"Prob & Acc of recall for Individual 1: {p1}, {acc1}")

        p2, acc2 = someone_elses_memory.simulate_trial(
            all_my_arguments.list_of_letters)
        print(f"Prob & Acc of recall for Individual 2: {p2}, {acc2}")


if __name__ == '__main__':

    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--list_of_letters', type=str, default='57312')
    my_parser.add_argument('--num_trials', type=int, default=20)
    all_my_arguments = my_parser.parse_args()

    run(all_my_arguments=all_my_arguments)
