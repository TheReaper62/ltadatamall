from distutils.core import setup
setup(
    name='LTADatamall',
    packages=['LTADatamall'],
    version='0.0.1',
    license='MIT',
    description='LTA Datamall API Wrapper',
    author='FishballNoodles',
    author_email='joelkhor.work@gmail.com',
    url='https://github.com/TheReaper62/LTA-Datamall',
    download_url='https://github.com/TheReaper62/LTA-Datamall/archive/refs/tags/v0.0.1.tar.gz',
    keywords=['lta','datamall','bus timing','train','service','passenger volume','taxi'],
    install_requires=[
        'requests',
        'aiohttp',
        'asyncio',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
