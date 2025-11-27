"""
Pydantic models for cqhyxk API
"""
from datetime import datetime
from enum import IntEnum
from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field


def validate_enum(value: int, enum_class: IntEnum) -> Union[IntEnum, int]:
    """Validate enum value, return as enum if valid, otherwise return raw value"""
    try:
        return enum_class(value)
    except ValueError:
        return value


def create_enum_validator(enum_class: IntEnum):
    """Create a validator for a specific enum class"""
    return lambda v: validate_enum(v, enum_class)


class IdentityStatus(IntEnum):
    """身份状态 - 3.1.1 身份状态"""
    NORMAL = 1  # 正常
    DATASOURCE_DELETED = 2  # 数据源删除
    PLATFORM_DELETED = 3  # 身份中台删除
    DISABLED = 4  # 禁用
    INVALID = 5  # 失效
    RECYCLE_BIN = 6  # 回收站人员


class Gender(IntEnum):
    """性别 - 3.1.2 性别"""
    UNKNOWN = 1  # 未知
    MALE = 2  # 男性
    FEMALE = 3  # 女性


class IdCardType(IntEnum):
    """身份证件类型 - 3.1.3 身份证件类型"""
    ID_CARD = 1  # 居民身份证
    HK_Macao_PASS = 2  # 港澳通行证
    PASSPORT = 3  # 护照


class Nation(IntEnum):
    """民族 - 3.1.4 民族"""
    HAN = 1  # 汉族
    MONGOLIAN = 2  # 蒙古族
    HUI = 3  # 回族
    TIBETAN = 4  # 藏族
    UIGHUR = 5  # 维吾尔族
    MIAO = 6  # 苗族
    YI = 7  # 彝族
    ZHUANG = 8  # 壮族
    BUYI = 9  # 布依族
    KOREAN = 10  # 朝鲜族
    MANCHU = 11  # 满族
    DONG = 12  # 侗族
    YAO = 13  # 瑶族
    BAI = 14  # 白族
    TUJIA = 15  # 土家族
    HANI = 16  # 哈尼族
    KAZAKH = 17  # 哈萨克族
    DAI = 18  # 傣族
    LI = 19  # 黎族
    LISU = 20  # 傈僳族
    WA = 21  # 佤族
    SHE = 22  # 畲族
    GAOSHAN = 23  # 高山族
    LAHU = 24  # 拉祜族
    SHUI = 25  # 水族
    DONGXIANG = 26  # 东乡族
    NAXI = 27  # 纳西族
    JINGPO = 28  # 景颇族
    KIRGHIZ = 29  # 柯尔克孜族
    TU = 30  # 土族
    DAUR = 31  # 达斡尔族
    MULAO = 32  # 仫佬族
    QIANG = 33  # 羌族
    BLANG = 34  # 布朗族
    SALAR = 35  # 撒拉族
    MAONAN = 36  # 毛难族
    GELAO = 37  # 仡佬族
    XIBE = 38  # 锡伯族
    ACHANG = 39  # 阿昌族
    PUMI = 40  # 普米族
    TAJIK = 41  # 塔吉克族
    NU = 42  # 怒族
    UZBEK = 43  # 乌孜别克族
    RUSSIAN = 44  # 俄罗斯族
    EWIENK = 45  # 鄂温克族
    BENG = 46  # 崩龙族
    BAOAN = 47  # 保安族
    YUGUR = 48  # 裕固族
    JING = 49  # 京族
    TATAR = 50  # 塔塔尔族
    DRUNG = 51  # 独龙族
    ORCHUN = 52  # 鄂伦春族
    HEZHE = 53  # 赫哲族
    MENBA = 54  # 门巴族
    LUOBA = 55  # 珞巴族
    JINO = 56  # 基诺族
    OTHER = 57  # 其他
    FOREIGN_CHINESE = 58  # 外国血统中国人士


class PoliticalStatus(IntEnum):
    """政治面貌 - 3.1.5 政治面貌"""
    PARTY_MEMBER = 1  # 党员
    LEAGUE_MEMBER = 2  # 共青团员


