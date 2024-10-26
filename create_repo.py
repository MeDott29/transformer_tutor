import os

# Define the files to create
files = [
    "matrix.js",           # Basic matrix operations and tensor manipulations
    "embedding.js",        # Positional and token embedding implementations
    "attention.js",        # Core attention mechanism
    "multihead.js",        # Multi-head attention implementation
    "feedforward.js",      # Feed-forward neural network component
    "layernorm.js",        # Layer normalization implementation
    "sublayer.js",         # Sublayer with residual connections
    "encoder.js",          # Complete encoder block
    "decoder.js",          # Complete decoder block
    "transformer.js",      # Full transformer architecture
    "masking.js",          # Padding and future masking utilities
    "vocabulary.js",       # Token handling and vocabulary management
    "optimizer.js",        # Basic gradient descent implementation
    "train.js",            # Training loop and loss calculation
    "inference.js",        # Inference and generation utilities
    "config.js",           # Model configuration and hyperparameters
    "example.js",          # Simple translation example
    "visualization.js",    # Attention visualization helpers
]

# Create README.md with content
readme_content = """\
# A Set of Files to Give to a Tutor

If you want to learn how transformers work at a granular level, these files provide modular implementations and examples. Each file corresponds to a specific component of the transformer architecture, from basic data structures to model training and inference utilities.
"""

def create_files():
    # Create README.md
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("Created: README.md")

    # Create each file with a comment header
    for filename in files:
        with open(filename, "w") as f:
            f.write(f"// {filename} - Placeholder for {filename.split('.')[0].capitalize()} module\n")
        print(f"Created: {filename}")

if __name__ == "__main__":
    create_files()
