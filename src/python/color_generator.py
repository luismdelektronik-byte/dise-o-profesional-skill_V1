"""
Color Palette Generator Module
Generates harmonious color palettes based on color theory
"""

import colorsys
import json
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class ColorScheme(Enum):
    """Color harmony schemes"""
    MONOCHROMATIC = "monochromatic"
    ANALOGOUS = "analogous"
    COMPLEMENTARY = "complementary"
    TRIADIC = "triadic"
    TETRADIC = "tetradic"
    SPLIT_COMPLEMENTARY = "split_complementary"


@dataclass
class Color:
    """Represents a single color in multiple formats"""
    hex: str
    rgb: Tuple[int, int, int]
    hsl: Tuple[float, float, float]
    
    def to_hex(self) -> str:
        """Convert to hex format"""
        return self.hex
    
    def to_rgb(self) -> str:
        """Convert to RGB string"""
        r, g, b = self.rgb
        return f"rgb({r}, {g}, {b})"
    
    def to_rgba(self, alpha: float = 1.0) -> str:
        """Convert to RGBA string"""
        r, g, b = self.rgb
        return f"rgba({r}, {g}, {b}, {alpha})"
    
    def to_hsl(self) -> str:
        """Convert to HSL string"""
        h, s, l = self.hsl
        return f"hsl({int(h)}, {int(s)}%, {int(l)}%)"


@dataclass
class ColorPalette:
    """Collection of colors with harmony"""
    colors: List[Color]
    scheme: ColorScheme
    base_color: str
    accessibility_report: Dict = None
    
    def export_hex(self) -> List[str]:
        """Export all colors as hex"""
        return [color.to_hex() for color in self.colors]
    
    def export_rgb(self) -> List[str]:
        """Export all colors as RGB"""
        return [color.to_rgb() for color in self.colors]
    
    def export_css_variables(self) -> str:
        """Export as CSS custom properties"""
        css = ":root {\n"
        for i, color in enumerate(self.colors):
            css += f"  --color-{i}: {color.to_hex()};\n"
        css += "}\n"
        return css
    
    def export_tailwind(self) -> Dict[str, str]:
        """Export as Tailwind config"""
        tailwind = {}
        for i, color in enumerate(self.colors):
            tailwind[f"color-{i}"] = color.to_hex()
        return tailwind
    
    def wcag_contrast_report(self) -> Dict:
        """Generate WCAG contrast accessibility report"""
        if not self.accessibility_report:
            self.accessibility_report = self._calculate_contrast()
        return self.accessibility_report
    
    def _calculate_contrast(self) -> Dict:
        """Calculate contrast ratios between colors"""
        report = {
            "scheme": self.scheme.value,
            "contrasts": []
        }
        
        for i, color1 in enumerate(self.colors):
            for j, color2 in enumerate(self.colors):
                if i < j:
                    contrast = self._contrast_ratio(color1.rgb, color2.rgb)
                    wcag_level = self._wcag_level(contrast)
                    report["contrasts"].append({
                        "color1": color1.hex,
                        "color2": color2.hex,
                        "ratio": round(contrast, 2),
                        "wcag_level": wcag_level
                    })
        
        return report
    
    @staticmethod
    def _contrast_ratio(rgb1: Tuple[int, int, int], 
                       rgb2: Tuple[int, int, int]) -> float:
        """Calculate WCAG contrast ratio"""
        l1 = ColorPaletteGenerator.luminance(rgb1)
        l2 = ColorPaletteGenerator.luminance(rgb2)
        
        lighter = max(l1, l2)
        darker = min(l1, l2)
        
        return (lighter + 0.05) / (darker + 0.05)
    
    @staticmethod
    def _wcag_level(ratio: float) -> str:
        """Determine WCAG compliance level"""
        if ratio >= 7:
            return "AAA"
        elif ratio >= 4.5:
            return "AA"
        else:
            return "Fail"


