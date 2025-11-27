# 身份中台V2.0 OpenAPI接口文档
## 文档概述
### 适用范围
本手册专门针对身份中台V2.0开放接口对接提供指导。

### 目标读者
- 第三方开发者
- 合作伙伴技术团队

## 接入说明
### 接入流程
1. 获取测试AppKey和AppSecret；
2. 按照接口文档进行对接；
3. 使用测试环境联调验证接口；
4. 联系管理员创建正式合作方，对其进行相关API接口授权，获取到AppKey和AppSecret；
5. 线上环境验证。

### 通用说明
#### 请求基础地址
`域名/backend/school-platform/openapi`

#### 通用请求头
| 字段名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| app-secret | string | 是 | 应用密钥 |
| app-key | string | 是 | 应用标识 |
| Content-Type | string | 是 | application/json |

#### 通用响应结构
```json
{
  "code": "00000000",
  "message": "请求成功", 
  "data": {}
}
```

#### 响应参数说明
| 参数名称 | 参数说明 | 类型 |
| --- | --- | --- |
| code | 状态码 | string |
| message | 状态描述 | string |
| data | 响应数据，根据接口不同返回不同结构 | object |

#### 状态码说明
- 200（代码 00000000）：请求成功；
- 其他错误码见各接口返回结果说明。

## 接口列表
### 人员相关接口
#### 人员身份信息分页列表
- 接口地址: `/open-api/member/identity/page`
- 请求方式: POST
- 请求数据类型: application/x-www-form-urlencoded, application/json
- 响应数据类型: */*

##### 请求示例
```json
{
  "current": 0,
  "size": 0,
  "updateTimeStart": "",
  "updateTimeEnd": "",
  "sourceUserId": ""
}
```

##### 请求参数
| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
| --- | --- | --- | --- | --- |
| request | 人员身份信息分页查询请求参数 | body | true | object |
| current | 当前页 | - | false | integer(int64) |
| size | 页面大小，默认 10 | - | false | integer(int64) |
| sourceUserId | 源系统用户 id（学工号） | - | false | string |
| updateTimeStart | 更新时间 - 开始 | - | false | string(date-time) |
| updateTimeEnd | 更新时间 - 结束 | - | false | string(date-time) |

##### 响应状态
| 状态码 | 说明 |
| --- | --- |
| 200 | OK |

##### 响应参数
| 参数名称 | 参数说明 | 类型 |
| --- | --- | --- |
| code | 状态码 | string |
| message | 状态描述 | string |
| data | 响应数据 | object |
| page | 分页信息 | object |
| total | 总数（分页信息内字段） | integer(int64) |
| size | 返回结果数量（分页信息内字段） | integer(int64) |
| content | 查询结果（data内数组字段） | array |
| sourceUserId | 源系统用户 id（学工号，content内字段） | string |
| status | 身份状态（字典，3.1.1 身份状态，content内字段） | integer(int32) |
| name | 姓名（content内字段） | string |
| gender | 性别（字典，3.1.2 性别，content内字段） | integer(int32) |
| idCardType | 身份证件类型（字典，3.1.3 身份证件类型，content内字段） | integer(int32) |
| idCardNum | 身份证件号（content内字段） | string |
| mobile | 手机号（content内字段） | string |
| nation | 民族（字典，3.1.4 民族，content内字段） | integer(int32) |
| nativePlace | 籍贯（content内字段） | string |
| politicalStatus | 政治面貌（字典，3.1.5 政治面貌，content内字段） | integer(int32) |
| orgList | 所属组织信息（一个身份可能在多个组织下，content内数组字段） | array |
| orgId | 组织编码（orgList内字段） | string |
| orgName | 组织名称（orgList内字段） | string |
| orgType | 组织类型（字典，orgList内字段） | integer(int32) |
| sourceOrgId | 组织原编码（orgList内字段） | string |
| associationSourceOrgId | 关联校内组织原编码（orgList内字段） | string |
| mainOrg | 主组织（content内对象字段） | object |
| mainOrg.orgId | 组织编码（主组织内字段） | string |
| mainOrg.orgName | 组织名称（主组织内字段） | string |
| mainOrg.orgType | 组织类型（字典，3.1.6 组织类型，主组织内字段） | integer(int32) |
| mainOrg.sourceOrgId | 组织原编码（主组织内字段） | string |
| mainOrg.associationSourceOrgId | 关联校内组织原编码（主组织内字段） | string |
| entityType | 身份类型（字典，3.1.7 实体类型，content内字段） | integer(int32) |
| dataMap | 人员身份信息详情（所有字段，content内字段） | object |
| updateTime | 更新时间（content内字段） | string(date-time) |
| empty | 空标识（data内字段） | boolean |

##### 响应示例
```json
{
  "code": "00000000",
  "message": "请求成功",
  "data": {
    "page": {
      "total": 0,
      "size": 0
    },
    "content": [
      {
        "sourceUserId": "",
        "status": 0,
        "name": "",
        "gender": 0,
        "idCardType": 0,
        "idCardNum": "",
        "mobile": "",
        "nation": 0,
        "nativePlace": "",
        "politicalStatus": 0,
        "orgList": [
          {
            "orgId": "",
            "orgName": "",
            "orgType": 0,
            "sourceOrgId": "",
            "associationSourceOrgId": ""
          }
        ],
        "mainOrg": {
          "orgId": "",
          "orgName": "",
          "orgType": 0,
          "sourceOrgId": "",
          "associationSourceOrgId": ""
        },
        "entityType": 0,
        "dataMap": {},
        "updateTime": ""
      }
    ],
    "empty": true
  }
}
```

#### 根据学工号获取人脸照片
- 接口地址: `/open-api/member/face-photos`
- 请求方式: GET
- 请求数据类型: application/x-www-form-urlencoded
- 响应数据类型: */*

