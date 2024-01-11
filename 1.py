I was playing around with gpt the other day and found something helpful (maybe)
from ahpy import Ahp
from PyInquirer import prompt

def get_user_weights(items, category):
    question = {
        'type': 'checkbox',
        'message': f'Set weights for {category} (press space to select)',
        'name': f'{category}_weights',
        'choices': [{'name': item} for item in items],
    }
    user_input = prompt([question])
    user_weights = [1 if item in user_input[f'{category}_weights'] else 0 for item in items]
    return user_weights

def create_pairwise_matrix(items, category):
    matrix = []
    for item in items:
        weights = get_user_weights(items, category)
        matrix.append(weights)
    return matrix

criteria = ["Flexibility", "Cost", "Security", "Performance", "Reliability"]

# Create pairwise comparison matrix for criteria
criteria_matrix = create_pairwise_matrix(criteria, "criteria")

# Create AHP model for criteria
criteria_model = Ahp("Cloud Criteria", criteria, criteria_matrix)
criteria_model.calculate_weights()

# Define cloud service providers
providers = ["Provider A", "Provider B", "Provider C"]

# Create pairwise comparison matrix for providers
providers_matrix = create_pairwise_matrix(providers, "providers")

# Create AHP model for providers
providers_model = Ahp("Cloud Providers", providers, providers_matrix)
providers_model.calculate_weights()

# Print initial criteria and provider weights
print("\nInitial Criteria Weights:")
print(criteria_model.weights)

print("\nInitial Provider Weights:")
print(providers_model.weights)

# Get user preferences for criteria
user_criteria_weights = get_user_weights(criteria, "criteria")
criteria_model.update_weights(user_criteria_weights)

# Get user preferences for providers
user_providers_weights = get_user_weights(providers, "providers")
providers_model.update_weights(user_providers_weights)

# Print final weights after user preferences
print("\nFinal Criteria Weights:")
print(criteria_model.weights)

print("\nFinal Provider Weights:")
print(providers_model.weights)

# Calculate final scores for providers
final_scores = criteria_model.weights * providers_model.weights
print("\nFinal Scores for Providers:")
for provider, score in zip(providers, final_scores):
    print(f"{provider}: {score:.2f}")
