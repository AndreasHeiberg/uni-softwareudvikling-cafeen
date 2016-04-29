from django.test import TestCase, RequestFactory
from cafe.middleware.method_override_middleware import MethodOverrideMiddleware
from django.http import QueryDict

class MethodOverrideMiddlewareTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_it_only_handles_post_requests(self):
        request = self.factory.get('/', {'_method': 'POST'})

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'GET')

    def test_it_does_not_change_normal_post_requests(self):
        request = self.factory.post('/')

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'POST')

    def test_it_can_overwrite_to_get(self):
        request = self.factory.post('/', {'_method': 'GET'})

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'GET')

    def test_it_can_overwrite_to_head(self):
        request = self.factory.post('/', {'_method': 'HEAD'})

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'HEAD')

    def test_it_can_overwrite_to_put(self):
        request = self.factory.post('/', {'_method': 'PUT'})

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'PUT')

    def test_it_can_overwrite_to_delete(self):
        request = self.factory.post('/', {'_method': 'DELETE'})

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'DELETE')

    def test_it_can_overwrite_to_options(self):
        request = self.factory.post('/', {'_method': 'OPTIONS'})

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'OPTIONS')

    def test_it_can_overwrite_to_patch(self):
        request = self.factory.post('/', {'_method': 'PATCH'})

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'PATCH')

    def test_it_also_sets_the_method_data_attribute(self):
        request = self.factory.post('/', {'_method': 'PUT', 'id': 2})

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'PUT')
        self.assertEqual(request.PUT, QueryDict('_method=PUT&id=2'))

        request = self.factory.post('/', {'_method': 'PATCH', 'id': 2})

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'PATCH')
        self.assertEqual(request.PATCH, QueryDict('_method=PATCH&id=2'))

    def test_it_can_use_a_header_to_overwrite(self):
        request = self.factory.post('/', {'id': 2}, HTTP_X_HTTP_METHOD_OVERRIDE='PUT')

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'PUT')
        self.assertEqual(request.PUT, QueryDict('id=2'))

        request = self.factory.post('/', {'id': 2}, HTTP_X_HTTP_METHOD_OVERRIDE='PATCH')

        classUnderTest = MethodOverrideMiddleware()
        classUnderTest.process_view(request)

        self.assertEqual(request.method, 'PATCH')
        self.assertEqual(request.PATCH, QueryDict('id=2'))