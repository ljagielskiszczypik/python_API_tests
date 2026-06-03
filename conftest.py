import pytest
from datetime import datetime
import os
import json

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{time}.html"

@pytest.fixture(scope='session')
def setup_teardown():
    print("preparing test resources")
    yield
    print("tearing down test resources")

@pytest.fixture()
def get_payload():
    json_path = os.path.join(os.path.dirname(__file__),"data","data.json")
    with open(json_path) as file:
        data=json.load(file)
    return data
