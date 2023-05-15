import pytest, json

from exorde_meta_tagger import meta_tagger_initialization, tag, zero_shot
from aiosow.autofill import autofill
from .sample import SAMPLE

CONFIG = meta_tagger_initialization()


def test_max_depth_is_set():
    assert CONFIG["max_depth"] == 2
    print("assert max_depth ok")


@pytest.mark.asyncio
async def test_result_of_tag_should_be_json_serializable():
    """Result requires to be serialiable to pass trough the network."""
    test_content = SAMPLE[:1]
    result = await autofill(tag, args=[test_content], memory=CONFIG)
    tag_result = json.dumps(result)
    print("got tag result")
    with open("tag-result.json", "w") as f:
        f.write(tag_result)


@pytest.mark.asyncio
async def test_result_of_zero_shot_should_be_json_serializable():
    """Result requires to be serialiable to pass trough the network."""
    test_content = SAMPLE[:1]
    print("starting zero_shot")
    result = await autofill(zero_shot, args=[test_content], memory=CONFIG)
    zero_shot_result = json.dumps(result)
    print("got zero_shot result")
    with open("zero_shot-result.json", "w") as f:
        f.write(zero_shot_result)
