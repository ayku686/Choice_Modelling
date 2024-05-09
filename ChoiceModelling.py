import numpy as np
import json

def calc_probabilities(parameters, data, utilities):
    """
    Calculates probabilities for each alternative in a multinomial choice setting
    using the logistic function.

    Parameters:
        - parameters: A dictionary containing the β coefficients.
        - data: A dictionary containing the independent variables (X1, X2, Sero, etc.).
        - utilities: A list of functions defining the deterministic utilities for each alternative.

    Returns:
        - prob_output: A dictionary with keys representing each alternative
          and values as lists containing the calculated probabilities for each data point.
    """

    # Check if the number of parameters matches the number of variables
    num_params = len(parameters)
    if num_params != len(data):
        raise ValueError("Number of parameters does not match the number of variables.")

    # Check if the number of utility functions matches the number of alternatives
    num_alternatives = 0
    for key in data.keys():
        if key.startswith('AV'):
            num_alternatives += 1
    if num_alternatives != len(utilities):
        raise ValueError("Number of utility functions does not match the number of alternatives.")

    # Initialize dictionary to store probabilities for each alternative
    prob_output = {}

    for alt in range(1, num_alternatives + 1):
        # Compute deterministic utility for the current alternative
        V = utilities[alt - 1](parameters, data)

        # Compute denominator of the probabilities
        exp_utilities = np.exp([utilities[i](parameters, data) for i in range(num_alternatives)])
        denominator = np.sum(exp_utilities, axis=0)

        # Compute probabilities for each data point
        probabilities = np.exp(V) / denominator

        # Store probabilities for the current alternative
        prob_output[f'P{alt}'] = probabilities.tolist()

    return prob_output


"""
    utility_function
    Define the deterministic utility function for Alternative 1,2 and 3.

    Parameters:
        - parameters: A dictionary containing the β coefficients.
        - data: A dictionary containing the independent variables.

    Returns:
        - V: A numpy array of deterministic utilities for Alternative 1.
    """
def utility_function_1(parameters, data):
    V1 = parameters['β01'] + parameters['β1'] * np.array(data['X1']) + parameters['βS1,13'] * np.array(data['S1'])
    return V1

def utility_function_2(parameters, data):
    V2 = parameters['β02'] + parameters['β2'] * np.array(data['X2']) + parameters['βS1,23'] * np.array(data['S1'])
    return V2

def utility_function_3(parameters, data):
    V3 = parameters['β03'] + parameters['β1'] * np.array(data['Sero']) + parameters['β2'] * np.array(data['Sero'])
    return V3

# Sample data
data = {
    'X1': [2, 1, 3, 4, 2, 1, 8, 7, 3, 2],
    'X2': [8, 7, 4, 1, 4, 7, 2, 2, 3, 1],
    'Sero': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'S1': [3, 8, 4, 7, 1, 6, 5, 9, 2, 3],
    'AV1': [1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    'AV2': [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    'AV3': [1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
}

# Parameters
parameters = {
    'β01': 0.1, 'β1': -0.5, 'β2': -0.4,
    'β02': 1, 'β03': 0, 'βS1,13': 0.33, 'βS1,23': 0.58
}

# List of utility functions for each alternative
utilities = [utility_function_1, utility_function_2, utility_function_3]

# Calculate probabilities
try:
    probabilities = calc_probabilities(parameters, data, utilities)
    with open('probabilities_output.txt', 'w') as f:
        json.dump(probabilities, f, indent=4)
    print("Probabilities calculated and saved to 'probabilities_output.txt'")
except ValueError as e:
    print("Error:", e)
