# mlx-med

Medical Image Processing and Analysis in Python using [MLX](https://github.com/ml-explore/mlx) for Apple Silicon

## Install

```bash
pip install mlx-med
```

```python
import mlx_med
```

## Development

```bash
uv sync              # create .venv and install the package (editable) + dev tools
uv run pytest        # run tests
uv run ruff check    # lint
uv run ruff format   # format
uv build             # build sdist + wheel into dist/
```

## License

MIT — see [LICENSE](LICENSE).
