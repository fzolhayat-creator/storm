"""
STORM Custom Branch v1.0
Configuration Loader

Centralized YAML configuration management.

Responsibilities:
    - Load YAML configuration files
    - Provide safe access to configuration values
    - Keep configuration logic separate from STORM components

This module does NOT:
    - Create models
    - Initialize retrievers
    - Modify generation behavior

It only provides configuration data.
"""


from pathlib import Path
import yaml

# ------------------------------------------------------------
# Repository Root Detection
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CONFIG_DIR = PROJECT_ROOT / "configs"

# ------------------------------------------------------------
# Generic YAML Loader
# ------------------------------------------------------------

def load_yaml(filename: str) -> dict:
    """
    Load YAML configuration file.

    Example:

        config = load_yaml(
            "generation_config.yaml"
        )

    """

    config_path = CONFIG_DIR / filename

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )


    with open(
        config_path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)

# ------------------------------------------------------------
# Specialized Configuration Loaders
# ------------------------------------------------------------

def load_generation_config() -> dict:
    """
    Loads generation_config.yaml
    """

    return load_yaml(
        "generation_config.yaml"
    )

def load_retrieval_config() -> dict:
    """
    Loads retrieval_config.yaml
    """

    return load_yaml(
        "retrieval_config.yaml"
    )

def load_model_config() -> dict:
    """
    Loads model_config.yaml
    """

    return load_yaml(
        "model_config.yaml"
    )

# ------------------------------------------------------------
# Convenience Helper
# ------------------------------------------------------------

def get_config_value(
    config: dict,
    *keys,
    default=None
):
    """
    Safely retrieve nested configuration values.

    Example:

        temperature = get_config_value(
            config,
            "article_generation",
            "temperature"
        )

    """

    value = config

    try:

        for key in keys:
            value = value[key]

        return value


    except (KeyError, TypeError):

        return default
