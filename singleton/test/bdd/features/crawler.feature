Feature: Crawler application that downloads all images in a given website
    As a user I wish to be able to give a website,
    scan the website for images,
    and download all <img> images from a website

Scenario: download images
    Given a website "http://localhost/ATRrepo/about.html"
    When images directory exist
    Then an image "http://localhost/ATRrepo/pictures/f.jpg" is downloaded