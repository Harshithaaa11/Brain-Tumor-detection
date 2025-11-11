import matplotlib.pyplot as plt
import numpy as np


def visualize_personality_traits(scores, traits=['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness',
                                                 'Neuroticism']):
    """
    Visualize personality traits using a radar chart.

    Parameters:
    - scores: List of scores for each trait (0-100 scale)
    - traits: List of trait names (default is Big Five)
    """

    # Number of traits
    num_vars = len(traits)

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Complete the loop
    scores += scores[:1]
    angles += angles[:1]

    # Initialize the figure
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Draw one axis per variable and add labels
    plt.xticks(angles[:-1], traits, color='grey', size=12)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([20, 40, 60, 80], ["20", "40", "60", "80"], color="grey", size=10)
    plt.ylim(0, 100)

    # Plot the data
    ax.plot(angles, scores, linewidth=1, linestyle='solid', color='blue')

    # Fill area
    ax.fill(angles, scores, 'blue', alpha=0.1)

    # Add title
    plt.title("Personality Traits Visualization", size=16, y=1.1)

    plt.show()


# Example usage
if _name_ == "_main_":
    # Sample scores (0-100) for each trait
    sample_scores = [75, 85, 60, 90, 45]  # O, C, E, A, N
    visualize_personality_traits(sample_scores)