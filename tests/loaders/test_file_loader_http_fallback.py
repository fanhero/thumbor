#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from mock import patch
from os.path import abspath, join, dirname

from unittest import TestCase
from tests.base import TestCase as AsyncTestCase
from preggy import expect

from thumbor.context import Context
from thumbor.config import Config

import thumbor
import thumbor.loaders.file_loader_http_fallback as loader


STORAGE_PATH = abspath(join(dirname(__file__), '../fixtures/images/'))


def dummy_file_load(context, url, callback, normalize_url_func={}):
    callback('file')


def dummy_http_load(context, url, callback, normalize_url_func={}):
    callback('http')


class FileLoaderHttpFallbackFileTestCase(TestCase):
    def setUp(self):
        config = Config(
            FILE_LOADER_ROOT_PATH=STORAGE_PATH
        )
        self.ctx = Context(config=config)

    @patch.object(thumbor.loaders.file_loader, 'load', dummy_file_load)
    def test_should_load_file(self):
        result = loader.load(self.ctx, 'image.jpg', lambda x: x).result()
        expect(result).to_equal('file')


class FileLoaderHttpFallbackHttpTestCase(AsyncTestCase):
    @patch.object(thumbor.loaders.http_loader, 'load', dummy_http_load)
    def test_should_load_http(self):
        url = self.get_url('http:/www.google.com/example_image.png')
        config = Config()
        ctx = Context(None, config, None)

        loader.load(ctx, url, self.stop)
        result = self.wait()

        expect(result).to_equal('http')
