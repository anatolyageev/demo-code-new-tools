from pydantic import \
    BaseModel, \
    ValidationError,\
    Field, \
    validator,\
    root_validator
from typing import List


class Tag(BaseModel):
    id: int
    tag_text: str


class City(BaseModel):
    city_id: int
    name: str = Field(alias='cityFullName')
    population: int
    tags: List[Tag]

    @validator('name')
    def name_should_be_spb(cls, v: str) -> str:
        if 'spb' not in v.lower():
            raise ValueError("Not with SPB!")
        return v


input_json = """
{
    "city_id":"123",
    "cityFullName":"Spb",
    "population":"200000",
    "tags": [
        {"id":1, "tag_text":"Big City"},
        {"id":2, "tag_text":"Capital"}
    ]
}
"""

try:
    city = City.parse_raw(input_json)
    print(city.__str__())
except ValidationError as e:
    print("Exception", e.json())
else:
    print(city)
    print(city.json(by_alias=True,
                    exclude={'city_id'}))



