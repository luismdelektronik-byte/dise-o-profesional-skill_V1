# 📘 Documentación Completa - Diseño Profesional Skill

## 🎯 Propósito de la Skill

Esta skill avanzada proporciona a los desarrolladores y diseñadores herramientas profesionales para:

- ✅ Generar diseños web completos automáticamente
- ✅ Crear paletas de color inteligentes basadas en teoría del diseño
- ✅ Convertir descripciones a código HTML/CSS limpio y semántico
- ✅ Optimizar assets para máximo rendimiento
- ✅ Implementar responsive design automáticamente
- ✅ Crear animaciones CSS avanzadas
- ✅ Analizar diseños con IA para mejora continua

---

## 🎨 Módulo 1: Generador de Paletas de Color

### Características
- Generación basada en **teoría del color armónica**
- Múltiples esquemas: Monocromático, Análogo, Complementario, Triádico, Tetrádico
- Exportación en: Hex, RGB, HSL, Tailwind CSS, CSS Variables
- Análisis de contraste y accesibilidad WCAG

### Uso

```python
from src.python.color_generator import ColorPaletteGenerator

# Crear instancia
generator = ColorPaletteGenerator()

# Generar paleta triádica desde color base
palette = generator.generate_palette(
    base_color="#3498db",
    scheme="triadic",
    count=5
)

# Exportar en diferentes formatos
print(palette.export_hex())        # ["#3498db", "#db3498", ...]
print(palette.export_rgb())        # [(52, 152, 219), ...]
print(palette.export_tailwind())   # Colores Tailwind listos
print(palette.export_css_vars())   # Variables CSS

# Verificar accesibilidad
print(palette.wcag_contrast_report())
```

### Esquemas Disponibles

| Esquema | Descripción | Uso |
|---------|-------------|-----|
| **Monocromático** | Variaciones de un color | Diseños minimalistas |
| **Análogo** | Colores adyacentes en la rueda | Armonía visual suave |
| **Complementario** | Colores opuestos | Alto contraste, energía |
| **Triádico** | 3 colores equidistantes | Dinamismo equilibrado |
| **Tetrádico** | 4 colores en rectángulo | Complejidad controlada |

---

## 🖼️ Módulo 2: Integración Canva API

### Características
- Crear diseños automáticamente desde templates
- Acceso a millones de assets profesionales
- Exportación en múltiples resoluciones
- Personalizació automática de elementos

### Uso

```python
from src.python.canva_integration import CanvaDesigner

designer = CanvaDesigner(api_key="your_api_key")

# Crear diseño desde template
design = designer.create_design(
    template_id="social_media_post_1080x1080",
    elements={
        "title": "Mi Producto Increíble",
        "subtitle": "Descubre la innovación",
        "background_color": "#3498db"
    }
)

# Exportar en alta resolución
design.export_png(resolution="4k", filename="design.png")
design.export_pdf(filename="design.pdf")

# Obtener URL para compartir
share_url = design.get_share_url()
```

### Templates Disponibles
- Social Media Posts (Instagram, Twitter, LinkedIn, Facebook)
- Presentations
- Business Cards
- Flyers
- Posters
- Banners
- Email Headers

---

## 💻 Módulo 3: Generador de Código HTML/CSS

### Características
- Convierte descripciones naturales a código limpio
- Genera componentes reutilizables
- Código semántico y accesible (WCAG AA)
- Integración automática de Google Fonts

### Uso

```python
from src.python.design_generator import CodeGenerator

generator = CodeGenerator()

# Generar HTML/CSS desde descripción
code = generator.generate_from_description(
    description="""
    Crear una tarjeta de producto con:
    - Imagen redondeada en la parte superior
    - Título en negrita
    - Descripción de 2 líneas máximo
    - Precio destacado en rojo
    - Botón \"Agregar al carrito\" en azul
    """,
    component_name="ProductCard",
    framework="tailwind"  # o "bootstrap", "plain-css"
)

print(code.html)
print(code.css)
print(code.javascript)
```

