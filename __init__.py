# __init__.py - Initialize the TZOOTZ VHS Node module

from .tzoootz_vhs_node import TZOOTZ_VHSNode  # Import the main VHS effect node class

NODE_CLASS_MAPPINGS = {
    "TZOOTZ_VHSNode": TZOOTZ_VHSNode,
}

__all__ = ["TZOOTZ_VHSNode"]
