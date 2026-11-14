from importlib.metadata import version

import mlx.core as mx

import mlx_med


def test_version():
    assert mlx_med.__version__ == version("mlx-med")


def test_mlx_available():
    assert mx.array([1, 2, 3]).sum().item() == 6
