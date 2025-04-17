# [Número]. Nombre del Problema

**Dificultad**: ⭐  
**Lenguaje**: Python  
**Tema**: Arrays/Hash Tables  

## 🚀 Enfoque
- Explica tu solución en 2-3 líneas.  
- Ejemplo: *"Usé un hash map para almacenar complementos, reduciendo la complejidad a O(n)"*.

## 💡 Complejidad
- **Tiempo**: O(n)  
- **Espacio**: O(n)  

## 📚 Solución
```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i