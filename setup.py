from setuptools import setup, find_packages

setup(name='csl_sdk2py',
      version='0.0.1',
      author='CSLRobotics',
      author_email='morrisx28@mail.ntut.edu.tw',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      license="BSD-3-Clause",
      packages=find_packages(include=['csl_sdk2py','csl_sdk2py.*']),
      description='CSL robot sdk for python',
      project_urls={
            "Source Code": "https://github.com/morrisx28/csl_sdk2_python",
      },
      python_requires='>=3.8',
      install_requires=[
            "cyclonedds==0.10.2",
            "numpy",
            "opencv-python",
      ],
      )