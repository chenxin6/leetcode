"""
自动整理 Python 类中的方法顺序

依赖：
    需要安装 libcst 库（pip install libcst）

适用场景：
    适用于需要规范化类方法顺序、提升代码可读性和维护性的场景
"""

import sys

import libcst as cst
import libcst.matchers as m


class ClassMethodSorter(cst.CSTTransformer):
    """
    一个 CSTTransformer，用于对每个类中的方法按如下规则排序：
    1. 魔法方法（即名称前后都有双下划线，如 __init__、__str__ 等），按名称排序，排在最前面；
    2. 公共方法（不以下划线开头），按名称排序，排在中间；
    3. 私有方法（以下划线开头，但不是魔法方法），按名称排序，排在最后；
    其他类成员（如属性、docstring、嵌套类等）保持原有顺序，并始终排在方法之前。
    """

    def leave_ClassDef(self, original_node, updated_node):
        """
        在离开类定义节点时，对类体中的方法按指定规则排序。
        非方法成员保持原有顺序，并排在方法之前。

        :param original_node: 原始的 ClassDef 节点
        :param updated_node: 可能已被修改的 ClassDef 节点
        :return: 排序后的新的 ClassDef 节点
        """
        # 分离方法和其他成员
        magic_methods = []
        public_methods = []
        private_methods = []
        others = []
        for stmt in updated_node.body.body:
            if m.matches(stmt, m.FunctionDef()):
                name = stmt.name.value  # type: ignore
                # 魔法方法：前后都有双下划线
                if name.startswith("__") and name.endswith("__"):
                    magic_methods.append(stmt)
                # 私有方法：以单下划线或双下划线开头，但不是魔法方法
                elif name.startswith("_"):
                    private_methods.append(stmt)
                # 公共方法：不以下划线开头
                else:
                    public_methods.append(stmt)
            else:
                others.append(stmt)
        # 分别排序
        magic_methods_sorted = sorted(magic_methods, key=lambda f: f.name.value)
        public_methods_sorted = sorted(public_methods, key=lambda f: f.name.value)
        private_methods_sorted = sorted(private_methods, key=lambda f: f.name.value)
        # 合并：其他成员 + 魔法方法 + 公共方法 + 私有方法
        new_body = (
            list(others)
            + magic_methods_sorted
            + public_methods_sorted
            + private_methods_sorted
        )
        # 返回新的类定义节点
        return updated_node.with_changes(
            body=updated_node.body.with_changes(body=new_body)
        )


def reorder_class_methods_by_type(source_code):
    """
    对给定 Python 源代码中的每个类的方法和成员按照 ClassMethodSorter 定义的规则排序

    :param source_code: 需要处理的 Python 源代码字符串
    :return: 方法已按类型排序后的新源代码字符串
    """
    tree = cst.parse_module(source_code)
    new_tree = tree.visit(ClassMethodSorter())
    return new_tree.code


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
        new_code = reorder_class_methods_by_type(code)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_code)
