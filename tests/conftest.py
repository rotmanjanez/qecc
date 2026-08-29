# Copyright (c) 2023 - 2026 Chair for Design Automation, TUM
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

"""Global test configuration."""

from __future__ import annotations

import matplotlib

# The plotting tests only need figures to be rendered, never shown. Pinning the
# non-interactive backend keeps them off the runners' GUI toolkits, which are not
# always usable (windows-2025 ships no working Tcl/Tk).
matplotlib.use("Agg")
