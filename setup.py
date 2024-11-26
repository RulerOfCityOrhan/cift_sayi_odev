from setuptools import setup

package_name = 'cift_sayi'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='orhan',
    maintainer_email='atik.orhan81@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = cift_sayi.publisher_member_function:main',
            'listener = cift_sayi.subscriber_member_function:main',
        ],
    },
)
