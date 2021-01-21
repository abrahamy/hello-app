from __future__ import annotations

import logging
import string
import postal.parser as parser


logger = logging.getLogger(__name__)


class ParseError(Exception):
    pass


def parse(address: str) -> tuple[str]:
    try:
        if not isinstance(address, str):
            raise TypeError("`address` is not a string.")

        parts = parser.parse_address(address)
        parts = {k: v.lower() for v, k in parts}
        house_number, street = parts["house_number"], parts["road"]

        # match input case
        words = address.translate(str.maketrans("", "", string.punctuation)).split()
        for word in words:
            lower = word.lower()
            street = street.replace(lower, word)
            house_number = house_number.replace(lower, word)

        return {"street": street, "housenumber": house_number}
    except (KeyError, TypeError, ValueError) as e:
        logger.warning(e)
        raise ParseError(f"Unable to parse address: {address}")