from setuptools import setup, find_packages

setup(name='rss_parser',
      version='1.3',
      description='RSS Parser',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.9',
          'Topic :: Text Processing :: Linguistic',
      ],
      author='Maksim Zhydovich',
      author_email='maksim.zhidovich@yandex.by',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'markdown',
          'requests',
          'beautifulsoup4',
          'json',
          'logging',
          'datetime',
          'argparse'
      ],
      include_package_data=True,
      zip_safe=False)