##### 请求参数
| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
| --- | --- | --- | --- | --- |
| sourceUserId | 学工号 | query | true | string |

##### 响应状态
| 状态码 | 说明 |
| --- | --- |
| 200 | OK |

##### 响应参数
| 参数名称 | 参数说明 | 类型 |
| --- | --- | --- |
| code | 状态码 | string |
| message | 状态描述 | string |
| data | 响应数据 | object |
| content | 数据集合（data内数组字段） | array |
| faceType | 照片类型（字典，3.1.8 照片类型，content内字段） | integer(int32) |
| faceFactory | 人脸服务厂商（字典，3.1.13 人脸服务产商，content内字段） | integer(int32) |
| faceId | 人脸照 id，对接方可用于区分是否变更（content内字段） | string |
| imageBase64 | 照片（Base64 编码，content内字段） | string |

##### 响应示例
```json
{
  "code": "00000000",
  "message": "请求成功",
  "data": {
    "content": [
      {
        "idCardNum": "",
        "faceType": 0,
        "faceFactory": 0,
        "faceId": "",
        "imageBase64": ""
      }
    ]
  }
}
```

### 组织相关接口
#### 组织列表
- 接口地址: `/open-api/org/list`
- 请求方式: GET
- 请求数据类型: application/x-www-form-urlencoded
- 响应数据类型: */*

##### 请求参数
| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
| --- | --- | --- | --- | --- |
| physical | 是否实体组织，true: 只查询实体组织，false: 查询非实体组织，null: 查询所有组织 | query | false | string |
| internal | 是否校内组织（true: 查询校内组织；false: 查询非校内组织；null: 查询所有组织） | query | false | string |
| orgId | 组织 id | query | false | string |

##### 响应状态
| 状态码 | 说明 |
| --- | --- |
| 200 | OK |

##### 响应参数
| 参数名称 | 参数说明 | 类型 |
| --- | --- | --- |
| code | 状态码 | string |
| message | 状态描述 | string |
| data | 响应数据 | object |
| content | 数据集合（data内数组字段） | array |
| orgId | 组织编码（content内字段） | string |
| orgName | 组织名称（content内字段） | string |
| parentOrgId | 父组织编码（content内字段） | string |
| orgType | 组织类型（字典，3.1.6 组织类型，content内字段） | integer(int32) |
| physical | 是否是实体（content内字段） | boolean |
| sourceOrgId | 组织原编码（content内字段） | string |
| sourceParentOrgId | 父组织原编码（content内字段） | string |
| associationSourceOrgId | 关联校内组织原编码（content内字段） | string |
| level | 组织层级（content内字段） | integer(int32) |
| internal | 是否校内组织（true: 校内组织，false: 非校内，content内字段） | boolean |
| updateTime | 更新时间（content内字段） | string(date-time) |

##### 响应示例
```json
{
  "code": "00000000",
  "message": "请求成功",
  "data": {
    "content": [
      {
        "orgId": "",
        "orgName": "",
        "parentOrgId": "",
        "orgType": 0,
        "physical": true,
        "sourceOrgId": "",
        "sourceParentOrgId": "",
        "associationSourceOrgId": "",
        "level": 0,
        "internal": true,
        "updateTime": ""
      }
    ]
  }
}
```

### 标签相关接口
#### 标签列表
- 接口地址: `/open-api/tag/list`
- 请求方式: GET
- 请求数据类型: application/x-www-form-urlencoded
- 响应数据类型: */*

