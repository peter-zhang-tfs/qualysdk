"""
software.py - contains the Software dataclass for the Qualys VMDR module.
"""

from dataclasses import dataclass, field
from typing import *


@dataclass(frozen=True)
class Software:
    """
    Software - represents a single software entry in a SoftwareList.

    This class is used to represent a single software entry in a SoftwareList,
    which is used to represent the software that is affected by a vulnerability.

    This class is frozen, meaning that once an object is created, it cannot be modified.
    It can be used as a key in a dictionary or as an element in a set.
    """

    PRODUCT: str = field(metadata={"description": "The name of the software."})
    VENDOR: str = field(
        metadata={"description": "The vendor of the software."},
        default="",
        compare=False,
    )

    def __str__(self):
        return self.PRODUCT

    def __contains__(
        self, item
    ):  # allows us to use the 'in' operator. for example, 'if "Adobe" in software'. this is a fuzzy search.
        # see if it was found in the name or vendor:
        return item in self.PRODUCT or item in self.VENDOR

    def copy(self):
        return Software(PRODUCT=self.PRODUCT, VENDOR=self.VENDOR)

    def is_vendor(self, vendor: str):
        return self.VENDOR.lower() == vendor.lower()

    def is_name(self, product: str):
        return self.PRODUCT.lower() == product.lower()

    @classmethod
    def from_dict(cls, data: Union[dict, list]):
        """
        from_dict - create a Software object from a dictionary.

        This function is used to create a Software object from a dictionary.
        """
        # make sure that the dictionary has the required keys and nothing else:
        required_keys = {"PRODUCT", "VENDOR"}

        if not required_keys.issubset(data.keys()):
            raise ValueError(
                f"Dictionary must contain the following keys: {required_keys}"
            )

        return cls(**data)