### Frameworks Soportados
- **Tailwind CSS** - Utility-first, muy moderno
- **Bootstrap** - Completo y ampliamente usado
- **CSS Puro** - Flexbox/Grid, sin dependencias
- **Material Design** - Componentes Material

---

## 📱 Módulo 4: Responsive Design Automation

### Características
- Breakpoints automáticos e inteligentes
- Media queries generadas automáticamente
- Grillas fluidas (CSS Grid + Flexbox)
- Optimización para todos los dispositivos

### Breakpoints Predeterminados

```css
/* Mobile First */
/* xs */ 320px
/* sm */ 640px (tablets pequeñas)
/* md */ 768px (tablets)
/* lg */ 1024px (laptops)
/* xl */ 1280px (desktops)
/* 2xl */ 1536px (4K)
```

### Uso

```python
from src.python.responsive_builder import ResponsiveBuilder

builder = ResponsiveBuilder()

# Generar layout responsive automático
layout = builder.create_responsive_layout(
    structure="3-column-grid",
    breakpoints=["xs", "sm", "md", "lg", "xl"],
    gaps="2rem"
)

# Personalizar para cada breakpoint
layout.set_columns(breakpoint="xs", columns=1)  # Mobile: 1 columna
layout.set_columns(breakpoint="md", columns=2)  # Tablet: 2 columnas
layout.set_columns(breakpoint="lg", columns=3)  # Desktop: 3 columnas

print(layout.generate_css())
print(layout.generate_html())
```

---

## ✨ Módulo 5: Animaciones CSS Avanzadas

### Características
- Biblioteca de 100+ animaciones profesionales
- Sincronización automática con eventos
- Performance optimizado (GPU-accelerated)
- Parámetros configurables

### Animaciones Disponibles

| Categoría | Ejemplos |
|-----------|----------|
| **Entrada** | fadeIn, slideIn, zoomIn, rotateIn |
| **Salida** | fadeOut, slideOut, zoomOut, rotateOut |
| **Atención** | bounce, pulse, shake, swing, wobble |
| **Transición** | flip, fold, roll, spin, zoom |
| **Complejas** | staggered, cascade, morph, morphing |

### Uso

```python
from src.python.animation_library import AnimationLibrary

anim = AnimationLibrary()

# Crear animación personalizada
animation = anim.create_animation(
    name="fade-slide-in",
    duration="0.8s",
    delay="0.2s",
    easing="ease-out-cubic",
    iterations="once"
)

# Agregar keyframes
animation.add_keyframe(percent=0, properties={"opacity": 0, "transform": "translateX(-20px)"})
animation.add_keyframe(percent=100, properties={"opacity": 1, "transform": "translateX(0)"})

print(animation.generate_css())

# Usar en elemento
element_css = anim.apply_animation_to_element(
    selector=".card",
    animation=animation,
    trigger="on-scroll"  # o "on-hover", "on-click", "on-load"
)
```

### Generador Rápido

```python
# Generar animación estándar
css = anim.quick_animation("bounceIn", duration="0.6s")
# Resultado: @keyframes bounceIn { ... }
```

---

## 🚀 Módulo 6: Optimización de Assets

### Características
- **HTML**: Minificación, compresión, eliminación de comentarios
- **CSS**: Tree-shaking, minificación, autoprefixer
- **Imágenes**: Conversión a WebP/AVIF, compresión sin pérdida
- **JavaScript**: Minificación, code splitting
- **Lazy Loading**: Implementación automática

### Uso

