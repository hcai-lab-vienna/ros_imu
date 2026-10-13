from setuptools import find_packages, setup

package_name = 'ros_imu'

setup(
    name=package_name,
    version='0.2.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bernhard',
    maintainer_email='bernhard-hoerl@gmx.at',
    description='ROS2 wrapper for serial IMU data.',
    license='Apache License 2.0',
    extras_require={},
    entry_points={
        'console_scripts': [
            'ros_imu_node = ros_imu.ros_imu_node:main',
        ],
    },
)
