from src.llm_service import generate_comparison

def compare_policies(policy_a, policy_b):
    return generate_comparison(policy_a, policy_b)
