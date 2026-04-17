# Reflexión sobre `git bisect`

### 1. Cómo funciona `git bisect` y qué problema resuelve
`git bisect` es una herramienta que utiliza la búsqueda binaria para encontrar el commit exacto que introdujo un bug en el historial del repositorio. Funciona acotando el historial a la mitad iterativamente, pidiéndote (o probando automáticamente) si el estado intermedio es "bueno" o "malo". Resuelve el problema de no saber cuándo o cómo se rompió una funcionalidad que antes funcionaba correctamente, especialmente cuando han pasado decenas o cientos de commits desde la última vez que se sabe que funcionó bien.

### 2. Situación real donde sería útil
Es extremadamente útil en integraciones continuas o ramas de desarrollo largas. Por ejemplo: si estás trabajando en el frontend y descubres que un modal dejó de funcionar hace una semana, pero desde entonces ha habido 50 commits de varios desarrolladores tocando estilos, scripts y la API. Probar commit por commit sería muy tedioso, pero con `git bisect` puedes encontrar el origen del problema en solo unos 6 o 7 pasos de prueba.

### 3. Requisitos previos para que sea eficaz
- **Un historial de commits "ejecutable"**: Si la compilación o ejecución del proyecto se rompe constantemente por otras razones a lo largo del historial, no podrás probar el bug específico.
- **Tests reproducibles (idealmente automatizados)**: Es clave poder saber de manera determinista si un commit específico es "bueno" o "malo" ejecutando un comando, script o test unitario aislado.
- **Commits pequeños e independientes (atomicidad)**: Si el commit problemático que encuentra `bisect` modifica 20 archivos y agrega 1000 líneas, encontrar el error exacto seguirá siendo difícil.