class OrgType(IntEnum):
    """组织类型 - 3.1.6 组织类型"""
    ROOT = 1000  # 根组织
    FACULTY = 1100  # 教职工组织
    STUDENT = 1200  # 学生组织
    STUDENT_XILIAN = 1201  # 学生组织（西联）
    STUDENT_UNDERGRAD = 1202  # 学生组织（本科）
    STUDENT_POSTGRAD = 1203  # 学生组织（研究生）
    STUDENT_ADULT = 1204  # 学生组织（成教生）
    POSTDOCTOR = 1300  # 博士后组织
    ALUMNI = 1400  # 校友组织
    EXTERNAL = 1500  # 校外人员组织
    NON_STAFF = 1501  # 非在职工作人员
    BUSINESS_ASSOCIATES = 1505  # 业务往来人员
    FAMILY = 1506  # 家属组织
    VISITOR = 1507  # 访客组织
    TEMPORARY = 1600  # 临时人员组织
    VIRTUAL = 1700  # 虚拟组织
    OTHER = 9999  # 其他


class EntityType(IntEnum):
    """实体类型 - 3.1.7 实体类型"""
    SCHOOL_HIRED = 100  # 校聘校管人员
    EXTERNAL_STUDENT = 201  # 校外联合培养学生
    UNDERGRADUATE = 202  # 本科生
    GRADUATE = 203  # 研究生
    ADULT_EDUCATION = 204  # 成教生
    INTERNATIONAL = 205  # 留学生
    POSTDOCTOR = 300  # 博士后
    ALUMNI = 400  # 校友
    NON_STAFF = 501  # 非在职工作人员
    OTHER = 504  # 其他人员
    BUSINESS_ASSOCIATES = 505  # 业务往来人员
    COLLEGE_HIRED = 701  # 院聘院管人员
    AFFILIATED = 706  # 附属机构人员
    OTHER_707 = 707  # 其他人员
    ROOT = 1000  # 根组织
    FACULTY = 1100  # 教职工组织
    STUDENT = 1200  # 学生组织
    EXTERNAL_STUDENT_ORG = 1201  # 校外联合培养学生组织
    UNDERGRADUATE_ORG = 1202  # 本科生组织
    GRADUATE_ORG = 1203  # 研究生组织
    ADULT_EDUCATION_ORG = 1204  # 成教生组织
    INTERNATIONAL_ORG = 1205  # 留学生组织
    POSTDOCTOR_ORG = 1300  # 博士后组织
    ALUMNI_ORG = 1400  # 校友组织
    NON_STAFF_ORG = 1501  # 非在职工作人员组织
    BUSINESS_ASSOCIATES_ORG = 1505  # 业务往来人员组织
    VIRTUAL_ORG = 1700  # 虚拟组织
    AFFILIATED_ORG = 1806  # 附属机构组织
    OTHER_ORG = 1807  # 其他人员组织


class FaceType(IntEnum):
    """照片类型 - 3.1.8 照片类型"""
    AI_PHOTO = 1  # AI 照
    ID_PHOTO = 2  # 证件照
    CHSI_PHOTO = 3  # 学信网照
    PORTRAIT = 4  # 形象照


class TagType(IntEnum):
    """标签类型 - 3.1.9 标签类型"""
    NORMAL = 1  # 普通标签
    ATTRIBUTE = 2  # 属性标签
    COMBINATION = 3  # 组合标签


class Status(IntEnum):
    """状态 - 3.1.10 状态"""
    DISABLED = 0  # 禁用
    ENABLED = 1  # 启用


class EventType(IntEnum):
    """订阅事件类型 - 3.1.11 订阅事件类型"""
    PERSONNEL = 1  # 人员变动事件
    ORGANIZATION = 2  # 组织变动事件
    TAG = 3  # 标签变动事件
    TAG_MEMBER = 4  # 标签成员变动事件


class DataChangeStatus(IntEnum):
    """数据变更状态 - 3.1.12 数据变更状态"""
    ADDED = 1  # 新增
    UPDATED = 2  # 更新
    DELETED = 3  # 删除


class FaceFactory(IntEnum):
    """人脸服务产商 - 3.1.13 人脸服务产商"""
    DEFAULT = 1  # 默认厂商


class CommonResponse(BaseModel):
    """通用响应模型"""
    code: str = Field(..., description="状态码")
    message: str = Field(..., description="状态描述")
    data: Optional[Dict[str, Any]] = Field(None, description="响应数据，根据接口不同返回不同结构")


