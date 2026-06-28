# SGS Simulator

- 三国杀模拟器
- 单机，无GUI，主要供测试武将强度使用

## 安装

本项目使用 [uv](https://docs.astral.sh/uv/) workspace 管理 Python 环境。
sgssim 是 GamesDiy 仓库的子包之一，虚拟环境在仓库根目录。

```bash
# 安装 uv（如未安装）
# Windows: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# macOS/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh

# 在仓库根目录同步所有子包依赖
cd ../..  # 回到 GamesDiy/
uv sync --all-extras
```

## 命令用法

所有命令通过 `uv run` 执行（在仓库根目录或 sgssim 目录下均可）：

### `sgs-run` — 交互式运行器

启动 TUI 界面，手动开始一局游戏：

```bash
# 默认 8 人局
uv run sgs-run

# 2 人局（主公 vs 反贼）
uv run sgs-run -c builtin:rp:2

# 固定随机种子
uv run sgs-run -c builtin:rp:5 -s 42

# 查看完整帮助
uv run sgs-run --help
```

### `sgs-sim` — 批量模拟

无界面批量运行模拟，用于测试武将强度：

```bash
# 运行 1 局（默认 8 人）
uv run sgs-sim

# 运行 100 局 2 人局
uv run sgs-sim -c builtin:rp:2 -n 100

# 固定种子，方便复现
uv run sgs-sim -c builtin:rp:8 -s 42 -n 50

# 调试日志
uv run sgs-sim -l debug

# 查看完整帮助
uv run sgs-sim --help
```

### `-c / --config` 参数语法

| 格式 | 说明 |
|------|------|
| `builtin:rp:2` | 2 人局（1 主公 vs 1 反贼） |
| `builtin:rp:5` | 5 人局（1 主 + 1 忠 + 2 反 + 1 内） |
| `builtin:rp:8` | 8 人局（1 主 + 2 忠 + 4 反 + 1 内） |
| `<json-file>` | 从 JSON 文件加载配置 |

JSON 配置示例：

```json
{
    "mode": "roleplay",
    "roles": {
        "主公": 1,
        "反贼": 1
    }
}
```

## 单元测试

使用 pytest 风格，测试文件位于 `tests/` 目录。

```bash
# 在仓库根目录运行全部测试
uv run pytest packages/sgssim/tests/ -v

# 运行单个测试文件
uv run pytest packages/sgssim/tests/test_engine.py -v

# 查看覆盖率（pytest-cov 已包含在 dev 依赖中）
uv run pytest packages/sgssim/tests/ --cov=sgssim --cov-report=term-missing
```
