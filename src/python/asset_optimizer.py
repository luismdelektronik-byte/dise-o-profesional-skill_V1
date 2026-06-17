"""
Asset Optimizer Module
Optimizes HTML, CSS, images, and JavaScript for production
"""

import re
from typing import Dict, Optional
from dataclasses import dataclass
from pathlib import Path


@dataclass
class OptimizationReport:
    """Report of optimization results"""
    original_size: int
    optimized_size: int
    size_reduction: float
    speed_improvement: float
    warnings: list


class AssetOptimizer:
    """Optimizes various assets for web performance"""
    
    @staticmethod
    def minify_html(content: str) -> str:
        """Minify HTML by removing unnecessary whitespace and comments"""
        # Remove HTML comments
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        # Remove whitespace between tags
        content = re.sub(r'>\s+<', '><', content)
        # Remove extra whitespace
        content = re.sub(r'\s+', ' ', content)
        return content.strip()
    
    @staticmethod
    def minify_css(content: str) -> str:
        """Minify CSS by removing comments and whitespace"""
        # Remove comments
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        # Remove unnecessary whitespace
        content = re.sub(r'\s+', ' ', content)
        # Remove spaces around special characters
        content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', content)
        return content.strip()
    
    @staticmethod
    def add_autoprefixer(css: str) -> str:
        """Add vendor prefixes for better browser compatibility"""
        prefixes = {
            'transform': '-webkit-transform',
            'transition': '-webkit-transition',
            'animation': '-webkit-animation',
        }
        
        result = css
        for prop, prefix in prefixes.items():
            pattern = f'{prop}\\s*:'
            replacement = f'{prefix}: ; {prop}:'
            result = re.sub(pattern, replacement, result)
        
        return result
    
    @staticmethod
    def generate_optimization_report(
        original_html: str,
        original_css: str,
        optimized_html: str,
        optimized_css: str
    ) -> OptimizationReport:
        """Generate detailed optimization report"""
        original_size = len(original_html) + len(original_css)
        optimized_size = len(optimized_html) + len(optimized_css)
        
        size_reduction = ((original_size - optimized_size) / original_size) * 100
        speed_improvement = size_reduction * 0.8
        
        return OptimizationReport(
            original_size=original_size,
            optimized_size=optimized_size,
            size_reduction=size_reduction,
            speed_improvement=speed_improvement,
            warnings=[]
        )