class PageRequest(BaseModel):
    """分页请求基类"""
    current: Optional[int] = Field(None, description="当前页")
    size: Optional[int] = Field(None, description="页面大小，默认 10")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class OrgInfo(BaseModel):
    """组织信息模型"""
    orgId: Optional[str] = Field(None, description="组织编码")
    orgName: Optional[str] = Field(None, description="组织名称")
    orgType: Optional[Union[OrgType, int]] = Field(None, description="组织类型")
    sourceOrgId: Optional[str] = Field(None, description="组织原编码")
    associationSourceOrgId: Optional[str] = Field(None, description="关联校内组织原编码")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class MainOrgInfo(BaseModel):
    """主组织信息模型"""
    orgId: Optional[str] = Field(None, description="组织编码")
    orgName: Optional[str] = Field(None, description="组织名称")
    orgType: Optional[Union[OrgType, int]] = Field(None, description="组织类型")
    sourceOrgId: Optional[str] = Field(None, description="组织原编码")
    associationSourceOrgId: Optional[str] = Field(None, description="关联校内组织原编码")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class IdentityInfo(BaseModel):
    """人员身份信息模型"""
    sourceUserId: Optional[str] = Field(None, description="源系统用户 id（学工号）")
    status: Optional[Union[IdentityStatus, int]] = Field(None, description="身份状态")
    name: Optional[str] = Field(None, description="姓名")
    gender: Optional[Union[Gender, int]] = Field(None, description="性别")
    idCardType: Optional[Union[IdCardType, int]] = Field(None, description="身份证件类型")
    idCardNum: Optional[str] = Field(None, description="身份证件号")
    mobile: Optional[str] = Field(None, description="手机号")
    nation: Optional[Union[Nation, int]] = Field(None, description="民族")
    nativePlace: Optional[str] = Field(None, description="籍贯")
    politicalStatus: Optional[Union[PoliticalStatus, int]] = Field(None, description="政治面貌")
    orgList: Optional[List[OrgInfo]] = Field(None, description="所属组织信息（一个身份可能在多个组织下）")
    mainOrg: Optional[MainOrgInfo] = Field(None, description="主组织")
    entityType: Optional[Union[EntityType, int]] = Field(None, description="身份类型")
    dataMap: Optional[Dict[str, Any]] = Field(None, description="人员身份信息详情（所有字段）")
    updateTime: Optional[datetime] = Field(None, description="更新时间")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class IdentityPageRequest(PageRequest):
    """人员身份信息分页查询请求参数"""
    updateTimeStart: Optional[str] = Field(None, description="更新时间 - 开始")
    updateTimeEnd: Optional[str] = Field(None, description="更新时间 - 结束")
    sourceUserId: Optional[str] = Field(None, description="源系统用户 id（学工号）")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class IdentityPageResponseData(BaseModel):
    """人员身份信息分页响应数据"""
    total: Optional[int] = Field(None, description="总数")
    size: Optional[int] = Field(None, description="返回结果数量")
    content: Optional[List[IdentityInfo]] = Field(None, description="查询结果")


class IdentityPageResponse(CommonResponse):
    """人员身份信息分页响应"""
    data: Optional[IdentityPageResponseData] = Field(None, description="响应数据")


class FacePhoto(BaseModel):
    """人脸照片模型"""
    faceType: Optional[Union[FaceType, int]] = Field(None, description="照片类型")
    faceFactory: Optional[Union[FaceFactory, int]] = Field(None, description="人脸服务厂商")
    faceId: Optional[str] = Field(None, description="人脸照 id，对接方可用于区分是否变更")
    imageBase64: Optional[str] = Field(None, description="照片（Base64 编码）")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class FacePhotosResponseData(BaseModel):
    """人脸照片响应数据"""
    content: Optional[List[FacePhoto]] = Field(None, description="数据集合")


class FacePhotosResponse(CommonResponse):
    """人脸照片响应"""
    data: Optional[FacePhotosResponseData] = Field(None, description="响应数据")