##### 请求参数
| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
| --- | --- | --- | --- | --- |
| tagId | 标签 id | query | false | string |

##### 响应状态
| 状态码 | 说明 |
| --- | --- |
| 200 | OK |

##### 响应参数
| 参数名称 | 参数说明 | 类型 |
| --- | --- | --- |
| code | 状态码 | string |
| message | 状态描述 | string |
| data | 响应数据 | object |
| content | 数据集合（data内数组字段） | array |
| tagId | 标签 id（content内字段） | string |
| tagName | 标签名称（content内字段） | string |
| tagCode | 标签编码（content内字段） | string |
| tagType | 标签类型（字典，3.1.9 标签类型，content内字段） | integer(int32) |
| sceneId | 使用场景 id（content内字段） | string |
| sceneName | 使用场景名称（content内字段） | string |
| status | 状态（字典，3.1.10 状态，content内字段） | integer(int32) |
| updateTime | 更新时间（content内字段） | string(date-time) |
| entityType | 实体类型（字典，3.1.7 实体类型，content内字段） | integer(int32) |

##### 响应示例
```json
{
  "code": "00000000",
  "message": "请求成功",
  "data": {
    "content": [
      {
        "tagId": "",
        "tagName": "",
        "tagCode": "",
        "tagType": 0,
        "sceneId": "",
        "sceneName": "",
        "status": 0,
        "updateTime": "",
        "entityType": 0
      }
    ]
  }
}
```

#### 人员标签关系分页列表
- 接口地址: `/open-api/tag/member-tags/page`
- 请求方式: POST
- 请求数据类型: application/x-www-form-urlencoded, application/json
- 响应数据类型: */*

##### 请求示例
```json
{
  "current": 0,
  "size": 0,
  "updateTimeStart": "",
  "updateTimeEnd": "",
  "tagId": ""
}
```

##### 请求参数
| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
| --- | --- | --- | --- | --- |
| request | 人员标签关系分页参数 | body | true | object |
| current | 当前页 | - | false | integer(int64) |
| size | 页面大小，默认 10 | - | false | integer(int64) |
| updateTimeStart | 更新时间 - 开始 | - | false | string(date-time) |
| updateTimeEnd | 更新时间 - 结束 | - | false | string(date-time) |
| sourceUserId | 源系统用户 id（学工号） | - | false | string |
| tagId | 标签 id | - | false | string |

##### 响应状态
| 状态码 | 说明 |
| --- | --- |
| 200 | OK |

##### 响应参数
| 参数名称 | 参数说明 | 类型 |
| --- | --- | --- |
| code | 状态码 | string |
| message | 状态描述 | string |
| data | 响应数据 | object |
| page | 分页信息（data内对象字段） | object |
| total | 总数（分页信息内字段） | integer(int64) |
| size | 返回结果数量（分页信息内字段） | integer(int64) |
| content | 查询结果（data内数组字段） | array |
| sourceUserId | 源系统用户 id（学工号，content内字段） | string |
| name | 姓名（content内字段） | string |
| tagId | 标签 id（content内字段） | string |
| tagName | 标签名称（content内字段） | string |
| tagCode | 标签编码（content内字段） | string |
| empty | 空标识（data内字段） | boolean |

##### 响应示例
```json
{
  "code": "00000000",
  "message": "请求成功",
  "data": {
    "page": {
      "total": 0,
      "size": 0
    },
    "content": [
      {
        "sourceUserId": "",
        "name": "",
        "tagId": "",
        "tagName": "",
        "tagCode": ""
      }
    ],
    "empty": true
  }
}
```

### 事件订阅相关接口
#### 事件订阅
- 接口地址: `/open-api/subscription/add`
- 请求方式: POST
- 请求数据类型: application/x-www-form-urlencoded, application/json
- 响应数据类型: */*

