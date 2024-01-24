# cb-palettes
A collection of cb-friendly color palettes

## Installation

```
$ git clone https://github.com/tjkessler/cb-palettes
$ cd cb-palettes
$ pip install .
```

## Built-in palettes:

### Paul Tol: bright

![tolbright](./docs/img/tolbright.png)

```python
from cb_palettes import TolBright

colors_hex: Tuple[str] = TolBright().hex
colors_hsv: Tuple[Tuple[float]] = TolBright().hsv
colors_rgb: Tuple[Tuple[int]] = TolBright().rgb
colors_rgb_norm: Tuple[Tuple[float]] = TolBright().rgb_norm
```

### Paul Tol: dark

![toldark](./docs/img/toldark.png)

```python
from cb_palettes import TolDark

colors_hex: Tuple[str] = TolDark().hex
colors_hsv: Tuple[Tuple[float]] = TolDark().hsv
colors_rgb: Tuple[Tuple[int]] = TolDark().rgb
colors_rgb_norm: Tuple[Tuple[float]] = TolDark().rgb_norm
```

### Paul Tol: high contrast

![tolhighcontrast](./docs/img/tolhighcontrast.png)

```python
from cb_palettes import TolHighContrast

colors_hex: Tuple[str] = TolHighContrast().hex
colors_hsv: Tuple[Tuple[float]] = TolHighContrast().hsv
colors_rgb: Tuple[Tuple[int]] = TolHighContrast().rgb
colors_rgb_norm: Tuple[Tuple[float]] = TolHighContrast().rgb_norm
```

### Paul Tol: light

![tollight](./docs/img/tollight.png)

```python
from cb_palettes import TolLight

colors_hex: Tuple[str] = TolLight().hex
colors_hsv: Tuple[Tuple[float]] = TolLight().hsv
colors_rgb: Tuple[Tuple[int]] = TolLight().rgb
colors_rgb_norm: Tuple[Tuple[float]] = TolLight().rgb_norm
```

### Paul Tol: medium contrast

![tolmediumcontrast](./docs/img/tolmediumcontrast.png)

```python
from cb_palettes import TolMediumContrast

colors_hex: Tuple[str] = TolMediumContrast().hex
colors_hsv: Tuple[Tuple[float]] = TolMediumContrast().hsv
colors_rgb: Tuple[Tuple[int]] = TolMediumContrast().rgb
colors_rgb_norm: Tuple[Tuple[float]] = TolMediumContrast().rgb_norm
```

### Paul Tol: muted

![tolmuted](./docs/img/tolmuted.png)

```python
from cb_palettes import TolMuted

colors_hex: Tuple[str] = TolMuted().hex
colors_hsv: Tuple[Tuple[float]] = TolMuted().hsv
colors_rgb: Tuple[Tuple[int]] = TolMuted().rgb
colors_rgb_norm: Tuple[Tuple[float]] = TolMuted().rgb_norm
```

### Paul Tol: pale

![tolpale](./docs/img/tolpale.png)

```python
from cb_palettes import TolPale

colors_hex: Tuple[str] = TolPale().hex
colors_hsv: Tuple[Tuple[float]] = TolPale().hsv
colors_rgb: Tuple[Tuple[int]] = TolPale().rgb
colors_rgb_norm: Tuple[Tuple[float]] = TolPale().rgb_norm
```

### Paul Tol: vibrant

![tolvibrant](./docs/img/tolvibrant.png)

```python
from cb_palettes import TolVibrant

colors_hex: Tuple[str] = TolVibrant().hex
colors_hsv: Tuple[Tuple[float]] = TolVibrant().hsv
colors_rgb: Tuple[Tuple[int]] = TolVibrant().rgb
colors_rgb_norm: Tuple[Tuple[float]] = TolVibrant().rgb_norm
```
