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
from typing import Optional, Set
from typing_extensions import Self

class FetchBlockChartResponse(BaseModel):
    """
    FetchBlockChartResponse
    """ # noqa: E501
    display_name: Optional[StrictStr] = Field(default=None, alias="displayName")
    description: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    chart_yaml: Optional[StrictStr] = Field(default=None, description="Contents of Chart.yaml which define the chart's metadata.", alias="chartYaml")
    overrides_yaml: Optional[StrictStr] = Field(default=None, description="Contents of overrides.yaml which specify configuration overrides.", alias="overridesYaml")
    __properties: ClassVar[List[str]] = ["displayName", "description", "version", "chartYaml", "overridesYaml"]

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
        """Create an instance of FetchBlockChartResponse from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FetchBlockChartResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "displayName": obj.get("displayName"),
            "description": obj.get("description"),
            "version": obj.get("version"),
            "chartYaml": obj.get("chartYaml"),
            "overridesYaml": obj.get("overridesYaml")
        })
        return _obj


