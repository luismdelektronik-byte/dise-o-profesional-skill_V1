"""
Design Generator Module
Converts natural language descriptions to clean HTML/CSS code
"""

from typing import Optional, Dict, List
from dataclasses import dataclass
from enum import Enum
import json


class Framework(Enum):
    """Supported CSS frameworks"""
    TAILWIND = "tailwind"
    BOOTSTRAP = "bootstrap"
    PLAIN_CSS = "plain_css"
    MATERIAL = "material"


@dataclass
class GeneratedCode:
    """Container for generated HTML, CSS, and JS"""
    html: str
    css: str
    javascript: str = ""
    framework: Framework = Framework.TAILWIND
    component_name: str = ""
    
    def to_html_file(self) -> str:
        """Generate complete HTML file"""
        html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.component_name}</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700;900&display=swap" rel="stylesheet">
"""
        
        if self.framework == Framework.TAILWIND:
            html += '    <script src="https://cdn.tailwindcss.com"></script>\n'
        elif self.framework == Framework.BOOTSTRAP:
            html += '    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">\n'
        
        html += """    <style>
""" + self.css + """
    </style>
</head>
<body>
""" + self.html + """
"""
        
        if self.javascript:
            html += """    <script>
""" + self.javascript + """
    </script>
"""
        
        html += """</body>
</html>"""
        
        return html


class DesignGenerator:
    """Generates HTML/CSS from natural language descriptions"""
    
    # Template components
    TEMPLATES = {
        "product_card": {
            "html": """<div class="product-card">
    <img src="{{image_url}}" alt="{{product_name}}" class="product-image">
    <h3 class="product-title">{{product_name}}</h3>
    <p class="product-description">{{description}}</p>
    <div class="product-footer">
        <span class="product-price">${{price}}</span>
        <button class="btn-add">Agregar</button>
    </div>
</div>""",
            "css_tailwind": """
.product-card {
    @apply bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow overflow-hidden;
}
.product-image {
    @apply w-full h-48 object-cover;
}
.product-title {
    @apply text-lg font-bold p-4 text-gray-900;
}
.product-description {
    @apply text-sm text-gray-600 px-4;
}
.product-footer {
    @apply flex justify-between items-center p-4 bg-gray-50;
}
.product-price {
    @apply text-2xl font-bold text-red-600;
}
.btn-add {
    @apply bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition;
}"""
        },
        "hero_section": {
            "html": """<section class="hero">
    <div class="hero-content">
        <h1 class="hero-title">{{title}}</h1>
        <p class="hero-subtitle">{{subtitle}}</p>
        <button class="btn-primary">{{cta_text}}</button>
    </div>
    <img src="{{background_image}}" alt="Hero" class="hero-background">
</section>""",
            "css_tailwind": """
.hero {
    @apply relative w-full h-screen flex items-center justify-center overflow-hidden;
}
.hero-background {
    @apply absolute inset-0 w-full h-full object-cover -z-10;
}
.hero-content {
    @apply text-center text-white z-10 max-w-2xl;
}
.hero-title {
    @apply text-5xl md:text-6xl font-bold mb-4;
}
.hero-subtitle {
    @apply text-xl md:text-2xl mb-8 opacity-90;
}
.btn-primary {
    @apply bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 transition;
}"""
        }
    }
    
    @staticmethod
    def generate_from_description(
        description: str,
        component_name: str = "Component",
        framework: str = "tailwind"
    ) -> GeneratedCode:
        """
        Generate HTML/CSS from natural language description
        """
        
        framework_enum = Framework(framework)
        
        # Analyze description to determine component type
        desc_lower = description.lower()
        
        if "product" in desc_lower and "card" in desc_lower:
            template = DesignGenerator.TEMPLATES["product_card"]
        elif "hero" in desc_lower or "banner" in desc_lower:
            template = DesignGenerator.TEMPLATES["hero_section"]
        else:
            template = {"html": "<div>Component</div>", "css_tailwind": ".component { }", "javascript": ""}
        
        return GeneratedCode(
            html=template.get("html", ""),
            css=template.get("css_" + framework, ""),
            javascript=template.get("javascript", ""),
            framework=framework_enum,
            component_name=component_name
        )


if __name__ == "__main__":
    generator = DesignGenerator()
    code = generator.generate_from_description(
        "Create a product card with image and title",
        component_name="ProductCard",
        framework="tailwind"
    )
    print(code.to_html_file())