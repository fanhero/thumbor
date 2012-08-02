#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from os.path import join
import tempfile
import derpconf.config as config
from derpconf.config import Config


Config.define('MAX_WIDTH', 0, "Max width in pixels for images read or generated by thumbor", 'Imaging')
Config.define('MAX_HEIGHT', 0, "Max height in pixels for images read or generated by thumbor", 'Imaging')
Config.define('MIN_WIDTH', 1, "Min width in pixels for images read or generated by thumbor", 'Imaging')
Config.define('MIN_HEIGHT', 1, "Min width in pixels for images read or generated by thumbor", 'Imaging')
Config.define('ALLOWED_SOURCES', [], "Allowed domains for the http loader to download. These are regular expressions.", 'Imaging')
Config.define('QUALITY', 80, 'Quality index used for generated JPEG images', 'Imaging')
Config.define('MAX_AGE', 24 * 60 * 60, 'Max AGE sent as a header for the image served by thumbor in seconds', 'Imaging')
Config.define('MAX_AGE_TEMP_IMAGE', 0, "Indicates the Max AGE header in seconds for temporary images (images that haven't been detected yet)", 'Imaging')
Config.define('RESPECT_ORIENTATION', False, 'Indicates whether thumbor should rotate images that have an Orientation EXIF header', 'Imaging')

Config.define('LOADER',  'thumbor.loaders.http_loader', 'The loader thumbor should use to load the original image. This must be the full name of a python module (python must be able to import it)', 'Extensibility')
Config.define('STORAGE', 'thumbor.storages.file_storage', 'The file storage thumbor should use to store original images. This must be the full name of a python module (python must be able to import it)', 'Extensibility')
Config.define('RESULT_STORAGE', None, 'The result storage thumbor should use to store generated images. This must be the full name of a python module (python must be able to import it)', 'Extensibility')
Config.define('ENGINE', 'thumbor.engines.pil', 'The imaging engine thumbor should use to perform image operations. This must be the full name of a python module (python must be able to import it)', 'Extensibility')

Config.define('SECURITY_KEY', 'MY_SECURE_KEY', 'The security key thumbor uses to sign image URLs', 'Security')

Config.define('ALLOW_UNSAFE_URL', True, 'Indicates if the /unsafe URL should be available', 'Security')
Config.define('ALLOW_OLD_URLS', True, 'Indicates if encrypted (old style) URLs should be allowed', 'Security')

# FILE LOADER OPTIONS
Config.define('FILE_LOADER_ROOT_PATH', '/tmp', 'The root path where the File Loader will try to find images', 'File Loader')

# HTTP LOADER OPTIONS
Config.define('MAX_SOURCE_SIZE', 0, "Max size in Kb for images downloaded by thumbor's HTTP Loader", 'HTTP Loader')
Config.define('REQUEST_TIMEOUT_SECONDS', 120, "Maximum number of seconds to wait for an original image to download", 'HTTP Loader')

# FILE STORAGE GENERIC OPTIONS
Config.define('STORAGE_EXPIRATION_SECONDS', 60 * 60 * 24 * 30, "Expiration in seconds for the images in the File Storage. Defaults to one month", 'File Storage') # default one month
Config.define('STORES_CRYPTO_KEY_FOR_EACH_IMAGE', False, 'Indicates whether thumbor should store the signing key for each image in the file storage. This allows the key to be changed and old images to still be properly found', 'File Storage')

# FILE STORAGE OPTIONS
Config.define('FILE_STORAGE_ROOT_PATH', join(tempfile.gettempdir(), 'thumbor', 'storage'), 'The root path where the File Storage will try to find images', 'File Storage')

# PHOTO UPLOAD OPTIONS
Config.define('UPLOAD_MAX_SIZE', 0, "Max size in Kb for images uploaded to thumbor", 'Upload')
Config.define('UPLOAD_ENABLED', False, 'Indicates whether thumbor should enable File uploads', 'Upload')
Config.define('UPLOAD_PHOTO_STORAGE', 'thumbor.storages.file_storage', 'The type of storage to store uploaded images with', 'Upload')
Config.define('UPLOAD_DELETE_ALLOWED', False, 'Indicates whether image deletion should be allowed', 'Upload')
Config.define('UPLOAD_PUT_ALLOWED', False, 'Indicates whether image overwrite should be allowed', 'Upload')

