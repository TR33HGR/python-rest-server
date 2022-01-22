from hamcrest import assert_that, equal_to
from microblog.microblog import app


def test_secret_key_imported_from_config():
    assert_that(app.config['SECRET_KEY'], equal_to('you-will-never-guess'))