```python
from src.python.asset_optimizer import AssetOptimizer

optimizer = AssetOptimizer()

# Minificar HTML
optimizer.minify_html("index.html", output="index.min.html")

# Minificar CSS
optimizer.minify_css("styles.css", output="styles.min.css")
optimizer.add_autoprefixer("styles.css")

# Optimizar imágenes
optimizer.convert_images(
    source_dir="images/",
    target_format="webp",  # o "avif"
    quality=0.8,
    output_dir="images/optimized/"
)

# Lazy loading
optimizer.add_lazy_loading("index.html", output="index.lazy.html")

# Reporte de optimización
report = optimizer.generate_optimization_report()
print(f"Reducción de tamaño: {report.size_reduction}%")
print(f"Mejora de velocidad: {report.speed_improvement}%")
```

### Resultados Típicos
- **HTML**: 40-60% reducción de tamaño
- **CSS**: 35-50% reducción
- **Imágenes**: 60-80% reducción (WebP)
- **Velocidad de carga**: +30-50% más rápido

---

## 👁️ Módulo 7: Análisis de Diseños con IA

### Características
- Análisis de accesibilidad (WCAG)
- Evaluación de UX/UI
- Sugerencias de mejora automáticas
- Análisis de tipografía y color
- Reporte detallado

### Uso

```python
from src.python.design_analyzer import DesignAnalyzer

analyzer = DesignAnalyzer()

# Analizar imagen de diseño
analysis = analyzer.analyze_image("design.png")

# Accesibilidad
print(f"Puntuación WCAG: {analysis.wcag_score}/100")
print(f"Contraste: {analysis.contrast_issues}")
print(f"Recomendaciones: {analysis.accessibility_recommendations}")

# Diseño y UX
print(f"Puntuación de Diseño: {analysis.design_score}/100")
print(f"Análisis de Tipografía: {analysis.typography_analysis}")
print(f"Análisis de Color: {analysis.color_analysis}")

# Recomendaciones
for rec in analysis.design_recommendations:
    print(f"- {rec.category}: {rec.message}")

# Exportar reporte
analysis.export_report("design_analysis.pdf")
```

### Aspectos Analizados
- ✅ Contraste de colores
- ✅ Jerarquía visual
- ✅ Tipografía legible
- ✅ Espaciado y alineación
- ✅ Responsive compatibility
- ✅ Accesibilidad WCAG
- ✅ Performance

---

## 🔌 Módulo 8: Integraciones Externas

### 1. Canva API
```python
designer = CanvaDesigner(api_key="xxx")
design = designer.create_design(template_id="xxx")
```

### 2. Unsplash / Pexels
```python
from src.python.image_provider import ImageProvider

provider = ImageProvider()
images = provider.search("mountain landscape", source="unsplash")
image_url = images[0].download_high_res()
```

### 3. Google Fonts
```python
from src.python.font_provider import FontProvider

fonts = FontProvider()
font = fonts.get_font("Roboto", weights=[400, 700, 900])
css_import = font.get_css_import()
```

### 4. Icon Libraries
```python
from src.python.icon_provider import IconProvider

icons = IconProvider()
icon = icons.get_icon("heart", library="fontawesome", size="2x")
html = icon.to_html()
```

### 5. Claude Vision
```python
from src.python.design_analyzer import DesignAnalyzer

analyzer = DesignAnalyzer()  # Usa Claude Vision internamente
analysis = analyzer.analyze_image("design.png")
```

---

## 🌐 Módulo 9: Java Integration

### DesignGenerator.java
```java
DesignGenerator generator = new DesignGenerator();
Design design = generator.generateFromDescription(
    "Card component with image and title",
    Framework.TAILWIND
);
System.out.println(design.getHtml());
System.out.println(design.getCss());
```

### CanvaIntegration.java
```java
CanvaIntegration canva = new CanvaIntegration("api_key");
DesignProject project = canva.createDesign("template_id");
project.exportToPNG("output.png", Resolution.HIGH_RES);
```

### ResponsiveBuilder.java
```java
ResponsiveBuilder builder = new ResponsiveBuilder();
ResponsiveLayout layout = builder.createGrid(3, Breakpoint.MOBILE_FIRST);
layout.setColumns(Breakpoint.XS, 1);
layout.setColumns(Breakpoint.MD, 2);
layout.setColumns(Breakpoint.LG, 3);
```

