#!/usr/bin/env python3
# ./build_executable.py

"""
Builds the standalone binary using maxson_build_utils.
"""

from __future__ import annotations

from cellshift._version import __version__
from cellshift.context import APP_NAME_PRETTY, SRC_FOLDER_NAME
from cellshift.paths import get_icns_icon, get_ico_icon, get_png_icon
from maxson_build_utils.build_executable import run_build_executable

if __name__ == "__main__":
    run_build_executable(
        src_folder_name=SRC_FOLDER_NAME,
        version=__version__,
        app_name_pretty=APP_NAME_PRETTY,
        icon_png_path=get_png_icon(),
        icon_ico_path=get_ico_icon(),
        icon_icns_path=get_icns_icon(),
        collect_data_pkgs=[SRC_FOLDER_NAME],
        collect_binary_pkgs=[],
    )