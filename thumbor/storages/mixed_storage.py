#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from thumbor.storages import BaseStorage
from thumbor.config import conf
from thumbor.utils import real_import

class Storage(BaseStorage):
    def __init__(self, file_storage=None, crypto_storage=None):
        if file_storage:
            self.file_storage = file_storage
        else:
            self.file_storage = real_import(conf.MIXED_STORAGE_FILE_STORAGE).Storage()

        if file_storage:
            self.crypto_storage = crypto_storage
        else:
            self.crypto_storage = real_import(conf.MIXED_STORAGE_CRYPTO_STORAGE).Storage()

    def put(self, path, bytes):
        self.file_storage.put(path, bytes)

    def put_crypto(self, path):
        import ipdb;ipdb.set_trace()
        self.crypto_storage.put_crypto(path)

    def get_crypto(self, path):
        return self.crypto_storage.get_crypto(path)

    def get(self, path):
        return self.file_storage.get(path)

