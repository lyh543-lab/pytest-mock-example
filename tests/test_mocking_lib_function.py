from unittest.mock import Mock, patch, call

from pytest_mock import MockFixture

from app.greetings import get_greeting_string_from_import_function, get_greeting_string_from_import_module, get_greeting_string_from_import_class_method
from lib.utils import HostUtils


def test_get_greeting_string_from_import_function(mocker: MockFixture):
    mocked_getlogin = mocker.patch('app.greetings.getlogin', return_value='user')
    assert get_greeting_string_from_import_function() == 'Greetings, user'

    mocked_getlogin.assert_has_calls([
        mocker.call(),
    ])


# decorator-style of mocker.patch
@patch('app.greetings.getlogin', return_value='user')
def test_get_greeting_string_from_import_function__decorator_style(mocked_get_login: Mock):
    assert get_greeting_string_from_import_function() == 'Greetings, user'

    mocked_get_login.assert_has_calls([
        call(),
    ])
    # you can also use assert_called_with
    mocked_get_login.assert_called_with()


def test_get_greeting_string_from_import_module(mocker: MockFixture):
    mocked_getlogin = mocker.patch('os.getlogin', return_value='user')
    assert get_greeting_string_from_import_module() == 'Greetings, user'

    mocked_getlogin.assert_has_calls([
        mocker.call(),
    ])


def test_get_greeting_string_from_import_class_method(mocker: MockFixture):
    mocked_get_username = mocker.patch.object(HostUtils, 'get_username', return_value='user')
    mocked_get_current_path = mocker.patch.object(HostUtils, 'get_current_path', return_value='/')
    assert get_greeting_string_from_import_class_method() == 'Greetings, user'
    assert HostUtils().get_current_path('qwerty') == '/'

    mocked_get_username.assert_has_calls([
        mocker.call(),
    ])
    mocked_get_current_path.assert_has_calls([
        mocker.call('qwerty')
    ])


# decorator-style of mocker.patch.object
@patch.object(HostUtils, 'get_username', return_value='user')
@patch.object(HostUtils, 'get_current_path', return_value='/')
def test_get_greeting_string_from_import_class_method_decorator_style(mocked_get_current_path: Mock, mocked_get_username: Mock):
    assert get_greeting_string_from_import_class_method() == 'Greetings, user'
    assert HostUtils().get_current_path('qwerty') == '/'

    mocked_get_username.assert_has_calls([
        call(),
    ])
    mocked_get_current_path.assert_has_calls([
        call('qwerty')
    ])
