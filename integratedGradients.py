import torch
import torch.nn.functional as F


def generate_scaled_inputs_and_gradients(model: torch.nn.Module, input: torch.Tensor, targets: torch.Tensor, steps: int = 200) -> torch.Tensor:
    # Check if CUDA is available
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("CUDA is available. Using GPU.")
    else:
        device = torch.device("cpu")
        print("CUDA is not available. Using CPU.")
    model.eval()
    # we set the baseline to be zero
    baseline = torch.zeros_like(input, device=device)  # Ensure baseline is on the same device

    averaged_gradients = torch.zeros_like(input, device=device)
    # Interpolate scaled inputs and compute gradients
    for i in range(steps + 1):
        # Generate the scaled input
        scaled_input = (float(i) / steps) * input
        scaled_input.requires_grad_(True)
        
        output = model(scaled_input)
        loss = F.cross_entropy(output, targets)  
        model.zero_grad()
        loss.backward()
        input_gradients = scaled_input.grad
        assert scaled_input.grad is not None
        averaged_gradients += scaled_input.grad / steps

    scaled_averaged_integrated_gradients = averaged_gradients * input
        
    
    return scaled_averaged_integrated_gradients