class OrgInfoDetail(BaseModel):
    """组织信息详情模型"""
    orgId: Optional[str] = Field(None, description="组织编码")
    orgName: Optional[str] = Field(None, description="组织名称")
    parentOrgId: Optional[str] = Field(None, description="父组织编码")
    orgType: Optional[Union[OrgType, int]] = Field(None, description="组织类型")
    physical: Optional[bool] = Field(None, description="是否是实体")
    sourceOrgId: Optional[str] = Field(None, description="组织原编码")
    sourceParentOrgId: Optional[str] = Field(None, description="父组织原编码")
    associationSourceOrgId: Optional[str] = Field(None, description="关联校内组织原编码")
    level: Optional[int] = Field(None, description="组织层级")
    internal: Optional[bool] = Field(None, description="是否校内组织（true: 校内组织，false: 非校内）")
    updateTime: Optional[datetime] = Field(None, description="更新时间")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class OrgListResponseData(BaseModel):
    """组织列表响应数据"""
    content: Optional[List[OrgInfoDetail]] = Field(None, description="数据集合")


class OrgListResponse(CommonResponse):
    """组织列表响应"""
    data: Optional[OrgListResponseData] = Field(None, description="响应数据")


class TagInfo(BaseModel):
    """标签信息模型"""
    tagId: Optional[str] = Field(None, description="标签 id")
    tagName: Optional[str] = Field(None, description="标签名称")
    tagCode: Optional[str] = Field(None, description="标签编码")
    tagType: Optional[Union[TagType, int]] = Field(None, description="标签类型")
    sceneId: Optional[str] = Field(None, description="使用场景 id")
    sceneName: Optional[str] = Field(None, description="使用场景名称")
    status: Optional[Union[Status, int]] = Field(None, description="状态")
    updateTime: Optional[datetime] = Field(None, description="更新时间")
    entityType: Optional[Union[EntityType, int]] = Field(None, description="实体类型")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class TagListResponseData(BaseModel):
    """标签列表响应数据"""
    content: Optional[List[TagInfo]] = Field(None, description="数据集合")


class TagListResponse(CommonResponse):
    """标签列表响应"""
    data: Optional[TagListResponseData] = Field(None, description="响应数据")


class MemberTagPageRequest(PageRequest):
    """人员标签关系分页请求参数"""
    updateTimeStart: Optional[str] = Field(None, description="更新时间 - 开始")
    updateTimeEnd: Optional[str] = Field(None, description="更新时间 - 结束")
    sourceUserId: Optional[str] = Field(None, description="源系统用户 id（学工号）")
    tagId: Optional[str] = Field(None, description="标签 id")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class MemberTagInfo(BaseModel):
    """人员标签关系信息模型"""
    sourceUserId: Optional[str] = Field(None, description="源系统用户 id（学工号）")
    name: Optional[str] = Field(None, description="姓名")
    tagId: Optional[str] = Field(None, description="标签 id")
    tagName: Optional[str] = Field(None, description="标签名称")
    tagCode: Optional[str] = Field(None, description="标签编码")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class MemberTagPageResponseData(BaseModel):
    """人员标签关系分页响应数据"""
    total: Optional[int] = Field(None, description="总数")
    size: Optional[int] = Field(None, description="返回结果数量")
    content: Optional[List[MemberTagInfo]] = Field(None, description="查询结果")
    empty: Optional[bool] = Field(None, description="空标识")


class MemberTagPageResponse(CommonResponse):
    """人员标签关系分页响应"""
    data: Optional[MemberTagPageResponseData] = Field(None, description="响应数据")


class SubscriptionRequest(BaseModel):
    """事件订阅请求参数"""
    eventType: EventType = Field(..., description="事件类型")
    callbackUrl: str = Field(..., description="事件推送的回调地址")

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat() if v else None}


class SubscriptionResponseData(BaseModel):
    """事件订阅响应数据"""
    result: Optional[str] = Field(None, description="返回结果")


class SubscriptionResponse(CommonResponse):
    """事件订阅响应"""
    data: Optional[SubscriptionResponseData] = Field(None, description="响应数据")


class CancelSubscriptionRequest(BaseModel):
    """取消事件订阅请求参数"""
    event_type: EventType = Field(..., alias="eventType", description="事件类型")


class CallbackRequest(BaseModel):
    """回调请求参数"""
    event_type: EventType = Field(..., alias="eventType", description="事件类型")
    data_status: DataChangeStatus = Field(..., alias="dataStatus", description="数据变更状态")
    data_ids: List[str] = Field(..., alias="dataIds", description="数据 id（变更数据 id：当 eventType=1 时为学工号；当 eventType=2 时为组织 id；当 eventType=3 时为标签 id；当 eventType=4 时为标签 id）")