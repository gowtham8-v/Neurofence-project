from hooks import save_activation


def attach_hooks(model):
    """
    Attach hooks to every transformer block.
    """

    handles = []

    for i, block in enumerate(model.transformer.h):

        handle = block.register_forward_hook(
            save_activation(f"Block{i}")
        )

        handles.append(handle)

    return handles


def remove_hooks(handles):
    """
    Remove all registered hooks.
    """

    for handle in handles:
        handle.remove()