from setuptools import setup

setup(
    name="django_vote_system",
    version='0.0.1',
    description='A django application to vote any model',
    author='hakancelik96',
    author_email='hakancelik96@outlook.com',
    packages=["django_vote_system"],
    include_package_data=True,
    install_requires=[],
    url="https://github.com/djangoapps/django_vote_system",
    license='MIT',
    zip_safe=False,
    keywords="django, django-app, django-application, vote, vote-application, votes, vote-system",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
