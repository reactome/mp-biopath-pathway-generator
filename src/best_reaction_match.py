import numpy as np
from scipy.optimize import linear_sum_assignment


def create_raw_counts_matrix(input_reactions, output_reactions, decomposed_uid_mapping):
    n = len(input_reactions)
    m = len(output_reactions)
    reaction_to_reaction_counts = [[0 for _ in range(m)] for _ in range(n)]
    for i, input_reaction in enumerate(list(input_reactions)):
        input_rows = decomposed_uid_mapping[decomposed_uid_mapping['uid'] == input_reaction]
        input_component_ids = set(input_rows['component_id'])
        for j, output_reaction in enumerate(list(output_reactions)):
            output_rows = decomposed_uid_mapping[decomposed_uid_mapping['uid'] == output_reaction]
            output_component_ids = set(output_rows['component_id'])
            count = len(input_component_ids.intersection(output_component_ids))
            reaction_to_reaction_counts[i][j] = count

    return np.array(reaction_to_reaction_counts)


def find_best_reaction_match(input_reactions, output_reactions, decomposed_uid_mapping):
    counts = create_raw_counts_matrix(input_reactions, output_reactions, decomposed_uid_mapping)
    num_rows, num_cols = counts.shape

    if num_rows != num_cols:
        # Pad the counts matrix with zeros to make it square
        max_dim = max(num_rows, num_cols)
        padded_counts = np.zeros((max_dim, max_dim))
        padded_counts[:num_rows, :num_cols] = counts
    else:
        padded_counts = counts

    # Convert counts to negative values to transform the maximum matching problem into a minimum cost matching problem
    costs = -padded_counts
    row_indices, col_indices = linear_sum_assignment(costs)

    matched_pairs = [(i, j) for i, j in zip(row_indices, col_indices) if i < num_rows and j < num_cols]
    matched_counts = [counts[i][j] for i, j in matched_pairs]

    reaction_matches = []
    for pair, count in zip(matched_pairs, matched_counts):
        input_id = list(input_reactions)[pair[0]]
        output_id = list(output_reactions)[pair[1]]
        reaction_match = (input_id, output_id)
        # print(f"Reaction pair: {reaction_match}, Count: {count}")
        reaction_matches.append(reaction_match)

    return [reaction_matches, matched_counts]
