
import numpy as np
# Here are the vector representations of |0> and |1>, for convenience
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])
"""
    Compute a normalized quantum state given arbitrary amplitudes.

    Args:
        alpha (complex): The amplitude associated with the |0> state.
        beta (complex): The amplitude associated with the |1> state.

    Returns:
        np.array[complex]: A vector (numpy array) with 2 elements that represents
        a normalized quantum state.
"""

    ##################
    # YOUR CODE HERE #
    ##################
   
def normalize_state(alpha, beta):
  if (round(np.abs(alpha)**2 + np.abs(beta)**2,2) == 1):
    vector = np.array([alpha,beta])
    print(f"the state ${vector} is normalized")
    return vector
  else:
    magnitude = np.sqrt(np.abs(alpha)**2 + np.abs(beta)**2)
    alpha_prime = alpha / magnitude
    beta_prime = beta / magnitude
    print(np.abs(alpha_prime)**2 + np.abs(beta_prime)**2)
    if (round((np.abs(alpha_prime)**2 + np.abs(beta_prime)**2),3) == 1):
      new_vector = np.array([alpha_prime, beta_prime])
      print(f"the new state ${new_vector} is normalized")
      return new_vector
    else:
      print(f"the new state ${alpha_prime} and ${beta_prime} are not normalized")
      return


normalize_state(1-2j, 2-3j)