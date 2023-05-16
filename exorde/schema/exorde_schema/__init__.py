import json
from importlib import metadata

from jschemator import Schema
from jschemator.fields import (
    ArrayField,
    DateTimeField,
    NumberField,
    StringField,
    UrlField,
    Compose,
    ObjectField,
)


# TODO: ChildField
# TODO: Description pour chaque champs
# TODO: $id


class Emotion(Schema):
    love = NumberField()
    admiration = NumberField()
    joy = NumberField()
    approval = NumberField()
    caring = NumberField()
    excitement = NumberField()
    gratitude = NumberField()
    desire = NumberField()
    anger = NumberField()
    optimism = NumberField()
    disapproval = NumberField()
    grief = NumberField()
    annoyance = NumberField()
    pride = NumberField()
    curiosity = NumberField()
    neutral = NumberField()
    disgust = NumberField()
    disappointment = NumberField()
    realization = NumberField()
    fear = NumberField()
    relief = NumberField()
    confusion = NumberField()
    remorse = NumberField()
    embarrassement = NumberField()
    suprise = NumberField()
    sadness = NumberField()
    nervousness = NumberField()


class Advertising(Schema):
    advertise = NumberField()
    recommend = NumberField()


class Irony(Schema):
    non_irony = NumberField()
    irony = NumberField()


class TextType(Schema):
    assumption = NumberField()
    anecdote = NumberField()
    none = NumberField()
    definition = NumberField()
    testimony = NumberField()
    other = NumberField()
    study = NumberField()


class SourceType(Schema):
    social = NumberField()
    computers = NumberField()
    games = NumberField()
    business = NumberField()
    streaming = NumberField()
    ecommerce = NumberField()
    forums = NumberField()
    photography = NumberField()
    travel = NumberField()
    adult = NumberField()
    law = NumberField()
    sports = NumberField()
    education = NumberField()
    food = NumberField()
    health = NumberField()


class Age(Schema):
    below_twenty = NumberField()
    twenty_thirty = NumberField()
    thirty_forty = NumberField()
    forty_more = NumberField()


class Gender(Schema):
    female = NumberField()
    male = NumberField()

class Classification(Schema):
    topic = StringField()
    weight = NumberField()

class Item(Schema):
    """Posts & Comments both are independants Items"""

    content = StringField(description="Text body of the item")
    summary = StringField(description="Short version of the content")
    picture = UrlField(description="Image linked to the item")
    author = StringField(
        description="SHA1 encoding of the username assigned as creator of the item on it source plateform"
    ) 
    created_at = DateTimeField(
        description="ISO8601/RFC3339 Date of creation of the item"
    )
    language = StringField(
        description="ISO639-1 language code that consist of two lowercase letters"
    )  
    title = StringField(description="Headline of the item")
    domain = UrlField(
        description="Domain name on which the item was retrieved"
    )
    url = UrlField(
        description="Uniform-Resource-Locator that identifies the location of the item"
    )
    external_id = StringField(description="Identifier used by source")
    external_parent_id = StringField(
        description="Identifier used by source of parent item"
    )
    # classification = zero_shot
    classification = ArrayField(
        description="Probable categorization(s) of the post in a pre-determined set of general topics (list of objects with float associated for each topic, expressing their likelihood)",
        ObjectField(Classification)
    )
    top_keywords = ArrayField(
        description="The main keywords extracted from the content field", 
        StringField())  # yake
    
    # meta-data (tagger)
    translation = StringField(
        description="The content translated in English language")
    
    embedding = ArrayField(
        description="Vector/numerical representation of the translated content (field: translation), produced by a NLP encoder model", 
        NumberField())

    language_score = ArrayField(
        description="Readability score of the text", 
        ArrayField(Compose(StringField(), NumberField()))
    )

    # known size_list
    age = ObjectField(
        description="Probable age range of the author",
        Age)
    irony = ObjectField(
        description="Measure of how much a post is ironic (in %)",
        Irony)
    emotion = ObjectField(
        description="Emotion classification of the post, using the go-emotion standard of 28 precise emotions",
        Emotion)
    text_type = ObjectField(
        description="Type (category) of the post (article, etc)",
        TextType)
    source_type = ObjectField(
        description="Type (category) of the source that has produced the post",
        SourceType)
    gender = ObjectField(
        description="Probable gender (female or male) of the author",
        Gender)

    # unknown size list
    sentiment = NumberField(
        description="Measure of post sentiment from negative to positive (-1 = negative, +1 = positive, 0 = neutral)")
    # meta-data (tag) end

    collected_at = DateTimeField(
        description="ISO8601/RFC3339 Date of collection of the item"
    )
    collection_client_version = StringField(
        description="Version identifier of client that collected the item."
    )


def print_schema():
    print(
        json.dumps(
            Item().json_schema(
                **{
                    "$schema": "http://json-schema.org/draft-07/schema#",
                    "$id": f'https://github.com/exorde-labs/exorde/repo/tree/v{metadata.version("exorde_schema")}/exorde/schema/schema.json',
                }
            ),
            indent=4,
        )
    )
