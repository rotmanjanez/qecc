# Copyright (c) 2023 - 2026 Chair for Design Automation, TUM
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

"""Global test configuration."""

from __future__ import annotations

import os

# The plotting tests never show a figure, so keep matplotlib off the runners' GUI
# toolkits, which are not always usable (windows-2025 ships no working Tcl/Tk).
# Set through the environment rather than `matplotlib.use` so that matplotlib is
# not imported before the tests that need it.
os.environ.setdefault("MPLBACKEND", "Agg")
