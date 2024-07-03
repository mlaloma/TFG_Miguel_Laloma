<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit9b54f9b6d0bdc5a2c6f5726cc1981a4c
{
    public static $prefixLengthsPsr4 = array (
        'D' => 
        array (
            'DgoraWcas\\' => 10,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'DgoraWcas\\' => 
        array (
            0 => __DIR__ . '/../..' . '/includes',
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInit9b54f9b6d0bdc5a2c6f5726cc1981a4c::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInit9b54f9b6d0bdc5a2c6f5726cc1981a4c::$prefixDirsPsr4;
            $loader->classMap = ComposerStaticInit9b54f9b6d0bdc5a2c6f5726cc1981a4c::$classMap;

        }, null, ClassLoader::class);
    }
}