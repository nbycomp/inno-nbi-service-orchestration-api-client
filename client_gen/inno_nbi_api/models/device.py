# coding: utf-8

"""
    NBI Service Orchestration API

    Provides a robust interface for orchestrating service chains across cloud and edge computing environments, facilitating deployment, management, and updates of service chains to ensure dynamic, efficient operations across diverse infrastructure setups.

    The version of the OpenAPI document: 1.0.0
    Contact: support@nearbycomputing.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from inno_nbi_api.models.device_cloud_resource_chart import DeviceCloudResourceChart
from inno_nbi_api.models.device_position import DevicePosition
from inno_nbi_api.models.device_progress import DeviceProgress
from inno_nbi_api.models.device_tags_inner import DeviceTagsInner
from typing import Optional, Set
from typing_extensions import Self

class Device(BaseModel):
    """
    Device
    """ # noqa: E501
    id: Optional[StrictStr] = None
    tags: Optional[List[DeviceTagsInner]] = None
    display_name: Optional[StrictStr] = Field(default=None, alias="displayName")
    position: Optional[DevicePosition] = None
    specs: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    progress: Optional[DeviceProgress] = None
    site: Optional[StrictStr] = None
    cloud_resource_chart: Optional[DeviceCloudResourceChart] = Field(default=None, alias="cloudResourceChart")
    org: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "tags", "displayName", "position", "specs", "status", "progress", "site", "cloudResourceChart", "org"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Device from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of position
        if self.position:
            _dict['position'] = self.position.to_dict()
        # override the default output from pydantic by calling `to_dict()` of progress
        if self.progress:
            _dict['progress'] = self.progress.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cloud_resource_chart
        if self.cloud_resource_chart:
            _dict['cloudResourceChart'] = self.cloud_resource_chart.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Device from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "tags": [DeviceTagsInner.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "displayName": obj.get("displayName"),
            "position": DevicePosition.from_dict(obj["position"]) if obj.get("position") is not None else None,
            "specs": obj.get("specs"),
            "status": obj.get("status"),
            "progress": DeviceProgress.from_dict(obj["progress"]) if obj.get("progress") is not None else None,
            "site": obj.get("site"),
            "cloudResourceChart": DeviceCloudResourceChart.from_dict(obj["cloudResourceChart"]) if obj.get("cloudResourceChart") is not None else None,
            "org": obj.get("org")
        })
        return _obj


