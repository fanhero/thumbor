# coding: utf-8

# Copyright (c) 2015-2016, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from tornado.concurrent import return_future

from thumbor.result_storages import BaseStorage, ResultStorageResult

from thumbor.aws.variable_storage import VariableAwsStorage

from thumbor.utils import logger


class Storage(VariableAwsStorage, BaseStorage):
    """
    S3 Result Storage
    """
    def __init__(self, context):
        """
        Constructor
        :param Context context: Thumbor's context
        """
        BaseStorage.__init__(self, context)

    def _set_bucket(self, bucket):
        """
        Initializes a new instance of VariableAwsStorage with a given bucket
        :param bucket: AWS bucket to store data at
        """
        VariableAwsStorage.__init__(self, bucket, self.context, 'RESULT_STORAGE')

    @return_future
    def put(self, bytes, callback=None):
        """
        Stores image
        :param bytes bytes: Data to store
        :param callable callback: Method called once done
        :rtype: string
        """
        path = self._normalize_path(self.context.request.url)

        if callback is None:
            def callback(key):
                self._handle_error(key)

        super(Storage, self).set(bytes, path, callback=callback)

    @return_future
    def get(self, path=None, callback=None):
        """
        Retrieves data
        :param string path: Path to load data (defaults to request URL)
        :param callable callback: Method called once done
        """
        if path is None:
            path = self.context.request.image_url

        def return_result(key):
            if key is None or self._get_error(key) or self.is_expired(key):
                callback(None)
            else:
                result = ResultStorageResult()
                result.buffer     = key['Body'].read()
                result.successful = True
                result.metadata   = key.copy()
                result.metadata.pop('Body')

                logger.debug(str(result.metadata))

                callback(result)
        bucket, key = self._get_bucket_and_key(path)
        print(key)
        self._set_bucket(bucket)
        super(Storage, self).get(key, callback=return_result)

    def _get_bucket(self, url):
        """
        Retrieves the bucket based on the URL
        :param string url: URL to parse
        :return: bucket name
        :rtype: string
        """
        url_by_piece = url.lstrip("/").split("/")

        return url_by_piece[0]

    def _get_bucket_and_key(self, url):
        """
        Returns bucket and key from url
        :param Context context: Thumbor's context
        :param string url: The URL to parse
        :return: A tuple with the bucket and the key detected
        :rtype: tuple
        """
        req = self.context.request
        shape = str(req.width) + 'x' + str(req.height) + '_'
        bucket = self._get_bucket(url)
        key = shape + '/'.join(url.lstrip('/').split('/')[1:])

        return bucket, key
