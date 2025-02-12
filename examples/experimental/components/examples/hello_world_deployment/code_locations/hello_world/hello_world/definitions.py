from pathlib import Path

import dagster as dg
from dagster_components import ComponentTypeRegistry, build_component_defs
from dagster_components.core.component_key import GlobalComponentKey
from dagster_components.lib.pipes_subprocess_script_collection import (
    PipesSubprocessScriptCollection,
)

defs = build_component_defs(
    Path(__file__).parent / "components",
    registry=ComponentTypeRegistry(
        {
            GlobalComponentKey.from_typename(
                "pipes_subprocess_script_collection@here"
            ): PipesSubprocessScriptCollection
        }
    ),
)

if __name__ == "__main__":
    dg.Definitions.validate_loadable(defs)
