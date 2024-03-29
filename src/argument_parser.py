import argparse
import logging
import sys
from argparse import Namespace


def parse_args() -> Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="pathway_creation"
    )
    parser.add_argument("--debug", action="store_true", help="Enable debugging")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument(
        "--pathway-list", type=str, help="Input file containing pathway information"
    )
    parser.add_argument("--pathway-id", type=str, help="Single pathway ID to process")
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Output folder (default: output)",
    )

    return parser.parse_args()


# Configure the logging settings
def configure_logging(debug_flag: bool, verbose_flag: bool) -> None:
    log_level: int
    if verbose_flag:
        log_level = logging.DEBUG
    elif debug_flag:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO
    logging.basicConfig(
        filename="debug_log.txt",
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)


logger: logging.Logger = logging.getLogger(__name__)
