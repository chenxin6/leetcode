## 1. 开发环境 Get Started
### 1.1 使用 Anaconda 安装 python 3.13

```
conda remove -n py313 --all
conda create -n py313 python=3.13
source activate py313
```

### 1.2 安装 VS Code 插件

详见文件 .vscode/extensions.json 中的 recommendations 配置

### 1.3 设置 VS Code

详见文件 .vscode/setting.json

### 1.4 依赖管理 poetry

```
python -m pip install poetry==2.4.1
poetry install --no-root
```

### 1.5 pre-commit

```
# Install pre-commit
python -m pip install pre-commit
# Install libcst (only-binary if you don't have rust compiler)
python -m pip install --only-binary=:all: libcst
# Execute below command at root directory to install git hooks into your `.git/` directory.
pre-commit install --config ./.pre-commit-config.yaml
```


## 2. 代码风格
### 规则

- 必须按照该文档的 `开发环境 Get Started` 准备好开发环境
- VS Code 飘红提示必须解决，遇到 python 语言特性导致的飘红可以使用 `# type: ignore` 或 `# pylint: disable=W0212` 忽略
- 函数的出入参必须要有类型声明
- 写注释时，字母和汉字之间需要有一个空格

### 目录结构

- .vscode
    - extensions.json：vscode 插件的推荐配置
    - setting.json：vscode 项目的整体配置
- hook：commit 的钩子脚本
- interview：面试时的答题
- src：leetcode 的答题
- .gitignore：git 忽略提交的规则
- .pre-commit-config.yaml：pre-commit 的配置
- poetry.lock：poetry lock 文件
- pyproject.toml：project 依赖包的配置
- README.md：该文档


## 其他
### poetry 的注意事项

其他可能会用到的命令

```
# 增加依赖
poetry add {依赖名}
 
# 安装依赖
poetry install

# 更新依赖
poetry update {依赖名}

# 删除依赖
poetry remove {依赖名}

# 环境信息
poetry env info

# 展示依赖版本
poetry show -t
```

如果 poetry.lock 文件冲突，应该删除 `rm poetry.lock` 并使用 `poetry update` 重新生成 poetry.lock 文件

### sdk 开发和发版（以 wxms 为例，暂时用不到发版）

```
# 开发 sdk 时为了解决 python 项目的路径问题，需要运行下面这个命令（**千万注意修改的代码是不是该项目中的代码**）
pip install -e ./sdk-wxms

# sdk 发版
cd ./sdk-wxms
vi pyproject.toml # 修改 sdk pyproject.toml 的 version
./build.sh

# 修改项目中使用的 sdk 版本
vi pyproject.toml # 修改 pyproject.toml sdk 的 version
rm poetry.lock
poetry update
# 推送代码即可自动触发镜像构建
```
