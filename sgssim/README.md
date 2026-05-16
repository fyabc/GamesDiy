# SGS Simulator

- 三国杀模拟器
- 单机，无GUI，主要供测试武将强度使用

## 安装

```bash
pip install -e .
```

## 命令用法

### `sgs-run` — 交互式运行器

启动 TUI 界面，手动开始一局游戏：

```bash
# 默认 8 人局
sgs-run

# 2 人局（主公 vs 反贼）
sgs-run -c builtin:rp:2

# 固定随机种子
sgs-run -c builtin:rp:5 -s 42

# 查看完整帮助
sgs-run --help
```

### `sgs-sim` — 批量模拟

无界面批量运行模拟，用于测试武将强度：

```bash
# 运行 1 局（默认 8 人）
sgs-sim

# 运行 100 局 2 人局
sgs-sim -c builtin:rp:2 -n 100

# 固定种子，方便复现
sgs-sim -c builtin:rp:8 -s 42 -n 50

# 调试日志
sgs-sim -l debug

# 查看完整帮助
sgs-sim --help
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
# 安装测试依赖
pip install -e ".[dev]"

# 运行全部测试
pytest tests/ -v

# 运行单个测试文件
pytest tests/test_engine.py -v

# 查看覆盖率
pip install pytest-cov
pytest tests/ --cov=sgssim --cov-report=term-missing
```
