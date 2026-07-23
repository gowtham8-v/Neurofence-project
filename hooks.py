import torch

# Dictionary to store activations
activations = {}


def save_activation(layer_name):
    """
    Creates a forward hook that stores the output of a layer.
    """

    def hook(module, inputs, output):

        if isinstance(output, tuple):
            tensor = output[0]
        else:
            tensor = output

        activations[layer_name] = tensor.detach().cpu()

    return hook