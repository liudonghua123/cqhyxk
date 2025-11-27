# cqhyxk SDK

身份中台V2.0 OpenAPI 的 Python SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/pypi/pyversions/cqhyxk)](https://pypi.org/project/cqhyxk/)

## 概述

此 SDK 提供了一个 Python 接口，用于与身份中台V2.0 API 进行交互，允许您以编程方式管理人员、组织、标签和事件订阅。

SDK 提供以下功能：

- **类型安全**: 所有请求和响应都通过 Pydantic 模型进行验证
- **环境配置**: 从环境变量加载凭据
- **完整 API 覆盖**: 包含 OpenAPI 规范中的所有端点
- **错误处理**: 使用自定义异常进行全面错误处理
- **文档**: 为所有方法提供详细文档

## 安装

使用 pip 安装包：

```bash
pip install cqhyxk
```

或使用 uv：

```bash
uv pip install cqhyxk
```

## 快速开始

1. **通过创建 `.env` 文件设置环境变量**（参见 `.env.example`）：

    ```env
    CQHYXK_BASEURL=https://your-domain/backend/school-platform/openapi
    CQHYXK_APP_KEY=your_app_key_here
    CQHYXK_APP_SECRET=your_app_secret_here
    ```

2. **初始化客户端并进行 API 调用**：

    ```python
    from cqhyxk import CqhyxkClient
    from cqhyxk.models import IdentityPageRequest

    # 初始化客户端（凭据从环境变量加载）
    client = CqhyxkClient()

    # 示例：获取前 10 个身份信息
    request = IdentityPageRequest(current=0, size=10)
    response = client.get_identity_list(request)
    
    print(f"检索到 {len(response.data.content)} 个身份信息")
    for identity in response.data.content:
        print(f"- {identity.name} ({identity.sourceUserId})")
    ```

## 配置

SDK 支持通过环境变量进行配置：

- `CQHYXK_BASEURL`: API 的基础 URL（默认值：`https://your-domain/backend/school-platform/openapi`）
- `CQHYXK_APP_KEY`: 用于 API 身份验证的应用程序密钥
- `CQHYXK_APP_SECRET`: 用于 API 身份验证的应用程序密钥

您也可以直接将这些值传递给构造函数：

```python
client = CqhyxkClient(
    app_key="your_app_key",
    app_secret="your_app_secret", 
    base_url="https://your-api-domain.com"
)
```

## 可用方法

### 人员方法

- `get_identity_list(request)`: 获取人员身份信息的分页列表
- `get_face_photos(source_user_id)`: 根据学工号获取人脸照片

### 组织方法

- `get_org_list(physical, internal, org_id)`: 获取组织列表

### 标签方法

- `get_tag_list(tag_id)`: 获取标签列表
- `get_member_tags_page(request)`: 获取人员标签关系的分页列表

### 事件订阅方法

- `add_subscription(request)`: 订阅事件
- `cancel_subscription(event_type)`: 取消事件订阅

有关每个方法的详细文档，包括参数和响应格式，请查看源代码中的文档字符串。

## 示例

运行示例脚本来查看 SDK 的实际效果：

```bash
python example.py
```

在运行示例之前，请确保已正确配置环境变量。

## 开发

以开发模式安装包：

```bash
git clone https://github.com/liudonghua123/cqhyxk.git
cd cqhyxk
pip install -e .
```

或使用 uv：

```bash
uv pip install -e .
```

## 贡献

1. Fork 仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 进行更改
4. 如适用，添加测试
5. 提交更改 (`git commit -m 'Add some amazing feature'`)
6. 推送到分支 (`git push origin feature/amazing-feature`)
7. 打开 Pull Request

## 许可证

此项目根据 MIT 许可证授权 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 支持

如果您遇到任何问题，请在 GitHub 仓库中提交错误报告或联系维护者。

## API 文档

有关详细 API 文档，请参阅 [原始 OpenAPI 规范](docs/cqhyxk_OpenAPI_v2.4.md)。