---

## 📊 Workflows Completos

### Workflow 1: Crear Landing Page Completa

```python
from src.python.color_generator import ColorPaletteGenerator
from src.python.design_generator import CodeGenerator
from src.python.responsive_builder import ResponsiveBuilder
from src.python.asset_optimizer import AssetOptimizer

# 1. Generar paleta de color
palette_gen = ColorPaletteGenerator()
palette = palette_gen.generate_palette("#FF6B6B", "triadic")

# 2. Generar código
code_gen = CodeGenerator()
code = code_gen.generate_from_description("""
    Landing page profesional con:
    - Header con navegación
    - Hero section grande
    - 3 características destacadas
    - Call-to-action button
    - Footer con redes sociales
""", framework="tailwind")

# 3. Hacer responsive
builder = ResponsiveBuilder()
responsive_code = builder.apply_responsive_design(code)

# 4. Optimizar
optimizer = AssetOptimizer()
optimizer.minify_html(code.html, "index.html")
optimizer.minify_css(code.css, "styles.css")

# 5. Resultado final
print("✅ Landing page lista para producción")
```

### Workflow 2: Optimizar Diseño Existente

```python
from src.python.design_analyzer import DesignAnalyzer
from src.python.asset_optimizer import AssetOptimizer

# 1. Analizar
analyzer = DesignAnalyzer()
analysis = analyzer.analyze_image("current_design.png")

# 2. Obtener recomendaciones
for rec in analysis.design_recommendations:
    print(f"📝 {rec.message}")

# 3. Optimizar
optimizer = AssetOptimizer()
optimizer.convert_images("images/", target_format="webp")
optimizer.minify_html("index.html")

print(f"✅ Mejora de velocidad: +{analysis.potential_speed_gain}%")
```

---

## 🔧 Configuración Inicial

### 1. Variables de Entorno (.env)

```env
# Canva
CANVA_API_KEY=your_api_key
CANVA_API_SECRET=your_api_secret

# Unsplash
UNSPLASH_API_KEY=your_api_key

# Pexels
PEXELS_API_KEY=your_api_key

# Google Fonts
GOOGLE_FONTS_API_KEY=your_api_key

# Claude
CLAUDE_API_KEY=your_api_key
```

### 2. Instalación Python

```bash
pip install -r src/python/requirements.txt
```

### 3. Instalación Java

```bash
cd src/java
mvn clean install
```

---

## 📚 Ejemplos Avanzados

Ver carpeta `/examples` para:
- Landing pages completas
- E-commerce sites
- Portfolios profesionales
- Dashboards interactivos
- Aplicaciones web progresivas

---

## 🚀 Casos de Uso

| Caso de Uso | Módulos Usados |
|------------|------------------|
| Crear sitio web desde cero | Colores + Generador + Responsive + Optimización |
| Mejorar diseño existente | Analizador + Recomendaciones |
| Generar assets rápidamente | Canva + Unsplash + Fonts |
| Optimizar velocidad | Asset Optimizer + Lazy Loading |
| Cumplir WCAG | Analizador + Recomendaciones |
| Crear componentes | Generador + Animaciones |

---

## ✅ Checklist de Calidad

- ✅ Código limpio y documentado
- ✅ Tests unitarios incluidos
- ✅ Accesibilidad WCAG AA
- ✅ Performance optimizado
- ✅ Seguridad de APIs
- ✅ Ejemplos funcionales
- ✅ Documentación completa

---

## 📞 Soporte

Para preguntas, reportar bugs o sugerir mejoras:
- Abre un issue en GitHub
- Revisa la documentación en `/docs`
- Consulta los ejemplos en `/examples`

---

**Última actualización:** Junio 2026  
**Versión:** 1.0.0  
**Autor:** @luismdelektronik-byte