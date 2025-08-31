"""
UI Package for Resume Analyzer

This package contains all UI-related components for the Resume Analyzer application:
- styles.py: Custom CSS and theme configuration
- components.py: Reusable UI components and widgets
- theme_manager.py: Dark/Light mode theme management
- layout.py: Page layouts and section management (future)

Usage:
    from ui.styles import load_custom_css
    from ui.components import render_header, render_upload_section
    from ui.theme_manager import initialize_theme, render_theme_toggle
"""

__version__ = "1.0.0"
__all__ = ["styles", "components", "theme_manager"]