# ALIASES FOR OLD PHOTO UPLOAD OPTIONS
Config.alias('MAX_SIZE', 'UPLOAD_MAX_SIZE')
Config.alias('ENABLE_ORIGINAL_PHOTO_UPLOAD', 'UPLOAD_ENABLED')
Config.alias('ORIGINAL_PHOTO_STORAGE', 'UPLOAD_PHOTO_STORAGE')
Config.alias('ALLOW_ORIGINAL_PHOTO_DELETION', 'UPLOAD_DELETE_ALLOWED')
Config.alias('ALLOW_ORIGINAL_PHOTO_PUTTING', 'UPLOAD_PUT_ALLOWED')

# MONGO STORAGE OPTIONS
Config.define('MONGO_STORAGE_SERVER_HOST', 'localhost', 'MongoDB storage server host', 'MongoDB Storage')
Config.define('MONGO_STORAGE_SERVER_PORT', 27017, 'MongoDB storage server port', 'MongoDB Storage')
Config.define('MONGO_STORAGE_SERVER_DB', 'thumbor', 'MongoDB storage server database name', 'MongoDB Storage')
Config.define('MONGO_STORAGE_SERVER_COLLECTION', 'images', 'MongoDB storage image collection', 'MongoDB Storage')

# REDIS STORAGE OPTIONS
Config.define('REDIS_STORAGE_SERVER_HOST', 'localhost', 'Redis storage server host', 'Redis Storage')
Config.define('REDIS_STORAGE_SERVER_PORT', 6379, 'Redis storage server port', 'Redis Storage')
Config.define('REDIS_STORAGE_SERVER_DB', 0, 'Redis storage database index', 'Redis Storage')
Config.define('REDIS_STORAGE_SERVER_PASSWORD', None, 'Redis storage server password', 'Redis Storage')

# MIXED STORAGE OPTIONS
Config.define('MIXED_STORAGE_FILE_STORAGE', 'thumbor.storages.no_storage', 'Mixed Storage file storage. This must be the full name of a python module (python must be able to import it)', 'Mixed Storage')
Config.define('MIXED_STORAGE_CRYPTO_STORAGE', 'thumbor.storages.no_storage', 'Mixed Storage signing key storage. This must be the full name of a python module (python must be able to import it)', 'Mixed Storage')
Config.define('MIXED_STORAGE_DETECTOR_STORAGE', 'thumbor.storages.no_storage', 'Mixed Storage detector information storage. This must be the full name of a python module (python must be able to import it)', 'Mixed Storage')

# JSON META ENGINE OPTIONS
Config.define('META_CALLBACK_NAME', None, 'The callback function name that should be used by the META route for JSONP access', 'Meta')

# DETECTORS OPTIONS
Config.define('DETECTORS', [], 'List of detectors that thumbor should use to find faces and/or features. All of them must be full names of python modules (python must be able to import it)', 'Detection')

# FACE DETECTOR CASCADE FILE
Config.define('FACE_DETECTOR_CASCADE_FILE', 'haarcascade_frontalface_alt.xml', 'The cascade file that opencv will use to detect faces', 'Detection')

# AVAILABLE FILTERS
Config.define('FILTERS', [], 'List of filters that thumbor will allow to be used in generated images. All of them must be full names of python modules (python must be able to import it)', 'Filters')

# RESULT STORAGE
Config.define('RESULT_STORAGE_EXPIRATION_SECONDS', 0, 'Expiration in seconds of generated images in the result storage', 'Result Storage') # Never expires
Config.define('RESULT_STORAGE_FILE_STORAGE_ROOT_PATH', join(tempfile.gettempdir(), 'thumbor', 'result_storage'), 'Path where the Result storage will store generated images', 'Result Storage')
Config.define('RESULT_STORAGE_STORES_UNSAFE', False, 'Indicates whether unsafe requests should also be stored in the Result Storage', 'Result Storage')

# QUEUED DETECTOR REDIS OPTIONS
Config.define('REDIS_QUEUE_SERVER_HOST', 'localhost', 'Server host for the queued redis detector', 'Queued Redis Detector')
Config.define('REDIS_QUEUE_SERVER_PORT', 6379, 'Server port for the queued redis detector', 'Queued Redis Detector')
Config.define('REDIS_QUEUE_SERVER_DB', 0, 'Server database index for the queued redis detector', 'Queued Redis Detector')
Config.define('REDIS_QUEUE_SERVER_PASSWORD', None, 'Server password for the queued redis detector', 'Queued Redis Detector')

def generate_config():
    config.generate_config()

def format_value(value):
    if isinstance(value, basestring):
        return "'%s'" % value
    if isinstance(value, (tuple, list, set)):
        representation = '[\n'
        for item in value:
            representation += '#    %s' % item
        representation += '#]'
        return representation
    return value

if __name__ == '__main__':
    generate_config()
