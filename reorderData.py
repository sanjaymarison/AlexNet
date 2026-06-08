import numpy as np
from collections import Counter

# Load balanced data
try:
    balanced_data = np.load('balanced_data.npy', allow_pickle=True)
    print(f"Balanced data shape: {balanced_data.shape}")
    print(f"Number of samples: {len(balanced_data)}")
    
    # Check the structure of first few samples
    print("\nFirst sample structure:")
    print(f"Sample 0: {balanced_data[0][0].shape} -> {balanced_data[0][1]}")
    print(f"Sample 1: {balanced_data[1][0].shape} -> {balanced_data[1][1]}")
    print(f"Sample 2: {balanced_data[2][0].shape} -> {balanced_data[2][1]}")
    
    # Count unique outputs
    outputs = [str(sample[1]) for sample in balanced_data]
    output_counts = Counter(outputs)
    print(f"\nOutput distribution:")
    for output, count in output_counts.items():
        print(f"  {output}: {count}")
    
    # Check if all outputs have the same length
    output_lengths = [len(sample[1]) for sample in balanced_data]
    unique_lengths = set(output_lengths)
    print(f"\nOutput lengths: {unique_lengths}")
    
    if len(unique_lengths) == 1:
        num_classes = list(unique_lengths)[0]
        print(f"Number of classes: {num_classes}")
    else:
        print("Warning: Inconsistent output lengths!")
        
except Exception as e:
    print(f"Error loading data: {e}") 