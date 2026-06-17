# 📚 Ejemplos de Uso - Diseño Profesional Skill

Esta carpeta contiene ejemplos completos de cómo usar la skill para crear diferentes tipos de proyectos web.

## 📁 Estructura

```
examples/
├── landing-page/          # Landing page profesional
├── ecommerce-site/        # Sitio de e-commerce
├── portfolio/             # Portfolio personal
├── dashboard/             # Dashboard interactivo
└── responsive-components/ # Componentes responsive
```

## 🚀 Proyectos Incluidos

### 1. Landing Page
Ejemplo de landing page moderna con:
- Hero section
- Features section
- Call-to-action
- Footer
- Responsive design

### 2. E-commerce Site
Sitio de tienda online con:
- Product grid
- Shopping cart
- Filtros
- Checkout

### 3. Portfolio
Portfolio profesional con:
- About section
- Proyectos showcase
- Skills
- Contact form

### 4. Dashboard
Dashboard interactivo con:
- Charts y gráficos
- Data tables
- KPIs
- Real-time updates

## 📖 Cómo Usar

```python
from src.python.color_generator import ColorPaletteGenerator
from src.python.design_generator import DesignGenerator

# Crear paleta
palette_gen = ColorPaletteGenerator()
palette = palette_gen.generate_palette("#FF6B6B", "triadic")

# Generar código
designer = DesignGenerator()
code = designer.generate_from_description(
    "Create a professional landing page",
    framework="tailwind"
)
```

## 💡 Tips

- Combina diferentes módulos para máximos resultados
- Usa paletas armónicas para mejor visual
- Siempre optimiza assets antes de producción
- Valida accesibilidad WCAG

## 📞 Soporte

Para dudas sobre los ejemplos, consulta la documentación principal en `/docs/SKILL.md`