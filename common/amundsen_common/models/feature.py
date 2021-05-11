# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional, Dict

import attr

from amundsen_common.models.user import User
from amundsen_common.models.badge import Badge
from amundsen_common.models.tag import Tag
from amundsen_common.models.table import Column, Stat, ProgrammaticDescription, Watermark
from marshmallow3_annotations.ext.attrs import AttrsSchema


@attr.s(auto_attribs=True, kw_only=True)
class Query:
    name: Optional[str]
    text: str
    url: Optional[str]


class QuerySchema(AttrsSchema):
    class Meta:
        target = Query
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class ColumnItem:
    column_name = column_name
    column_type = column_type


class ColumnItemSchema(AttrsSchema):
    class Meta:
        target = ColumnItem
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class DataSample:
    # Modeled after preview data model in FE
    columns: List[ColumnItem]
    data: List[Dict]
    error_text: str


class DataSampleSchema(AttrsSchema):
    class Meta:
        target = DataSample
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class Feature:
    key: Optional[str] = attr.ib(default=None)
    name: str
    version: str  # ex: "1.2.0"
    status: str
    feature_group: str
    entity: List[str]
    data_type: Optional[str]
    availability: List[str]
    description: Optional[str] = attr.ib(default=None)
    owners: List[User]
    badges: List[Badge]
    owner_tags: Optional[List[Tag]]  # non editable
    tags: List[Tag]  # editable
    programmatic_descriptions: List[ProgrammaticDescription]
    watermarks: List[Watermark]
    last_updated_timestamp: Optional[int]
    created_timestamp: Optional[int]
    partition_column: Optional[Column]


class FeatureSchema(AttrsSchema):
    class Meta:
        target = Feature
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class FeatureSummary:
    key: str  # ex: test_feature_group_name/test_feature_name/1.2.0
    name: str
    version: str
    availability: List[str]
    entity: List[str]
    description: Optional[str] = attr.ib(default=None)
    badges: List[Badge]
    last_updated_timestamp: Optional[int]


class FeatureSummarySchema(AttrsSchema):
    class Meta:
        target = FeatureSummary
        register_as_scheme = True
