from typing import Literal

ApiInformationEnvironment = Literal["production", "sandbox"]

API_INFORMATION_ENVIRONMENT_VALUES: set[ApiInformationEnvironment] = {
    "production",
    "sandbox",
}


def check_api_information_environment(value: str) -> ApiInformationEnvironment:
    if value in API_INFORMATION_ENVIRONMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_INFORMATION_ENVIRONMENT_VALUES!r}"
    )
