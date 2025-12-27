import pytest


@pytest.mark.parametrize("coursename",["Course1","Course2","Course3","Course4","Course5"])
def test_createsamplecourse(coursename):
    print("Course name is:",coursename)
