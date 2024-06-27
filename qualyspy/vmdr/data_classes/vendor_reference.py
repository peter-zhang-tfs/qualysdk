"""
vendor_reference.py - contains the VendorReference dataclass for the Qualys VMDR module.
"""

from dataclasses import dataclass, field
from typing import *


@dataclass(frozen=True)
class VendorReference:
    """
    VendorReference - represents a single vendor bulletin reference in a ReferenceList.

    This class is used to represent a single vendor bulletin reference in a ReferenceList,
    which is used to represent the vendor bulletin references for a vulnerability.

    This class is frozen, meaning that once an object is created, it cannot be modified.
    It can be used as a key in a dictionary or as an element in a set.
    """

    ID: str = field(metadata={"description": "The ID of the vendor reference."})
    URL: str = field(
        metadata={"description": "The URL of the vendor reference."},
        default="",
        compare=False,
    )

    def __post_init__(self):
        # check that url is a string:
        if not isinstance(self.URL, str):
            raise TypeError(
                f"VendorReference URL must be a string, not {type(self.URL)}"
            )

    def __str__(self) -> str:
        return self.ID

    def __contains__(self, item):
        # see if it was found in the name or vendor:
        return item in self.ID or item in self.URL

    def copy(self):
        return VendorReference(ID=self.ID, URL=self.URL)

    def is_id(self, id: int):
        return self.ID == id

    def is_url(self, url: str):
        return self.URL == url

    @classmethod
    def from_dict(cls, data: dict):
        """
        from_dict - create a Software object from a dictionary.

        This function is used to create a Software object from a dictionary.
        """
        # make sure that the dictionary has the required keys and nothing else:
        required_keys = {"ID"}
        if not required_keys.issubset(data.keys()):
            raise ValueError(
                f"Dictionary must contain the following keys: {required_keys}"
            )

        return cls(**data)
