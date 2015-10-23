from setuptools import setup, find_packages

setup(
    version='1.0.0',
    description='python-shotgunorm',
    long_description=open('README.md').read(),
    author='NFXPlugins',
    author_email='admin@nfxplugins.com',
    name='ShotgunORM',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'shotgun_api3',
    ],
    license="BSD 3-Clause",
)
