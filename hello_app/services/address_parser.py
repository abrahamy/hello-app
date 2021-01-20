from __future__ import annotations

import logging
import postal.parser as parser


logger = logging.getLogger(__name__)


class ParseError(Exception):
    pass


def parse(address: str) -> tuple[str]:
    try:
        if not isinstance(address, str):
            raise TypeError("`address` is not a string.")

        parts = parser.parse_address(address)
        parts = {k: v for v, k in parts}

        house_number, street = parts["house_number"], parts["road"].lower()

        # match input case
        original_words = [i.strip() for i in address.split()]
        for word in original_words:
            street = street.replace(word.lower(), word)

        return {"housenumber": house_number, "street": street}
    except (KeyError, TypeError, ValueError) as e:
        logger.warning(e)
        raise ParseError(f"Unable to parse address: {address}")