##### 请求示例
```json
{
  "eventType": 0,
  "callbackUrl": ""
}
```

##### 请求参数
| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
| --- | --- | --- | --- | --- |
| request | 新增事件订阅请求参数 | body | true | object |
| eventType | 事件类型（字典，3.1.11 订阅事件类型） | - | true | integer(int32) |
| callbackUrl | 事件推送的回调地址 | - | true | string |

##### 响应状态
| 状态码 | 说明 |
| --- | --- |
| 200 | OK |

##### 响应参数
| 参数名称 | 参数说明 | 类型 |
| --- | --- | --- |
| code | 状态码 | string |
| message | 状态描述 | string |
| data | 响应数据 | object |
| result | 返回结果（data内字段） | string |

##### 响应示例
```json
{
  "code": "00000000",
  "message": "请求成功",
  "data": {
    "result": ""
  }
}
```

#### 取消事件订阅
- 接口地址: `/open-api/subscription/cancel`
- 请求方式: POST
- 请求数据类型: application/x-www-form-urlencoded, application/json
- 响应数据类型: */*

##### 请求示例
```json
{
  "eventType": 0
}
```

##### 请求参数
| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
| --- | --- | --- | --- | --- |
| eventType | 事件类型（字典，3.1.11 订阅事件类型） | body | true | integer(int32) |

##### 响应状态
| 状态码 | 说明 |
| --- | --- |
| 200 | OK |

##### 响应参数
| 参数名称 | 参数说明 | 类型 |
| --- | --- | --- |
| code | 状态码 | string |
| message | 状态描述 | string |
| data | 响应数据 | object |

##### 响应示例
```json
{
  "code": "00000000",
  "message": "请求成功",
  "data": {}
}
```

#### 事件订阅 - 回调（对接方按照如下格式定义接口）
- 接口地址: 对接方自定义
- 请求方式: POST
- 请求数据类型: application/json
- 响应数据类型: */*

##### 请求示例
```json
{
  "eventType": 1,
  "dataStatus": 1,
  "dataIds": []
}
```

##### 请求参数
| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
| --- | --- | --- | --- | --- |
| request | 回调参数 | body | true | object |
| eventType | 事件类型（字典，3.1.11 订阅事件类型） | - | true | integer(int32) |
| dataStatus | 数据变更状态（字典，3.1.12 数据变更状态） | - | true | integer(int32) |
| dataIds | 数据 id（变更数据 id：当 eventType=1 时为学工号；当 eventType=2 时为组织 id；当 eventType=3 时为标签 id；当 eventType=4 时为标签 id） | - | true | array(string) |

##### 响应状态
| 状态码 | 说明 |
| --- | --- |
| 200 | 回调成功 |
| 其他 | 回调失败 |

## 附录：数据字典
### 3.1.1 身份状态
| 字典值 | 说明 |
| --- | --- |
| 1 | 正常 |
| 2 | 数据源删除 |
| 3 | 身份中台删除 |
| 4 | 禁用 |
| 5 | 失效 |
| 6 | 回收站人员 |

### 3.1.2 性别
| 字典值 | 说明 |
| --- | --- |
| 1 | 未知 |
| 2 | 男性 |
| 3 | 女性 |

### 3.1.3 身份证件类型
| 字典值 | 说明 |
| --- | --- |
| 1 | 居民身份证 |
| 2 | 港澳通行证 |
| 3 | 护照 |

