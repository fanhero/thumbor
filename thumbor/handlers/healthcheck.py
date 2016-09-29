#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com
from redis import Redis, RedisError

from thumbor.handlers import BaseHandler, ContextHandler
from thumbor.utils import logger

from remotecv.unique_queue import UniqueQueue


class HealthcheckHandler(BaseHandler):
    def get(self):
        self.write('WORKING')

    def head(self, *args, **kwargs):
        self.set_status(200)


class QueueSizeHandler(ContextHandler):
    queue = None

    def get(self):
        response = {'name': self.context.config.WORKER_NAME, 'quantity': 0}
        try:
            if not QueueSizeHandler.queue:
                redis = Redis(host=self.context.config.REDIS_QUEUE_SERVER_HOST,
                              port=self.context.config.REDIS_QUEUE_SERVER_PORT,
                              db=self.context.config.REDIS_QUEUE_SERVER_DB,
                              password=self.context.config.REDIS_QUEUE_SERVER_PASSWORD)
                QueueSizeHandler.queue = UniqueQueue(server=redis)
            pending = QueueSizeHandler.queue.info().get('pending')
            response['quantity'] = pending
            self.write(response)
        except RedisError:
            self.context.request.detection_error = True
            QueueSizeHandler.queue = None
            logger.exception('Redis Error')
            self.write(response)
