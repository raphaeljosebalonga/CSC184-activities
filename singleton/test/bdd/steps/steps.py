from lettuce import *
from nose.tools import assert_equal

from crawler import Singleton, ImageDownloaderThread, traverse_site, download_images

import httplib2
import os
import re
import threading
import urllib
from urlparse import urlparse, urljoin

from BeautifulSoup import BeautifulSoup

@step(u'Given a website "([^"]*)"')
def given_a_website_group1(step, website):
    root = 'http://localhost/ATRrepo/about.html'
    parsed_root = urlparse(root)
    singleton = Singleton()
    singleton.queue_to_parse = [root]
    singleton.to_visit = set()
    singleton.downloaded = set()
    assert_equal(singleton.queue_to_parse.pop(), website)

@step(u'When images directory exist')
def when_images_directory_exist(step):
    root = 'http://localhost/ATRrepo/about.html'
    parsed_root = urlparse(root)
    singleton = Singleton()
    singleton.queue_to_parse = [root]
    singleton.to_visit = set()
    singleton.downloaded = set()
    if not os.path.exists('images'):
        os.makedirs('images')
    assert_equal(os.path.exists('images'), True)

@step(u'Then an image "([^"]*)" is downloaded')
def then_an_image_group1_is_downloaded(step, img_src):
    root = 'http://localhost/ATRrepo/about.html'
    parsed_root = urlparse(root)
    singleton = Singleton()
    singleton.queue_to_parse = [root]
    singleton.to_visit = set()
    singleton.downloaded = set()
    if not os.path.exists('images'):
        os.makedirs('images')
    thread1 = ImageDownloaderThread(1, "Thread-1", 1)
    thread1.start()
    url = singleton.queue_to_parse.pop()
    http = httplib2.Http()
    try:
    	status, response = http.request(url)
    except Exception:
    	None
    bs = BeautifulSoup(response)
    images = BeautifulSoup.findAll(bs, 'img')
    
    for image in images:
            src = image.get('src')
            src = urljoin(url, src)

    assert_equal(src, img_src)