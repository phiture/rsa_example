from setuptools import setup
import setuptools

setup(
    name='rsa_example',
    description='Encryption / Decryption command line tool',
    version='0.5',
    url='https://github.com/phiture/rsa_example',
    author='Abdul Majeed Alkattan',
    author_email='alkattan@phiture.com',
    packages=["rsa_example"], 
    keywords=['python','rsa','cmd'],
    install_requires=['cryptography'],
    long_description="""

# About Phiture

_[Phiture](http://phiture.com) is a Berlin-based mobile growth consultancy working with the teams behind leading apps. Using the company’s industry-acclaimed Mobile Growth Stack as a strategic framework, Phiture team offers 4 key services: App Store Optimization, Apple Search Ads, User Retention services and Growth Consulting._

### RSA Encryption/Decryption Example
    """,
    
    )