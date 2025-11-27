"""
API client for cqhyxk SDK
"""
import json
from typing import Optional, Dict, Any
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from .models import (
    IdentityPageRequest, IdentityPageResponse,
    FacePhotosResponse, OrgListResponse,
    TagListResponse, MemberTagPageRequest,
    MemberTagPageResponse, SubscriptionRequest,
    SubscriptionResponse, CancelSubscriptionRequest, CommonResponse
)
from .exceptions import AuthenticationError, APIError, RequestError


class CqhyxkClient:
    """
    身份中台V2.0 OpenAPI Client
    
    This client provides methods to interact with the Identity Management Platform API,
    including personnel, organization, tag, and event subscription functionality.
    """
    
    def __init__(self, app_key: Optional[str] = None, app_secret: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize the client with app credentials.

        Args:
            app_key (Optional[str]): Application key for authentication.
                If not provided, will be loaded from CQHYXK_APP_KEY environment variable.
            app_secret (Optional[str]): Application secret for authentication.
                If not provided, will be loaded from CQHYXK_APP_SECRET environment variable.
            base_url (Optional[str]): Base URL for the API.
                If not provided, will be loaded from CQHYXK_BASEURL environment variable.
        """
        # Use provided values or load from environment variables
        self.app_key = app_key or os.getenv('CQHYXK_APP_KEY')
        self.app_secret = app_secret or os.getenv('CQHYXK_APP_SECRET')
        self.base_url = base_url or os.getenv('CQHYXK_BASEURL', 'https://your-domain/backend/school-platform/openapi')

        if not self.app_key:
            raise ValueError("app_key is required. Either pass it as parameter or set CQHYXK_APP_KEY environment variable.")
        if not self.app_secret:
            raise ValueError("app_secret is required. Either pass it as parameter or set CQHYXK_APP_SECRET environment variable.")

        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "app-key": self.app_key,
            "app-secret": self.app_secret
        })
    
    def _make_request(self, method: str, endpoint: str, params: Optional[Dict] = None, json_data: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Make an HTTP request to the API.
        
        Args:
            method (str): HTTP method (GET, POST, etc.)
            endpoint (str): API endpoint
            params (Optional[Dict]): Query parameters
            json_data (Optional[Dict]): JSON payload for the request
            
        Returns:
            Dict[str, Any]: JSON response from the API
            
        Raises:
            AuthenticationError: If authentication fails
            APIError: If the API returns an error response
            RequestError: If there's an error making the request
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json_data
            )
            
            # Check if the request was successful
            if response.status_code == 401:
                raise AuthenticationError("Authentication failed. Please check your app key and secret.")
            
            response.raise_for_status()
            
            # Parse the JSON response
            data = response.json()
            
            # Check for API error codes
            if data.get('code') != '00000000':
                message = data.get('message', 'Unknown error')
                # Safely handle potential Unicode encoding issues in error messages
                try:
                    message = str(message)
                except UnicodeError:
                    message = message.encode('utf-8', errors='ignore').decode('utf-8')

                raise APIError(
                    message=message,
                    code=data.get('code')
                )
            
            return data

        except requests.exceptions.RequestException as e:
            raise RequestError(f"Request failed: {str(e)}")
        except json.JSONDecodeError as e:
            raise RequestError(f"Failed to decode JSON response: {str(e)}")

    def _get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Helper method for GET requests"""
        return self._make_request('GET', endpoint, params=params)

    def _post(self, endpoint: str, json_data: Optional[Dict] = None) -> Dict[str, Any]:
        """Helper method for POST requests"""
        return self._make_request('POST', endpoint, json_data=json_data)

    def get_identity_list(self, request: IdentityPageRequest) -> IdentityPageResponse:
        """
        人员身份信息分页列表

        获取人员身份信息的分页列表，支持按更新时间、学工号等条件筛选。

        Args:
            request (IdentityPageRequest): 人员身份信息分页查询请求参数
                - current: 当前页（可选，默认为0）
                - size: 页面大小（可选，默认为10）
                - updateTimeStart: 更新时间 - 开始（可选）
                - updateTimeEnd: 更新时间 - 结束（可选）
                - sourceUserId: 源系统用户 id（学工号，可选）

        Returns:
            IdentityPageResponse: 人员身份信息分页响应
                - code: 状态码（200表示成功）
                - message: 状态描述
                - data: 响应数据
                    - page: 分页信息
                        - total: 总数
                        - size: 返回结果数量
                    - content: 查询结果列表
                        - sourceUserId: 源系统用户 id（学工号）
                        - status: 身份状态
                        - name: 姓名
                        - gender: 性别
                        - idCardType: 身份证件类型
                        - idCardNum: 身份证件号
                        - mobile: 手机号
                        - nation: 民族
                        - nativePlace: 籍贯
                        - politicalStatus: 政治面貌
                        - orgList: 所属组织信息
                        - mainOrg: 主组织
                        - entityType: 身份类型
                        - dataMap: 人员身份信息详情
                        - updateTime: 更新时间
                    - empty: 空标识

        Response Example:
            {
                "code": "00000000",
                "message": "请求成功",
                "data": {
                    "page": {
                        "total": 100,
                        "size": 10
                    },
                    "content": [
                        {
                            "sourceUserId": "2021001",
                            "status": 1,
                            "name": "张三",
                            "gender": 2,
                            "idCardType": 1,
                            "idCardNum": "123456789012345678",
                            "mobile": "13800138000",
                            "nation": 1,
                            "nativePlace": "北京市",
                            "politicalStatus": 1,
                            "orgList": [
                                {
                                    "orgId": "org001",
                                    "orgName": "计算机学院",
                                    "orgType": 1100,
                                    "sourceOrgId": "source001",
                                    "associationSourceOrgId": "assoc001"
                                }
                            ],
                            "mainOrg": {
                                "orgId": "org001",
                                "orgName": "计算机学院",
                                "orgType": 1100,
                                "sourceOrgId": "source001",
                                "associationSourceOrgId": "assoc001"
                            },
                            "entityType": 202,
                            "dataMap": {
                                "major": "计算机科学与技术",
                                "grade": "2021"
                            },
                            "updateTime": "2023-01-01T10:00:00Z"
                        }
                    ],
                    "empty": false
                }
            }
        """
        response_data = self._post("/open-api/member/identity/page", json_data=request.dict(exclude_none=True))
        return IdentityPageResponse(**response_data)

    def get_face_photos(self, source_user_id: str) -> FacePhotosResponse:
        """
        根据学工号获取人脸照片

        通过学工号查询对应的人员人脸照片信息。

        Args:
            source_user_id (str): 学工号

        Returns:
            FacePhotosResponse: 人脸照片响应
                - code: 状态码（200表示成功）
                - message: 状态描述
                - data: 响应数据
                    - content: 数据集合
                        - face_type: 照片类型
                        - face_factory: 人脸服务厂商
                        - face_id: 人脸照 id，对接方可用于区分是否变更
                        - image_base64: 照片（Base64 编码）

        Response Example:
            {
                "code": "00000000",
                "message": "请求成功",
                "data": {
                    "content": [
                        {
                            "faceType": 2,
                            "faceFactory": 1,
                            "faceId": "face_001",
                            "imageBase64": "iVBORw0KGgoAAAANSUhEUgAAAAUA..."
                        }
                    ]
                }
            }
        """
        params = {"sourceUserId": source_user_id}
        response_data = self._get("/open-api/member/face-photos", params=params)
        return FacePhotosResponse(**response_data)

    def get_org_list(self, physical: Optional[str] = None, internal: Optional[str] = None, org_id: Optional[str] = None) -> OrgListResponse:
        """
        组织列表

        获取组织列表，支持按实体组织、校内组织、组织ID等条件筛选。

        Args:
            physical (Optional[str]): 是否实体组织，true: 只查询实体组织，false: 查询非实体组织，null: 查询所有组织
            internal (Optional[str]): 是否校内组织（true: 查询校内组织；false: 查询非校内组织；null: 查询所有组织）
            org_id (Optional[str]): 组织 id（orgId）

        Returns:
            OrgListResponse: 组织列表响应
                - code: 状态码（200表示成功）
                - message: 状态描述
                - data: 响应数据
                    - content: 数据集合
                        - orgId: 组织编码
                        - orgName: 组织名称
                        - parentOrgId: 父组织编码
                        - orgType: 组织类型
                        - physical: 是否是实体
                        - sourceOrgId: 组织原编码
                        - sourceParentOrgId: 父组织原编码
                        - associationSourceOrgId: 关联校内组织原编码
                        - level: 组织层级
                        - internal: 是否校内组织（true: 校内组织，false: 非校内）
                        - updateTime: 更新时间

        Response Example:
            {
                "code": "00000000",
                "message": "请求成功",
                "data": {
                    "content": [
                        {
                            "orgId": "org001",
                            "orgName": "计算机学院",
                            "parentOrgId": "root001",
                            "orgType": 1100,
                            "physical": true,
                            "sourceOrgId": "source001",
                            "sourceParentOrgId": "source_root001",
                            "associationSourceOrgId": "assoc001",
                            "level": 2,
                            "internal": true,
                            "updateTime": "2023-01-01T10:00:00Z"
                        }
                    ]
                }
            }
        """
        params = {}
        if physical is not None:
            params['physical'] = physical
        if internal is not None:
            params['internal'] = internal
        if org_id is not None:
            params['orgId'] = org_id

        response_data = self._get("/open-api/org/list", params=params)
        return OrgListResponse(**response_data)

    def get_tag_list(self, tag_id: Optional[str] = None) -> TagListResponse:
        """
        标签列表

        获取标签列表，支持按标签ID筛选。

        Args:
            tag_id (Optional[str]): 标签 id（tagId）

        Returns:
            TagListResponse: 标签列表响应
                - code: 状态码（200表示成功）
                - message: 状态描述
                - data: 响应数据
                    - content: 数据集合
                        - tagId: 标签 id
                        - tagName: 标签名称
                        - tagCode: 标签编码
                        - tagType: 标签类型
                        - sceneId: 使用场景 id
                        - sceneName: 使用场景名称
                        - status: 状态
                        - updateTime: 更新时间
                        - entityType: 实体类型

        Response Example:
            {
                "code": "00000000",
                "message": "请求成功",
                "data": {
                    "content": [
                        {
                            "tagId": "tag001",
                            "tagName": "优秀学生",
                            "tagCode": "EXCELLENT_STUDENT",
                            "tagType": 1,
                            "sceneId": "scene001",
                            "sceneName": "奖学金评选",
                            "status": 1,
                            "updateTime": "2023-01-01T10:00:00Z",
                            "entityType": 202
                        }
                    ]
                }
            }
        """
        params = {}
        if tag_id is not None:
            params['tagId'] = tag_id

        response_data = self._get("/open-api/tag/list", params=params)
        return TagListResponse(**response_data)

    def get_member_tags_page(self, request: MemberTagPageRequest) -> MemberTagPageResponse:
        """
        人员标签关系分页列表

        获取人员标签关系的分页列表，支持按更新时间、标签ID等条件筛选。

        Args:
            request (MemberTagPageRequest): 人员标签关系分页参数
                - current: 当前页（可选，默认为0）
                - size: 页面大小（可选，默认为10）
                - updateTimeStart: 更新时间 - 开始（可选）
                - updateTimeEnd: 更新时间 - 结束（可选）
                - sourceUserId: 源系统用户 id（学工号，可选）
                - tagId: 标签 id（可选）

        Returns:
            MemberTagPageResponse: 人员标签关系分页响应
                - code: 状态码（200表示成功）
                - message: 状态描述
                - data: 响应数据
                    - page: 分页信息
                        - total: 总数
                        - size: 返回结果数量
                    - content: 查询结果
                        - sourceUserId: 源系统用户 id（学工号）
                        - name: 姓名
                        - tagId: 标签 id
                        - tagName: 标签名称
                        - tagCode: 标签编码
                    - empty: 空标识

        Response Example:
            {
                "code": "00000000",
                "message": "请求成功",
                "data": {
                    "page": {
                        "total": 50,
                        "size": 10
                    },
                    "content": [
                        {
                            "sourceUserId": "2021001",
                            "name": "张三",
                            "tagId": "tag001",
                            "tagName": "优秀学生",
                            "tagCode": "EXCELLENT_STUDENT"
                        }
                    ],
                    "empty": false
                }
            }
        """
        response_data = self._post("/open-api/tag/member-tags/page", json_data=request.dict(exclude_none=True))
        return MemberTagPageResponse(**response_data)

    def add_subscription(self, request: SubscriptionRequest) -> SubscriptionResponse:
        """
        事件订阅

        订阅特定类型的事件，当事件发生时，系统会向指定的回调地址发送通知。

        Args:
            request (SubscriptionRequest): 新增事件订阅请求参数
                - eventType: 事件类型（1: 人员变动事件, 2: 组织变动事件, 3: 标签变动事件, 4: 标签成员变动事件）
                - callbackUrl: 事件推送的回调地址

        Returns:
            SubscriptionResponse: 事件订阅响应
                - code: 状态码（200表示成功）
                - message: 状态描述
                - data: 响应数据
                    - result: 返回结果

        Response Example:
            {
                "code": "00000000",
                "message": "请求成功",
                "data": {
                    "result": "success"
                }
            }
        """
        response_data = self._post("/open-api/subscription/add", json_data=request.dict(exclude_none=True))
        return SubscriptionResponse(**response_data)

    def cancel_subscription(self, event_type: int) -> CommonResponse:
        """
        取消事件订阅

        取消订阅特定类型的事件。

        Args:
            event_type (int): 事件类型（eventType 1: 人员变动事件, 2: 组织变动事件, 3: 标签变动事件, 4: 标签成员变动事件）

        Returns:
            CommonResponse: 通用响应
                - code: 状态码（200表示成功）
                - message: 状态描述
                - data: 响应数据（空对象）

        Response Example:
            {
                "code": "00000000",
                "message": "请求成功",
                "data": {}
            }
        """
        request_data = {"eventType": event_type}
        response_data = self._post("/open-api/subscription/cancel", json_data=request_data)
        return CommonResponse(**response_data)