from enum import Enum
from madtypes import Schema, Annotation

from exorde_data.models import Item as CollectedItem
from exorde_lab.models import (
    TopKeywords,
    Translation,
    Analysis,
    Classification,
)


class CollectedAt(str, metaclass=Annotation):
    description = "ISO8601/RFC3339 Date of collection of the item"
    annotation = str
    pattern = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}\.[0-9]{1,6}?Z$"


class CollectionClientVersion(str, metaclass=Annotation):
    description = (
        "Client identifier with version of the client that collected the item."
    )
    annotation = str


class CollectionModule(str, metaclass=Annotation):
    description = "Module that scraped the item."
    annotation = str


class BatchKindEnum(Enum):
    SPOTTING = "SPOTTING"
    VALIDATION = "VALIDATION"


from madtypes import subtract_fields

ProtocolItem = subtract_fields("content")(CollectedItem)
ProtocolTranslation = subtract_fields("translation")(Translation)


class ProtocolAnalysis(
    Classification, Analysis, ProtocolTranslation, TopKeywords
):
    pass


class Item(Schema):
    item: ProtocolItem

    analysis: ProtocolAnalysis

    collection_client_version: CollectionClientVersion
    collection_module: CollectionModule
    collected_at: CollectedAt


class Batch(Schema):
    items: list[Item]
    kind: BatchKindEnum
