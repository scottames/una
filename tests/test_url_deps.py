# pyright: reportPrivateUsage=false

from una import package_deps
from una.models import ExtDep

_parse_deps_table = package_deps._parse_deps_table


def test_parse_url_dependency():
    # simple URL dependency
    dep = "name @ http://foo.com"
    result = _parse_deps_table(dep)
    assert result == ExtDep(name="name", version=" @ http://foo.com")


def test_parse_url_dependency_with_extras():
    # URL dependency with extras
    dep = "name[fred,bar] @ http://foo.com"
    result = _parse_deps_table(dep)
    assert result == ExtDep(name="name[fred,bar]", version=" @ http://foo.com")


def test_parse_url_dependency_with_environment_marker():
    # URL dependency with an environment marker
    dep = "name @ http://foo.com ; python_version=='2.7'"
    result = _parse_deps_table(dep)
    assert result == ExtDep(name="name", version=" @ http://foo.com ; python_version=='2.7'")


def test_parse_url_dependency_with_extras_and_environment_marker():
    # URL dependency with extras and an environment marker
    dep = "name[fred,bar] @ http://foo.com ; python_version=='2.7'"
    result = _parse_deps_table(dep)
    assert result == ExtDep(
        name="name[fred,bar]", version=" @ http://foo.com ; python_version=='2.7'"
    )


def test_parse_regular_dependency():
    # typical
    dep = "name>=1.0.0"
    result = _parse_deps_table(dep)
    assert result == ExtDep(name="name", version=">=1.0.0")


def test_parse_dependency_with_environment_marker():
    # typical with an environment marker
    dep = "name>=1.0.0 ; python_version>='3.6'"
    result = _parse_deps_table(dep)
    assert result.name == "name"
    assert ">=1.0.0 ; python_version>='3.6'" in result.version
