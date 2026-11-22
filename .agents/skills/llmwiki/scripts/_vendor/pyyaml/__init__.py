"""Loading-only interface for the bundled PyYAML 6.0.3 parser.

The eleven parser modules are unchanged upstream sources. This local
interface omits emitters, dumpers, and the optional LibYAML extension.
See LICENSE and ../NOTICE.md for attribution and source details.
"""

from .error import YAMLError
from .loader import SafeLoader


def load(stream, Loader=SafeLoader):
    loader = Loader(stream)
    try:
        return loader.get_single_data()
    finally:
        loader.dispose()
