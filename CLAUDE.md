# SanGuoSha DIY 项目

## Python 环境（uv workspace）

仓库使用 [uv](https://docs.astral.sh/uv/) workspace 统一管理所有 Python 子包（Python 3.12）。
子包位于 `packages/` 目录下，当前子包：`packages/sgssim`。

```bash
# 首次安装 / 同步依赖（在仓库根目录）
uv sync --all-extras

# 运行子包命令（在仓库根目录或子包目录下均可）
uv run sgs-sim -n 100 -s 42
uv run sgs-run
uv run pytest packages/sgssim/tests/ -v

# 添加新子包：创建 packages/<name>/ 并在其中放 pyproject.toml
```

锁文件 `uv.lock`（根目录）需提交到版本控制。