### 3.1.4 民族
| 字典值 | 说明 |
| --- | --- |
| 1 | 汉族 |
| 2 | 蒙古族 |
| 3 | 回族 |
| 4 | 藏族 |
| 5 | 维吾尔族 |
| 6 | 苗族 |
| 7 | 彝族 |
| 8 | 壮族 |
| 9 | 布依族 |
| 10 | 朝鲜族 |
| 11 | 满族 |
| 12 | 侗族 |
| 13 | 瑶族 |
| 14 | 白族 |
| 15 | 土家族 |
| 16 | 哈尼族 |
| 17 | 哈萨克族 |
| 18 | 傣族 |
| 19 | 黎族 |
| 20 | 傈僳族 |
| 21 | 佤族 |
| 22 | 畲族 |
| 23 | 高山族 |
| 24 | 拉祜族 |
| 25 | 水族 |
| 26 | 东乡族 |
| 27 | 纳西族 |
| 28 | 景颇族 |
| 29 | 柯尔克孜族 |
| 30 | 土族 |
| 31 | 达斡尔族 |
| 32 | 仫佬族 |
| 33 | 羌族 |
| 34 | 布朗族 |
| 35 | 撒拉族 |
| 36 | 毛难族 |
| 37 | 仡佬族 |
| 38 | 锡伯族 |
| 39 | 阿昌族 |
| 40 | 普米族 |
| 41 | 塔吉克族 |
| 42 | 怒族 |
| 43 | 乌孜别克族 |
| 44 | 俄罗斯族 |
| 45 | 鄂温克族 |
| 46 | 崩龙族 |
| 47 | 保安族 |
| 48 | 裕固族 |
| 49 | 京族 |
| 50 | 塔塔尔族 |
| 51 | 独龙族 |
| 52 | 鄂伦春族 |
| 53 | 赫哲族 |
| 54 | 门巴族 |
| 55 | 珞巴族 |
| 56 | 基诺族 |
| 57 | 其他 |
| 58 | 外国血统中国人士 |

### 3.1.5 政治面貌
| 字典值 | 说明 |
| --- | --- |
| 1 | 党员 |
| 2 | 共青团员 |

### 3.1.6 组织类型
| 字典值 | 说明 |
| --- | --- |
| 1000 | 根组织 |
| 1100 | 教职工组织 |
| 1200 | 学生组织 |
| 1201 | 学生组织（西联） |
| 1202 | 学生组织（本科） |
| 1203 | 学生组织（研究生） |
| 1204 | 学生组织（成教生） |
| 1300 | 博士后组织 |
| 1400 | 校友组织 |
| 1500 | 校外人员组织 |
| 1501 | 非在职工作人员 |
| 1505 | 业务往来人员 |
| 1506 | 家属组织 |
| 1507 | 访客组织 |
| 1600 | 临时人员组织 |
| 1700 | 虚拟组织 |
| 9999 | 其他 |

### 3.1.7 实体类型
| 字典值 | 说明 |
| --- | --- |
| 100 | 校聘校管人员 |
| 201 | 校外联合培养学生 |
| 202 | 本科生 |
| 203 | 研究生 |
| 204 | 成教生 |
| 205 | 留学生 |
| 300 | 博士后 |
| 400 | 校友 |
| 501 | 非在职工作人员 |
| 504 | 其他人员 |
| 505 | 业务往来人员 |
| 701 | 院聘院管人员 |
| 706 | 附属机构人员 |
| 707 | 其他人员 |
| 1000 | 根组织 |
| 1100 | 教职工组织 |
| 1200 | 学生组织 |
| 1201 | 校外联合培养学生组织 |
| 1202 | 本科生组织 |
| 1203 | 研究生组织 |
| 1204 | 成教生组织 |
| 1205 | 留学生组织 |
| 1300 | 博士后组织 |
| 1400 | 校友组织 |
| 1501 | 非在职工作人员组织 |
| 1505 | 业务往来人员组织 |
| 1700 | 虚拟组织 |
| 1806 | 附属机构组织 |
| 1807 | 其他人员组织 |

### 3.1.8 照片类型
| 字典值 | 说明 |
| --- | --- |
| 1 | AI 照 |
| 2 | 证件照 |
| 3 | 学信网照 |
| 4 | 形象照 |

### 3.1.9 标签类型
| 字典值 | 说明 |
| --- | --- |
| 1 | 普通标签 |
| 2 | 属性标签 |
| 3 | 组合标签 |

### 3.1.10 状态
| 字典值 | 说明 |
| --- | --- |
| 0 | 禁用 |
| 1 | 启用 |

### 3.1.11 订阅事件类型
| 字典值 | 说明 |
| --- | --- |
| 1 | 人员变动事件 |
| 2 | 组织变动事件 |
| 3 | 标签变动事件 |
| 4 | 标签成员变动事件 |

### 3.1.12 数据变更状态
| 字典值 | 说明 |
| --- | --- |
| 1 | 新增 |
| 2 | 更新 |
| 3 | 删除 |

### 3.1.13 人脸服务产商
| 字典值 | 说明 |
| --- | --- |
| 1 | 默认厂商 |