"""Week 1 topic definitions and learning objectives."""

LEVELS = ("Beginner", "Advanced")

TOPICS = {
    "Q-learning": {
        "description": "Value-based reinforcement learning and action-value updates.",
        "objectives": (
            "Explain the role of states, actions, rewards and the Q-function.",
            "Interpret the Q-learning update equation.",
            "Calculate a Q-value update from supplied numeric values.",
        ),
    },
    "Backpropagation": {
        "description": "Gradient-based training of neural networks using the chain rule.",
        "objectives": (
            "Describe the forward and backward passes.",
            "Explain how the chain rule is used to compute gradients.",
            "Work through a small numerical gradient example.",
        ),
    },
    "Transformer self-attention": {
        "description": "How attention connects tokens within a Transformer sequence.",
        "objectives": (
            "Identify queries, keys and values in self-attention.",
            "Explain how attention scores are computed and normalized.",
            "Interpret a small attention-weight example.",
        ),
    },
}