class ColorPaletteGenerator:
    """Main color palette generator"""
    
    @staticmethod
    def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
        """Convert hex to RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @staticmethod
    def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
        """Convert RGB to hex"""
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
    
    @staticmethod
    def rgb_to_hsl(rgb: Tuple[int, int, int]) -> Tuple[float, float, float]:
        """Convert RGB to HSL"""
        r, g, b = [x / 255.0 for x in rgb]
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return h * 360, s * 100, l * 100
    
    @staticmethod
    def luminance(rgb: Tuple[int, int, int]) -> float:
        """Calculate relative luminance for WCAG"""
        r, g, b = [x / 255.0 for x in rgb]
        
        def adjust(c):
            if c <= 0.03928:
                return c / 12.92
            else:
                return ((c + 0.055) / 1.055) ** 2.4
        
        return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)
    
    @staticmethod
    def generate_palette(base_color: str, 
                        scheme: str = "triadic",
                        count: int = 5) -> ColorPalette:
        """
        Generate color palette based on harmony scheme
        """
        
        # Convert to HSL
        rgb = ColorPaletteGenerator.hex_to_rgb(base_color)
        h, s, l = ColorPaletteGenerator.rgb_to_hsl(rgb)
        
        # Generate colors based on scheme
        hues = []
        scheme_enum = ColorScheme(scheme)
        
        if scheme_enum == ColorScheme.MONOCHROMATIC:
            for i in range(count):
                variation = (i - count // 2) * (20 / count)
                hues.append((h, s, max(10, min(90, l + variation))))
        
        elif scheme_enum == ColorScheme.ANALOGOUS:
            angle = 30
            for i in range(count):
                offset = (i - count // 2) * (angle / (count - 1)) if count > 1 else 0
                hues.append(((h + offset) % 360, s, l))
        
        elif scheme_enum == ColorScheme.COMPLEMENTARY:
            for i in range(count):
                if i < count // 2:
                    offset = i * (180 / (count // 2))
                else:
                    offset = 180 + (i - count // 2) * (180 / (count - count // 2))
                hues.append(((h + offset) % 360, s, l))
        
        elif scheme_enum == ColorScheme.TRIADIC:
            for i in range(count):
                offset = (i % 3) * 120 + (i // 3) * 10
                hues.append(((h + offset) % 360, s, l))
        
        elif scheme_enum == ColorScheme.TETRADIC:
            for i in range(count):
                offset = (i % 4) * 90 + (i // 4) * 5
                hues.append(((h + offset) % 360, s, l))
        
        elif scheme_enum == ColorScheme.SPLIT_COMPLEMENTARY:
            for i in range(count):
                angles = [0, 150, 210]
                offset = angles[i % 3] if i < len(angles) else 0
                hues.append(((h + offset) % 360, s, l))
        
        # Create Color objects
        colors = []
        for hsl_color in hues[:count]:
            rgb_color = ColorPaletteGenerator.hsl_to_rgb(hsl_color)
            hex_color = ColorPaletteGenerator.rgb_to_hex(rgb_color)
            color = Color(
                hex=hex_color,
                rgb=rgb_color,
                hsl=hsl_color
            )
            colors.append(color)
        
        return ColorPalette(
            colors=colors,
            scheme=scheme_enum,
            base_color=base_color
        )
    
    @staticmethod
    def hsl_to_rgb(hsl: Tuple[float, float, float]) -> Tuple[int, int, int]:
        """Convert HSL to RGB"""
        h, s, l = hsl[0] / 360, hsl[1] / 100, hsl[2] / 100
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return int(r * 255), int(g * 255), int(b * 255)


if __name__ == "__main__":
    generator = ColorPaletteGenerator()
    palette = generator.generate_palette("#3498db", "triadic", count=5)
    
    print("Triadic Palette:")
    print("HEX:", palette.export_hex())
    print("\nCSS Variables:")
    print(palette.export_css_variables())