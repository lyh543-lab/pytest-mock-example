from pytest_mock import MockFixture

from lib.request_manager import request_ten_times, call_ten_times


def test_call_with_mock_function(mocker: MockFixture):
    mocked_func = mocker.Mock()
    # treat Mock as a function
    call_ten_times(mocked_func)

    mocked_func.assert_has_calls([
        mocker.call(index) for index in range(10)
    ])


def test_call_with_mock_object(mocker: MockFixture):
    mocked_request = mocker.Mock()
    # treat Mock as an object
    request_ten_times(mocked_request)

    mocked_request.assert_has_calls([
        # here you should use `call.get()` instead of `call()` to assert `mock.get()` has been called
        mocker.call.get(index) for index in range(10)
    ])


def test_type_of_mock_field(mocker: MockFixture):
    mock = mocker.Mock()
    assert isinstance(mock, mocker.Mock)
    assert isinstance(mock.get, mocker.Mock)
    assert isinstance(mock.unknown_field,  mocker.Mock)
    assert isinstance(mock.unknown_field.field2,  mocker.Mock)
