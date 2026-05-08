django_sprint4
├── LICENSE
├── README.md
├── blogicum/
│   ├── blog/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── admin.cpython-310.pyc
│   │   │   ├── apps.cpython-310.pyc
│   │   │   ├── forms.cpython-310.pyc
│   │   │   ├── models.cpython-310.pyc
│   │   │   ├── urls.cpython-310.pyc
│   │   │   └── views.cpython-310.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations/
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_alter_post_category.py
│   │   │   ├── 0003_alter_post_category.py
│   │   │   ├── 0004_post_image.py
│   │   │   ├── 0005_comment.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__/
│   │   │       ├── 0001_initial.cpython-310.pyc
│   │   │       ├── 0002_alter_post_category.cpython-310.pyc
│   │   │       ├── 0003_alter_post_category.cpython-310.pyc
│   │   │       ├── 0004_post_image.cpython-310.pyc
│   │   │       ├── 0005_comment.cpython-310.pyc
│   │   │       └── __init__.cpython-310.pyc
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── blogicum/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── settings.cpython-310.pyc
│   │   │   ├── urls.cpython-310.pyc
│   │   │   └── wsgi.cpython-310.pyc
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── media/
│   │   └── posts_images/
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── admin.cpython-310.pyc
│   │   │   ├── apps.cpython-310.pyc
│   │   │   ├── models.cpython-310.pyc
│   │   │   ├── urls.cpython-310.pyc
│   │   │   └── views.cpython-310.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   │   ├── __init__.py
│   │   │   └── __pycache__/
│   │   │       └── __init__.cpython-310.pyc
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── static/
│   │   ├── css/
│   │   │   └── bootstrap.min.css
│   │   └── img/
│   │       ├── fav/
│   │       │   ├── android-chrome-192x192.png
│   │       │   ├── android-chrome-256x256.png
│   │       │   ├── apple-touch-icon.png
│   │       │   ├── favicon-16x16.png
│   │       │   ├── favicon-32x32.png
│   │       │   ├── favicon.ico
│   │       │   └── mstile-150x150.png
│   │       └── logo.png
│   └── templates/
│       ├── base.html
│       ├── blog/
│       │   ├── category.html
│       │   ├── comment.html
│       │   ├── create.html
│       │   ├── detail.html
│       │   ├── index.html
│       │   ├── profile.html
│       │   └── user.html
│       ├── includes/
│       │   ├── category_link.html
│       │   ├── comments.html
│       │   ├── footer.html
│       │   ├── header.html
│       │   ├── paginator.html
│       │   └── post_card.html
│       ├── pages/
│       │   ├── 403csrf.html
│       │   ├── 404.html
│       │   ├── 500.html
│       │   ├── about.html
│       │   └── rules.html
│       └── registration/
│           ├── logged_out.html
│           ├── login.html
│           ├── password_change_done.html
│           ├── password_change_form.html
│           ├── password_reset_complete.html
│           ├── password_reset_confirm.html
│           ├── password_reset_done.html
│           ├── password_reset_form.html
│           └── registration_form.html
├── db.json
├── pytest.ini
├── requirements.txt
├── setup.cfg
├── templates/
│   ├── base.html
│   ├── blog/
│   │   ├── category.html
│   │   ├── comment.html
│   │   ├── create.html
│   │   ├── detail.html
│   │   ├── index.html
│   │   ├── profile.html
│   │   └── user.html
│   ├── includes/
│   │   ├── category_link.html
│   │   ├── comments.html
│   │   ├── footer.html
│   │   ├── header.html
│   │   ├── paginator.html
│   │   └── post_card.html
│   ├── pages/
│   │   ├── 403csrf.html
│   │   ├── 404.html
│   │   ├── 500.html
│   │   ├── about.html
│   │   └── rules.html
│   └── registration/
│       ├── logged_out.html
│       ├── login.html
│       ├── password_change_done.html
│       ├── password_change_form.html
│       ├── password_reset_complete.html
│       ├── password_reset_confirm.html
│       ├── password_reset_done.html
│       ├── password_reset_form.html
│       └── registration_form.html
├── test-results.txt
├── tests/
│   ├── __pycache__/
│   │   ├── conftest.cpython-310-pytest-7.1.3.pyc
│   │   ├── test_comment.cpython-310-pytest-7.1.3.pyc
│   │   ├── test_content.cpython-310-pytest-7.1.3.pyc
│   │   ├── test_edit.cpython-310-pytest-7.1.3.pyc
│   │   ├── test_emails.cpython-310-pytest-7.1.3.pyc
│   │   ├── test_err_pages.cpython-310-pytest-7.1.3.pyc
│   │   ├── test_post.cpython-310-pytest-7.1.3.pyc
│   │   ├── test_static_pages.cpython-310-pytest-7.1.3.pyc
│   │   └── test_users.cpython-310-pytest-7.1.3.pyc
│   ├── adapters/
│   │   ├── __pycache__/
│   │   │   ├── comment.cpython-310-pytest-7.1.3.pyc
│   │   │   ├── model_adapter.cpython-310.pyc
│   │   │   ├── post.cpython-310.pyc
│   │   │   ├── student_adapter.cpython-310.pyc
│   │   │   └── user.cpython-310.pyc
│   │   ├── comment.py
│   │   ├── model_adapter.py
│   │   ├── post.py
│   │   ├── student_adapter.py
│   │   └── user.py
│   ├── conftest.py
│   ├── fixtures/
│   │   ├── __pycache__/
│   │   │   ├── categories.cpython-310-pytest-7.1.3.pyc
│   │   │   ├── comments.cpython-310-pytest-7.1.3.pyc
│   │   │   ├── locations.cpython-310-pytest-7.1.3.pyc
│   │   │   ├── posts.cpython-310-pytest-7.1.3.pyc
│   │   │   └── types.cpython-310.pyc
│   │   ├── categories.py
│   │   ├── comments.py
│   │   ├── locations.py
│   │   ├── posts.py
│   │   └── types.py
│   ├── form/
│   │   ├── __pycache__/
│   │   │   ├── base_form_tester.cpython-310.pyc
│   │   │   ├── base_tester.cpython-310.pyc
│   │   │   ├── delete_tester.cpython-310.pyc
│   │   │   └── find_urls.cpython-310.pyc
│   │   ├── base_form_tester.py
│   │   ├── base_tester.py
│   │   ├── comment/
│   │   │   ├── __pycache__/
│   │   │   │   ├── create_form_tester.cpython-310.pyc
│   │   │   │   ├── delete_tester.cpython-310.pyc
│   │   │   │   ├── edit_form_tester.cpython-310.pyc
│   │   │   │   └── find_urls.cpython-310.pyc
│   │   │   ├── create_form_tester.py
│   │   │   ├── delete_tester.py
│   │   │   ├── edit_form_tester.py
│   │   │   └── find_urls.py
│   │   ├── delete_tester.py
│   │   ├── find_urls.py
│   │   ├── post/
│   │   │   ├── __pycache__/
│   │   │   │   ├── create_form_tester.cpython-310.pyc
│   │   │   │   ├── delete_tester.cpython-310.pyc
│   │   │   │   ├── edit_form_tester.cpython-310.pyc
│   │   │   │   ├── find_urls.cpython-310.pyc
│   │   │   │   └── form_tester.cpython-310.pyc
│   │   │   ├── create_form_tester.py
│   │   │   ├── delete_tester.py
│   │   │   ├── edit_form_tester.py
│   │   │   ├── find_urls.py
│   │   │   └── form_tester.py
│   │   └── user/
│   │       ├── __pycache__/
│   │       │   └── edit_form_tester.cpython-310.pyc
│   │       └── edit_form_tester.py
│   ├── test_comment.py
│   ├── test_content.py
│   ├── test_edit.py
│   ├── test_emails.py
│   ├── test_err_pages.py
│   ├── test_post.py
│   ├── test_static_pages.py
│   └── test_users.py
├── users.txt
└── venv/
    ├── Include/
    ├── Lib/
    │   └── site-packages/
    │       ├── Django-3.2.16.dist-info/
    │       │   ├── AUTHORS
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── LICENSE.python
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── Faker-12.0.1.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE.txt
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   ├── top_level.txt
    │       │   └── zip-safe
    │       ├── PIL/
    │       │   ├── BdfFontFile.py
    │       │   ├── BlpImagePlugin.py
    │       │   ├── BmpImagePlugin.py
    │       │   ├── BufrStubImagePlugin.py
    │       │   ├── ContainerIO.py
    │       │   ├── CurImagePlugin.py
    │       │   ├── DcxImagePlugin.py
    │       │   ├── DdsImagePlugin.py
    │       │   ├── EpsImagePlugin.py
    │       │   ├── ExifTags.py
    │       │   ├── FitsImagePlugin.py
    │       │   ├── FitsStubImagePlugin.py
    │       │   ├── FliImagePlugin.py
    │       │   ├── FontFile.py
    │       │   ├── FpxImagePlugin.py
    │       │   ├── FtexImagePlugin.py
    │       │   ├── GbrImagePlugin.py
    │       │   ├── GdImageFile.py
    │       │   ├── GifImagePlugin.py
    │       │   ├── GimpGradientFile.py
    │       │   ├── GimpPaletteFile.py
    │       │   ├── GribStubImagePlugin.py
    │       │   ├── Hdf5StubImagePlugin.py
    │       │   ├── IcnsImagePlugin.py
    │       │   ├── IcoImagePlugin.py
    │       │   ├── ImImagePlugin.py
    │       │   ├── Image.py
    │       │   ├── ImageChops.py
    │       │   ├── ImageCms.py
    │       │   ├── ImageColor.py
    │       │   ├── ImageDraw.py
    │       │   ├── ImageDraw2.py
    │       │   ├── ImageEnhance.py
    │       │   ├── ImageFile.py
    │       │   ├── ImageFilter.py
    │       │   ├── ImageFont.py
    │       │   ├── ImageGrab.py
    │       │   ├── ImageMath.py
    │       │   ├── ImageMode.py
    │       │   ├── ImageMorph.py
    │       │   ├── ImageOps.py
    │       │   ├── ImagePalette.py
    │       │   ├── ImagePath.py
    │       │   ├── ImageQt.py
    │       │   ├── ImageSequence.py
    │       │   ├── ImageShow.py
    │       │   ├── ImageStat.py
    │       │   ├── ImageTk.py
    │       │   ├── ImageTransform.py
    │       │   ├── ImageWin.py
    │       │   ├── ImtImagePlugin.py
    │       │   ├── IptcImagePlugin.py
    │       │   ├── Jpeg2KImagePlugin.py
    │       │   ├── JpegImagePlugin.py
    │       │   ├── JpegPresets.py
    │       │   ├── McIdasImagePlugin.py
    │       │   ├── MicImagePlugin.py
    │       │   ├── MpegImagePlugin.py
    │       │   ├── MpoImagePlugin.py
    │       │   ├── MspImagePlugin.py
    │       │   ├── PSDraw.py
    │       │   ├── PaletteFile.py
    │       │   ├── PalmImagePlugin.py
    │       │   ├── PcdImagePlugin.py
    │       │   ├── PcfFontFile.py
    │       │   ├── PcxImagePlugin.py
    │       │   ├── PdfImagePlugin.py
    │       │   ├── PdfParser.py
    │       │   ├── PixarImagePlugin.py
    │       │   ├── PngImagePlugin.py
    │       │   ├── PpmImagePlugin.py
    │       │   ├── PsdImagePlugin.py
    │       │   ├── PyAccess.py
    │       │   ├── SgiImagePlugin.py
    │       │   ├── SpiderImagePlugin.py
    │       │   ├── SunImagePlugin.py
    │       │   ├── TarIO.py
    │       │   ├── TgaImagePlugin.py
    │       │   ├── TiffImagePlugin.py
    │       │   ├── TiffTags.py
    │       │   ├── WalImageFile.py
    │       │   ├── WebPImagePlugin.py
    │       │   ├── WmfImagePlugin.py
    │       │   ├── XVThumbImagePlugin.py
    │       │   ├── XbmImagePlugin.py
    │       │   ├── XpmImagePlugin.py
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__/
    │       │   │   ├── BdfFontFile.cpython-310.pyc
    │       │   │   ├── BlpImagePlugin.cpython-310.pyc
    │       │   │   ├── BmpImagePlugin.cpython-310.pyc
    │       │   │   ├── BufrStubImagePlugin.cpython-310.pyc
    │       │   │   ├── ContainerIO.cpython-310.pyc
    │       │   │   ├── CurImagePlugin.cpython-310.pyc
    │       │   │   ├── DcxImagePlugin.cpython-310.pyc
    │       │   │   ├── DdsImagePlugin.cpython-310.pyc
    │       │   │   ├── EpsImagePlugin.cpython-310.pyc
    │       │   │   ├── ExifTags.cpython-310.pyc
    │       │   │   ├── FitsImagePlugin.cpython-310.pyc
    │       │   │   ├── FitsStubImagePlugin.cpython-310.pyc
    │       │   │   ├── FliImagePlugin.cpython-310.pyc
    │       │   │   ├── FontFile.cpython-310.pyc
    │       │   │   ├── FpxImagePlugin.cpython-310.pyc
    │       │   │   ├── FtexImagePlugin.cpython-310.pyc
    │       │   │   ├── GbrImagePlugin.cpython-310.pyc
    │       │   │   ├── GdImageFile.cpython-310.pyc
    │       │   │   ├── GifImagePlugin.cpython-310.pyc
    │       │   │   ├── GimpGradientFile.cpython-310.pyc
    │       │   │   ├── GimpPaletteFile.cpython-310.pyc
    │       │   │   ├── GribStubImagePlugin.cpython-310.pyc
    │       │   │   ├── Hdf5StubImagePlugin.cpython-310.pyc
    │       │   │   ├── IcnsImagePlugin.cpython-310.pyc
    │       │   │   ├── IcoImagePlugin.cpython-310.pyc
    │       │   │   ├── ImImagePlugin.cpython-310.pyc
    │       │   │   ├── Image.cpython-310.pyc
    │       │   │   ├── ImageChops.cpython-310.pyc
    │       │   │   ├── ImageCms.cpython-310.pyc
    │       │   │   ├── ImageColor.cpython-310.pyc
    │       │   │   ├── ImageDraw.cpython-310.pyc
    │       │   │   ├── ImageDraw2.cpython-310.pyc
    │       │   │   ├── ImageEnhance.cpython-310.pyc
    │       │   │   ├── ImageFile.cpython-310.pyc
    │       │   │   ├── ImageFilter.cpython-310.pyc
    │       │   │   ├── ImageFont.cpython-310.pyc
    │       │   │   ├── ImageGrab.cpython-310.pyc
    │       │   │   ├── ImageMath.cpython-310.pyc
    │       │   │   ├── ImageMode.cpython-310.pyc
    │       │   │   ├── ImageMorph.cpython-310.pyc
    │       │   │   ├── ImageOps.cpython-310.pyc
    │       │   │   ├── ImagePalette.cpython-310.pyc
    │       │   │   ├── ImagePath.cpython-310.pyc
    │       │   │   ├── ImageQt.cpython-310.pyc
    │       │   │   ├── ImageSequence.cpython-310.pyc
    │       │   │   ├── ImageShow.cpython-310.pyc
    │       │   │   ├── ImageStat.cpython-310.pyc
    │       │   │   ├── ImageTk.cpython-310.pyc
    │       │   │   ├── ImageTransform.cpython-310.pyc
    │       │   │   ├── ImageWin.cpython-310.pyc
    │       │   │   ├── ImtImagePlugin.cpython-310.pyc
    │       │   │   ├── IptcImagePlugin.cpython-310.pyc
    │       │   │   ├── Jpeg2KImagePlugin.cpython-310.pyc
    │       │   │   ├── JpegImagePlugin.cpython-310.pyc
    │       │   │   ├── JpegPresets.cpython-310.pyc
    │       │   │   ├── McIdasImagePlugin.cpython-310.pyc
    │       │   │   ├── MicImagePlugin.cpython-310.pyc
    │       │   │   ├── MpegImagePlugin.cpython-310.pyc
    │       │   │   ├── MpoImagePlugin.cpython-310.pyc
    │       │   │   ├── MspImagePlugin.cpython-310.pyc
    │       │   │   ├── PSDraw.cpython-310.pyc
    │       │   │   ├── PaletteFile.cpython-310.pyc
    │       │   │   ├── PalmImagePlugin.cpython-310.pyc
    │       │   │   ├── PcdImagePlugin.cpython-310.pyc
    │       │   │   ├── PcfFontFile.cpython-310.pyc
    │       │   │   ├── PcxImagePlugin.cpython-310.pyc
    │       │   │   ├── PdfImagePlugin.cpython-310.pyc
    │       │   │   ├── PdfParser.cpython-310.pyc
    │       │   │   ├── PixarImagePlugin.cpython-310.pyc
    │       │   │   ├── PngImagePlugin.cpython-310.pyc
    │       │   │   ├── PpmImagePlugin.cpython-310.pyc
    │       │   │   ├── PsdImagePlugin.cpython-310.pyc
    │       │   │   ├── PyAccess.cpython-310.pyc
    │       │   │   ├── SgiImagePlugin.cpython-310.pyc
    │       │   │   ├── SpiderImagePlugin.cpython-310.pyc
    │       │   │   ├── SunImagePlugin.cpython-310.pyc
    │       │   │   ├── TarIO.cpython-310.pyc
    │       │   │   ├── TgaImagePlugin.cpython-310.pyc
    │       │   │   ├── TiffImagePlugin.cpython-310.pyc
    │       │   │   ├── TiffTags.cpython-310.pyc
    │       │   │   ├── WalImageFile.cpython-310.pyc
    │       │   │   ├── WebPImagePlugin.cpython-310.pyc
    │       │   │   ├── WmfImagePlugin.cpython-310.pyc
    │       │   │   ├── XVThumbImagePlugin.cpython-310.pyc
    │       │   │   ├── XbmImagePlugin.cpython-310.pyc
    │       │   │   ├── XpmImagePlugin.cpython-310.pyc
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── __main__.cpython-310.pyc
    │       │   │   ├── _binary.cpython-310.pyc
    │       │   │   ├── _deprecate.cpython-310.pyc
    │       │   │   ├── _tkinter_finder.cpython-310.pyc
    │       │   │   ├── _util.cpython-310.pyc
    │       │   │   ├── _version.cpython-310.pyc
    │       │   │   └── features.cpython-310.pyc
    │       │   ├── _binary.py
    │       │   ├── _deprecate.py
    │       │   ├── _imaging.cp310-win_amd64.pyd
    │       │   ├── _imagingcms.cp310-win_amd64.pyd
    │       │   ├── _imagingft.cp310-win_amd64.pyd
    │       │   ├── _imagingmath.cp310-win_amd64.pyd
    │       │   ├── _imagingmorph.cp310-win_amd64.pyd
    │       │   ├── _imagingtk.cp310-win_amd64.pyd
    │       │   ├── _tkinter_finder.py
    │       │   ├── _util.py
    │       │   ├── _version.py
    │       │   ├── _webp.cp310-win_amd64.pyd
    │       │   └── features.py
    │       ├── Pillow-9.3.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── top_level.txt
    │       │   └── zip-safe
    │       ├── __pycache__/
    │       │   ├── flake8_docstrings.cpython-310.pyc
    │       │   ├── mccabe.cpython-310.pyc
    │       │   ├── pep8ext_naming.cpython-310.pyc
    │       │   ├── pycodestyle.cpython-310.pyc
    │       │   └── six.cpython-310.pyc
    │       ├── _distutils_hack/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   └── override.cpython-310.pyc
    │       │   └── override.py
    │       ├── _pytest/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── _argcomplete.cpython-310.pyc
    │       │   │   ├── _version.cpython-310.pyc
    │       │   │   ├── cacheprovider.cpython-310.pyc
    │       │   │   ├── capture.cpython-310.pyc
    │       │   │   ├── compat.cpython-310.pyc
    │       │   │   ├── debugging.cpython-310.pyc
    │       │   │   ├── deprecated.cpython-310.pyc
    │       │   │   ├── doctest.cpython-310.pyc
    │       │   │   ├── faulthandler.cpython-310.pyc
    │       │   │   ├── fixtures.cpython-310.pyc
    │       │   │   ├── freeze_support.cpython-310.pyc
    │       │   │   ├── helpconfig.cpython-310.pyc
    │       │   │   ├── hookspec.cpython-310.pyc
    │       │   │   ├── junitxml.cpython-310.pyc
    │       │   │   ├── legacypath.cpython-310.pyc
    │       │   │   ├── logging.cpython-310.pyc
    │       │   │   ├── main.cpython-310.pyc
    │       │   │   ├── monkeypatch.cpython-310.pyc
    │       │   │   ├── nodes.cpython-310.pyc
    │       │   │   ├── nose.cpython-310.pyc
    │       │   │   ├── outcomes.cpython-310.pyc
    │       │   │   ├── pastebin.cpython-310.pyc
    │       │   │   ├── pathlib.cpython-310.pyc
    │       │   │   ├── pytester.cpython-310.pyc
    │       │   │   ├── pytester_assertions.cpython-310.pyc
    │       │   │   ├── python.cpython-310.pyc
    │       │   │   ├── python_api.cpython-310.pyc
    │       │   │   ├── python_path.cpython-310.pyc
    │       │   │   ├── recwarn.cpython-310.pyc
    │       │   │   ├── reports.cpython-310.pyc
    │       │   │   ├── runner.cpython-310.pyc
    │       │   │   ├── scope.cpython-310.pyc
    │       │   │   ├── setuponly.cpython-310.pyc
    │       │   │   ├── setupplan.cpython-310.pyc
    │       │   │   ├── skipping.cpython-310.pyc
    │       │   │   ├── stash.cpython-310.pyc
    │       │   │   ├── stepwise.cpython-310.pyc
    │       │   │   ├── terminal.cpython-310.pyc
    │       │   │   ├── threadexception.cpython-310.pyc
    │       │   │   ├── timing.cpython-310.pyc
    │       │   │   ├── tmpdir.cpython-310.pyc
    │       │   │   ├── unittest.cpython-310.pyc
    │       │   │   ├── unraisableexception.cpython-310.pyc
    │       │   │   ├── warning_types.cpython-310.pyc
    │       │   │   └── warnings.cpython-310.pyc
    │       │   ├── _argcomplete.py
    │       │   ├── _code/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── code.cpython-310.pyc
    │       │   │   │   └── source.cpython-310.pyc
    │       │   │   ├── code.py
    │       │   │   └── source.py
    │       │   ├── _io/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── saferepr.cpython-310.pyc
    │       │   │   │   ├── terminalwriter.cpython-310.pyc
    │       │   │   │   └── wcwidth.cpython-310.pyc
    │       │   │   ├── saferepr.py
    │       │   │   ├── terminalwriter.py
    │       │   │   └── wcwidth.py
    │       │   ├── _version.py
    │       │   ├── assertion/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── rewrite.cpython-310.pyc
    │       │   │   │   ├── truncate.cpython-310.pyc
    │       │   │   │   └── util.cpython-310.pyc
    │       │   │   ├── rewrite.py
    │       │   │   ├── truncate.py
    │       │   │   └── util.py
    │       │   ├── cacheprovider.py
    │       │   ├── capture.py
    │       │   ├── compat.py
    │       │   ├── config/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── argparsing.cpython-310.pyc
    │       │   │   │   ├── compat.cpython-310.pyc
    │       │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   └── findpaths.cpython-310.pyc
    │       │   │   ├── argparsing.py
    │       │   │   ├── compat.py
    │       │   │   ├── exceptions.py
    │       │   │   └── findpaths.py
    │       │   ├── debugging.py
    │       │   ├── deprecated.py
    │       │   ├── doctest.py
    │       │   ├── faulthandler.py
    │       │   ├── fixtures.py
    │       │   ├── freeze_support.py
    │       │   ├── helpconfig.py
    │       │   ├── hookspec.py
    │       │   ├── junitxml.py
    │       │   ├── legacypath.py
    │       │   ├── logging.py
    │       │   ├── main.py
    │       │   ├── mark/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── expression.cpython-310.pyc
    │       │   │   │   └── structures.cpython-310.pyc
    │       │   │   ├── expression.py
    │       │   │   └── structures.py
    │       │   ├── monkeypatch.py
    │       │   ├── nodes.py
    │       │   ├── nose.py
    │       │   ├── outcomes.py
    │       │   ├── pastebin.py
    │       │   ├── pathlib.py
    │       │   ├── py.typed
    │       │   ├── pytester.py
    │       │   ├── pytester_assertions.py
    │       │   ├── python.py
    │       │   ├── python_api.py
    │       │   ├── python_path.py
    │       │   ├── recwarn.py
    │       │   ├── reports.py
    │       │   ├── runner.py
    │       │   ├── scope.py
    │       │   ├── setuponly.py
    │       │   ├── setupplan.py
    │       │   ├── skipping.py
    │       │   ├── stash.py
    │       │   ├── stepwise.py
    │       │   ├── terminal.py
    │       │   ├── threadexception.py
    │       │   ├── timing.py
    │       │   ├── tmpdir.py
    │       │   ├── unittest.py
    │       │   ├── unraisableexception.py
    │       │   ├── warning_types.py
    │       │   └── warnings.py
    │       ├── asgiref-3.5.2.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   └── top_level.txt
    │       ├── asgiref/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── compatibility.cpython-310.pyc
    │       │   │   ├── current_thread_executor.cpython-310.pyc
    │       │   │   ├── local.cpython-310.pyc
    │       │   │   ├── server.cpython-310.pyc
    │       │   │   ├── sync.cpython-310.pyc
    │       │   │   ├── testing.cpython-310.pyc
    │       │   │   ├── timeout.cpython-310.pyc
    │       │   │   ├── typing.cpython-310.pyc
    │       │   │   └── wsgi.cpython-310.pyc
    │       │   ├── compatibility.py
    │       │   ├── current_thread_executor.py
    │       │   ├── local.py
    │       │   ├── py.typed
    │       │   ├── server.py
    │       │   ├── sync.py
    │       │   ├── testing.py
    │       │   ├── timeout.py
    │       │   ├── typing.py
    │       │   └── wsgi.py
    │       ├── attr/
    │       │   ├── __init__.py
    │       │   ├── __init__.pyi
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── _cmp.cpython-310.pyc
    │       │   │   ├── _compat.cpython-310.pyc
    │       │   │   ├── _config.cpython-310.pyc
    │       │   │   ├── _funcs.cpython-310.pyc
    │       │   │   ├── _make.cpython-310.pyc
    │       │   │   ├── _next_gen.cpython-310.pyc
    │       │   │   ├── _version_info.cpython-310.pyc
    │       │   │   ├── converters.cpython-310.pyc
    │       │   │   ├── exceptions.cpython-310.pyc
    │       │   │   ├── filters.cpython-310.pyc
    │       │   │   ├── setters.cpython-310.pyc
    │       │   │   └── validators.cpython-310.pyc
    │       │   ├── _cmp.py
    │       │   ├── _cmp.pyi
    │       │   ├── _compat.py
    │       │   ├── _config.py
    │       │   ├── _funcs.py
    │       │   ├── _make.py
    │       │   ├── _next_gen.py
    │       │   ├── _typing_compat.pyi
    │       │   ├── _version_info.py
    │       │   ├── _version_info.pyi
    │       │   ├── converters.py
    │       │   ├── converters.pyi
    │       │   ├── exceptions.py
    │       │   ├── exceptions.pyi
    │       │   ├── filters.py
    │       │   ├── filters.pyi
    │       │   ├── py.typed
    │       │   ├── setters.py
    │       │   ├── setters.pyi
    │       │   ├── validators.py
    │       │   └── validators.pyi
    │       ├── attrs-22.2.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   └── top_level.txt
    │       ├── attrs/
    │       │   ├── __init__.py
    │       │   ├── __init__.pyi
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── converters.cpython-310.pyc
    │       │   │   ├── exceptions.cpython-310.pyc
    │       │   │   ├── filters.cpython-310.pyc
    │       │   │   ├── setters.cpython-310.pyc
    │       │   │   └── validators.cpython-310.pyc
    │       │   ├── converters.py
    │       │   ├── exceptions.py
    │       │   ├── filters.py
    │       │   ├── py.typed
    │       │   ├── setters.py
    │       │   └── validators.py
    │       ├── beautifulsoup4-4.11.2.dist-info/
    │       │   ├── AUTHORS
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   └── top_level.txt
    │       ├── bs4/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── dammit.cpython-310.pyc
    │       │   │   ├── diagnose.cpython-310.pyc
    │       │   │   ├── element.cpython-310.pyc
    │       │   │   └── formatter.cpython-310.pyc
    │       │   ├── builder/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── _html5lib.cpython-310.pyc
    │       │   │   │   ├── _htmlparser.cpython-310.pyc
    │       │   │   │   └── _lxml.cpython-310.pyc
    │       │   │   ├── _html5lib.py
    │       │   │   ├── _htmlparser.py
    │       │   │   └── _lxml.py
    │       │   ├── dammit.py
    │       │   ├── diagnose.py
    │       │   ├── element.py
    │       │   ├── formatter.py
    │       │   └── tests/
    │       │       ├── __init__.py
    │       │       ├── __pycache__/
    │       │       │   ├── __init__.cpython-310.pyc
    │       │       │   ├── test_builder.cpython-310.pyc
    │       │       │   ├── test_builder_registry.cpython-310.pyc
    │       │       │   ├── test_dammit.cpython-310.pyc
    │       │       │   ├── test_docs.cpython-310.pyc
    │       │       │   ├── test_element.cpython-310.pyc
    │       │       │   ├── test_formatter.cpython-310.pyc
    │       │       │   ├── test_html5lib.cpython-310.pyc
    │       │       │   ├── test_htmlparser.cpython-310.pyc
    │       │       │   ├── test_lxml.cpython-310.pyc
    │       │       │   ├── test_navigablestring.cpython-310.pyc
    │       │       │   ├── test_pageelement.cpython-310.pyc
    │       │       │   ├── test_soup.cpython-310.pyc
    │       │       │   ├── test_tag.cpython-310.pyc
    │       │       │   └── test_tree.cpython-310.pyc
    │       │       ├── test_builder.py
    │       │       ├── test_builder_registry.py
    │       │       ├── test_dammit.py
    │       │       ├── test_docs.py
    │       │       ├── test_element.py
    │       │       ├── test_formatter.py
    │       │       ├── test_html5lib.py
    │       │       ├── test_htmlparser.py
    │       │       ├── test_lxml.py
    │       │       ├── test_navigablestring.py
    │       │       ├── test_pageelement.py
    │       │       ├── test_soup.py
    │       │       ├── test_tag.py
    │       │       └── test_tree.py
    │       ├── colorama-0.4.6.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   └── licenses/
    │       │       └── LICENSE.txt
    │       ├── colorama/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── ansi.cpython-310.pyc
    │       │   │   ├── ansitowin32.cpython-310.pyc
    │       │   │   ├── initialise.cpython-310.pyc
    │       │   │   ├── win32.cpython-310.pyc
    │       │   │   └── winterm.cpython-310.pyc
    │       │   ├── ansi.py
    │       │   ├── ansitowin32.py
    │       │   ├── initialise.py
    │       │   ├── tests/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── ansi_test.cpython-310.pyc
    │       │   │   │   ├── ansitowin32_test.cpython-310.pyc
    │       │   │   │   ├── initialise_test.cpython-310.pyc
    │       │   │   │   ├── isatty_test.cpython-310.pyc
    │       │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   └── winterm_test.cpython-310.pyc
    │       │   │   ├── ansi_test.py
    │       │   │   ├── ansitowin32_test.py
    │       │   │   ├── initialise_test.py
    │       │   │   ├── isatty_test.py
    │       │   │   ├── utils.py
    │       │   │   └── winterm_test.py
    │       │   ├── win32.py
    │       │   └── winterm.py
    │       ├── dateutil/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── _common.cpython-310.pyc
    │       │   │   ├── _version.cpython-310.pyc
    │       │   │   ├── easter.cpython-310.pyc
    │       │   │   ├── relativedelta.cpython-310.pyc
    │       │   │   ├── rrule.cpython-310.pyc
    │       │   │   ├── tzwin.cpython-310.pyc
    │       │   │   └── utils.cpython-310.pyc
    │       │   ├── _common.py
    │       │   ├── _version.py
    │       │   ├── easter.py
    │       │   ├── parser/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── _parser.cpython-310.pyc
    │       │   │   │   └── isoparser.cpython-310.pyc
    │       │   │   ├── _parser.py
    │       │   │   └── isoparser.py
    │       │   ├── relativedelta.py
    │       │   ├── rrule.py
    │       │   ├── tz/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── _common.cpython-310.pyc
    │       │   │   │   ├── _factories.cpython-310.pyc
    │       │   │   │   ├── tz.cpython-310.pyc
    │       │   │   │   └── win.cpython-310.pyc
    │       │   │   ├── _common.py
    │       │   │   ├── _factories.py
    │       │   │   ├── tz.py
    │       │   │   └── win.py
    │       │   ├── tzwin.py
    │       │   ├── utils.py
    │       │   └── zoneinfo/
    │       │       ├── __init__.py
    │       │       ├── __pycache__/
    │       │       │   ├── __init__.cpython-310.pyc
    │       │       │   └── rebuild.cpython-310.pyc
    │       │       ├── dateutil-zoneinfo.tar.gz
    │       │       └── rebuild.py
    │       ├── distutils-precedence.pth
    │       ├── django/
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── __main__.cpython-310.pyc
    │       │   │   └── shortcuts.cpython-310.pyc
    │       │   ├── apps/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── config.cpython-310.pyc
    │       │   │   │   └── registry.cpython-310.pyc
    │       │   │   ├── config.py
    │       │   │   └── registry.py
    │       │   ├── bin/
    │       │   │   ├── __pycache__/
    │       │   │   │   └── django-admin.cpython-310.pyc
    │       │   │   └── django-admin.py
    │       │   ├── conf/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   └── global_settings.cpython-310.pyc
    │       │   │   ├── app_template/
    │       │   │   │   ├── __init__.py-tpl
    │       │   │   │   ├── admin.py-tpl
    │       │   │   │   ├── apps.py-tpl
    │       │   │   │   ├── migrations/
    │       │   │   │   │   └── __init__.py-tpl
    │       │   │   │   ├── models.py-tpl
    │       │   │   │   ├── tests.py-tpl
    │       │   │   │   └── views.py-tpl
    │       │   │   ├── global_settings.py
    │       │   │   ├── locale/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── af/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── ar/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ar_DZ/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ast/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── az/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── be/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── bg/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── bn/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── br/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── bs/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ca/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── cs/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── cy/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── da/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── de/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── de_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── dsb/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── el/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── en/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── en_AU/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── en_GB/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── eo/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── es/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── es_AR/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── es_CO/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── es_MX/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── es_NI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── es_PR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── es_VE/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── et/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── eu/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── fa/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── fi/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── fr/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── fy/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ga/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── gd/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── gl/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── he/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── hi/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── hr/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── hsb/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── hu/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── hy/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── ia/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── id/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ig/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── io/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── is/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── it/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ja/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ka/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── kab/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── kk/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── km/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── kn/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ko/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ky/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── lb/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── lt/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── lv/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── mk/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ml/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── mn/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── mr/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── my/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── nb/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ne/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── nl/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── nn/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── os/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── pa/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── pl/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── pt/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ro/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ru/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── sk/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── sl/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── sq/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── sr/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── sr_Latn/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── sv/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── sw/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── ta/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── te/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── tg/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── th/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── tk/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── tr/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── tt/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── udm/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── uk/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── ur/
    │       │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │       ├── django.mo
    │       │   │   │   │       └── django.po
    │       │   │   │   ├── uz/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── vi/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   ├── zh_Hans/
    │       │   │   │   │   ├── LC_MESSAGES/
    │       │   │   │   │   │   ├── django.mo
    │       │   │   │   │   │   └── django.po
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   │   └── formats.py
    │       │   │   │   └── zh_Hant/
    │       │   │   │       ├── LC_MESSAGES/
    │       │   │   │       │   ├── django.mo
    │       │   │   │       │   └── django.po
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__/
    │       │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │       │   └── formats.cpython-310.pyc
    │       │   │   │       └── formats.py
    │       │   │   ├── project_template/
    │       │   │   │   ├── manage.py-tpl
    │       │   │   │   └── project_name/
    │       │   │   │       ├── __init__.py-tpl
    │       │   │   │       ├── asgi.py-tpl
    │       │   │   │       ├── settings.py-tpl
    │       │   │   │       ├── urls.py-tpl
    │       │   │   │       └── wsgi.py-tpl
    │       │   │   └── urls/
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__/
    │       │   │       │   ├── __init__.cpython-310.pyc
    │       │   │       │   ├── i18n.cpython-310.pyc
    │       │   │       │   └── static.cpython-310.pyc
    │       │   │       ├── i18n.py
    │       │   │       └── static.py
    │       │   ├── contrib/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   └── __init__.cpython-310.pyc
    │       │   │   ├── admin/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── actions.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── checks.cpython-310.pyc
    │       │   │   │   │   ├── decorators.cpython-310.pyc
    │       │   │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   │   ├── filters.cpython-310.pyc
    │       │   │   │   │   ├── forms.cpython-310.pyc
    │       │   │   │   │   ├── helpers.cpython-310.pyc
    │       │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   ├── options.cpython-310.pyc
    │       │   │   │   │   ├── sites.cpython-310.pyc
    │       │   │   │   │   ├── tests.cpython-310.pyc
    │       │   │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   │   └── widgets.cpython-310.pyc
    │       │   │   │   ├── actions.py
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── checks.py
    │       │   │   │   ├── decorators.py
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── filters.py
    │       │   │   │   ├── forms.py
    │       │   │   │   ├── helpers.py
    │       │   │   │   ├── locale/
    │       │   │   │   │   ├── af/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── am/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ar_DZ/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ast/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── az/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── be/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── bg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── bn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── br/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── bs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ca/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── cs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── cy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── da/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── de/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── dsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── el/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── en/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── en_AU/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── en_GB/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── eo/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── es/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── es_AR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── es_CO/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── es_MX/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── es_VE/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── et/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── eu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── fa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── fi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── fr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── fy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ga/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── gd/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── gl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── he/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── hi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── hr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── hsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── hu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── hy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ia/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── id/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── io/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── is/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── it/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ja/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ka/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── kab/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── kk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── km/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── kn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ko/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ky/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── lb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── lt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── lv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── mk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ml/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── mn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── mr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── my/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── nb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ne/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── nl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── nn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── os/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── pa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── pl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── pt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── pt_BR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ro/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ru/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── sk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── sl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── sq/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── sr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── sr_Latn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── sv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── sw/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ta/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── te/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── tg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── th/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── tr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── tt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── udm/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── uk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── ur/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── uz/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── vi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   ├── zh_Hans/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       ├── django.po
    │       │   │   │   │   │       ├── djangojs.mo
    │       │   │   │   │   │       └── djangojs.po
    │       │   │   │   │   └── zh_Hant/
    │       │   │   │   │       └── LC_MESSAGES/
    │       │   │   │   │           ├── django.mo
    │       │   │   │   │           ├── django.po
    │       │   │   │   │           ├── djangojs.mo
    │       │   │   │   │           └── djangojs.po
    │       │   │   │   ├── migrations/
    │       │   │   │   │   ├── 0001_initial.py
    │       │   │   │   │   ├── 0002_logentry_remove_auto_add.py
    │       │   │   │   │   ├── 0003_logentry_add_action_flag_choices.py
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── 0001_initial.cpython-310.pyc
    │       │   │   │   │       ├── 0002_logentry_remove_auto_add.cpython-310.pyc
    │       │   │   │   │       ├── 0003_logentry_add_action_flag_choices.cpython-310.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── models.py
    │       │   │   │   ├── options.py
    │       │   │   │   ├── sites.py
    │       │   │   │   ├── static/
    │       │   │   │   │   └── admin/
    │       │   │   │   │       ├── css/
    │       │   │   │   │       │   ├── autocomplete.css
    │       │   │   │   │       │   ├── base.css
    │       │   │   │   │       │   ├── changelists.css
    │       │   │   │   │       │   ├── dashboard.css
    │       │   │   │   │       │   ├── fonts.css
    │       │   │   │   │       │   ├── forms.css
    │       │   │   │   │       │   ├── login.css
    │       │   │   │   │       │   ├── nav_sidebar.css
    │       │   │   │   │       │   ├── responsive.css
    │       │   │   │   │       │   ├── responsive_rtl.css
    │       │   │   │   │       │   ├── rtl.css
    │       │   │   │   │       │   ├── vendor/
    │       │   │   │   │       │   │   └── select2/
    │       │   │   │   │       │   │       ├── LICENSE-SELECT2.md
    │       │   │   │   │       │   │       ├── select2.css
    │       │   │   │   │       │   │       └── select2.min.css
    │       │   │   │   │       │   └── widgets.css
    │       │   │   │   │       ├── fonts/
    │       │   │   │   │       │   ├── LICENSE.txt
    │       │   │   │   │       │   ├── README.txt
    │       │   │   │   │       │   ├── Roboto-Bold-webfont.woff
    │       │   │   │   │       │   ├── Roboto-Light-webfont.woff
    │       │   │   │   │       │   └── Roboto-Regular-webfont.woff
    │       │   │   │   │       ├── img/
    │       │   │   │   │       │   ├── LICENSE
    │       │   │   │   │       │   ├── README.txt
    │       │   │   │   │       │   ├── calendar-icons.svg
    │       │   │   │   │       │   ├── gis/
    │       │   │   │   │       │   │   ├── move_vertex_off.svg
    │       │   │   │   │       │   │   └── move_vertex_on.svg
    │       │   │   │   │       │   ├── icon-addlink.svg
    │       │   │   │   │       │   ├── icon-alert.svg
    │       │   │   │   │       │   ├── icon-calendar.svg
    │       │   │   │   │       │   ├── icon-changelink.svg
    │       │   │   │   │       │   ├── icon-clock.svg
    │       │   │   │   │       │   ├── icon-deletelink.svg
    │       │   │   │   │       │   ├── icon-no.svg
    │       │   │   │   │       │   ├── icon-unknown-alt.svg
    │       │   │   │   │       │   ├── icon-unknown.svg
    │       │   │   │   │       │   ├── icon-viewlink.svg
    │       │   │   │   │       │   ├── icon-yes.svg
    │       │   │   │   │       │   ├── inline-delete.svg
    │       │   │   │   │       │   ├── search.svg
    │       │   │   │   │       │   ├── selector-icons.svg
    │       │   │   │   │       │   ├── sorting-icons.svg
    │       │   │   │   │       │   ├── tooltag-add.svg
    │       │   │   │   │       │   └── tooltag-arrowright.svg
    │       │   │   │   │       └── js/
    │       │   │   │   │           ├── SelectBox.js
    │       │   │   │   │           ├── SelectFilter2.js
    │       │   │   │   │           ├── actions.js
    │       │   │   │   │           ├── admin/
    │       │   │   │   │           │   ├── DateTimeShortcuts.js
    │       │   │   │   │           │   └── RelatedObjectLookups.js
    │       │   │   │   │           ├── autocomplete.js
    │       │   │   │   │           ├── calendar.js
    │       │   │   │   │           ├── cancel.js
    │       │   │   │   │           ├── change_form.js
    │       │   │   │   │           ├── collapse.js
    │       │   │   │   │           ├── core.js
    │       │   │   │   │           ├── inlines.js
    │       │   │   │   │           ├── jquery.init.js
    │       │   │   │   │           ├── nav_sidebar.js
    │       │   │   │   │           ├── popup_response.js
    │       │   │   │   │           ├── prepopulate.js
    │       │   │   │   │           ├── prepopulate_init.js
    │       │   │   │   │           ├── urlify.js
    │       │   │   │   │           └── vendor/
    │       │   │   │   │               ├── jquery/
    │       │   │   │   │               │   ├── LICENSE.txt
    │       │   │   │   │               │   ├── jquery.js
    │       │   │   │   │               │   └── jquery.min.js
    │       │   │   │   │               ├── select2/
    │       │   │   │   │               │   ├── LICENSE.md
    │       │   │   │   │               │   ├── i18n/
    │       │   │   │   │               │   │   ├── af.js
    │       │   │   │   │               │   │   ├── ar.js
    │       │   │   │   │               │   │   ├── az.js
    │       │   │   │   │               │   │   ├── bg.js
    │       │   │   │   │               │   │   ├── bn.js
    │       │   │   │   │               │   │   ├── bs.js
    │       │   │   │   │               │   │   ├── ca.js
    │       │   │   │   │               │   │   ├── cs.js
    │       │   │   │   │               │   │   ├── da.js
    │       │   │   │   │               │   │   ├── de.js
    │       │   │   │   │               │   │   ├── dsb.js
    │       │   │   │   │               │   │   ├── el.js
    │       │   │   │   │               │   │   ├── en.js
    │       │   │   │   │               │   │   ├── es.js
    │       │   │   │   │               │   │   ├── et.js
    │       │   │   │   │               │   │   ├── eu.js
    │       │   │   │   │               │   │   ├── fa.js
    │       │   │   │   │               │   │   ├── fi.js
    │       │   │   │   │               │   │   ├── fr.js
    │       │   │   │   │               │   │   ├── gl.js
    │       │   │   │   │               │   │   ├── he.js
    │       │   │   │   │               │   │   ├── hi.js
    │       │   │   │   │               │   │   ├── hr.js
    │       │   │   │   │               │   │   ├── hsb.js
    │       │   │   │   │               │   │   ├── hu.js
    │       │   │   │   │               │   │   ├── hy.js
    │       │   │   │   │               │   │   ├── id.js
    │       │   │   │   │               │   │   ├── is.js
    │       │   │   │   │               │   │   ├── it.js
    │       │   │   │   │               │   │   ├── ja.js
    │       │   │   │   │               │   │   ├── ka.js
    │       │   │   │   │               │   │   ├── km.js
    │       │   │   │   │               │   │   ├── ko.js
    │       │   │   │   │               │   │   ├── lt.js
    │       │   │   │   │               │   │   ├── lv.js
    │       │   │   │   │               │   │   ├── mk.js
    │       │   │   │   │               │   │   ├── ms.js
    │       │   │   │   │               │   │   ├── nb.js
    │       │   │   │   │               │   │   ├── ne.js
    │       │   │   │   │               │   │   ├── nl.js
    │       │   │   │   │               │   │   ├── pl.js
    │       │   │   │   │               │   │   ├── ps.js
    │       │   │   │   │               │   │   ├── pt-BR.js
    │       │   │   │   │               │   │   ├── pt.js
    │       │   │   │   │               │   │   ├── ro.js
    │       │   │   │   │               │   │   ├── ru.js
    │       │   │   │   │               │   │   ├── sk.js
    │       │   │   │   │               │   │   ├── sl.js
    │       │   │   │   │               │   │   ├── sq.js
    │       │   │   │   │               │   │   ├── sr-Cyrl.js
    │       │   │   │   │               │   │   ├── sr.js
    │       │   │   │   │               │   │   ├── sv.js
    │       │   │   │   │               │   │   ├── th.js
    │       │   │   │   │               │   │   ├── tk.js
    │       │   │   │   │               │   │   ├── tr.js
    │       │   │   │   │               │   │   ├── uk.js
    │       │   │   │   │               │   │   ├── vi.js
    │       │   │   │   │               │   │   ├── zh-CN.js
    │       │   │   │   │               │   │   └── zh-TW.js
    │       │   │   │   │               │   ├── select2.full.js
    │       │   │   │   │               │   └── select2.full.min.js
    │       │   │   │   │               └── xregexp/
    │       │   │   │   │                   ├── LICENSE.txt
    │       │   │   │   │                   ├── xregexp.js
    │       │   │   │   │                   └── xregexp.min.js
    │       │   │   │   ├── templates/
    │       │   │   │   │   ├── admin/
    │       │   │   │   │   │   ├── 404.html
    │       │   │   │   │   │   ├── 500.html
    │       │   │   │   │   │   ├── actions.html
    │       │   │   │   │   │   ├── app_index.html
    │       │   │   │   │   │   ├── app_list.html
    │       │   │   │   │   │   ├── auth/
    │       │   │   │   │   │   │   └── user/
    │       │   │   │   │   │   │       ├── add_form.html
    │       │   │   │   │   │   │       └── change_password.html
    │       │   │   │   │   │   ├── base.html
    │       │   │   │   │   │   ├── base_site.html
    │       │   │   │   │   │   ├── change_form.html
    │       │   │   │   │   │   ├── change_form_object_tools.html
    │       │   │   │   │   │   ├── change_list.html
    │       │   │   │   │   │   ├── change_list_object_tools.html
    │       │   │   │   │   │   ├── change_list_results.html
    │       │   │   │   │   │   ├── date_hierarchy.html
    │       │   │   │   │   │   ├── delete_confirmation.html
    │       │   │   │   │   │   ├── delete_selected_confirmation.html
    │       │   │   │   │   │   ├── edit_inline/
    │       │   │   │   │   │   │   ├── stacked.html
    │       │   │   │   │   │   │   └── tabular.html
    │       │   │   │   │   │   ├── filter.html
    │       │   │   │   │   │   ├── includes/
    │       │   │   │   │   │   │   ├── fieldset.html
    │       │   │   │   │   │   │   └── object_delete_summary.html
    │       │   │   │   │   │   ├── index.html
    │       │   │   │   │   │   ├── invalid_setup.html
    │       │   │   │   │   │   ├── login.html
    │       │   │   │   │   │   ├── nav_sidebar.html
    │       │   │   │   │   │   ├── object_history.html
    │       │   │   │   │   │   ├── pagination.html
    │       │   │   │   │   │   ├── popup_response.html
    │       │   │   │   │   │   ├── prepopulated_fields_js.html
    │       │   │   │   │   │   ├── search_form.html
    │       │   │   │   │   │   ├── submit_line.html
    │       │   │   │   │   │   └── widgets/
    │       │   │   │   │   │       ├── clearable_file_input.html
    │       │   │   │   │   │       ├── foreign_key_raw_id.html
    │       │   │   │   │   │       ├── many_to_many_raw_id.html
    │       │   │   │   │   │       ├── radio.html
    │       │   │   │   │   │       ├── related_widget_wrapper.html
    │       │   │   │   │   │       ├── split_datetime.html
    │       │   │   │   │   │       └── url.html
    │       │   │   │   │   └── registration/
    │       │   │   │   │       ├── logged_out.html
    │       │   │   │   │       ├── password_change_done.html
    │       │   │   │   │       ├── password_change_form.html
    │       │   │   │   │       ├── password_reset_complete.html
    │       │   │   │   │       ├── password_reset_confirm.html
    │       │   │   │   │       ├── password_reset_done.html
    │       │   │   │   │       ├── password_reset_email.html
    │       │   │   │   │       └── password_reset_form.html
    │       │   │   │   ├── templatetags/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── admin_list.cpython-310.pyc
    │       │   │   │   │   │   ├── admin_modify.cpython-310.pyc
    │       │   │   │   │   │   ├── admin_urls.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   └── log.cpython-310.pyc
    │       │   │   │   │   ├── admin_list.py
    │       │   │   │   │   ├── admin_modify.py
    │       │   │   │   │   ├── admin_urls.py
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   └── log.py
    │       │   │   │   ├── tests.py
    │       │   │   │   ├── utils.py
    │       │   │   │   ├── views/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── autocomplete.cpython-310.pyc
    │       │   │   │   │   │   ├── decorators.cpython-310.pyc
    │       │   │   │   │   │   └── main.cpython-310.pyc
    │       │   │   │   │   ├── autocomplete.py
    │       │   │   │   │   ├── decorators.py
    │       │   │   │   │   └── main.py
    │       │   │   │   └── widgets.py
    │       │   │   ├── admindocs/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── middleware.cpython-310.pyc
    │       │   │   │   │   ├── urls.cpython-310.pyc
    │       │   │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   │   └── views.cpython-310.pyc
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── locale/
    │       │   │   │   │   ├── af/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar_DZ/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ast/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── az/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── be/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── br/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ca/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── da/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── de/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── dsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── el/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_AU/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_GB/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eo/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_AR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_CO/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_MX/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_VE/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── et/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ga/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gd/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── he/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ia/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── id/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── io/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── is/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── it/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ja/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ka/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kab/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── km/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ko/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ky/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ml/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── my/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ne/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── os/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt_BR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ro/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ru/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sq/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr_Latn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sw/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ta/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── te/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── th/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── udm/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ur/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── vi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── zh_Hans/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   └── zh_Hant/
    │       │   │   │   │       └── LC_MESSAGES/
    │       │   │   │   │           ├── django.mo
    │       │   │   │   │           └── django.po
    │       │   │   │   ├── middleware.py
    │       │   │   │   ├── templates/
    │       │   │   │   │   └── admin_doc/
    │       │   │   │   │       ├── bookmarklets.html
    │       │   │   │   │       ├── index.html
    │       │   │   │   │       ├── missing_docutils.html
    │       │   │   │   │       ├── model_detail.html
    │       │   │   │   │       ├── model_index.html
    │       │   │   │   │       ├── template_detail.html
    │       │   │   │   │       ├── template_filter_index.html
    │       │   │   │   │       ├── template_tag_index.html
    │       │   │   │   │       ├── view_detail.html
    │       │   │   │   │       └── view_index.html
    │       │   │   │   ├── urls.py
    │       │   │   │   ├── utils.py
    │       │   │   │   └── views.py
    │       │   │   ├── auth/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── admin.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── backends.cpython-310.pyc
    │       │   │   │   │   ├── base_user.cpython-310.pyc
    │       │   │   │   │   ├── checks.cpython-310.pyc
    │       │   │   │   │   ├── context_processors.cpython-310.pyc
    │       │   │   │   │   ├── decorators.cpython-310.pyc
    │       │   │   │   │   ├── forms.cpython-310.pyc
    │       │   │   │   │   ├── hashers.cpython-310.pyc
    │       │   │   │   │   ├── middleware.cpython-310.pyc
    │       │   │   │   │   ├── mixins.cpython-310.pyc
    │       │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   ├── password_validation.cpython-310.pyc
    │       │   │   │   │   ├── signals.cpython-310.pyc
    │       │   │   │   │   ├── tokens.cpython-310.pyc
    │       │   │   │   │   ├── urls.cpython-310.pyc
    │       │   │   │   │   ├── validators.cpython-310.pyc
    │       │   │   │   │   └── views.cpython-310.pyc
    │       │   │   │   ├── admin.py
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── backends.py
    │       │   │   │   ├── base_user.py
    │       │   │   │   ├── checks.py
    │       │   │   │   ├── common-passwords.txt.gz
    │       │   │   │   ├── context_processors.py
    │       │   │   │   ├── decorators.py
    │       │   │   │   ├── forms.py
    │       │   │   │   ├── handlers/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── modwsgi.cpython-310.pyc
    │       │   │   │   │   └── modwsgi.py
    │       │   │   │   ├── hashers.py
    │       │   │   │   ├── locale/
    │       │   │   │   │   ├── af/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar_DZ/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ast/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── az/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── be/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── br/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ca/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── da/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── de/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── dsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── el/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_AU/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_GB/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eo/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_AR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_CO/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_MX/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_VE/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── et/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ga/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gd/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── he/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ia/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── id/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── io/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── is/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── it/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ja/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ka/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kab/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── km/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ko/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ky/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ml/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── my/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ne/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── os/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt_BR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ro/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ru/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sq/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr_Latn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sw/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ta/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── te/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── th/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── udm/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ur/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uz/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── vi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── zh_Hans/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   └── zh_Hant/
    │       │   │   │   │       └── LC_MESSAGES/
    │       │   │   │   │           ├── django.mo
    │       │   │   │   │           └── django.po
    │       │   │   │   ├── management/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   │   └── commands/
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__/
    │       │   │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │   │       │   ├── changepassword.cpython-310.pyc
    │       │   │   │   │       │   └── createsuperuser.cpython-310.pyc
    │       │   │   │   │       ├── changepassword.py
    │       │   │   │   │       └── createsuperuser.py
    │       │   │   │   ├── middleware.py
    │       │   │   │   ├── migrations/
    │       │   │   │   │   ├── 0001_initial.py
    │       │   │   │   │   ├── 0002_alter_permission_name_max_length.py
    │       │   │   │   │   ├── 0003_alter_user_email_max_length.py
    │       │   │   │   │   ├── 0004_alter_user_username_opts.py
    │       │   │   │   │   ├── 0005_alter_user_last_login_null.py
    │       │   │   │   │   ├── 0006_require_contenttypes_0002.py
    │       │   │   │   │   ├── 0007_alter_validators_add_error_messages.py
    │       │   │   │   │   ├── 0008_alter_user_username_max_length.py
    │       │   │   │   │   ├── 0009_alter_user_last_name_max_length.py
    │       │   │   │   │   ├── 0010_alter_group_name_max_length.py
    │       │   │   │   │   ├── 0011_update_proxy_permissions.py
    │       │   │   │   │   ├── 0012_alter_user_first_name_max_length.py
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── 0001_initial.cpython-310.pyc
    │       │   │   │   │       ├── 0002_alter_permission_name_max_length.cpython-310.pyc
    │       │   │   │   │       ├── 0003_alter_user_email_max_length.cpython-310.pyc
    │       │   │   │   │       ├── 0004_alter_user_username_opts.cpython-310.pyc
    │       │   │   │   │       ├── 0005_alter_user_last_login_null.cpython-310.pyc
    │       │   │   │   │       ├── 0006_require_contenttypes_0002.cpython-310.pyc
    │       │   │   │   │       ├── 0007_alter_validators_add_error_messages.cpython-310.pyc
    │       │   │   │   │       ├── 0008_alter_user_username_max_length.cpython-310.pyc
    │       │   │   │   │       ├── 0009_alter_user_last_name_max_length.cpython-310.pyc
    │       │   │   │   │       ├── 0010_alter_group_name_max_length.cpython-310.pyc
    │       │   │   │   │       ├── 0011_update_proxy_permissions.cpython-310.pyc
    │       │   │   │   │       ├── 0012_alter_user_first_name_max_length.cpython-310.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── mixins.py
    │       │   │   │   ├── models.py
    │       │   │   │   ├── password_validation.py
    │       │   │   │   ├── signals.py
    │       │   │   │   ├── templates/
    │       │   │   │   │   ├── auth/
    │       │   │   │   │   │   └── widgets/
    │       │   │   │   │   │       └── read_only_password_hash.html
    │       │   │   │   │   └── registration/
    │       │   │   │   │       └── password_reset_subject.txt
    │       │   │   │   ├── tokens.py
    │       │   │   │   ├── urls.py
    │       │   │   │   ├── validators.py
    │       │   │   │   └── views.py
    │       │   │   ├── contenttypes/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── admin.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── checks.cpython-310.pyc
    │       │   │   │   │   ├── fields.cpython-310.pyc
    │       │   │   │   │   ├── forms.cpython-310.pyc
    │       │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   └── views.cpython-310.pyc
    │       │   │   │   ├── admin.py
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── checks.py
    │       │   │   │   ├── fields.py
    │       │   │   │   ├── forms.py
    │       │   │   │   ├── locale/
    │       │   │   │   │   ├── af/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar_DZ/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ast/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── az/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── be/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── br/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ca/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── da/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── de/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── dsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── el/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_AU/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_GB/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eo/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_AR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_CO/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_MX/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_VE/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── et/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ga/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gd/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── he/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ia/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── id/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── io/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── is/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── it/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ja/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ka/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── km/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ko/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ky/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ml/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── my/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ne/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── os/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt_BR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ro/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ru/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sq/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr_Latn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sw/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ta/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── te/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── th/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── udm/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ur/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── vi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── zh_Hans/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   └── zh_Hant/
    │       │   │   │   │       └── LC_MESSAGES/
    │       │   │   │   │           ├── django.mo
    │       │   │   │   │           └── django.po
    │       │   │   │   ├── management/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   │   └── commands/
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__/
    │       │   │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │   │       │   └── remove_stale_contenttypes.cpython-310.pyc
    │       │   │   │   │       └── remove_stale_contenttypes.py
    │       │   │   │   ├── migrations/
    │       │   │   │   │   ├── 0001_initial.py
    │       │   │   │   │   ├── 0002_remove_content_type_name.py
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── 0001_initial.cpython-310.pyc
    │       │   │   │   │       ├── 0002_remove_content_type_name.cpython-310.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── models.py
    │       │   │   │   └── views.py
    │       │   │   ├── flatpages/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── admin.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── forms.cpython-310.pyc
    │       │   │   │   │   ├── middleware.cpython-310.pyc
    │       │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   ├── sitemaps.cpython-310.pyc
    │       │   │   │   │   ├── urls.cpython-310.pyc
    │       │   │   │   │   └── views.cpython-310.pyc
    │       │   │   │   ├── admin.py
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── forms.py
    │       │   │   │   ├── locale/
    │       │   │   │   │   ├── af/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar_DZ/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ast/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── az/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── be/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── br/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ca/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── da/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── de/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── dsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── el/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_AU/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_GB/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eo/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_AR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_CO/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_MX/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_VE/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── et/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ga/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gd/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── he/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ia/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── id/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── io/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── is/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── it/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ja/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ka/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── km/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ko/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ky/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ml/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── my/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ne/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── os/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt_BR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ro/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ru/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sq/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr_Latn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sw/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ta/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── te/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── th/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── udm/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ur/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── vi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── zh_Hans/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   └── zh_Hant/
    │       │   │   │   │       └── LC_MESSAGES/
    │       │   │   │   │           ├── django.mo
    │       │   │   │   │           └── django.po
    │       │   │   │   ├── middleware.py
    │       │   │   │   ├── migrations/
    │       │   │   │   │   ├── 0001_initial.py
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── 0001_initial.cpython-310.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── models.py
    │       │   │   │   ├── sitemaps.py
    │       │   │   │   ├── templatetags/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── flatpages.cpython-310.pyc
    │       │   │   │   │   └── flatpages.py
    │       │   │   │   ├── urls.py
    │       │   │   │   └── views.py
    │       │   │   ├── gis/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── feeds.cpython-310.pyc
    │       │   │   │   │   ├── geometry.cpython-310.pyc
    │       │   │   │   │   ├── measure.cpython-310.pyc
    │       │   │   │   │   ├── ptr.cpython-310.pyc
    │       │   │   │   │   ├── shortcuts.cpython-310.pyc
    │       │   │   │   │   └── views.cpython-310.pyc
    │       │   │   │   ├── admin/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── options.cpython-310.pyc
    │       │   │   │   │   │   └── widgets.cpython-310.pyc
    │       │   │   │   │   ├── options.py
    │       │   │   │   │   └── widgets.py
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── db/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   │   ├── backends/
    │       │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   │   └── utils.cpython-310.pyc
    │       │   │   │   │   │   ├── base/
    │       │   │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── adapter.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── features.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   │   │   │   └── operations.cpython-310.pyc
    │       │   │   │   │   │   │   ├── adapter.py
    │       │   │   │   │   │   │   ├── features.py
    │       │   │   │   │   │   │   ├── models.py
    │       │   │   │   │   │   │   └── operations.py
    │       │   │   │   │   │   ├── mysql/
    │       │   │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── features.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── introspection.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── operations.cpython-310.pyc
    │       │   │   │   │   │   │   │   └── schema.cpython-310.pyc
    │       │   │   │   │   │   │   ├── base.py
    │       │   │   │   │   │   │   ├── features.py
    │       │   │   │   │   │   │   ├── introspection.py
    │       │   │   │   │   │   │   ├── operations.py
    │       │   │   │   │   │   │   └── schema.py
    │       │   │   │   │   │   ├── oracle/
    │       │   │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── adapter.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── features.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── introspection.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── operations.cpython-310.pyc
    │       │   │   │   │   │   │   │   └── schema.cpython-310.pyc
    │       │   │   │   │   │   │   ├── adapter.py
    │       │   │   │   │   │   │   ├── base.py
    │       │   │   │   │   │   │   ├── features.py
    │       │   │   │   │   │   │   ├── introspection.py
    │       │   │   │   │   │   │   ├── models.py
    │       │   │   │   │   │   │   ├── operations.py
    │       │   │   │   │   │   │   └── schema.py
    │       │   │   │   │   │   ├── postgis/
    │       │   │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── adapter.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── const.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── features.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── introspection.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── operations.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── pgraster.cpython-310.pyc
    │       │   │   │   │   │   │   │   └── schema.cpython-310.pyc
    │       │   │   │   │   │   │   ├── adapter.py
    │       │   │   │   │   │   │   ├── base.py
    │       │   │   │   │   │   │   ├── const.py
    │       │   │   │   │   │   │   ├── features.py
    │       │   │   │   │   │   │   ├── introspection.py
    │       │   │   │   │   │   │   ├── models.py
    │       │   │   │   │   │   │   ├── operations.py
    │       │   │   │   │   │   │   ├── pgraster.py
    │       │   │   │   │   │   │   └── schema.py
    │       │   │   │   │   │   ├── spatialite/
    │       │   │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── adapter.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── client.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── features.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── introspection.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   │   │   │   ├── operations.cpython-310.pyc
    │       │   │   │   │   │   │   │   └── schema.cpython-310.pyc
    │       │   │   │   │   │   │   ├── adapter.py
    │       │   │   │   │   │   │   ├── base.py
    │       │   │   │   │   │   │   ├── client.py
    │       │   │   │   │   │   │   ├── features.py
    │       │   │   │   │   │   │   ├── introspection.py
    │       │   │   │   │   │   │   ├── models.py
    │       │   │   │   │   │   │   ├── operations.py
    │       │   │   │   │   │   │   └── schema.py
    │       │   │   │   │   │   └── utils.py
    │       │   │   │   │   └── models/
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__/
    │       │   │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │   │       │   ├── aggregates.cpython-310.pyc
    │       │   │   │   │       │   ├── fields.cpython-310.pyc
    │       │   │   │   │       │   ├── functions.cpython-310.pyc
    │       │   │   │   │       │   ├── lookups.cpython-310.pyc
    │       │   │   │   │       │   └── proxy.cpython-310.pyc
    │       │   │   │   │       ├── aggregates.py
    │       │   │   │   │       ├── fields.py
    │       │   │   │   │       ├── functions.py
    │       │   │   │   │       ├── lookups.py
    │       │   │   │   │       ├── proxy.py
    │       │   │   │   │       └── sql/
    │       │   │   │   │           ├── __init__.py
    │       │   │   │   │           ├── __pycache__/
    │       │   │   │   │           │   ├── __init__.cpython-310.pyc
    │       │   │   │   │           │   └── conversion.cpython-310.pyc
    │       │   │   │   │           └── conversion.py
    │       │   │   │   ├── feeds.py
    │       │   │   │   ├── forms/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── fields.cpython-310.pyc
    │       │   │   │   │   │   └── widgets.cpython-310.pyc
    │       │   │   │   │   ├── fields.py
    │       │   │   │   │   └── widgets.py
    │       │   │   │   ├── gdal/
    │       │   │   │   │   ├── LICENSE
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── datasource.cpython-310.pyc
    │       │   │   │   │   │   ├── driver.cpython-310.pyc
    │       │   │   │   │   │   ├── envelope.cpython-310.pyc
    │       │   │   │   │   │   ├── error.cpython-310.pyc
    │       │   │   │   │   │   ├── feature.cpython-310.pyc
    │       │   │   │   │   │   ├── field.cpython-310.pyc
    │       │   │   │   │   │   ├── geometries.cpython-310.pyc
    │       │   │   │   │   │   ├── geomtype.cpython-310.pyc
    │       │   │   │   │   │   ├── layer.cpython-310.pyc
    │       │   │   │   │   │   ├── libgdal.cpython-310.pyc
    │       │   │   │   │   │   └── srs.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── datasource.py
    │       │   │   │   │   ├── driver.py
    │       │   │   │   │   ├── envelope.py
    │       │   │   │   │   ├── error.py
    │       │   │   │   │   ├── feature.py
    │       │   │   │   │   ├── field.py
    │       │   │   │   │   ├── geometries.py
    │       │   │   │   │   ├── geomtype.py
    │       │   │   │   │   ├── layer.py
    │       │   │   │   │   ├── libgdal.py
    │       │   │   │   │   ├── prototypes/
    │       │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   │   ├── ds.cpython-310.pyc
    │       │   │   │   │   │   │   ├── errcheck.cpython-310.pyc
    │       │   │   │   │   │   │   ├── generation.cpython-310.pyc
    │       │   │   │   │   │   │   ├── geom.cpython-310.pyc
    │       │   │   │   │   │   │   ├── raster.cpython-310.pyc
    │       │   │   │   │   │   │   └── srs.cpython-310.pyc
    │       │   │   │   │   │   ├── ds.py
    │       │   │   │   │   │   ├── errcheck.py
    │       │   │   │   │   │   ├── generation.py
    │       │   │   │   │   │   ├── geom.py
    │       │   │   │   │   │   ├── raster.py
    │       │   │   │   │   │   └── srs.py
    │       │   │   │   │   ├── raster/
    │       │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   │   ├── band.cpython-310.pyc
    │       │   │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   │   ├── const.cpython-310.pyc
    │       │   │   │   │   │   │   └── source.cpython-310.pyc
    │       │   │   │   │   │   ├── band.py
    │       │   │   │   │   │   ├── base.py
    │       │   │   │   │   │   ├── const.py
    │       │   │   │   │   │   └── source.py
    │       │   │   │   │   └── srs.py
    │       │   │   │   ├── geoip2/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   └── resources.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   └── resources.py
    │       │   │   │   ├── geometry.py
    │       │   │   │   ├── geos/
    │       │   │   │   │   ├── LICENSE
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── collections.cpython-310.pyc
    │       │   │   │   │   │   ├── coordseq.cpython-310.pyc
    │       │   │   │   │   │   ├── error.cpython-310.pyc
    │       │   │   │   │   │   ├── factory.cpython-310.pyc
    │       │   │   │   │   │   ├── geometry.cpython-310.pyc
    │       │   │   │   │   │   ├── io.cpython-310.pyc
    │       │   │   │   │   │   ├── libgeos.cpython-310.pyc
    │       │   │   │   │   │   ├── linestring.cpython-310.pyc
    │       │   │   │   │   │   ├── mutable_list.cpython-310.pyc
    │       │   │   │   │   │   ├── point.cpython-310.pyc
    │       │   │   │   │   │   ├── polygon.cpython-310.pyc
    │       │   │   │   │   │   └── prepared.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── collections.py
    │       │   │   │   │   ├── coordseq.py
    │       │   │   │   │   ├── error.py
    │       │   │   │   │   ├── factory.py
    │       │   │   │   │   ├── geometry.py
    │       │   │   │   │   ├── io.py
    │       │   │   │   │   ├── libgeos.py
    │       │   │   │   │   ├── linestring.py
    │       │   │   │   │   ├── mutable_list.py
    │       │   │   │   │   ├── point.py
    │       │   │   │   │   ├── polygon.py
    │       │   │   │   │   ├── prepared.py
    │       │   │   │   │   └── prototypes/
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__/
    │       │   │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │   │       │   ├── coordseq.cpython-310.pyc
    │       │   │   │   │       │   ├── errcheck.cpython-310.pyc
    │       │   │   │   │       │   ├── geom.cpython-310.pyc
    │       │   │   │   │       │   ├── io.cpython-310.pyc
    │       │   │   │   │       │   ├── misc.cpython-310.pyc
    │       │   │   │   │       │   ├── predicates.cpython-310.pyc
    │       │   │   │   │       │   ├── prepared.cpython-310.pyc
    │       │   │   │   │       │   ├── threadsafe.cpython-310.pyc
    │       │   │   │   │       │   └── topology.cpython-310.pyc
    │       │   │   │   │       ├── coordseq.py
    │       │   │   │   │       ├── errcheck.py
    │       │   │   │   │       ├── geom.py
    │       │   │   │   │       ├── io.py
    │       │   │   │   │       ├── misc.py
    │       │   │   │   │       ├── predicates.py
    │       │   │   │   │       ├── prepared.py
    │       │   │   │   │       ├── threadsafe.py
    │       │   │   │   │       └── topology.py
    │       │   │   │   ├── locale/
    │       │   │   │   │   ├── af/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar_DZ/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ast/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── az/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── be/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── br/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ca/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── da/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── de/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── dsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── el/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_AU/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_GB/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eo/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_AR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_CO/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_MX/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_VE/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── et/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ga/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gd/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── he/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ia/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── id/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── io/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── is/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── it/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ja/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ka/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── km/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ko/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ky/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ml/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── my/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ne/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── os/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt_BR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ro/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ru/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sq/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr_Latn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sw/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ta/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── te/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── th/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── udm/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ur/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── vi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── zh_Hans/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   └── zh_Hant/
    │       │   │   │   │       └── LC_MESSAGES/
    │       │   │   │   │           ├── django.mo
    │       │   │   │   │           └── django.po
    │       │   │   │   ├── management/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   │   └── commands/
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__/
    │       │   │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │   │       │   ├── inspectdb.cpython-310.pyc
    │       │   │   │   │       │   └── ogrinspect.cpython-310.pyc
    │       │   │   │   │       ├── inspectdb.py
    │       │   │   │   │       └── ogrinspect.py
    │       │   │   │   ├── measure.py
    │       │   │   │   ├── ptr.py
    │       │   │   │   ├── serializers/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── geojson.cpython-310.pyc
    │       │   │   │   │   └── geojson.py
    │       │   │   │   ├── shortcuts.py
    │       │   │   │   ├── sitemaps/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── kml.cpython-310.pyc
    │       │   │   │   │   │   └── views.cpython-310.pyc
    │       │   │   │   │   ├── kml.py
    │       │   │   │   │   └── views.py
    │       │   │   │   ├── static/
    │       │   │   │   │   └── gis/
    │       │   │   │   │       ├── css/
    │       │   │   │   │       │   └── ol3.css
    │       │   │   │   │       ├── img/
    │       │   │   │   │       │   ├── draw_line_off.svg
    │       │   │   │   │       │   ├── draw_line_on.svg
    │       │   │   │   │       │   ├── draw_point_off.svg
    │       │   │   │   │       │   ├── draw_point_on.svg
    │       │   │   │   │       │   ├── draw_polygon_off.svg
    │       │   │   │   │       │   └── draw_polygon_on.svg
    │       │   │   │   │       └── js/
    │       │   │   │   │           └── OLMapWidget.js
    │       │   │   │   ├── templates/
    │       │   │   │   │   └── gis/
    │       │   │   │   │       ├── admin/
    │       │   │   │   │       │   ├── openlayers.html
    │       │   │   │   │       │   ├── openlayers.js
    │       │   │   │   │       │   ├── osm.html
    │       │   │   │   │       │   └── osm.js
    │       │   │   │   │       ├── kml/
    │       │   │   │   │       │   ├── base.kml
    │       │   │   │   │       │   └── placemarks.kml
    │       │   │   │   │       ├── openlayers-osm.html
    │       │   │   │   │       └── openlayers.html
    │       │   │   │   ├── utils/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── layermapping.cpython-310.pyc
    │       │   │   │   │   │   ├── ogrinfo.cpython-310.pyc
    │       │   │   │   │   │   ├── ogrinspect.cpython-310.pyc
    │       │   │   │   │   │   └── srs.cpython-310.pyc
    │       │   │   │   │   ├── layermapping.py
    │       │   │   │   │   ├── ogrinfo.py
    │       │   │   │   │   ├── ogrinspect.py
    │       │   │   │   │   └── srs.py
    │       │   │   │   └── views.py
    │       │   │   ├── humanize/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   └── apps.cpython-310.pyc
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── locale/
    │       │   │   │   │   ├── af/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar_DZ/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ast/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── az/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── be/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── br/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ca/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── da/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── de/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── dsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── el/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_AU/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_GB/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eo/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_AR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_CO/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_MX/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_VE/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── et/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ga/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gd/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── he/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ia/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── id/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── io/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── is/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── it/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ja/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ka/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── km/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ko/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ky/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ml/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ms/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── my/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ne/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── os/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt_BR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ro/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ru/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sq/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr_Latn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sw/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ta/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── te/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── th/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── udm/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ur/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uz/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── vi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── zh_Hans/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   └── zh_Hant/
    │       │   │   │   │       └── LC_MESSAGES/
    │       │   │   │   │           ├── django.mo
    │       │   │   │   │           └── django.po
    │       │   │   │   └── templatetags/
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__/
    │       │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │       │   └── humanize.cpython-310.pyc
    │       │   │   │       └── humanize.py
    │       │   │   ├── messages/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── api.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── constants.cpython-310.pyc
    │       │   │   │   │   ├── context_processors.cpython-310.pyc
    │       │   │   │   │   ├── middleware.cpython-310.pyc
    │       │   │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   │   └── views.cpython-310.pyc
    │       │   │   │   ├── api.py
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── constants.py
    │       │   │   │   ├── context_processors.py
    │       │   │   │   ├── middleware.py
    │       │   │   │   ├── storage/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── cookie.cpython-310.pyc
    │       │   │   │   │   │   ├── fallback.cpython-310.pyc
    │       │   │   │   │   │   └── session.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── cookie.py
    │       │   │   │   │   ├── fallback.py
    │       │   │   │   │   └── session.py
    │       │   │   │   ├── utils.py
    │       │   │   │   └── views.py
    │       │   │   ├── postgres/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── constraints.cpython-310.pyc
    │       │   │   │   │   ├── functions.cpython-310.pyc
    │       │   │   │   │   ├── indexes.cpython-310.pyc
    │       │   │   │   │   ├── lookups.cpython-310.pyc
    │       │   │   │   │   ├── operations.cpython-310.pyc
    │       │   │   │   │   ├── search.cpython-310.pyc
    │       │   │   │   │   ├── serializers.cpython-310.pyc
    │       │   │   │   │   ├── signals.cpython-310.pyc
    │       │   │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   │   └── validators.cpython-310.pyc
    │       │   │   │   ├── aggregates/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── general.cpython-310.pyc
    │       │   │   │   │   │   ├── mixins.cpython-310.pyc
    │       │   │   │   │   │   └── statistics.cpython-310.pyc
    │       │   │   │   │   ├── general.py
    │       │   │   │   │   ├── mixins.py
    │       │   │   │   │   └── statistics.py
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── constraints.py
    │       │   │   │   ├── fields/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── array.cpython-310.pyc
    │       │   │   │   │   │   ├── citext.cpython-310.pyc
    │       │   │   │   │   │   ├── hstore.cpython-310.pyc
    │       │   │   │   │   │   ├── jsonb.cpython-310.pyc
    │       │   │   │   │   │   ├── ranges.cpython-310.pyc
    │       │   │   │   │   │   └── utils.cpython-310.pyc
    │       │   │   │   │   ├── array.py
    │       │   │   │   │   ├── citext.py
    │       │   │   │   │   ├── hstore.py
    │       │   │   │   │   ├── jsonb.py
    │       │   │   │   │   ├── ranges.py
    │       │   │   │   │   └── utils.py
    │       │   │   │   ├── forms/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── array.cpython-310.pyc
    │       │   │   │   │   │   ├── hstore.cpython-310.pyc
    │       │   │   │   │   │   ├── jsonb.cpython-310.pyc
    │       │   │   │   │   │   └── ranges.cpython-310.pyc
    │       │   │   │   │   ├── array.py
    │       │   │   │   │   ├── hstore.py
    │       │   │   │   │   ├── jsonb.py
    │       │   │   │   │   └── ranges.py
    │       │   │   │   ├── functions.py
    │       │   │   │   ├── indexes.py
    │       │   │   │   ├── jinja2/
    │       │   │   │   │   └── postgres/
    │       │   │   │   │       └── widgets/
    │       │   │   │   │           └── split_array.html
    │       │   │   │   ├── locale/
    │       │   │   │   │   ├── af/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar_DZ/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── az/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── be/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ca/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── da/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── de/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── dsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── el/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eo/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_AR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_CO/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_MX/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── et/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gd/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── he/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ia/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── id/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── is/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── it/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ja/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ka/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ko/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ky/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ml/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ne/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt_BR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ro/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ru/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sq/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr_Latn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uz/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── zh_Hans/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   └── zh_Hant/
    │       │   │   │   │       └── LC_MESSAGES/
    │       │   │   │   │           ├── django.mo
    │       │   │   │   │           └── django.po
    │       │   │   │   ├── lookups.py
    │       │   │   │   ├── operations.py
    │       │   │   │   ├── search.py
    │       │   │   │   ├── serializers.py
    │       │   │   │   ├── signals.py
    │       │   │   │   ├── templates/
    │       │   │   │   │   └── postgres/
    │       │   │   │   │       └── widgets/
    │       │   │   │   │           └── split_array.html
    │       │   │   │   ├── utils.py
    │       │   │   │   └── validators.py
    │       │   │   ├── redirects/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── admin.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── middleware.cpython-310.pyc
    │       │   │   │   │   └── models.cpython-310.pyc
    │       │   │   │   ├── admin.py
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── locale/
    │       │   │   │   │   ├── af/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar_DZ/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ast/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── az/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── be/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── br/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ca/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── da/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── de/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── dsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── el/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_AU/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_GB/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eo/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_AR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_CO/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_MX/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_VE/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── et/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ga/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gd/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── he/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ia/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── id/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── io/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── is/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── it/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ja/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ka/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kab/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── km/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ko/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ky/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ml/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── my/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ne/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── os/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt_BR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ro/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ru/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sq/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr_Latn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sw/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ta/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── te/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── th/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── udm/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ur/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uz/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── vi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── zh_Hans/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   └── zh_Hant/
    │       │   │   │   │       └── LC_MESSAGES/
    │       │   │   │   │           ├── django.mo
    │       │   │   │   │           └── django.po
    │       │   │   │   ├── middleware.py
    │       │   │   │   ├── migrations/
    │       │   │   │   │   ├── 0001_initial.py
    │       │   │   │   │   ├── 0002_alter_redirect_new_path_help_text.py
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── 0001_initial.cpython-310.pyc
    │       │   │   │   │       ├── 0002_alter_redirect_new_path_help_text.cpython-310.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── models.py
    │       │   │   ├── sessions/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── base_session.cpython-310.pyc
    │       │   │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   │   ├── middleware.cpython-310.pyc
    │       │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   └── serializers.cpython-310.pyc
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── backends/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── cache.cpython-310.pyc
    │       │   │   │   │   │   ├── cached_db.cpython-310.pyc
    │       │   │   │   │   │   ├── db.cpython-310.pyc
    │       │   │   │   │   │   ├── file.cpython-310.pyc
    │       │   │   │   │   │   └── signed_cookies.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── cache.py
    │       │   │   │   │   ├── cached_db.py
    │       │   │   │   │   ├── db.py
    │       │   │   │   │   ├── file.py
    │       │   │   │   │   └── signed_cookies.py
    │       │   │   │   ├── base_session.py
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── locale/
    │       │   │   │   │   ├── af/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar_DZ/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ast/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── az/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── be/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── br/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ca/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── da/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── de/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── dsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── el/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_AU/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_GB/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eo/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_AR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_CO/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_MX/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_VE/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── et/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ga/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gd/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── he/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ia/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── id/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── io/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── is/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── it/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ja/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ka/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kab/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── km/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ko/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ky/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ml/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── my/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ne/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── os/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt_BR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ro/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ru/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sq/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr_Latn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sw/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ta/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── te/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── th/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── udm/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ur/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uz/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── vi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── zh_Hans/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   └── zh_Hant/
    │       │   │   │   │       └── LC_MESSAGES/
    │       │   │   │   │           ├── django.mo
    │       │   │   │   │           └── django.po
    │       │   │   │   ├── management/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   │   └── commands/
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__/
    │       │   │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │   │       │   └── clearsessions.cpython-310.pyc
    │       │   │   │   │       └── clearsessions.py
    │       │   │   │   ├── middleware.py
    │       │   │   │   ├── migrations/
    │       │   │   │   │   ├── 0001_initial.py
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── 0001_initial.cpython-310.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── models.py
    │       │   │   │   └── serializers.py
    │       │   │   ├── sitemaps/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   └── views.cpython-310.pyc
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── management/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   │   └── commands/
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__/
    │       │   │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │   │       │   └── ping_google.cpython-310.pyc
    │       │   │   │   │       └── ping_google.py
    │       │   │   │   ├── templates/
    │       │   │   │   │   ├── sitemap.xml
    │       │   │   │   │   └── sitemap_index.xml
    │       │   │   │   └── views.py
    │       │   │   ├── sites/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── admin.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── checks.cpython-310.pyc
    │       │   │   │   │   ├── management.cpython-310.pyc
    │       │   │   │   │   ├── managers.cpython-310.pyc
    │       │   │   │   │   ├── middleware.cpython-310.pyc
    │       │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   ├── requests.cpython-310.pyc
    │       │   │   │   │   └── shortcuts.cpython-310.pyc
    │       │   │   │   ├── admin.py
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── checks.py
    │       │   │   │   ├── locale/
    │       │   │   │   │   ├── af/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ar_DZ/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ast/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── az/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── be/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── br/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── bs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ca/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cs/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── cy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── da/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── de/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── dsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── el/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_AU/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── en_GB/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eo/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_AR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_CO/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_MX/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── es_VE/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── et/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── eu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── fy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ga/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gd/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── gl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── he/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hsb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hu/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── hy/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ia/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── id/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── io/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── is/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── it/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ja/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ka/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kab/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── km/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── kn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ko/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ky/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── lv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ml/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── mr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── my/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nb/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ne/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── nn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── os/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pa/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── pt_BR/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ro/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ru/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sl/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sq/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sr_Latn/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sv/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── sw/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ta/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── te/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tg/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── th/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tr/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── tt/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── udm/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uk/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── ur/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── uz/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── vi/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   ├── zh_Hans/
    │       │   │   │   │   │   └── LC_MESSAGES/
    │       │   │   │   │   │       ├── django.mo
    │       │   │   │   │   │       └── django.po
    │       │   │   │   │   └── zh_Hant/
    │       │   │   │   │       └── LC_MESSAGES/
    │       │   │   │   │           ├── django.mo
    │       │   │   │   │           └── django.po
    │       │   │   │   ├── management.py
    │       │   │   │   ├── managers.py
    │       │   │   │   ├── middleware.py
    │       │   │   │   ├── migrations/
    │       │   │   │   │   ├── 0001_initial.py
    │       │   │   │   │   ├── 0002_alter_domain_unique.py
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── 0001_initial.cpython-310.pyc
    │       │   │   │   │       ├── 0002_alter_domain_unique.cpython-310.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── models.py
    │       │   │   │   ├── requests.py
    │       │   │   │   └── shortcuts.py
    │       │   │   ├── staticfiles/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── apps.cpython-310.pyc
    │       │   │   │   │   ├── checks.cpython-310.pyc
    │       │   │   │   │   ├── finders.cpython-310.pyc
    │       │   │   │   │   ├── handlers.cpython-310.pyc
    │       │   │   │   │   ├── storage.cpython-310.pyc
    │       │   │   │   │   ├── testing.cpython-310.pyc
    │       │   │   │   │   ├── urls.cpython-310.pyc
    │       │   │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   │   └── views.cpython-310.pyc
    │       │   │   │   ├── apps.py
    │       │   │   │   ├── checks.py
    │       │   │   │   ├── finders.py
    │       │   │   │   ├── handlers.py
    │       │   │   │   ├── management/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   │   └── commands/
    │       │   │   │   │       ├── __init__.py
    │       │   │   │   │       ├── __pycache__/
    │       │   │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │   │       │   ├── collectstatic.cpython-310.pyc
    │       │   │   │   │       │   ├── findstatic.cpython-310.pyc
    │       │   │   │   │       │   └── runserver.cpython-310.pyc
    │       │   │   │   │       ├── collectstatic.py
    │       │   │   │   │       ├── findstatic.py
    │       │   │   │   │       └── runserver.py
    │       │   │   │   ├── storage.py
    │       │   │   │   ├── testing.py
    │       │   │   │   ├── urls.py
    │       │   │   │   ├── utils.py
    │       │   │   │   └── views.py
    │       │   │   └── syndication/
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__/
    │       │   │       │   ├── __init__.cpython-310.pyc
    │       │   │       │   ├── apps.cpython-310.pyc
    │       │   │       │   └── views.cpython-310.pyc
    │       │   │       ├── apps.py
    │       │   │       └── views.py
    │       │   ├── core/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── asgi.cpython-310.pyc
    │       │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   ├── paginator.cpython-310.pyc
    │       │   │   │   ├── signals.cpython-310.pyc
    │       │   │   │   ├── signing.cpython-310.pyc
    │       │   │   │   ├── validators.cpython-310.pyc
    │       │   │   │   └── wsgi.cpython-310.pyc
    │       │   │   ├── asgi.py
    │       │   │   ├── cache/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   └── utils.cpython-310.pyc
    │       │   │   │   ├── backends/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── db.cpython-310.pyc
    │       │   │   │   │   │   ├── dummy.cpython-310.pyc
    │       │   │   │   │   │   ├── filebased.cpython-310.pyc
    │       │   │   │   │   │   ├── locmem.cpython-310.pyc
    │       │   │   │   │   │   └── memcached.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── db.py
    │       │   │   │   │   ├── dummy.py
    │       │   │   │   │   ├── filebased.py
    │       │   │   │   │   ├── locmem.py
    │       │   │   │   │   └── memcached.py
    │       │   │   │   └── utils.py
    │       │   │   ├── checks/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── async_checks.cpython-310.pyc
    │       │   │   │   │   ├── caches.cpython-310.pyc
    │       │   │   │   │   ├── database.cpython-310.pyc
    │       │   │   │   │   ├── messages.cpython-310.pyc
    │       │   │   │   │   ├── model_checks.cpython-310.pyc
    │       │   │   │   │   ├── registry.cpython-310.pyc
    │       │   │   │   │   ├── templates.cpython-310.pyc
    │       │   │   │   │   ├── translation.cpython-310.pyc
    │       │   │   │   │   └── urls.cpython-310.pyc
    │       │   │   │   ├── async_checks.py
    │       │   │   │   ├── caches.py
    │       │   │   │   ├── compatibility/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── database.py
    │       │   │   │   ├── messages.py
    │       │   │   │   ├── model_checks.py
    │       │   │   │   ├── registry.py
    │       │   │   │   ├── security/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── csrf.cpython-310.pyc
    │       │   │   │   │   │   └── sessions.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── csrf.py
    │       │   │   │   │   └── sessions.py
    │       │   │   │   ├── templates.py
    │       │   │   │   ├── translation.py
    │       │   │   │   └── urls.py
    │       │   │   ├── exceptions.py
    │       │   │   ├── files/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   ├── images.cpython-310.pyc
    │       │   │   │   │   ├── locks.cpython-310.pyc
    │       │   │   │   │   ├── move.cpython-310.pyc
    │       │   │   │   │   ├── storage.cpython-310.pyc
    │       │   │   │   │   ├── temp.cpython-310.pyc
    │       │   │   │   │   ├── uploadedfile.cpython-310.pyc
    │       │   │   │   │   ├── uploadhandler.cpython-310.pyc
    │       │   │   │   │   └── utils.cpython-310.pyc
    │       │   │   │   ├── base.py
    │       │   │   │   ├── images.py
    │       │   │   │   ├── locks.py
    │       │   │   │   ├── move.py
    │       │   │   │   ├── storage.py
    │       │   │   │   ├── temp.py
    │       │   │   │   ├── uploadedfile.py
    │       │   │   │   ├── uploadhandler.py
    │       │   │   │   └── utils.py
    │       │   │   ├── handlers/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── asgi.cpython-310.pyc
    │       │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   ├── exception.cpython-310.pyc
    │       │   │   │   │   └── wsgi.cpython-310.pyc
    │       │   │   │   ├── asgi.py
    │       │   │   │   ├── base.py
    │       │   │   │   ├── exception.py
    │       │   │   │   └── wsgi.py
    │       │   │   ├── mail/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── message.cpython-310.pyc
    │       │   │   │   │   └── utils.cpython-310.pyc
    │       │   │   │   ├── backends/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── console.cpython-310.pyc
    │       │   │   │   │   │   ├── dummy.cpython-310.pyc
    │       │   │   │   │   │   ├── filebased.cpython-310.pyc
    │       │   │   │   │   │   ├── locmem.cpython-310.pyc
    │       │   │   │   │   │   └── smtp.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── console.py
    │       │   │   │   │   ├── dummy.py
    │       │   │   │   │   ├── filebased.py
    │       │   │   │   │   ├── locmem.py
    │       │   │   │   │   └── smtp.py
    │       │   │   │   ├── message.py
    │       │   │   │   └── utils.py
    │       │   │   ├── management/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   ├── color.cpython-310.pyc
    │       │   │   │   │   ├── sql.cpython-310.pyc
    │       │   │   │   │   ├── templates.cpython-310.pyc
    │       │   │   │   │   └── utils.cpython-310.pyc
    │       │   │   │   ├── base.py
    │       │   │   │   ├── color.py
    │       │   │   │   ├── commands/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── check.cpython-310.pyc
    │       │   │   │   │   │   ├── compilemessages.cpython-310.pyc
    │       │   │   │   │   │   ├── createcachetable.cpython-310.pyc
    │       │   │   │   │   │   ├── dbshell.cpython-310.pyc
    │       │   │   │   │   │   ├── diffsettings.cpython-310.pyc
    │       │   │   │   │   │   ├── dumpdata.cpython-310.pyc
    │       │   │   │   │   │   ├── flush.cpython-310.pyc
    │       │   │   │   │   │   ├── inspectdb.cpython-310.pyc
    │       │   │   │   │   │   ├── loaddata.cpython-310.pyc
    │       │   │   │   │   │   ├── makemessages.cpython-310.pyc
    │       │   │   │   │   │   ├── makemigrations.cpython-310.pyc
    │       │   │   │   │   │   ├── migrate.cpython-310.pyc
    │       │   │   │   │   │   ├── runserver.cpython-310.pyc
    │       │   │   │   │   │   ├── sendtestemail.cpython-310.pyc
    │       │   │   │   │   │   ├── shell.cpython-310.pyc
    │       │   │   │   │   │   ├── showmigrations.cpython-310.pyc
    │       │   │   │   │   │   ├── sqlflush.cpython-310.pyc
    │       │   │   │   │   │   ├── sqlmigrate.cpython-310.pyc
    │       │   │   │   │   │   ├── sqlsequencereset.cpython-310.pyc
    │       │   │   │   │   │   ├── squashmigrations.cpython-310.pyc
    │       │   │   │   │   │   ├── startapp.cpython-310.pyc
    │       │   │   │   │   │   ├── startproject.cpython-310.pyc
    │       │   │   │   │   │   ├── test.cpython-310.pyc
    │       │   │   │   │   │   └── testserver.cpython-310.pyc
    │       │   │   │   │   ├── check.py
    │       │   │   │   │   ├── compilemessages.py
    │       │   │   │   │   ├── createcachetable.py
    │       │   │   │   │   ├── dbshell.py
    │       │   │   │   │   ├── diffsettings.py
    │       │   │   │   │   ├── dumpdata.py
    │       │   │   │   │   ├── flush.py
    │       │   │   │   │   ├── inspectdb.py
    │       │   │   │   │   ├── loaddata.py
    │       │   │   │   │   ├── makemessages.py
    │       │   │   │   │   ├── makemigrations.py
    │       │   │   │   │   ├── migrate.py
    │       │   │   │   │   ├── runserver.py
    │       │   │   │   │   ├── sendtestemail.py
    │       │   │   │   │   ├── shell.py
    │       │   │   │   │   ├── showmigrations.py
    │       │   │   │   │   ├── sqlflush.py
    │       │   │   │   │   ├── sqlmigrate.py
    │       │   │   │   │   ├── sqlsequencereset.py
    │       │   │   │   │   ├── squashmigrations.py
    │       │   │   │   │   ├── startapp.py
    │       │   │   │   │   ├── startproject.py
    │       │   │   │   │   ├── test.py
    │       │   │   │   │   └── testserver.py
    │       │   │   │   ├── sql.py
    │       │   │   │   ├── templates.py
    │       │   │   │   └── utils.py
    │       │   │   ├── paginator.py
    │       │   │   ├── serializers/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   ├── json.cpython-310.pyc
    │       │   │   │   │   ├── jsonl.cpython-310.pyc
    │       │   │   │   │   ├── python.cpython-310.pyc
    │       │   │   │   │   ├── pyyaml.cpython-310.pyc
    │       │   │   │   │   └── xml_serializer.cpython-310.pyc
    │       │   │   │   ├── base.py
    │       │   │   │   ├── json.py
    │       │   │   │   ├── jsonl.py
    │       │   │   │   ├── python.py
    │       │   │   │   ├── pyyaml.py
    │       │   │   │   └── xml_serializer.py
    │       │   │   ├── servers/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   └── basehttp.cpython-310.pyc
    │       │   │   │   └── basehttp.py
    │       │   │   ├── signals.py
    │       │   │   ├── signing.py
    │       │   │   ├── validators.py
    │       │   │   └── wsgi.py
    │       │   ├── db/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── transaction.cpython-310.pyc
    │       │   │   │   └── utils.cpython-310.pyc
    │       │   │   ├── backends/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── ddl_references.cpython-310.pyc
    │       │   │   │   │   ├── signals.cpython-310.pyc
    │       │   │   │   │   └── utils.cpython-310.pyc
    │       │   │   │   ├── base/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── client.cpython-310.pyc
    │       │   │   │   │   │   ├── creation.cpython-310.pyc
    │       │   │   │   │   │   ├── features.cpython-310.pyc
    │       │   │   │   │   │   ├── introspection.cpython-310.pyc
    │       │   │   │   │   │   ├── operations.cpython-310.pyc
    │       │   │   │   │   │   ├── schema.cpython-310.pyc
    │       │   │   │   │   │   └── validation.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── client.py
    │       │   │   │   │   ├── creation.py
    │       │   │   │   │   ├── features.py
    │       │   │   │   │   ├── introspection.py
    │       │   │   │   │   ├── operations.py
    │       │   │   │   │   ├── schema.py
    │       │   │   │   │   └── validation.py
    │       │   │   │   ├── ddl_references.py
    │       │   │   │   ├── dummy/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   └── features.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   └── features.py
    │       │   │   │   ├── mysql/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── client.cpython-310.pyc
    │       │   │   │   │   │   ├── compiler.cpython-310.pyc
    │       │   │   │   │   │   ├── creation.cpython-310.pyc
    │       │   │   │   │   │   ├── features.cpython-310.pyc
    │       │   │   │   │   │   ├── introspection.cpython-310.pyc
    │       │   │   │   │   │   ├── operations.cpython-310.pyc
    │       │   │   │   │   │   ├── schema.cpython-310.pyc
    │       │   │   │   │   │   └── validation.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── client.py
    │       │   │   │   │   ├── compiler.py
    │       │   │   │   │   ├── creation.py
    │       │   │   │   │   ├── features.py
    │       │   │   │   │   ├── introspection.py
    │       │   │   │   │   ├── operations.py
    │       │   │   │   │   ├── schema.py
    │       │   │   │   │   └── validation.py
    │       │   │   │   ├── oracle/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── client.cpython-310.pyc
    │       │   │   │   │   │   ├── creation.cpython-310.pyc
    │       │   │   │   │   │   ├── features.cpython-310.pyc
    │       │   │   │   │   │   ├── functions.cpython-310.pyc
    │       │   │   │   │   │   ├── introspection.cpython-310.pyc
    │       │   │   │   │   │   ├── operations.cpython-310.pyc
    │       │   │   │   │   │   ├── schema.cpython-310.pyc
    │       │   │   │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   │   │   └── validation.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── client.py
    │       │   │   │   │   ├── creation.py
    │       │   │   │   │   ├── features.py
    │       │   │   │   │   ├── functions.py
    │       │   │   │   │   ├── introspection.py
    │       │   │   │   │   ├── operations.py
    │       │   │   │   │   ├── schema.py
    │       │   │   │   │   ├── utils.py
    │       │   │   │   │   └── validation.py
    │       │   │   │   ├── postgresql/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── client.cpython-310.pyc
    │       │   │   │   │   │   ├── creation.cpython-310.pyc
    │       │   │   │   │   │   ├── features.cpython-310.pyc
    │       │   │   │   │   │   ├── introspection.cpython-310.pyc
    │       │   │   │   │   │   ├── operations.cpython-310.pyc
    │       │   │   │   │   │   └── schema.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── client.py
    │       │   │   │   │   ├── creation.py
    │       │   │   │   │   ├── features.py
    │       │   │   │   │   ├── introspection.py
    │       │   │   │   │   ├── operations.py
    │       │   │   │   │   └── schema.py
    │       │   │   │   ├── signals.py
    │       │   │   │   ├── sqlite3/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── client.cpython-310.pyc
    │       │   │   │   │   │   ├── creation.cpython-310.pyc
    │       │   │   │   │   │   ├── features.cpython-310.pyc
    │       │   │   │   │   │   ├── introspection.cpython-310.pyc
    │       │   │   │   │   │   ├── operations.cpython-310.pyc
    │       │   │   │   │   │   └── schema.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── client.py
    │       │   │   │   │   ├── creation.py
    │       │   │   │   │   ├── features.py
    │       │   │   │   │   ├── introspection.py
    │       │   │   │   │   ├── operations.py
    │       │   │   │   │   └── schema.py
    │       │   │   │   └── utils.py
    │       │   │   ├── migrations/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── autodetector.cpython-310.pyc
    │       │   │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   │   ├── executor.cpython-310.pyc
    │       │   │   │   │   ├── graph.cpython-310.pyc
    │       │   │   │   │   ├── loader.cpython-310.pyc
    │       │   │   │   │   ├── migration.cpython-310.pyc
    │       │   │   │   │   ├── optimizer.cpython-310.pyc
    │       │   │   │   │   ├── questioner.cpython-310.pyc
    │       │   │   │   │   ├── recorder.cpython-310.pyc
    │       │   │   │   │   ├── serializer.cpython-310.pyc
    │       │   │   │   │   ├── state.cpython-310.pyc
    │       │   │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   │   └── writer.cpython-310.pyc
    │       │   │   │   ├── autodetector.py
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── executor.py
    │       │   │   │   ├── graph.py
    │       │   │   │   ├── loader.py
    │       │   │   │   ├── migration.py
    │       │   │   │   ├── operations/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   │   ├── fields.cpython-310.pyc
    │       │   │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   │   ├── special.cpython-310.pyc
    │       │   │   │   │   │   └── utils.cpython-310.pyc
    │       │   │   │   │   ├── base.py
    │       │   │   │   │   ├── fields.py
    │       │   │   │   │   ├── models.py
    │       │   │   │   │   ├── special.py
    │       │   │   │   │   └── utils.py
    │       │   │   │   ├── optimizer.py
    │       │   │   │   ├── questioner.py
    │       │   │   │   ├── recorder.py
    │       │   │   │   ├── serializer.py
    │       │   │   │   ├── state.py
    │       │   │   │   ├── utils.py
    │       │   │   │   └── writer.py
    │       │   │   ├── models/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── aggregates.cpython-310.pyc
    │       │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   ├── constants.cpython-310.pyc
    │       │   │   │   │   ├── constraints.cpython-310.pyc
    │       │   │   │   │   ├── deletion.cpython-310.pyc
    │       │   │   │   │   ├── enums.cpython-310.pyc
    │       │   │   │   │   ├── expressions.cpython-310.pyc
    │       │   │   │   │   ├── indexes.cpython-310.pyc
    │       │   │   │   │   ├── lookups.cpython-310.pyc
    │       │   │   │   │   ├── manager.cpython-310.pyc
    │       │   │   │   │   ├── options.cpython-310.pyc
    │       │   │   │   │   ├── query.cpython-310.pyc
    │       │   │   │   │   ├── query_utils.cpython-310.pyc
    │       │   │   │   │   ├── signals.cpython-310.pyc
    │       │   │   │   │   └── utils.cpython-310.pyc
    │       │   │   │   ├── aggregates.py
    │       │   │   │   ├── base.py
    │       │   │   │   ├── constants.py
    │       │   │   │   ├── constraints.py
    │       │   │   │   ├── deletion.py
    │       │   │   │   ├── enums.py
    │       │   │   │   ├── expressions.py
    │       │   │   │   ├── fields/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── files.cpython-310.pyc
    │       │   │   │   │   │   ├── json.cpython-310.pyc
    │       │   │   │   │   │   ├── mixins.cpython-310.pyc
    │       │   │   │   │   │   ├── proxy.cpython-310.pyc
    │       │   │   │   │   │   ├── related.cpython-310.pyc
    │       │   │   │   │   │   ├── related_descriptors.cpython-310.pyc
    │       │   │   │   │   │   ├── related_lookups.cpython-310.pyc
    │       │   │   │   │   │   └── reverse_related.cpython-310.pyc
    │       │   │   │   │   ├── files.py
    │       │   │   │   │   ├── json.py
    │       │   │   │   │   ├── mixins.py
    │       │   │   │   │   ├── proxy.py
    │       │   │   │   │   ├── related.py
    │       │   │   │   │   ├── related_descriptors.py
    │       │   │   │   │   ├── related_lookups.py
    │       │   │   │   │   └── reverse_related.py
    │       │   │   │   ├── functions/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── comparison.cpython-310.pyc
    │       │   │   │   │   │   ├── datetime.cpython-310.pyc
    │       │   │   │   │   │   ├── math.cpython-310.pyc
    │       │   │   │   │   │   ├── mixins.cpython-310.pyc
    │       │   │   │   │   │   ├── text.cpython-310.pyc
    │       │   │   │   │   │   └── window.cpython-310.pyc
    │       │   │   │   │   ├── comparison.py
    │       │   │   │   │   ├── datetime.py
    │       │   │   │   │   ├── math.py
    │       │   │   │   │   ├── mixins.py
    │       │   │   │   │   ├── text.py
    │       │   │   │   │   └── window.py
    │       │   │   │   ├── indexes.py
    │       │   │   │   ├── lookups.py
    │       │   │   │   ├── manager.py
    │       │   │   │   ├── options.py
    │       │   │   │   ├── query.py
    │       │   │   │   ├── query_utils.py
    │       │   │   │   ├── signals.py
    │       │   │   │   ├── sql/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── compiler.cpython-310.pyc
    │       │   │   │   │   │   ├── constants.cpython-310.pyc
    │       │   │   │   │   │   ├── datastructures.cpython-310.pyc
    │       │   │   │   │   │   ├── query.cpython-310.pyc
    │       │   │   │   │   │   ├── subqueries.cpython-310.pyc
    │       │   │   │   │   │   └── where.cpython-310.pyc
    │       │   │   │   │   ├── compiler.py
    │       │   │   │   │   ├── constants.py
    │       │   │   │   │   ├── datastructures.py
    │       │   │   │   │   ├── query.py
    │       │   │   │   │   ├── subqueries.py
    │       │   │   │   │   └── where.py
    │       │   │   │   └── utils.py
    │       │   │   ├── transaction.py
    │       │   │   └── utils.py
    │       │   ├── dispatch/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   └── dispatcher.cpython-310.pyc
    │       │   │   ├── dispatcher.py
    │       │   │   └── license.txt
    │       │   ├── forms/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── boundfield.cpython-310.pyc
    │       │   │   │   ├── fields.cpython-310.pyc
    │       │   │   │   ├── forms.cpython-310.pyc
    │       │   │   │   ├── formsets.cpython-310.pyc
    │       │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   ├── renderers.cpython-310.pyc
    │       │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   └── widgets.cpython-310.pyc
    │       │   │   ├── boundfield.py
    │       │   │   ├── fields.py
    │       │   │   ├── forms.py
    │       │   │   ├── formsets.py
    │       │   │   ├── jinja2/
    │       │   │   │   └── django/
    │       │   │   │       └── forms/
    │       │   │   │           └── widgets/
    │       │   │   │               ├── attrs.html
    │       │   │   │               ├── checkbox.html
    │       │   │   │               ├── checkbox_option.html
    │       │   │   │               ├── checkbox_select.html
    │       │   │   │               ├── clearable_file_input.html
    │       │   │   │               ├── date.html
    │       │   │   │               ├── datetime.html
    │       │   │   │               ├── email.html
    │       │   │   │               ├── file.html
    │       │   │   │               ├── hidden.html
    │       │   │   │               ├── input.html
    │       │   │   │               ├── input_option.html
    │       │   │   │               ├── multiple_hidden.html
    │       │   │   │               ├── multiple_input.html
    │       │   │   │               ├── multiwidget.html
    │       │   │   │               ├── number.html
    │       │   │   │               ├── password.html
    │       │   │   │               ├── radio.html
    │       │   │   │               ├── radio_option.html
    │       │   │   │               ├── select.html
    │       │   │   │               ├── select_date.html
    │       │   │   │               ├── select_option.html
    │       │   │   │               ├── splitdatetime.html
    │       │   │   │               ├── splithiddendatetime.html
    │       │   │   │               ├── text.html
    │       │   │   │               ├── textarea.html
    │       │   │   │               ├── time.html
    │       │   │   │               └── url.html
    │       │   │   ├── models.py
    │       │   │   ├── renderers.py
    │       │   │   ├── templates/
    │       │   │   │   └── django/
    │       │   │   │       └── forms/
    │       │   │   │           └── widgets/
    │       │   │   │               ├── attrs.html
    │       │   │   │               ├── checkbox.html
    │       │   │   │               ├── checkbox_option.html
    │       │   │   │               ├── checkbox_select.html
    │       │   │   │               ├── clearable_file_input.html
    │       │   │   │               ├── date.html
    │       │   │   │               ├── datetime.html
    │       │   │   │               ├── email.html
    │       │   │   │               ├── file.html
    │       │   │   │               ├── hidden.html
    │       │   │   │               ├── input.html
    │       │   │   │               ├── input_option.html
    │       │   │   │               ├── multiple_hidden.html
    │       │   │   │               ├── multiple_input.html
    │       │   │   │               ├── multiwidget.html
    │       │   │   │               ├── number.html
    │       │   │   │               ├── password.html
    │       │   │   │               ├── radio.html
    │       │   │   │               ├── radio_option.html
    │       │   │   │               ├── select.html
    │       │   │   │               ├── select_date.html
    │       │   │   │               ├── select_option.html
    │       │   │   │               ├── splitdatetime.html
    │       │   │   │               ├── splithiddendatetime.html
    │       │   │   │               ├── text.html
    │       │   │   │               ├── textarea.html
    │       │   │   │               ├── time.html
    │       │   │   │               └── url.html
    │       │   │   ├── utils.py
    │       │   │   └── widgets.py
    │       │   ├── http/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── cookie.cpython-310.pyc
    │       │   │   │   ├── multipartparser.cpython-310.pyc
    │       │   │   │   ├── request.cpython-310.pyc
    │       │   │   │   └── response.cpython-310.pyc
    │       │   │   ├── cookie.py
    │       │   │   ├── multipartparser.py
    │       │   │   ├── request.py
    │       │   │   └── response.py
    │       │   ├── middleware/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── cache.cpython-310.pyc
    │       │   │   │   ├── clickjacking.cpython-310.pyc
    │       │   │   │   ├── common.cpython-310.pyc
    │       │   │   │   ├── csrf.cpython-310.pyc
    │       │   │   │   ├── gzip.cpython-310.pyc
    │       │   │   │   ├── http.cpython-310.pyc
    │       │   │   │   ├── locale.cpython-310.pyc
    │       │   │   │   └── security.cpython-310.pyc
    │       │   │   ├── cache.py
    │       │   │   ├── clickjacking.py
    │       │   │   ├── common.py
    │       │   │   ├── csrf.py
    │       │   │   ├── gzip.py
    │       │   │   ├── http.py
    │       │   │   ├── locale.py
    │       │   │   └── security.py
    │       │   ├── shortcuts.py
    │       │   ├── template/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── autoreload.cpython-310.pyc
    │       │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   ├── context.cpython-310.pyc
    │       │   │   │   ├── context_processors.cpython-310.pyc
    │       │   │   │   ├── defaultfilters.cpython-310.pyc
    │       │   │   │   ├── defaulttags.cpython-310.pyc
    │       │   │   │   ├── engine.cpython-310.pyc
    │       │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   ├── library.cpython-310.pyc
    │       │   │   │   ├── loader.cpython-310.pyc
    │       │   │   │   ├── loader_tags.cpython-310.pyc
    │       │   │   │   ├── response.cpython-310.pyc
    │       │   │   │   ├── smartif.cpython-310.pyc
    │       │   │   │   └── utils.cpython-310.pyc
    │       │   │   ├── autoreload.py
    │       │   │   ├── backends/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   ├── django.cpython-310.pyc
    │       │   │   │   │   ├── dummy.cpython-310.pyc
    │       │   │   │   │   ├── jinja2.cpython-310.pyc
    │       │   │   │   │   └── utils.cpython-310.pyc
    │       │   │   │   ├── base.py
    │       │   │   │   ├── django.py
    │       │   │   │   ├── dummy.py
    │       │   │   │   ├── jinja2.py
    │       │   │   │   └── utils.py
    │       │   │   ├── base.py
    │       │   │   ├── context.py
    │       │   │   ├── context_processors.py
    │       │   │   ├── defaultfilters.py
    │       │   │   ├── defaulttags.py
    │       │   │   ├── engine.py
    │       │   │   ├── exceptions.py
    │       │   │   ├── library.py
    │       │   │   ├── loader.py
    │       │   │   ├── loader_tags.py
    │       │   │   ├── loaders/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── app_directories.cpython-310.pyc
    │       │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   ├── cached.cpython-310.pyc
    │       │   │   │   │   ├── filesystem.cpython-310.pyc
    │       │   │   │   │   └── locmem.cpython-310.pyc
    │       │   │   │   ├── app_directories.py
    │       │   │   │   ├── base.py
    │       │   │   │   ├── cached.py
    │       │   │   │   ├── filesystem.py
    │       │   │   │   └── locmem.py
    │       │   │   ├── response.py
    │       │   │   ├── smartif.py
    │       │   │   └── utils.py
    │       │   ├── templatetags/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── cache.cpython-310.pyc
    │       │   │   │   ├── i18n.cpython-310.pyc
    │       │   │   │   ├── l10n.cpython-310.pyc
    │       │   │   │   ├── static.cpython-310.pyc
    │       │   │   │   └── tz.cpython-310.pyc
    │       │   │   ├── cache.py
    │       │   │   ├── i18n.py
    │       │   │   ├── l10n.py
    │       │   │   ├── static.py
    │       │   │   └── tz.py
    │       │   ├── test/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── client.cpython-310.pyc
    │       │   │   │   ├── html.cpython-310.pyc
    │       │   │   │   ├── runner.cpython-310.pyc
    │       │   │   │   ├── selenium.cpython-310.pyc
    │       │   │   │   ├── signals.cpython-310.pyc
    │       │   │   │   ├── testcases.cpython-310.pyc
    │       │   │   │   └── utils.cpython-310.pyc
    │       │   │   ├── client.py
    │       │   │   ├── html.py
    │       │   │   ├── runner.py
    │       │   │   ├── selenium.py
    │       │   │   ├── signals.py
    │       │   │   ├── testcases.py
    │       │   │   └── utils.py
    │       │   ├── urls/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   ├── conf.cpython-310.pyc
    │       │   │   │   ├── converters.cpython-310.pyc
    │       │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   ├── resolvers.cpython-310.pyc
    │       │   │   │   └── utils.cpython-310.pyc
    │       │   │   ├── base.py
    │       │   │   ├── conf.py
    │       │   │   ├── converters.py
    │       │   │   ├── exceptions.py
    │       │   │   ├── resolvers.py
    │       │   │   └── utils.py
    │       │   ├── utils/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── _os.cpython-310.pyc
    │       │   │   │   ├── archive.cpython-310.pyc
    │       │   │   │   ├── asyncio.cpython-310.pyc
    │       │   │   │   ├── autoreload.cpython-310.pyc
    │       │   │   │   ├── baseconv.cpython-310.pyc
    │       │   │   │   ├── cache.cpython-310.pyc
    │       │   │   │   ├── connection.cpython-310.pyc
    │       │   │   │   ├── crypto.cpython-310.pyc
    │       │   │   │   ├── datastructures.cpython-310.pyc
    │       │   │   │   ├── dateformat.cpython-310.pyc
    │       │   │   │   ├── dateparse.cpython-310.pyc
    │       │   │   │   ├── dates.cpython-310.pyc
    │       │   │   │   ├── datetime_safe.cpython-310.pyc
    │       │   │   │   ├── deconstruct.cpython-310.pyc
    │       │   │   │   ├── decorators.cpython-310.pyc
    │       │   │   │   ├── deprecation.cpython-310.pyc
    │       │   │   │   ├── duration.cpython-310.pyc
    │       │   │   │   ├── encoding.cpython-310.pyc
    │       │   │   │   ├── feedgenerator.cpython-310.pyc
    │       │   │   │   ├── formats.cpython-310.pyc
    │       │   │   │   ├── functional.cpython-310.pyc
    │       │   │   │   ├── hashable.cpython-310.pyc
    │       │   │   │   ├── html.cpython-310.pyc
    │       │   │   │   ├── http.cpython-310.pyc
    │       │   │   │   ├── inspect.cpython-310.pyc
    │       │   │   │   ├── ipv6.cpython-310.pyc
    │       │   │   │   ├── itercompat.cpython-310.pyc
    │       │   │   │   ├── jslex.cpython-310.pyc
    │       │   │   │   ├── log.cpython-310.pyc
    │       │   │   │   ├── lorem_ipsum.cpython-310.pyc
    │       │   │   │   ├── module_loading.cpython-310.pyc
    │       │   │   │   ├── numberformat.cpython-310.pyc
    │       │   │   │   ├── regex_helper.cpython-310.pyc
    │       │   │   │   ├── safestring.cpython-310.pyc
    │       │   │   │   ├── termcolors.cpython-310.pyc
    │       │   │   │   ├── text.cpython-310.pyc
    │       │   │   │   ├── timesince.cpython-310.pyc
    │       │   │   │   ├── timezone.cpython-310.pyc
    │       │   │   │   ├── topological_sort.cpython-310.pyc
    │       │   │   │   ├── tree.cpython-310.pyc
    │       │   │   │   ├── version.cpython-310.pyc
    │       │   │   │   └── xmlutils.cpython-310.pyc
    │       │   │   ├── _os.py
    │       │   │   ├── archive.py
    │       │   │   ├── asyncio.py
    │       │   │   ├── autoreload.py
    │       │   │   ├── baseconv.py
    │       │   │   ├── cache.py
    │       │   │   ├── connection.py
    │       │   │   ├── crypto.py
    │       │   │   ├── datastructures.py
    │       │   │   ├── dateformat.py
    │       │   │   ├── dateparse.py
    │       │   │   ├── dates.py
    │       │   │   ├── datetime_safe.py
    │       │   │   ├── deconstruct.py
    │       │   │   ├── decorators.py
    │       │   │   ├── deprecation.py
    │       │   │   ├── duration.py
    │       │   │   ├── encoding.py
    │       │   │   ├── feedgenerator.py
    │       │   │   ├── formats.py
    │       │   │   ├── functional.py
    │       │   │   ├── hashable.py
    │       │   │   ├── html.py
    │       │   │   ├── http.py
    │       │   │   ├── inspect.py
    │       │   │   ├── ipv6.py
    │       │   │   ├── itercompat.py
    │       │   │   ├── jslex.py
    │       │   │   ├── log.py
    │       │   │   ├── lorem_ipsum.py
    │       │   │   ├── module_loading.py
    │       │   │   ├── numberformat.py
    │       │   │   ├── regex_helper.py
    │       │   │   ├── safestring.py
    │       │   │   ├── termcolors.py
    │       │   │   ├── text.py
    │       │   │   ├── timesince.py
    │       │   │   ├── timezone.py
    │       │   │   ├── topological_sort.py
    │       │   │   ├── translation/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── reloader.cpython-310.pyc
    │       │   │   │   │   ├── template.cpython-310.pyc
    │       │   │   │   │   ├── trans_null.cpython-310.pyc
    │       │   │   │   │   └── trans_real.cpython-310.pyc
    │       │   │   │   ├── reloader.py
    │       │   │   │   ├── template.py
    │       │   │   │   ├── trans_null.py
    │       │   │   │   └── trans_real.py
    │       │   │   ├── tree.py
    │       │   │   ├── version.py
    │       │   │   └── xmlutils.py
    │       │   └── views/
    │       │       ├── __init__.py
    │       │       ├── __pycache__/
    │       │       │   ├── __init__.cpython-310.pyc
    │       │       │   ├── csrf.cpython-310.pyc
    │       │       │   ├── debug.cpython-310.pyc
    │       │       │   ├── defaults.cpython-310.pyc
    │       │       │   ├── i18n.cpython-310.pyc
    │       │       │   └── static.cpython-310.pyc
    │       │       ├── csrf.py
    │       │       ├── debug.py
    │       │       ├── decorators/
    │       │       │   ├── __init__.py
    │       │       │   ├── __pycache__/
    │       │       │   │   ├── __init__.cpython-310.pyc
    │       │       │   │   ├── cache.cpython-310.pyc
    │       │       │   │   ├── clickjacking.cpython-310.pyc
    │       │       │   │   ├── common.cpython-310.pyc
    │       │       │   │   ├── csrf.cpython-310.pyc
    │       │       │   │   ├── debug.cpython-310.pyc
    │       │       │   │   ├── gzip.cpython-310.pyc
    │       │       │   │   ├── http.cpython-310.pyc
    │       │       │   │   └── vary.cpython-310.pyc
    │       │       │   ├── cache.py
    │       │       │   ├── clickjacking.py
    │       │       │   ├── common.py
    │       │       │   ├── csrf.py
    │       │       │   ├── debug.py
    │       │       │   ├── gzip.py
    │       │       │   ├── http.py
    │       │       │   └── vary.py
    │       │       ├── defaults.py
    │       │       ├── generic/
    │       │       │   ├── __init__.py
    │       │       │   ├── __pycache__/
    │       │       │   │   ├── __init__.cpython-310.pyc
    │       │       │   │   ├── base.cpython-310.pyc
    │       │       │   │   ├── dates.cpython-310.pyc
    │       │       │   │   ├── detail.cpython-310.pyc
    │       │       │   │   ├── edit.cpython-310.pyc
    │       │       │   │   └── list.cpython-310.pyc
    │       │       │   ├── base.py
    │       │       │   ├── dates.py
    │       │       │   ├── detail.py
    │       │       │   ├── edit.py
    │       │       │   └── list.py
    │       │       ├── i18n.py
    │       │       ├── static.py
    │       │       └── templates/
    │       │           ├── default_urlconf.html
    │       │           ├── technical_404.html
    │       │           ├── technical_500.html
    │       │           └── technical_500.txt
    │       ├── django_bootstrap5-22.2.dist-info/
    │       │   ├── AUTHORS
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   └── top_level.txt
    │       ├── django_bootstrap5/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── __init__.cpython-39.pyc
    │       │   │   ├── components.cpython-310.pyc
    │       │   │   ├── core.cpython-310.pyc
    │       │   │   ├── css.cpython-310.pyc
    │       │   │   ├── forms.cpython-310.pyc
    │       │   │   ├── html.cpython-310.pyc
    │       │   │   ├── renderers.cpython-310.pyc
    │       │   │   ├── size.cpython-310.pyc
    │       │   │   ├── text.cpython-310.pyc
    │       │   │   ├── utils.cpython-310.pyc
    │       │   │   └── widgets.cpython-310.pyc
    │       │   ├── components.py
    │       │   ├── core.py
    │       │   ├── css.py
    │       │   ├── forms.py
    │       │   ├── html.py
    │       │   ├── renderers.py
    │       │   ├── size.py
    │       │   ├── templates/
    │       │   │   └── django_bootstrap5/
    │       │   │       ├── bootstrap5.html
    │       │   │       ├── field_errors.html
    │       │   │       ├── field_help_text.html
    │       │   │       ├── form_errors.html
    │       │   │       ├── messages.html
    │       │   │       ├── pagination.html
    │       │   │       └── widgets/
    │       │   │           ├── clearable_file_input.html
    │       │   │           ├── radio_select.html
    │       │   │           └── radio_select_button_group.html
    │       │   ├── templatetags/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   └── django_bootstrap5.cpython-310.pyc
    │       │   │   └── django_bootstrap5.py
    │       │   ├── text.py
    │       │   ├── utils.py
    │       │   └── widgets.py
    │       ├── faker/
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── __main__.cpython-310.pyc
    │       │   │   ├── cli.cpython-310.pyc
    │       │   │   ├── config.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── config.cpython-310.pyc
    │       │   │   ├── documentor.cpython-310.pyc
    │       │   │   ├── exceptions.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── exceptions.cpython-310.pyc
    │       │   │   ├── factory.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── factory.cpython-310.pyc
    │       │   │   ├── generator.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── generator.cpython-310.pyc
    │       │   │   ├── proxy.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── proxy.cpython-310.pyc
    │       │   │   ├── typing.cpython-310-pytest-7.1.3.pyc
    │       │   │   └── typing.cpython-310.pyc
    │       │   ├── cli.py
    │       │   ├── config.py
    │       │   ├── contrib/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   └── __init__.cpython-310.pyc
    │       │   │   └── pytest/
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__/
    │       │   │       │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │       │   ├── __init__.cpython-310.pyc
    │       │   │       │   ├── plugin.cpython-310-pytest-7.1.3.pyc
    │       │   │       │   └── plugin.cpython-310.pyc
    │       │   │       └── plugin.py
    │       │   ├── decode/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── codes.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   └── codes.cpython-310.pyc
    │       │   │   └── codes.py
    │       │   ├── documentor.py
    │       │   ├── exceptions.py
    │       │   ├── factory.py
    │       │   ├── generator.py
    │       │   ├── providers/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   └── __init__.cpython-310.pyc
    │       │   │   ├── address/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── cs_CZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── da_DK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_AT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_DE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_AU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_CA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_GB/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_IE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_NZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_CO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_ES/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_MX/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fa_IR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fi_FI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fil_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── he_IL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hi_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hr_HR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hu_HU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hy_AM/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── id_ID/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── it_IT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ja_JP/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ka_GE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ko_KR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ne_NP/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_BE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_NL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── no_NO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ro_RO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sk_SK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sl_SI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sv_SE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ta_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tl_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── uk_UA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── zh_CN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── zh_TW/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── automotive/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_JO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_PS/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_SA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_DE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_CA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_GB/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_NZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_CO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_ES/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fil_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── he_IL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hu_HU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── id_ID/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_NL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── no_NO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ro_RO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sk_SK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sv_SE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tl_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── tr_TR/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── bank/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_AT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_DE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_GB/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_IE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_ES/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fa_IR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fi_FI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fil_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── it_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── it_IT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_NL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── no_NO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ro_RO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tl_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── tr_TR/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── barcode/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_CA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_ES/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_CA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── ja_JP/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── color/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── color.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── color.cpython-310.pyc
    │       │   │   │   ├── ar_PS/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── bg_BG/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── color.py
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_ES/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fa_IR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── he_IL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hr_HR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hu_HU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hy_AM/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sk_SK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── uk_UA/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── company/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── bg_BG/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── cs_CZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_DE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_MX/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fa_IR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fi_FI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fil_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hr_HR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hu_HU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hy_AM/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── id_ID/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── it_IT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ja_JP/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ko_KR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_NL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── no_NO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ro_RO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sk_SK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sl_SI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sv_SE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tl_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tr_TR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── zh_CN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── zh_TW/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── credit_card/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fa_IR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── ru_RU/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── currency/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── cs_CZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_AT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_DE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_AU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_CA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_ES/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_CA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── it_IT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_NL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ro_RO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sk_SK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sv_SE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── th_TH/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── date_time/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_AA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_EG/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── bn_BD/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── cs_CZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_AT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_DE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_ES/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fil_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hi_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hr_HR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hu_HU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hy_AM/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── id_ID/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── it_IT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ko_KR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_NL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ro_RO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sk_SK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sl_SI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ta_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tl_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── tr_TR/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── file/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   └── en_US/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── geo/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_AT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_IE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── tr_TR/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── internet/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_AA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── bg_BG/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── bs_BA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── cs_CZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_AT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_DE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_AU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_GB/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_NZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_ES/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fa_IR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fi_FI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fil_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hr_HR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hu_HU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── id_ID/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── it_IT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ja_JP/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ko_KR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── no_NO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ro_RO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sk_SK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sl_SI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sv_SE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tl_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── uk_UA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── zh_CN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── zh_TW/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── isbn/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── isbn.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   ├── isbn.cpython-310.pyc
    │       │   │   │   │   ├── rules.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── rules.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── isbn.py
    │       │   │   │   └── rules.py
    │       │   │   ├── job/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_AA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── bs_BA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_DE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fa_IR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fi_FI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hr_HR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hu_HU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hy_AM/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ja_JP/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ko_KR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ro_RO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sk_SK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tr_TR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── uk_UA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── zh_CN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── zh_TW/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── lorem/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_AA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── cs_CZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fil_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── he_IL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hy_AM/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ja_JP/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── la/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tl_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── zh_CN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── zh_TW/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── misc/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fil_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── tl_PH/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── person/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_AA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_PS/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_SA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── bg_BG/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── cs_CZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_AT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_DE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── dk_DK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_GB/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_IE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_NZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_CA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_CO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_ES/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_MX/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── et_EE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fa_IR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fi_FI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_CA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_QC/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ga_IE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── he_IL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hi_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hr_HR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hu_HU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hy_AM/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── id_ID/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── it_IT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ja_JP/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ka_GE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ko_KR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── lt_LT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── lv_LV/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ne_NP/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_NL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── no_NO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── or_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ro_RO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sl_SI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sv_SE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ta_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tr_TR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tw_GH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── uk_UA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── zh_CN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── zh_TW/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── phone_number/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_AE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_JO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ar_PS/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── bg_BG/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── bs_BA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── cs_CZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_DE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── dk_DK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_AU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_CA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_GB/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_NZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_CO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_ES/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_MX/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fa_IR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fi_FI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fil_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── he_IL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hi_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hr_HR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hu_HU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hy_AM/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── id_ID/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── it_IT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ja_JP/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ko_KR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── lt_LT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── lv_LV/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ne_NP/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_BE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_NL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── no_NO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ro_RO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sk_SK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sl_SI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sv_SE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ta_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tl_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tr_TR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tw_GH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── uk_UA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── zh_CN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── zh_TW/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── profile/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   └── en_US/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── python/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   └── en_US/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── ssn/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │   └── __init__.cpython-310.pyc
    │       │   │   │   ├── az_AZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── bg_BG/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── cs_CZ/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_AT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── de_DE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── dk_DK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_CY/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── el_GR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_CA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_GB/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_IE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_IN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── en_US/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_CA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_CO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_ES/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── es_MX/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── et_EE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fi_FI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fil_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_CH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── fr_FR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── he_IL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hr_HR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── hu_HU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── it_IT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ko_KR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── lb_LU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── lt_LT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── lv_LV/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── mt_MT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_BE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── nl_NL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── no_NO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pl_PL/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_BR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── pt_PT/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ro_RO/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── ru_RU/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sk_SK/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sl_SI/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── sv_SE/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── th_TH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tl_PH/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── tr_TR/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── uk_UA/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── zh_CN/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   └── zh_TW/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   └── user_agent/
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__/
    │       │   │       │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │       │   └── __init__.cpython-310.pyc
    │       │   │       └── en_US/
    │       │   │           ├── __init__.py
    │       │   │           └── __pycache__/
    │       │   │               └── __init__.cpython-310.pyc
    │       │   ├── proxy.py
    │       │   ├── py.typed
    │       │   ├── sphinx/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── autodoc.cpython-310.pyc
    │       │   │   │   ├── docstring.cpython-310.pyc
    │       │   │   │   ├── documentor.cpython-310.pyc
    │       │   │   │   └── validator.cpython-310.pyc
    │       │   │   ├── autodoc.py
    │       │   │   ├── docstring.py
    │       │   │   ├── documentor.py
    │       │   │   └── validator.py
    │       │   ├── typing.py
    │       │   └── utils/
    │       │       ├── __init__.py
    │       │       ├── __pycache__/
    │       │       │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │       │   ├── __init__.cpython-310.pyc
    │       │       │   ├── checksums.cpython-310.pyc
    │       │       │   ├── datasets.cpython-310.pyc
    │       │       │   ├── decorators.cpython-310-pytest-7.1.3.pyc
    │       │       │   ├── decorators.cpython-310.pyc
    │       │       │   ├── distribution.cpython-310-pytest-7.1.3.pyc
    │       │       │   ├── distribution.cpython-310.pyc
    │       │       │   ├── loading.cpython-310-pytest-7.1.3.pyc
    │       │       │   ├── loading.cpython-310.pyc
    │       │       │   ├── text.cpython-310-pytest-7.1.3.pyc
    │       │       │   └── text.cpython-310.pyc
    │       │       ├── checksums.py
    │       │       ├── datasets.py
    │       │       ├── decorators.py
    │       │       ├── distribution.py
    │       │       ├── loading.py
    │       │       └── text.py
    │       ├── flake8-5.0.4.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── flake8/
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── __main__.cpython-310.pyc
    │       │   │   ├── _compat.cpython-310.pyc
    │       │   │   ├── checker.cpython-310.pyc
    │       │   │   ├── defaults.cpython-310.pyc
    │       │   │   ├── discover_files.cpython-310.pyc
    │       │   │   ├── exceptions.cpython-310.pyc
    │       │   │   ├── processor.cpython-310.pyc
    │       │   │   ├── statistics.cpython-310.pyc
    │       │   │   ├── style_guide.cpython-310.pyc
    │       │   │   ├── utils.cpython-310.pyc
    │       │   │   └── violation.cpython-310.pyc
    │       │   ├── _compat.py
    │       │   ├── api/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   └── legacy.cpython-310.pyc
    │       │   │   └── legacy.py
    │       │   ├── checker.py
    │       │   ├── defaults.py
    │       │   ├── discover_files.py
    │       │   ├── exceptions.py
    │       │   ├── formatting/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── _windows_color.cpython-310.pyc
    │       │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   └── default.cpython-310.pyc
    │       │   │   ├── _windows_color.py
    │       │   │   ├── base.py
    │       │   │   └── default.py
    │       │   ├── main/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── application.cpython-310.pyc
    │       │   │   │   ├── cli.cpython-310.pyc
    │       │   │   │   ├── debug.cpython-310.pyc
    │       │   │   │   └── options.cpython-310.pyc
    │       │   │   ├── application.py
    │       │   │   ├── cli.py
    │       │   │   ├── debug.py
    │       │   │   └── options.py
    │       │   ├── options/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── aggregator.cpython-310.pyc
    │       │   │   │   ├── config.cpython-310.pyc
    │       │   │   │   └── manager.cpython-310.pyc
    │       │   │   ├── aggregator.py
    │       │   │   ├── config.py
    │       │   │   └── manager.py
    │       │   ├── plugins/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── finder.cpython-310.pyc
    │       │   │   │   ├── pycodestyle.cpython-310.pyc
    │       │   │   │   ├── pyflakes.cpython-310.pyc
    │       │   │   │   └── reporter.cpython-310.pyc
    │       │   │   ├── finder.py
    │       │   │   ├── pycodestyle.py
    │       │   │   ├── pyflakes.py
    │       │   │   └── reporter.py
    │       │   ├── processor.py
    │       │   ├── statistics.py
    │       │   ├── style_guide.py
    │       │   ├── utils.py
    │       │   └── violation.py
    │       ├── flake8_docstrings-1.7.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── flake8_docstrings.py
    │       ├── iniconfig-2.0.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   └── licenses/
    │       │       └── LICENSE
    │       ├── iniconfig/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── _parse.cpython-310.pyc
    │       │   │   ├── _version.cpython-310.pyc
    │       │   │   └── exceptions.cpython-310.pyc
    │       │   ├── _parse.py
    │       │   ├── _version.py
    │       │   ├── exceptions.py
    │       │   └── py.typed
    │       ├── mccabe-0.7.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── mccabe.py
    │       ├── mixer-7.2.2.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   └── top_level.txt
    │       ├── mixer/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── _compat.cpython-310.pyc
    │       │   │   ├── _faker.cpython-310.pyc
    │       │   │   ├── auto.cpython-310.pyc
    │       │   │   ├── factory.cpython-310.pyc
    │       │   │   ├── main.cpython-310.pyc
    │       │   │   ├── markov.cpython-310.pyc
    │       │   │   └── mix_types.cpython-310.pyc
    │       │   ├── _compat.py
    │       │   ├── _faker.py
    │       │   ├── auto.py
    │       │   ├── backend/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── django.cpython-310.pyc
    │       │   │   │   ├── flask.cpython-310.pyc
    │       │   │   │   ├── marshmallow.cpython-310.pyc
    │       │   │   │   ├── mongoengine.cpython-310.pyc
    │       │   │   │   ├── peewee.cpython-310.pyc
    │       │   │   │   ├── pony.cpython-310.pyc
    │       │   │   │   └── sqlalchemy.cpython-310.pyc
    │       │   │   ├── django.py
    │       │   │   ├── flask.py
    │       │   │   ├── marshmallow.py
    │       │   │   ├── mongoengine.py
    │       │   │   ├── peewee.py
    │       │   │   ├── pony.py
    │       │   │   └── sqlalchemy.py
    │       │   ├── factory.py
    │       │   ├── main.py
    │       │   ├── markov.py
    │       │   ├── mix_types.py
    │       │   └── resources/
    │       │       ├── file.txt
    │       │       └── image.gif
    │       ├── packaging-23.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── LICENSE.APACHE
    │       │   ├── LICENSE.BSD
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   └── WHEEL
    │       ├── packaging/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── _elffile.cpython-310.pyc
    │       │   │   ├── _manylinux.cpython-310.pyc
    │       │   │   ├── _musllinux.cpython-310.pyc
    │       │   │   ├── _parser.cpython-310.pyc
    │       │   │   ├── _structures.cpython-310.pyc
    │       │   │   ├── _tokenizer.cpython-310.pyc
    │       │   │   ├── markers.cpython-310.pyc
    │       │   │   ├── requirements.cpython-310.pyc
    │       │   │   ├── specifiers.cpython-310.pyc
    │       │   │   ├── tags.cpython-310.pyc
    │       │   │   ├── utils.cpython-310.pyc
    │       │   │   └── version.cpython-310.pyc
    │       │   ├── _elffile.py
    │       │   ├── _manylinux.py
    │       │   ├── _musllinux.py
    │       │   ├── _parser.py
    │       │   ├── _structures.py
    │       │   ├── _tokenizer.py
    │       │   ├── markers.py
    │       │   ├── py.typed
    │       │   ├── requirements.py
    │       │   ├── specifiers.py
    │       │   ├── tags.py
    │       │   ├── utils.py
    │       │   └── version.py
    │       ├── pep8_naming-0.13.3.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── pep8ext_naming.py
    │       ├── pip-26.1.1.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── licenses/
    │       │       ├── AUTHORS.txt
    │       │       ├── LICENSE.txt
    │       │       └── src/
    │       │           └── pip/
    │       │               └── _vendor/
    │       │                   ├── cachecontrol/
    │       │                   │   └── LICENSE.txt
    │       │                   ├── certifi/
    │       │                   │   └── LICENSE
    │       │                   ├── distlib/
    │       │                   │   └── LICENSE.txt
    │       │                   ├── distro/
    │       │                   │   └── LICENSE
    │       │                   ├── idna/
    │       │                   │   └── LICENSE.md
    │       │                   ├── msgpack/
    │       │                   │   └── COPYING
    │       │                   ├── packaging/
    │       │                   │   ├── LICENSE
    │       │                   │   ├── LICENSE.APACHE
    │       │                   │   └── LICENSE.BSD
    │       │                   ├── pkg_resources/
    │       │                   │   └── LICENSE
    │       │                   ├── platformdirs/
    │       │                   │   └── LICENSE
    │       │                   ├── pygments/
    │       │                   │   └── LICENSE
    │       │                   ├── pyproject_hooks/
    │       │                   │   └── LICENSE
    │       │                   ├── requests/
    │       │                   │   └── LICENSE
    │       │                   ├── resolvelib/
    │       │                   │   └── LICENSE
    │       │                   ├── rich/
    │       │                   │   └── LICENSE
    │       │                   ├── tomli/
    │       │                   │   └── LICENSE
    │       │                   ├── tomli_w/
    │       │                   │   └── LICENSE
    │       │                   ├── truststore/
    │       │                   │   └── LICENSE
    │       │                   └── urllib3/
    │       │                       └── LICENSE.txt
    │       ├── pip/
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pip-runner__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── __main__.cpython-310.pyc
    │       │   │   └── __pip-runner__.cpython-310.pyc
    │       │   ├── _internal/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── build_env.cpython-310.pyc
    │       │   │   │   ├── cache.cpython-310.pyc
    │       │   │   │   ├── configuration.cpython-310.pyc
    │       │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   ├── main.cpython-310.pyc
    │       │   │   │   ├── pyproject.cpython-310.pyc
    │       │   │   │   ├── self_outdated_check.cpython-310.pyc
    │       │   │   │   └── wheel_builder.cpython-310.pyc
    │       │   │   ├── build_env.py
    │       │   │   ├── cache.py
    │       │   │   ├── cli/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── autocompletion.cpython-310.pyc
    │       │   │   │   │   ├── base_command.cpython-310.pyc
    │       │   │   │   │   ├── cmdoptions.cpython-310.pyc
    │       │   │   │   │   ├── command_context.cpython-310.pyc
    │       │   │   │   │   ├── index_command.cpython-310.pyc
    │       │   │   │   │   ├── main.cpython-310.pyc
    │       │   │   │   │   ├── main_parser.cpython-310.pyc
    │       │   │   │   │   ├── parser.cpython-310.pyc
    │       │   │   │   │   ├── progress_bars.cpython-310.pyc
    │       │   │   │   │   ├── req_command.cpython-310.pyc
    │       │   │   │   │   ├── spinners.cpython-310.pyc
    │       │   │   │   │   └── status_codes.cpython-310.pyc
    │       │   │   │   ├── autocompletion.py
    │       │   │   │   ├── base_command.py
    │       │   │   │   ├── cmdoptions.py
    │       │   │   │   ├── command_context.py
    │       │   │   │   ├── index_command.py
    │       │   │   │   ├── main.py
    │       │   │   │   ├── main_parser.py
    │       │   │   │   ├── parser.py
    │       │   │   │   ├── progress_bars.py
    │       │   │   │   ├── req_command.py
    │       │   │   │   ├── spinners.py
    │       │   │   │   └── status_codes.py
    │       │   │   ├── commands/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── cache.cpython-310.pyc
    │       │   │   │   │   ├── check.cpython-310.pyc
    │       │   │   │   │   ├── completion.cpython-310.pyc
    │       │   │   │   │   ├── configuration.cpython-310.pyc
    │       │   │   │   │   ├── debug.cpython-310.pyc
    │       │   │   │   │   ├── download.cpython-310.pyc
    │       │   │   │   │   ├── freeze.cpython-310.pyc
    │       │   │   │   │   ├── hash.cpython-310.pyc
    │       │   │   │   │   ├── help.cpython-310.pyc
    │       │   │   │   │   ├── index.cpython-310.pyc
    │       │   │   │   │   ├── inspect.cpython-310.pyc
    │       │   │   │   │   ├── install.cpython-310.pyc
    │       │   │   │   │   ├── list.cpython-310.pyc
    │       │   │   │   │   ├── lock.cpython-310.pyc
    │       │   │   │   │   ├── search.cpython-310.pyc
    │       │   │   │   │   ├── show.cpython-310.pyc
    │       │   │   │   │   ├── uninstall.cpython-310.pyc
    │       │   │   │   │   └── wheel.cpython-310.pyc
    │       │   │   │   ├── cache.py
    │       │   │   │   ├── check.py
    │       │   │   │   ├── completion.py
    │       │   │   │   ├── configuration.py
    │       │   │   │   ├── debug.py
    │       │   │   │   ├── download.py
    │       │   │   │   ├── freeze.py
    │       │   │   │   ├── hash.py
    │       │   │   │   ├── help.py
    │       │   │   │   ├── index.py
    │       │   │   │   ├── inspect.py
    │       │   │   │   ├── install.py
    │       │   │   │   ├── list.py
    │       │   │   │   ├── lock.py
    │       │   │   │   ├── search.py
    │       │   │   │   ├── show.py
    │       │   │   │   ├── uninstall.py
    │       │   │   │   └── wheel.py
    │       │   │   ├── configuration.py
    │       │   │   ├── distributions/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   ├── installed.cpython-310.pyc
    │       │   │   │   │   ├── sdist.cpython-310.pyc
    │       │   │   │   │   └── wheel.cpython-310.pyc
    │       │   │   │   ├── base.py
    │       │   │   │   ├── installed.py
    │       │   │   │   ├── sdist.py
    │       │   │   │   └── wheel.py
    │       │   │   ├── exceptions.py
    │       │   │   ├── index/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── collector.cpython-310.pyc
    │       │   │   │   │   ├── package_finder.cpython-310.pyc
    │       │   │   │   │   └── sources.cpython-310.pyc
    │       │   │   │   ├── collector.py
    │       │   │   │   ├── package_finder.py
    │       │   │   │   └── sources.py
    │       │   │   ├── locations/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _distutils.cpython-310.pyc
    │       │   │   │   │   ├── _sysconfig.cpython-310.pyc
    │       │   │   │   │   └── base.cpython-310.pyc
    │       │   │   │   ├── _distutils.py
    │       │   │   │   ├── _sysconfig.py
    │       │   │   │   └── base.py
    │       │   │   ├── main.py
    │       │   │   ├── metadata/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _json.cpython-310.pyc
    │       │   │   │   │   ├── base.cpython-310.pyc
    │       │   │   │   │   └── pkg_resources.cpython-310.pyc
    │       │   │   │   ├── _json.py
    │       │   │   │   ├── base.py
    │       │   │   │   ├── importlib/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── _compat.cpython-310.pyc
    │       │   │   │   │   │   ├── _dists.cpython-310.pyc
    │       │   │   │   │   │   └── _envs.cpython-310.pyc
    │       │   │   │   │   ├── _compat.py
    │       │   │   │   │   ├── _dists.py
    │       │   │   │   │   └── _envs.py
    │       │   │   │   └── pkg_resources.py
    │       │   │   ├── models/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── candidate.cpython-310.pyc
    │       │   │   │   │   ├── direct_url.cpython-310.pyc
    │       │   │   │   │   ├── format_control.cpython-310.pyc
    │       │   │   │   │   ├── index.cpython-310.pyc
    │       │   │   │   │   ├── installation_report.cpython-310.pyc
    │       │   │   │   │   ├── link.cpython-310.pyc
    │       │   │   │   │   ├── release_control.cpython-310.pyc
    │       │   │   │   │   ├── scheme.cpython-310.pyc
    │       │   │   │   │   ├── search_scope.cpython-310.pyc
    │       │   │   │   │   ├── selection_prefs.cpython-310.pyc
    │       │   │   │   │   ├── target_python.cpython-310.pyc
    │       │   │   │   │   └── wheel.cpython-310.pyc
    │       │   │   │   ├── candidate.py
    │       │   │   │   ├── direct_url.py
    │       │   │   │   ├── format_control.py
    │       │   │   │   ├── index.py
    │       │   │   │   ├── installation_report.py
    │       │   │   │   ├── link.py
    │       │   │   │   ├── release_control.py
    │       │   │   │   ├── scheme.py
    │       │   │   │   ├── search_scope.py
    │       │   │   │   ├── selection_prefs.py
    │       │   │   │   ├── target_python.py
    │       │   │   │   └── wheel.py
    │       │   │   ├── network/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── auth.cpython-310.pyc
    │       │   │   │   │   ├── cache.cpython-310.pyc
    │       │   │   │   │   ├── download.cpython-310.pyc
    │       │   │   │   │   ├── lazy_wheel.cpython-310.pyc
    │       │   │   │   │   ├── session.cpython-310.pyc
    │       │   │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   │   └── xmlrpc.cpython-310.pyc
    │       │   │   │   ├── auth.py
    │       │   │   │   ├── cache.py
    │       │   │   │   ├── download.py
    │       │   │   │   ├── lazy_wheel.py
    │       │   │   │   ├── session.py
    │       │   │   │   ├── utils.py
    │       │   │   │   └── xmlrpc.py
    │       │   │   ├── operations/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── check.cpython-310.pyc
    │       │   │   │   │   ├── freeze.cpython-310.pyc
    │       │   │   │   │   └── prepare.cpython-310.pyc
    │       │   │   │   ├── build/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── build_tracker.cpython-310.pyc
    │       │   │   │   │   │   ├── metadata.cpython-310.pyc
    │       │   │   │   │   │   ├── metadata_editable.cpython-310.pyc
    │       │   │   │   │   │   ├── wheel.cpython-310.pyc
    │       │   │   │   │   │   └── wheel_editable.cpython-310.pyc
    │       │   │   │   │   ├── build_tracker.py
    │       │   │   │   │   ├── metadata.py
    │       │   │   │   │   ├── metadata_editable.py
    │       │   │   │   │   ├── wheel.py
    │       │   │   │   │   └── wheel_editable.py
    │       │   │   │   ├── check.py
    │       │   │   │   ├── freeze.py
    │       │   │   │   ├── install/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── wheel.cpython-310.pyc
    │       │   │   │   │   └── wheel.py
    │       │   │   │   └── prepare.py
    │       │   │   ├── pyproject.py
    │       │   │   ├── req/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── constructors.cpython-310.pyc
    │       │   │   │   │   ├── pep723.cpython-310.pyc
    │       │   │   │   │   ├── req_dependency_group.cpython-310.pyc
    │       │   │   │   │   ├── req_file.cpython-310.pyc
    │       │   │   │   │   ├── req_install.cpython-310.pyc
    │       │   │   │   │   ├── req_set.cpython-310.pyc
    │       │   │   │   │   └── req_uninstall.cpython-310.pyc
    │       │   │   │   ├── constructors.py
    │       │   │   │   ├── pep723.py
    │       │   │   │   ├── req_dependency_group.py
    │       │   │   │   ├── req_file.py
    │       │   │   │   ├── req_install.py
    │       │   │   │   ├── req_set.py
    │       │   │   │   └── req_uninstall.py
    │       │   │   ├── resolution/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   └── base.cpython-310.pyc
    │       │   │   │   ├── base.py
    │       │   │   │   ├── legacy/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── resolver.cpython-310.pyc
    │       │   │   │   │   └── resolver.py
    │       │   │   │   └── resolvelib/
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__/
    │       │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │       │   ├── base.cpython-310.pyc
    │       │   │   │       │   ├── candidates.cpython-310.pyc
    │       │   │   │       │   ├── factory.cpython-310.pyc
    │       │   │   │       │   ├── found_candidates.cpython-310.pyc
    │       │   │   │       │   ├── provider.cpython-310.pyc
    │       │   │   │       │   ├── reporter.cpython-310.pyc
    │       │   │   │       │   ├── requirements.cpython-310.pyc
    │       │   │   │       │   └── resolver.cpython-310.pyc
    │       │   │   │       ├── base.py
    │       │   │   │       ├── candidates.py
    │       │   │   │       ├── factory.py
    │       │   │   │       ├── found_candidates.py
    │       │   │   │       ├── provider.py
    │       │   │   │       ├── reporter.py
    │       │   │   │       ├── requirements.py
    │       │   │   │       └── resolver.py
    │       │   │   ├── self_outdated_check.py
    │       │   │   ├── utils/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _jaraco_text.cpython-310.pyc
    │       │   │   │   │   ├── _log.cpython-310.pyc
    │       │   │   │   │   ├── appdirs.cpython-310.pyc
    │       │   │   │   │   ├── compat.cpython-310.pyc
    │       │   │   │   │   ├── compatibility_tags.cpython-310.pyc
    │       │   │   │   │   ├── datetime.cpython-310.pyc
    │       │   │   │   │   ├── deprecation.cpython-310.pyc
    │       │   │   │   │   ├── direct_url_helpers.cpython-310.pyc
    │       │   │   │   │   ├── egg_link.cpython-310.pyc
    │       │   │   │   │   ├── entrypoints.cpython-310.pyc
    │       │   │   │   │   ├── filesystem.cpython-310.pyc
    │       │   │   │   │   ├── filetypes.cpython-310.pyc
    │       │   │   │   │   ├── glibc.cpython-310.pyc
    │       │   │   │   │   ├── hashes.cpython-310.pyc
    │       │   │   │   │   ├── logging.cpython-310.pyc
    │       │   │   │   │   ├── misc.cpython-310.pyc
    │       │   │   │   │   ├── packaging.cpython-310.pyc
    │       │   │   │   │   ├── pylock.cpython-310.pyc
    │       │   │   │   │   ├── retry.cpython-310.pyc
    │       │   │   │   │   ├── subprocess.cpython-310.pyc
    │       │   │   │   │   ├── temp_dir.cpython-310.pyc
    │       │   │   │   │   ├── unpacking.cpython-310.pyc
    │       │   │   │   │   ├── urls.cpython-310.pyc
    │       │   │   │   │   ├── virtualenv.cpython-310.pyc
    │       │   │   │   │   └── wheel.cpython-310.pyc
    │       │   │   │   ├── _jaraco_text.py
    │       │   │   │   ├── _log.py
    │       │   │   │   ├── appdirs.py
    │       │   │   │   ├── compat.py
    │       │   │   │   ├── compatibility_tags.py
    │       │   │   │   ├── datetime.py
    │       │   │   │   ├── deprecation.py
    │       │   │   │   ├── direct_url_helpers.py
    │       │   │   │   ├── egg_link.py
    │       │   │   │   ├── entrypoints.py
    │       │   │   │   ├── filesystem.py
    │       │   │   │   ├── filetypes.py
    │       │   │   │   ├── glibc.py
    │       │   │   │   ├── hashes.py
    │       │   │   │   ├── logging.py
    │       │   │   │   ├── misc.py
    │       │   │   │   ├── packaging.py
    │       │   │   │   ├── pylock.py
    │       │   │   │   ├── retry.py
    │       │   │   │   ├── subprocess.py
    │       │   │   │   ├── temp_dir.py
    │       │   │   │   ├── unpacking.py
    │       │   │   │   ├── urls.py
    │       │   │   │   ├── virtualenv.py
    │       │   │   │   └── wheel.py
    │       │   │   ├── vcs/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── bazaar.cpython-310.pyc
    │       │   │   │   │   ├── git.cpython-310.pyc
    │       │   │   │   │   ├── mercurial.cpython-310.pyc
    │       │   │   │   │   ├── subversion.cpython-310.pyc
    │       │   │   │   │   └── versioncontrol.cpython-310.pyc
    │       │   │   │   ├── bazaar.py
    │       │   │   │   ├── git.py
    │       │   │   │   ├── mercurial.py
    │       │   │   │   ├── subversion.py
    │       │   │   │   └── versioncontrol.py
    │       │   │   └── wheel_builder.py
    │       │   ├── _vendor/
    │       │   │   ├── README.rst
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   └── __init__.cpython-310.pyc
    │       │   │   ├── cachecontrol/
    │       │   │   │   ├── LICENSE.txt
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _cmd.cpython-310.pyc
    │       │   │   │   │   ├── adapter.cpython-310.pyc
    │       │   │   │   │   ├── cache.cpython-310.pyc
    │       │   │   │   │   ├── controller.cpython-310.pyc
    │       │   │   │   │   ├── filewrapper.cpython-310.pyc
    │       │   │   │   │   ├── heuristics.cpython-310.pyc
    │       │   │   │   │   ├── serialize.cpython-310.pyc
    │       │   │   │   │   └── wrapper.cpython-310.pyc
    │       │   │   │   ├── _cmd.py
    │       │   │   │   ├── adapter.py
    │       │   │   │   ├── cache.py
    │       │   │   │   ├── caches/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── file_cache.cpython-310.pyc
    │       │   │   │   │   │   └── redis_cache.cpython-310.pyc
    │       │   │   │   │   ├── file_cache.py
    │       │   │   │   │   └── redis_cache.py
    │       │   │   │   ├── controller.py
    │       │   │   │   ├── filewrapper.py
    │       │   │   │   ├── heuristics.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── serialize.py
    │       │   │   │   └── wrapper.py
    │       │   │   ├── certifi/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── __main__.cpython-310.pyc
    │       │   │   │   │   └── core.cpython-310.pyc
    │       │   │   │   ├── cacert.pem
    │       │   │   │   ├── core.py
    │       │   │   │   └── py.typed
    │       │   │   ├── distlib/
    │       │   │   │   ├── LICENSE.txt
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── compat.cpython-310.pyc
    │       │   │   │   │   ├── resources.cpython-310.pyc
    │       │   │   │   │   ├── scripts.cpython-310.pyc
    │       │   │   │   │   └── util.cpython-310.pyc
    │       │   │   │   ├── compat.py
    │       │   │   │   ├── resources.py
    │       │   │   │   ├── scripts.py
    │       │   │   │   ├── t32.exe
    │       │   │   │   ├── t64-arm.exe
    │       │   │   │   ├── t64.exe
    │       │   │   │   ├── util.py
    │       │   │   │   ├── w32.exe
    │       │   │   │   ├── w64-arm.exe
    │       │   │   │   └── w64.exe
    │       │   │   ├── distro/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── __main__.cpython-310.pyc
    │       │   │   │   │   └── distro.cpython-310.pyc
    │       │   │   │   ├── distro.py
    │       │   │   │   └── py.typed
    │       │   │   ├── idna/
    │       │   │   │   ├── LICENSE.md
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── codec.cpython-310.pyc
    │       │   │   │   │   ├── compat.cpython-310.pyc
    │       │   │   │   │   ├── core.cpython-310.pyc
    │       │   │   │   │   ├── idnadata.cpython-310.pyc
    │       │   │   │   │   ├── intranges.cpython-310.pyc
    │       │   │   │   │   ├── package_data.cpython-310.pyc
    │       │   │   │   │   └── uts46data.cpython-310.pyc
    │       │   │   │   ├── codec.py
    │       │   │   │   ├── compat.py
    │       │   │   │   ├── core.py
    │       │   │   │   ├── idnadata.py
    │       │   │   │   ├── intranges.py
    │       │   │   │   ├── package_data.py
    │       │   │   │   ├── py.typed
    │       │   │   │   └── uts46data.py
    │       │   │   ├── msgpack/
    │       │   │   │   ├── COPYING
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   │   ├── ext.cpython-310.pyc
    │       │   │   │   │   └── fallback.cpython-310.pyc
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── ext.py
    │       │   │   │   └── fallback.py
    │       │   │   ├── packaging/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── LICENSE.APACHE
    │       │   │   │   ├── LICENSE.BSD
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _elffile.cpython-310.pyc
    │       │   │   │   │   ├── _manylinux.cpython-310.pyc
    │       │   │   │   │   ├── _musllinux.cpython-310.pyc
    │       │   │   │   │   ├── _parser.cpython-310.pyc
    │       │   │   │   │   ├── _structures.cpython-310.pyc
    │       │   │   │   │   ├── _tokenizer.cpython-310.pyc
    │       │   │   │   │   ├── dependency_groups.cpython-310.pyc
    │       │   │   │   │   ├── direct_url.cpython-310.pyc
    │       │   │   │   │   ├── errors.cpython-310.pyc
    │       │   │   │   │   ├── markers.cpython-310.pyc
    │       │   │   │   │   ├── metadata.cpython-310.pyc
    │       │   │   │   │   ├── pylock.cpython-310.pyc
    │       │   │   │   │   ├── requirements.cpython-310.pyc
    │       │   │   │   │   ├── specifiers.cpython-310.pyc
    │       │   │   │   │   ├── tags.cpython-310.pyc
    │       │   │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   │   └── version.cpython-310.pyc
    │       │   │   │   ├── _elffile.py
    │       │   │   │   ├── _manylinux.py
    │       │   │   │   ├── _musllinux.py
    │       │   │   │   ├── _parser.py
    │       │   │   │   ├── _structures.py
    │       │   │   │   ├── _tokenizer.py
    │       │   │   │   ├── dependency_groups.py
    │       │   │   │   ├── direct_url.py
    │       │   │   │   ├── errors.py
    │       │   │   │   ├── licenses/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── _spdx.cpython-310.pyc
    │       │   │   │   │   └── _spdx.py
    │       │   │   │   ├── markers.py
    │       │   │   │   ├── metadata.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── pylock.py
    │       │   │   │   ├── requirements.py
    │       │   │   │   ├── specifiers.py
    │       │   │   │   ├── tags.py
    │       │   │   │   ├── utils.py
    │       │   │   │   └── version.py
    │       │   │   ├── pkg_resources/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   └── __pycache__/
    │       │   │   │       └── __init__.cpython-310.pyc
    │       │   │   ├── platformdirs/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── __main__.cpython-310.pyc
    │       │   │   │   │   ├── android.cpython-310.pyc
    │       │   │   │   │   ├── api.cpython-310.pyc
    │       │   │   │   │   ├── macos.cpython-310.pyc
    │       │   │   │   │   ├── unix.cpython-310.pyc
    │       │   │   │   │   ├── version.cpython-310.pyc
    │       │   │   │   │   └── windows.cpython-310.pyc
    │       │   │   │   ├── android.py
    │       │   │   │   ├── api.py
    │       │   │   │   ├── macos.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── unix.py
    │       │   │   │   ├── version.py
    │       │   │   │   └── windows.py
    │       │   │   ├── pygments/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── __main__.cpython-310.pyc
    │       │   │   │   │   ├── console.cpython-310.pyc
    │       │   │   │   │   ├── filter.cpython-310.pyc
    │       │   │   │   │   ├── formatter.cpython-310.pyc
    │       │   │   │   │   ├── lexer.cpython-310.pyc
    │       │   │   │   │   ├── modeline.cpython-310.pyc
    │       │   │   │   │   ├── plugin.cpython-310.pyc
    │       │   │   │   │   ├── regexopt.cpython-310.pyc
    │       │   │   │   │   ├── scanner.cpython-310.pyc
    │       │   │   │   │   ├── sphinxext.cpython-310.pyc
    │       │   │   │   │   ├── style.cpython-310.pyc
    │       │   │   │   │   ├── token.cpython-310.pyc
    │       │   │   │   │   ├── unistring.cpython-310.pyc
    │       │   │   │   │   └── util.cpython-310.pyc
    │       │   │   │   ├── console.py
    │       │   │   │   ├── filter.py
    │       │   │   │   ├── filters/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── formatter.py
    │       │   │   │   ├── formatters/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── _mapping.cpython-310.pyc
    │       │   │   │   │   └── _mapping.py
    │       │   │   │   ├── lexer.py
    │       │   │   │   ├── lexers/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── _mapping.cpython-310.pyc
    │       │   │   │   │   │   └── python.cpython-310.pyc
    │       │   │   │   │   ├── _mapping.py
    │       │   │   │   │   └── python.py
    │       │   │   │   ├── modeline.py
    │       │   │   │   ├── plugin.py
    │       │   │   │   ├── regexopt.py
    │       │   │   │   ├── scanner.py
    │       │   │   │   ├── sphinxext.py
    │       │   │   │   ├── style.py
    │       │   │   │   ├── styles/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── _mapping.cpython-310.pyc
    │       │   │   │   │   └── _mapping.py
    │       │   │   │   ├── token.py
    │       │   │   │   ├── unistring.py
    │       │   │   │   └── util.py
    │       │   │   ├── pyproject_hooks/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   └── _impl.cpython-310.pyc
    │       │   │   │   ├── _impl.py
    │       │   │   │   ├── _in_process/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   └── _in_process.cpython-310.pyc
    │       │   │   │   │   └── _in_process.py
    │       │   │   │   └── py.typed
    │       │   │   ├── requests/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── __version__.cpython-310.pyc
    │       │   │   │   │   ├── _internal_utils.cpython-310.pyc
    │       │   │   │   │   ├── adapters.cpython-310.pyc
    │       │   │   │   │   ├── api.cpython-310.pyc
    │       │   │   │   │   ├── auth.cpython-310.pyc
    │       │   │   │   │   ├── certs.cpython-310.pyc
    │       │   │   │   │   ├── compat.cpython-310.pyc
    │       │   │   │   │   ├── cookies.cpython-310.pyc
    │       │   │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   │   ├── help.cpython-310.pyc
    │       │   │   │   │   ├── hooks.cpython-310.pyc
    │       │   │   │   │   ├── models.cpython-310.pyc
    │       │   │   │   │   ├── packages.cpython-310.pyc
    │       │   │   │   │   ├── sessions.cpython-310.pyc
    │       │   │   │   │   ├── status_codes.cpython-310.pyc
    │       │   │   │   │   ├── structures.cpython-310.pyc
    │       │   │   │   │   └── utils.cpython-310.pyc
    │       │   │   │   ├── __version__.py
    │       │   │   │   ├── _internal_utils.py
    │       │   │   │   ├── adapters.py
    │       │   │   │   ├── api.py
    │       │   │   │   ├── auth.py
    │       │   │   │   ├── certs.py
    │       │   │   │   ├── compat.py
    │       │   │   │   ├── cookies.py
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── help.py
    │       │   │   │   ├── hooks.py
    │       │   │   │   ├── models.py
    │       │   │   │   ├── packages.py
    │       │   │   │   ├── sessions.py
    │       │   │   │   ├── status_codes.py
    │       │   │   │   ├── structures.py
    │       │   │   │   └── utils.py
    │       │   │   ├── resolvelib/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── providers.cpython-310.pyc
    │       │   │   │   │   ├── reporters.cpython-310.pyc
    │       │   │   │   │   └── structs.cpython-310.pyc
    │       │   │   │   ├── providers.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── reporters.py
    │       │   │   │   ├── resolvers/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── abstract.cpython-310.pyc
    │       │   │   │   │   │   ├── criterion.cpython-310.pyc
    │       │   │   │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   │   │   └── resolution.cpython-310.pyc
    │       │   │   │   │   ├── abstract.py
    │       │   │   │   │   ├── criterion.py
    │       │   │   │   │   ├── exceptions.py
    │       │   │   │   │   └── resolution.py
    │       │   │   │   └── structs.py
    │       │   │   ├── rich/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __main__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── __main__.cpython-310.pyc
    │       │   │   │   │   ├── _cell_widths.cpython-310.pyc
    │       │   │   │   │   ├── _emoji_codes.cpython-310.pyc
    │       │   │   │   │   ├── _emoji_replace.cpython-310.pyc
    │       │   │   │   │   ├── _export_format.cpython-310.pyc
    │       │   │   │   │   ├── _extension.cpython-310.pyc
    │       │   │   │   │   ├── _fileno.cpython-310.pyc
    │       │   │   │   │   ├── _inspect.cpython-310.pyc
    │       │   │   │   │   ├── _log_render.cpython-310.pyc
    │       │   │   │   │   ├── _loop.cpython-310.pyc
    │       │   │   │   │   ├── _null_file.cpython-310.pyc
    │       │   │   │   │   ├── _palettes.cpython-310.pyc
    │       │   │   │   │   ├── _pick.cpython-310.pyc
    │       │   │   │   │   ├── _ratio.cpython-310.pyc
    │       │   │   │   │   ├── _spinners.cpython-310.pyc
    │       │   │   │   │   ├── _stack.cpython-310.pyc
    │       │   │   │   │   ├── _timer.cpython-310.pyc
    │       │   │   │   │   ├── _win32_console.cpython-310.pyc
    │       │   │   │   │   ├── _windows.cpython-310.pyc
    │       │   │   │   │   ├── _windows_renderer.cpython-310.pyc
    │       │   │   │   │   ├── _wrap.cpython-310.pyc
    │       │   │   │   │   ├── abc.cpython-310.pyc
    │       │   │   │   │   ├── align.cpython-310.pyc
    │       │   │   │   │   ├── ansi.cpython-310.pyc
    │       │   │   │   │   ├── bar.cpython-310.pyc
    │       │   │   │   │   ├── box.cpython-310.pyc
    │       │   │   │   │   ├── cells.cpython-310.pyc
    │       │   │   │   │   ├── color.cpython-310.pyc
    │       │   │   │   │   ├── color_triplet.cpython-310.pyc
    │       │   │   │   │   ├── columns.cpython-310.pyc
    │       │   │   │   │   ├── console.cpython-310.pyc
    │       │   │   │   │   ├── constrain.cpython-310.pyc
    │       │   │   │   │   ├── containers.cpython-310.pyc
    │       │   │   │   │   ├── control.cpython-310.pyc
    │       │   │   │   │   ├── default_styles.cpython-310.pyc
    │       │   │   │   │   ├── diagnose.cpython-310.pyc
    │       │   │   │   │   ├── emoji.cpython-310.pyc
    │       │   │   │   │   ├── errors.cpython-310.pyc
    │       │   │   │   │   ├── file_proxy.cpython-310.pyc
    │       │   │   │   │   ├── filesize.cpython-310.pyc
    │       │   │   │   │   ├── highlighter.cpython-310.pyc
    │       │   │   │   │   ├── json.cpython-310.pyc
    │       │   │   │   │   ├── jupyter.cpython-310.pyc
    │       │   │   │   │   ├── layout.cpython-310.pyc
    │       │   │   │   │   ├── live.cpython-310.pyc
    │       │   │   │   │   ├── live_render.cpython-310.pyc
    │       │   │   │   │   ├── logging.cpython-310.pyc
    │       │   │   │   │   ├── markup.cpython-310.pyc
    │       │   │   │   │   ├── measure.cpython-310.pyc
    │       │   │   │   │   ├── padding.cpython-310.pyc
    │       │   │   │   │   ├── pager.cpython-310.pyc
    │       │   │   │   │   ├── palette.cpython-310.pyc
    │       │   │   │   │   ├── panel.cpython-310.pyc
    │       │   │   │   │   ├── pretty.cpython-310.pyc
    │       │   │   │   │   ├── progress.cpython-310.pyc
    │       │   │   │   │   ├── progress_bar.cpython-310.pyc
    │       │   │   │   │   ├── prompt.cpython-310.pyc
    │       │   │   │   │   ├── protocol.cpython-310.pyc
    │       │   │   │   │   ├── region.cpython-310.pyc
    │       │   │   │   │   ├── repr.cpython-310.pyc
    │       │   │   │   │   ├── rule.cpython-310.pyc
    │       │   │   │   │   ├── scope.cpython-310.pyc
    │       │   │   │   │   ├── screen.cpython-310.pyc
    │       │   │   │   │   ├── segment.cpython-310.pyc
    │       │   │   │   │   ├── spinner.cpython-310.pyc
    │       │   │   │   │   ├── status.cpython-310.pyc
    │       │   │   │   │   ├── style.cpython-310.pyc
    │       │   │   │   │   ├── styled.cpython-310.pyc
    │       │   │   │   │   ├── syntax.cpython-310.pyc
    │       │   │   │   │   ├── table.cpython-310.pyc
    │       │   │   │   │   ├── terminal_theme.cpython-310.pyc
    │       │   │   │   │   ├── text.cpython-310.pyc
    │       │   │   │   │   ├── theme.cpython-310.pyc
    │       │   │   │   │   ├── themes.cpython-310.pyc
    │       │   │   │   │   ├── traceback.cpython-310.pyc
    │       │   │   │   │   └── tree.cpython-310.pyc
    │       │   │   │   ├── _cell_widths.py
    │       │   │   │   ├── _emoji_codes.py
    │       │   │   │   ├── _emoji_replace.py
    │       │   │   │   ├── _export_format.py
    │       │   │   │   ├── _extension.py
    │       │   │   │   ├── _fileno.py
    │       │   │   │   ├── _inspect.py
    │       │   │   │   ├── _log_render.py
    │       │   │   │   ├── _loop.py
    │       │   │   │   ├── _null_file.py
    │       │   │   │   ├── _palettes.py
    │       │   │   │   ├── _pick.py
    │       │   │   │   ├── _ratio.py
    │       │   │   │   ├── _spinners.py
    │       │   │   │   ├── _stack.py
    │       │   │   │   ├── _timer.py
    │       │   │   │   ├── _win32_console.py
    │       │   │   │   ├── _windows.py
    │       │   │   │   ├── _windows_renderer.py
    │       │   │   │   ├── _wrap.py
    │       │   │   │   ├── abc.py
    │       │   │   │   ├── align.py
    │       │   │   │   ├── ansi.py
    │       │   │   │   ├── bar.py
    │       │   │   │   ├── box.py
    │       │   │   │   ├── cells.py
    │       │   │   │   ├── color.py
    │       │   │   │   ├── color_triplet.py
    │       │   │   │   ├── columns.py
    │       │   │   │   ├── console.py
    │       │   │   │   ├── constrain.py
    │       │   │   │   ├── containers.py
    │       │   │   │   ├── control.py
    │       │   │   │   ├── default_styles.py
    │       │   │   │   ├── diagnose.py
    │       │   │   │   ├── emoji.py
    │       │   │   │   ├── errors.py
    │       │   │   │   ├── file_proxy.py
    │       │   │   │   ├── filesize.py
    │       │   │   │   ├── highlighter.py
    │       │   │   │   ├── json.py
    │       │   │   │   ├── jupyter.py
    │       │   │   │   ├── layout.py
    │       │   │   │   ├── live.py
    │       │   │   │   ├── live_render.py
    │       │   │   │   ├── logging.py
    │       │   │   │   ├── markup.py
    │       │   │   │   ├── measure.py
    │       │   │   │   ├── padding.py
    │       │   │   │   ├── pager.py
    │       │   │   │   ├── palette.py
    │       │   │   │   ├── panel.py
    │       │   │   │   ├── pretty.py
    │       │   │   │   ├── progress.py
    │       │   │   │   ├── progress_bar.py
    │       │   │   │   ├── prompt.py
    │       │   │   │   ├── protocol.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── region.py
    │       │   │   │   ├── repr.py
    │       │   │   │   ├── rule.py
    │       │   │   │   ├── scope.py
    │       │   │   │   ├── screen.py
    │       │   │   │   ├── segment.py
    │       │   │   │   ├── spinner.py
    │       │   │   │   ├── status.py
    │       │   │   │   ├── style.py
    │       │   │   │   ├── styled.py
    │       │   │   │   ├── syntax.py
    │       │   │   │   ├── table.py
    │       │   │   │   ├── terminal_theme.py
    │       │   │   │   ├── text.py
    │       │   │   │   ├── theme.py
    │       │   │   │   ├── themes.py
    │       │   │   │   ├── traceback.py
    │       │   │   │   └── tree.py
    │       │   │   ├── tomli/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _parser.cpython-310.pyc
    │       │   │   │   │   ├── _re.cpython-310.pyc
    │       │   │   │   │   └── _types.cpython-310.pyc
    │       │   │   │   ├── _parser.py
    │       │   │   │   ├── _re.py
    │       │   │   │   ├── _types.py
    │       │   │   │   └── py.typed
    │       │   │   ├── tomli_w/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   └── _writer.cpython-310.pyc
    │       │   │   │   ├── _writer.py
    │       │   │   │   └── py.typed
    │       │   │   ├── truststore/
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _api.cpython-310.pyc
    │       │   │   │   │   ├── _macos.cpython-310.pyc
    │       │   │   │   │   ├── _openssl.cpython-310.pyc
    │       │   │   │   │   ├── _ssl_constants.cpython-310.pyc
    │       │   │   │   │   └── _windows.cpython-310.pyc
    │       │   │   │   ├── _api.py
    │       │   │   │   ├── _macos.py
    │       │   │   │   ├── _openssl.py
    │       │   │   │   ├── _ssl_constants.py
    │       │   │   │   ├── _windows.py
    │       │   │   │   └── py.typed
    │       │   │   ├── urllib3/
    │       │   │   │   ├── LICENSE.txt
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _base_connection.cpython-310.pyc
    │       │   │   │   │   ├── _collections.cpython-310.pyc
    │       │   │   │   │   ├── _request_methods.cpython-310.pyc
    │       │   │   │   │   ├── _version.cpython-310.pyc
    │       │   │   │   │   ├── connection.cpython-310.pyc
    │       │   │   │   │   ├── connectionpool.cpython-310.pyc
    │       │   │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   │   ├── fields.cpython-310.pyc
    │       │   │   │   │   ├── filepost.cpython-310.pyc
    │       │   │   │   │   ├── poolmanager.cpython-310.pyc
    │       │   │   │   │   └── response.cpython-310.pyc
    │       │   │   │   ├── _base_connection.py
    │       │   │   │   ├── _collections.py
    │       │   │   │   ├── _request_methods.py
    │       │   │   │   ├── _version.py
    │       │   │   │   ├── connection.py
    │       │   │   │   ├── connectionpool.py
    │       │   │   │   ├── contrib/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── pyopenssl.cpython-310.pyc
    │       │   │   │   │   │   └── socks.cpython-310.pyc
    │       │   │   │   │   ├── emscripten/
    │       │   │   │   │   │   ├── __init__.py
    │       │   │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   │   ├── connection.cpython-310.pyc
    │       │   │   │   │   │   │   ├── fetch.cpython-310.pyc
    │       │   │   │   │   │   │   ├── request.cpython-310.pyc
    │       │   │   │   │   │   │   └── response.cpython-310.pyc
    │       │   │   │   │   │   ├── connection.py
    │       │   │   │   │   │   ├── emscripten_fetch_worker.js
    │       │   │   │   │   │   ├── fetch.py
    │       │   │   │   │   │   ├── request.py
    │       │   │   │   │   │   └── response.py
    │       │   │   │   │   ├── pyopenssl.py
    │       │   │   │   │   └── socks.py
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── fields.py
    │       │   │   │   ├── filepost.py
    │       │   │   │   ├── http2/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── __pycache__/
    │       │   │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   │   ├── connection.cpython-310.pyc
    │       │   │   │   │   │   └── probe.cpython-310.pyc
    │       │   │   │   │   ├── connection.py
    │       │   │   │   │   └── probe.py
    │       │   │   │   ├── poolmanager.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── response.py
    │       │   │   │   └── util/
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── __pycache__/
    │       │   │   │       │   ├── __init__.cpython-310.pyc
    │       │   │   │       │   ├── connection.cpython-310.pyc
    │       │   │   │       │   ├── proxy.cpython-310.pyc
    │       │   │   │       │   ├── request.cpython-310.pyc
    │       │   │   │       │   ├── response.cpython-310.pyc
    │       │   │   │       │   ├── retry.cpython-310.pyc
    │       │   │   │       │   ├── ssl_.cpython-310.pyc
    │       │   │   │       │   ├── ssl_match_hostname.cpython-310.pyc
    │       │   │   │       │   ├── ssltransport.cpython-310.pyc
    │       │   │   │       │   ├── timeout.cpython-310.pyc
    │       │   │   │       │   ├── url.cpython-310.pyc
    │       │   │   │       │   ├── util.cpython-310.pyc
    │       │   │   │       │   └── wait.cpython-310.pyc
    │       │   │   │       ├── connection.py
    │       │   │   │       ├── proxy.py
    │       │   │   │       ├── request.py
    │       │   │   │       ├── response.py
    │       │   │   │       ├── retry.py
    │       │   │   │       ├── ssl_.py
    │       │   │   │       ├── ssl_match_hostname.py
    │       │   │   │       ├── ssltransport.py
    │       │   │   │       ├── timeout.py
    │       │   │   │       ├── url.py
    │       │   │   │       ├── util.py
    │       │   │   │       └── wait.py
    │       │   │   └── vendor.txt
    │       │   └── py.typed
    │       ├── pkg_resources/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   └── __init__.cpython-310.pyc
    │       │   ├── _vendor/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── appdirs.cpython-310.pyc
    │       │   │   │   └── zipp.cpython-310.pyc
    │       │   │   ├── appdirs.py
    │       │   │   ├── importlib_resources/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _adapters.cpython-310.pyc
    │       │   │   │   │   ├── _common.cpython-310.pyc
    │       │   │   │   │   ├── _compat.cpython-310.pyc
    │       │   │   │   │   ├── _itertools.cpython-310.pyc
    │       │   │   │   │   ├── _legacy.cpython-310.pyc
    │       │   │   │   │   ├── abc.cpython-310.pyc
    │       │   │   │   │   ├── readers.cpython-310.pyc
    │       │   │   │   │   └── simple.cpython-310.pyc
    │       │   │   │   ├── _adapters.py
    │       │   │   │   ├── _common.py
    │       │   │   │   ├── _compat.py
    │       │   │   │   ├── _itertools.py
    │       │   │   │   ├── _legacy.py
    │       │   │   │   ├── abc.py
    │       │   │   │   ├── readers.py
    │       │   │   │   └── simple.py
    │       │   │   ├── jaraco/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── context.cpython-310.pyc
    │       │   │   │   │   └── functools.cpython-310.pyc
    │       │   │   │   ├── context.py
    │       │   │   │   ├── functools.py
    │       │   │   │   └── text/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── more_itertools/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── more.cpython-310.pyc
    │       │   │   │   │   └── recipes.cpython-310.pyc
    │       │   │   │   ├── more.py
    │       │   │   │   └── recipes.py
    │       │   │   ├── packaging/
    │       │   │   │   ├── __about__.py
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __about__.cpython-310.pyc
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _manylinux.cpython-310.pyc
    │       │   │   │   │   ├── _musllinux.cpython-310.pyc
    │       │   │   │   │   ├── _structures.cpython-310.pyc
    │       │   │   │   │   ├── markers.cpython-310.pyc
    │       │   │   │   │   ├── requirements.cpython-310.pyc
    │       │   │   │   │   ├── specifiers.cpython-310.pyc
    │       │   │   │   │   ├── tags.cpython-310.pyc
    │       │   │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   │   └── version.cpython-310.pyc
    │       │   │   │   ├── _manylinux.py
    │       │   │   │   ├── _musllinux.py
    │       │   │   │   ├── _structures.py
    │       │   │   │   ├── markers.py
    │       │   │   │   ├── requirements.py
    │       │   │   │   ├── specifiers.py
    │       │   │   │   ├── tags.py
    │       │   │   │   ├── utils.py
    │       │   │   │   └── version.py
    │       │   │   ├── pyparsing/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── actions.cpython-310.pyc
    │       │   │   │   │   ├── common.cpython-310.pyc
    │       │   │   │   │   ├── core.cpython-310.pyc
    │       │   │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   │   ├── helpers.cpython-310.pyc
    │       │   │   │   │   ├── results.cpython-310.pyc
    │       │   │   │   │   ├── testing.cpython-310.pyc
    │       │   │   │   │   ├── unicode.cpython-310.pyc
    │       │   │   │   │   └── util.cpython-310.pyc
    │       │   │   │   ├── actions.py
    │       │   │   │   ├── common.py
    │       │   │   │   ├── core.py
    │       │   │   │   ├── diagram/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── helpers.py
    │       │   │   │   ├── results.py
    │       │   │   │   ├── testing.py
    │       │   │   │   ├── unicode.py
    │       │   │   │   └── util.py
    │       │   │   └── zipp.py
    │       │   └── extern/
    │       │       ├── __init__.py
    │       │       └── __pycache__/
    │       │           └── __init__.cpython-310.pyc
    │       ├── pluggy-1.0.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   └── top_level.txt
    │       ├── pluggy/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── _callers.cpython-310.pyc
    │       │   │   ├── _hooks.cpython-310.pyc
    │       │   │   ├── _manager.cpython-310.pyc
    │       │   │   ├── _result.cpython-310.pyc
    │       │   │   ├── _tracing.cpython-310.pyc
    │       │   │   └── _version.cpython-310.pyc
    │       │   ├── _callers.py
    │       │   ├── _hooks.py
    │       │   ├── _manager.py
    │       │   ├── _result.py
    │       │   ├── _tracing.py
    │       │   └── _version.py
    │       ├── py-1.11.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   └── top_level.txt
    │       ├── py/
    │       │   ├── __init__.py
    │       │   ├── __init__.pyi
    │       │   ├── __metainfo.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── __metainfo.cpython-310.pyc
    │       │   │   ├── _builtin.cpython-310.pyc
    │       │   │   ├── _error.cpython-310.pyc
    │       │   │   ├── _std.cpython-310.pyc
    │       │   │   ├── _version.cpython-310.pyc
    │       │   │   ├── _xmlgen.cpython-310.pyc
    │       │   │   └── test.cpython-310.pyc
    │       │   ├── _builtin.py
    │       │   ├── _code/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── _assertionnew.cpython-310.pyc
    │       │   │   │   ├── _assertionold.cpython-310.pyc
    │       │   │   │   ├── _py2traceback.cpython-310.pyc
    │       │   │   │   ├── assertion.cpython-310.pyc
    │       │   │   │   ├── code.cpython-310.pyc
    │       │   │   │   └── source.cpython-310.pyc
    │       │   │   ├── _assertionnew.py
    │       │   │   ├── _assertionold.py
    │       │   │   ├── _py2traceback.py
    │       │   │   ├── assertion.py
    │       │   │   ├── code.py
    │       │   │   └── source.py
    │       │   ├── _error.py
    │       │   ├── _io/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── capture.cpython-310.pyc
    │       │   │   │   ├── saferepr.cpython-310.pyc
    │       │   │   │   └── terminalwriter.cpython-310.pyc
    │       │   │   ├── capture.py
    │       │   │   ├── saferepr.py
    │       │   │   └── terminalwriter.py
    │       │   ├── _log/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── log.cpython-310.pyc
    │       │   │   │   └── warning.cpython-310.pyc
    │       │   │   ├── log.py
    │       │   │   └── warning.py
    │       │   ├── _path/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── cacheutil.cpython-310.pyc
    │       │   │   │   ├── common.cpython-310.pyc
    │       │   │   │   ├── local.cpython-310.pyc
    │       │   │   │   ├── svnurl.cpython-310.pyc
    │       │   │   │   └── svnwc.cpython-310.pyc
    │       │   │   ├── cacheutil.py
    │       │   │   ├── common.py
    │       │   │   ├── local.py
    │       │   │   ├── svnurl.py
    │       │   │   └── svnwc.py
    │       │   ├── _process/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── cmdexec.cpython-310.pyc
    │       │   │   │   ├── forkedfunc.cpython-310.pyc
    │       │   │   │   └── killproc.cpython-310.pyc
    │       │   │   ├── cmdexec.py
    │       │   │   ├── forkedfunc.py
    │       │   │   └── killproc.py
    │       │   ├── _std.py
    │       │   ├── _vendored_packages/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   └── __init__.cpython-310.pyc
    │       │   │   ├── apipkg-2.0.0.dist-info/
    │       │   │   │   ├── INSTALLER
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── METADATA
    │       │   │   │   ├── RECORD
    │       │   │   │   ├── REQUESTED
    │       │   │   │   ├── WHEEL
    │       │   │   │   └── top_level.txt
    │       │   │   ├── apipkg/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   └── version.cpython-310.pyc
    │       │   │   │   └── version.py
    │       │   │   ├── iniconfig-1.1.1.dist-info/
    │       │   │   │   ├── INSTALLER
    │       │   │   │   ├── LICENSE
    │       │   │   │   ├── METADATA
    │       │   │   │   ├── RECORD
    │       │   │   │   ├── REQUESTED
    │       │   │   │   ├── WHEEL
    │       │   │   │   └── top_level.txt
    │       │   │   └── iniconfig/
    │       │   │       ├── __init__.py
    │       │   │       ├── __init__.pyi
    │       │   │       ├── __pycache__/
    │       │   │       │   └── __init__.cpython-310.pyc
    │       │   │       └── py.typed
    │       │   ├── _version.py
    │       │   ├── _xmlgen.py
    │       │   ├── error.pyi
    │       │   ├── iniconfig.pyi
    │       │   ├── io.pyi
    │       │   ├── path.pyi
    │       │   ├── py.typed
    │       │   ├── test.py
    │       │   └── xml.pyi
    │       ├── pycodestyle-2.9.1.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── pycodestyle.py
    │       ├── pydocstyle-6.3.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   └── entry_points.txt
    │       ├── pydocstyle/
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── __main__.cpython-310.pyc
    │       │   │   ├── _version.cpython-310.pyc
    │       │   │   ├── checker.cpython-310.pyc
    │       │   │   ├── cli.cpython-310.pyc
    │       │   │   ├── config.cpython-310.pyc
    │       │   │   ├── parser.cpython-310.pyc
    │       │   │   ├── utils.cpython-310.pyc
    │       │   │   ├── violations.cpython-310.pyc
    │       │   │   └── wordlists.cpython-310.pyc
    │       │   ├── _version.py
    │       │   ├── checker.py
    │       │   ├── cli.py
    │       │   ├── config.py
    │       │   ├── data/
    │       │   │   ├── imperatives.txt
    │       │   │   └── imperatives_blacklist.txt
    │       │   ├── parser.py
    │       │   ├── utils.py
    │       │   ├── violations.py
    │       │   └── wordlists.py
    │       ├── pyflakes-2.5.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── pyflakes/
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── __main__.cpython-310.pyc
    │       │   │   ├── api.cpython-310.pyc
    │       │   │   ├── checker.cpython-310.pyc
    │       │   │   ├── messages.cpython-310.pyc
    │       │   │   └── reporter.cpython-310.pyc
    │       │   ├── api.py
    │       │   ├── checker.py
    │       │   ├── messages.py
    │       │   ├── reporter.py
    │       │   ├── scripts/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   └── pyflakes.cpython-310.pyc
    │       │   │   └── pyflakes.py
    │       │   └── test/
    │       │       ├── __init__.py
    │       │       ├── __pycache__/
    │       │       │   ├── __init__.cpython-310.pyc
    │       │       │   ├── harness.cpython-310.pyc
    │       │       │   ├── test_api.cpython-310.pyc
    │       │       │   ├── test_builtin.cpython-310.pyc
    │       │       │   ├── test_checker.cpython-310.pyc
    │       │       │   ├── test_code_segment.cpython-310.pyc
    │       │       │   ├── test_dict.cpython-310.pyc
    │       │       │   ├── test_doctests.cpython-310.pyc
    │       │       │   ├── test_imports.cpython-310.pyc
    │       │       │   ├── test_is_literal.cpython-310.pyc
    │       │       │   ├── test_match.cpython-310.pyc
    │       │       │   ├── test_other.cpython-310.pyc
    │       │       │   ├── test_type_annotations.cpython-310.pyc
    │       │       │   └── test_undefined_names.cpython-310.pyc
    │       │       ├── harness.py
    │       │       ├── test_api.py
    │       │       ├── test_builtin.py
    │       │       ├── test_checker.py
    │       │       ├── test_code_segment.py
    │       │       ├── test_dict.py
    │       │       ├── test_doctests.py
    │       │       ├── test_imports.py
    │       │       ├── test_is_literal.py
    │       │       ├── test_match.py
    │       │       ├── test_other.py
    │       │       ├── test_type_annotations.py
    │       │       └── test_undefined_names.py
    │       ├── pytest-7.1.3.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── pytest/
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   └── __main__.cpython-310.pyc
    │       │   └── py.typed
    │       ├── pytest_django-4.5.2.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── pytest_django/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── _version.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── _version.cpython-310.pyc
    │       │   │   ├── asserts.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── asserts.cpython-310.pyc
    │       │   │   ├── django_compat.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── django_compat.cpython-310.pyc
    │       │   │   ├── fixtures.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── fixtures.cpython-310.pyc
    │       │   │   ├── lazy_django.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── lazy_django.cpython-310.pyc
    │       │   │   ├── live_server_helper.cpython-310-pytest-7.1.3.pyc
    │       │   │   ├── live_server_helper.cpython-310.pyc
    │       │   │   ├── plugin.cpython-310-pytest-7.1.3.pyc
    │       │   │   └── plugin.cpython-310.pyc
    │       │   ├── _version.py
    │       │   ├── asserts.py
    │       │   ├── django_compat.py
    │       │   ├── fixtures.py
    │       │   ├── lazy_django.py
    │       │   ├── live_server_helper.py
    │       │   ├── plugin.py
    │       │   └── py.typed
    │       ├── python_dateutil-2.8.2.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── top_level.txt
    │       │   └── zip-safe
    │       ├── pytz-2022.7.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE.txt
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── top_level.txt
    │       │   └── zip-safe
    │       ├── pytz/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── exceptions.cpython-310.pyc
    │       │   │   ├── lazy.cpython-310.pyc
    │       │   │   ├── reference.cpython-310.pyc
    │       │   │   ├── tzfile.cpython-310.pyc
    │       │   │   └── tzinfo.cpython-310.pyc
    │       │   ├── exceptions.py
    │       │   ├── lazy.py
    │       │   ├── reference.py
    │       │   ├── tzfile.py
    │       │   ├── tzinfo.py
    │       │   └── zoneinfo/
    │       │       ├── Africa/
    │       │       │   ├── Abidjan
    │       │       │   ├── Accra
    │       │       │   ├── Addis_Ababa
    │       │       │   ├── Algiers
    │       │       │   ├── Asmara
    │       │       │   ├── Asmera
    │       │       │   ├── Bamako
    │       │       │   ├── Bangui
    │       │       │   ├── Banjul
    │       │       │   ├── Bissau
    │       │       │   ├── Blantyre
    │       │       │   ├── Brazzaville
    │       │       │   ├── Bujumbura
    │       │       │   ├── Cairo
    │       │       │   ├── Casablanca
    │       │       │   ├── Ceuta
    │       │       │   ├── Conakry
    │       │       │   ├── Dakar
    │       │       │   ├── Dar_es_Salaam
    │       │       │   ├── Djibouti
    │       │       │   ├── Douala
    │       │       │   ├── El_Aaiun
    │       │       │   ├── Freetown
    │       │       │   ├── Gaborone
    │       │       │   ├── Harare
    │       │       │   ├── Johannesburg
    │       │       │   ├── Juba
    │       │       │   ├── Kampala
    │       │       │   ├── Khartoum
    │       │       │   ├── Kigali
    │       │       │   ├── Kinshasa
    │       │       │   ├── Lagos
    │       │       │   ├── Libreville
    │       │       │   ├── Lome
    │       │       │   ├── Luanda
    │       │       │   ├── Lubumbashi
    │       │       │   ├── Lusaka
    │       │       │   ├── Malabo
    │       │       │   ├── Maputo
    │       │       │   ├── Maseru
    │       │       │   ├── Mbabane
    │       │       │   ├── Mogadishu
    │       │       │   ├── Monrovia
    │       │       │   ├── Nairobi
    │       │       │   ├── Ndjamena
    │       │       │   ├── Niamey
    │       │       │   ├── Nouakchott
    │       │       │   ├── Ouagadougou
    │       │       │   ├── Porto-Novo
    │       │       │   ├── Sao_Tome
    │       │       │   ├── Timbuktu
    │       │       │   ├── Tripoli
    │       │       │   ├── Tunis
    │       │       │   └── Windhoek
    │       │       ├── America/
    │       │       │   ├── Adak
    │       │       │   ├── Anchorage
    │       │       │   ├── Anguilla
    │       │       │   ├── Antigua
    │       │       │   ├── Araguaina
    │       │       │   ├── Argentina/
    │       │       │   │   ├── Buenos_Aires
    │       │       │   │   ├── Catamarca
    │       │       │   │   ├── ComodRivadavia
    │       │       │   │   ├── Cordoba
    │       │       │   │   ├── Jujuy
    │       │       │   │   ├── La_Rioja
    │       │       │   │   ├── Mendoza
    │       │       │   │   ├── Rio_Gallegos
    │       │       │   │   ├── Salta
    │       │       │   │   ├── San_Juan
    │       │       │   │   ├── San_Luis
    │       │       │   │   ├── Tucuman
    │       │       │   │   └── Ushuaia
    │       │       │   ├── Aruba
    │       │       │   ├── Asuncion
    │       │       │   ├── Atikokan
    │       │       │   ├── Atka
    │       │       │   ├── Bahia
    │       │       │   ├── Bahia_Banderas
    │       │       │   ├── Barbados
    │       │       │   ├── Belem
    │       │       │   ├── Belize
    │       │       │   ├── Blanc-Sablon
    │       │       │   ├── Boa_Vista
    │       │       │   ├── Bogota
    │       │       │   ├── Boise
    │       │       │   ├── Buenos_Aires
    │       │       │   ├── Cambridge_Bay
    │       │       │   ├── Campo_Grande
    │       │       │   ├── Cancun
    │       │       │   ├── Caracas
    │       │       │   ├── Catamarca
    │       │       │   ├── Cayenne
    │       │       │   ├── Cayman
    │       │       │   ├── Chicago
    │       │       │   ├── Chihuahua
    │       │       │   ├── Ciudad_Juarez
    │       │       │   ├── Coral_Harbour
    │       │       │   ├── Cordoba
    │       │       │   ├── Costa_Rica
    │       │       │   ├── Creston
    │       │       │   ├── Cuiaba
    │       │       │   ├── Curacao
    │       │       │   ├── Danmarkshavn
    │       │       │   ├── Dawson
    │       │       │   ├── Dawson_Creek
    │       │       │   ├── Denver
    │       │       │   ├── Detroit
    │       │       │   ├── Dominica
    │       │       │   ├── Edmonton
    │       │       │   ├── Eirunepe
    │       │       │   ├── El_Salvador
    │       │       │   ├── Ensenada
    │       │       │   ├── Fort_Nelson
    │       │       │   ├── Fort_Wayne
    │       │       │   ├── Fortaleza
    │       │       │   ├── Glace_Bay
    │       │       │   ├── Godthab
    │       │       │   ├── Goose_Bay
    │       │       │   ├── Grand_Turk
    │       │       │   ├── Grenada
    │       │       │   ├── Guadeloupe
    │       │       │   ├── Guatemala
    │       │       │   ├── Guayaquil
    │       │       │   ├── Guyana
    │       │       │   ├── Halifax
    │       │       │   ├── Havana
    │       │       │   ├── Hermosillo
    │       │       │   ├── Indiana/
    │       │       │   │   ├── Indianapolis
    │       │       │   │   ├── Knox
    │       │       │   │   ├── Marengo
    │       │       │   │   ├── Petersburg
    │       │       │   │   ├── Tell_City
    │       │       │   │   ├── Vevay
    │       │       │   │   ├── Vincennes
    │       │       │   │   └── Winamac
    │       │       │   ├── Indianapolis
    │       │       │   ├── Inuvik
    │       │       │   ├── Iqaluit
    │       │       │   ├── Jamaica
    │       │       │   ├── Jujuy
    │       │       │   ├── Juneau
    │       │       │   ├── Kentucky/
    │       │       │   │   ├── Louisville
    │       │       │   │   └── Monticello
    │       │       │   ├── Knox_IN
    │       │       │   ├── Kralendijk
    │       │       │   ├── La_Paz
    │       │       │   ├── Lima
    │       │       │   ├── Los_Angeles
    │       │       │   ├── Louisville
    │       │       │   ├── Lower_Princes
    │       │       │   ├── Maceio
    │       │       │   ├── Managua
    │       │       │   ├── Manaus
    │       │       │   ├── Marigot
    │       │       │   ├── Martinique
    │       │       │   ├── Matamoros
    │       │       │   ├── Mazatlan
    │       │       │   ├── Mendoza
    │       │       │   ├── Menominee
    │       │       │   ├── Merida
    │       │       │   ├── Metlakatla
    │       │       │   ├── Mexico_City
    │       │       │   ├── Miquelon
    │       │       │   ├── Moncton
    │       │       │   ├── Monterrey
    │       │       │   ├── Montevideo
    │       │       │   ├── Montreal
    │       │       │   ├── Montserrat
    │       │       │   ├── Nassau
    │       │       │   ├── New_York
    │       │       │   ├── Nipigon
    │       │       │   ├── Nome
    │       │       │   ├── Noronha
    │       │       │   ├── North_Dakota/
    │       │       │   │   ├── Beulah
    │       │       │   │   ├── Center
    │       │       │   │   └── New_Salem
    │       │       │   ├── Nuuk
    │       │       │   ├── Ojinaga
    │       │       │   ├── Panama
    │       │       │   ├── Pangnirtung
    │       │       │   ├── Paramaribo
    │       │       │   ├── Phoenix
    │       │       │   ├── Port-au-Prince
    │       │       │   ├── Port_of_Spain
    │       │       │   ├── Porto_Acre
    │       │       │   ├── Porto_Velho
    │       │       │   ├── Puerto_Rico
    │       │       │   ├── Punta_Arenas
    │       │       │   ├── Rainy_River
    │       │       │   ├── Rankin_Inlet
    │       │       │   ├── Recife
    │       │       │   ├── Regina
    │       │       │   ├── Resolute
    │       │       │   ├── Rio_Branco
    │       │       │   ├── Rosario
    │       │       │   ├── Santa_Isabel
    │       │       │   ├── Santarem
    │       │       │   ├── Santiago
    │       │       │   ├── Santo_Domingo
    │       │       │   ├── Sao_Paulo
    │       │       │   ├── Scoresbysund
    │       │       │   ├── Shiprock
    │       │       │   ├── Sitka
    │       │       │   ├── St_Barthelemy
    │       │       │   ├── St_Johns
    │       │       │   ├── St_Kitts
    │       │       │   ├── St_Lucia
    │       │       │   ├── St_Thomas
    │       │       │   ├── St_Vincent
    │       │       │   ├── Swift_Current
    │       │       │   ├── Tegucigalpa
    │       │       │   ├── Thule
    │       │       │   ├── Thunder_Bay
    │       │       │   ├── Tijuana
    │       │       │   ├── Toronto
    │       │       │   ├── Tortola
    │       │       │   ├── Vancouver
    │       │       │   ├── Virgin
    │       │       │   ├── Whitehorse
    │       │       │   ├── Winnipeg
    │       │       │   ├── Yakutat
    │       │       │   └── Yellowknife
    │       │       ├── Antarctica/
    │       │       │   ├── Casey
    │       │       │   ├── Davis
    │       │       │   ├── DumontDUrville
    │       │       │   ├── Macquarie
    │       │       │   ├── Mawson
    │       │       │   ├── McMurdo
    │       │       │   ├── Palmer
    │       │       │   ├── Rothera
    │       │       │   ├── South_Pole
    │       │       │   ├── Syowa
    │       │       │   ├── Troll
    │       │       │   └── Vostok
    │       │       ├── Arctic/
    │       │       │   └── Longyearbyen
    │       │       ├── Asia/
    │       │       │   ├── Aden
    │       │       │   ├── Almaty
    │       │       │   ├── Amman
    │       │       │   ├── Anadyr
    │       │       │   ├── Aqtau
    │       │       │   ├── Aqtobe
    │       │       │   ├── Ashgabat
    │       │       │   ├── Ashkhabad
    │       │       │   ├── Atyrau
    │       │       │   ├── Baghdad
    │       │       │   ├── Bahrain
    │       │       │   ├── Baku
    │       │       │   ├── Bangkok
    │       │       │   ├── Barnaul
    │       │       │   ├── Beirut
    │       │       │   ├── Bishkek
    │       │       │   ├── Brunei
    │       │       │   ├── Calcutta
    │       │       │   ├── Chita
    │       │       │   ├── Choibalsan
    │       │       │   ├── Chongqing
    │       │       │   ├── Chungking
    │       │       │   ├── Colombo
    │       │       │   ├── Dacca
    │       │       │   ├── Damascus
    │       │       │   ├── Dhaka
    │       │       │   ├── Dili
    │       │       │   ├── Dubai
    │       │       │   ├── Dushanbe
    │       │       │   ├── Famagusta
    │       │       │   ├── Gaza
    │       │       │   ├── Harbin
    │       │       │   ├── Hebron
    │       │       │   ├── Ho_Chi_Minh
    │       │       │   ├── Hong_Kong
    │       │       │   ├── Hovd
    │       │       │   ├── Irkutsk
    │       │       │   ├── Istanbul
    │       │       │   ├── Jakarta
    │       │       │   ├── Jayapura
    │       │       │   ├── Jerusalem
    │       │       │   ├── Kabul
    │       │       │   ├── Kamchatka
    │       │       │   ├── Karachi
    │       │       │   ├── Kashgar
    │       │       │   ├── Kathmandu
    │       │       │   ├── Katmandu
    │       │       │   ├── Khandyga
    │       │       │   ├── Kolkata
    │       │       │   ├── Krasnoyarsk
    │       │       │   ├── Kuala_Lumpur
    │       │       │   ├── Kuching
    │       │       │   ├── Kuwait
    │       │       │   ├── Macao
    │       │       │   ├── Macau
    │       │       │   ├── Magadan
    │       │       │   ├── Makassar
    │       │       │   ├── Manila
    │       │       │   ├── Muscat
    │       │       │   ├── Nicosia
    │       │       │   ├── Novokuznetsk
    │       │       │   ├── Novosibirsk
    │       │       │   ├── Omsk
    │       │       │   ├── Oral
    │       │       │   ├── Phnom_Penh
    │       │       │   ├── Pontianak
    │       │       │   ├── Pyongyang
    │       │       │   ├── Qatar
    │       │       │   ├── Qostanay
    │       │       │   ├── Qyzylorda
    │       │       │   ├── Rangoon
    │       │       │   ├── Riyadh
    │       │       │   ├── Saigon
    │       │       │   ├── Sakhalin
    │       │       │   ├── Samarkand
    │       │       │   ├── Seoul
    │       │       │   ├── Shanghai
    │       │       │   ├── Singapore
    │       │       │   ├── Srednekolymsk
    │       │       │   ├── Taipei
    │       │       │   ├── Tashkent
    │       │       │   ├── Tbilisi
    │       │       │   ├── Tehran
    │       │       │   ├── Tel_Aviv
    │       │       │   ├── Thimbu
    │       │       │   ├── Thimphu
    │       │       │   ├── Tokyo
    │       │       │   ├── Tomsk
    │       │       │   ├── Ujung_Pandang
    │       │       │   ├── Ulaanbaatar
    │       │       │   ├── Ulan_Bator
    │       │       │   ├── Urumqi
    │       │       │   ├── Ust-Nera
    │       │       │   ├── Vientiane
    │       │       │   ├── Vladivostok
    │       │       │   ├── Yakutsk
    │       │       │   ├── Yangon
    │       │       │   ├── Yekaterinburg
    │       │       │   └── Yerevan
    │       │       ├── Atlantic/
    │       │       │   ├── Azores
    │       │       │   ├── Bermuda
    │       │       │   ├── Canary
    │       │       │   ├── Cape_Verde
    │       │       │   ├── Faeroe
    │       │       │   ├── Faroe
    │       │       │   ├── Jan_Mayen
    │       │       │   ├── Madeira
    │       │       │   ├── Reykjavik
    │       │       │   ├── South_Georgia
    │       │       │   ├── St_Helena
    │       │       │   └── Stanley
    │       │       ├── Australia/
    │       │       │   ├── ACT
    │       │       │   ├── Adelaide
    │       │       │   ├── Brisbane
    │       │       │   ├── Broken_Hill
    │       │       │   ├── Canberra
    │       │       │   ├── Currie
    │       │       │   ├── Darwin
    │       │       │   ├── Eucla
    │       │       │   ├── Hobart
    │       │       │   ├── LHI
    │       │       │   ├── Lindeman
    │       │       │   ├── Lord_Howe
    │       │       │   ├── Melbourne
    │       │       │   ├── NSW
    │       │       │   ├── North
    │       │       │   ├── Perth
    │       │       │   ├── Queensland
    │       │       │   ├── South
    │       │       │   ├── Sydney
    │       │       │   ├── Tasmania
    │       │       │   ├── Victoria
    │       │       │   ├── West
    │       │       │   └── Yancowinna
    │       │       ├── Brazil/
    │       │       │   ├── Acre
    │       │       │   ├── DeNoronha
    │       │       │   ├── East
    │       │       │   └── West
    │       │       ├── CET
    │       │       ├── CST6CDT
    │       │       ├── Canada/
    │       │       │   ├── Atlantic
    │       │       │   ├── Central
    │       │       │   ├── Eastern
    │       │       │   ├── Mountain
    │       │       │   ├── Newfoundland
    │       │       │   ├── Pacific
    │       │       │   ├── Saskatchewan
    │       │       │   └── Yukon
    │       │       ├── Chile/
    │       │       │   ├── Continental
    │       │       │   └── EasterIsland
    │       │       ├── Cuba
    │       │       ├── EET
    │       │       ├── EST
    │       │       ├── EST5EDT
    │       │       ├── Egypt
    │       │       ├── Eire
    │       │       ├── Etc/
    │       │       │   ├── GMT
    │       │       │   ├── GMT+0
    │       │       │   ├── GMT+1
    │       │       │   ├── GMT+10
    │       │       │   ├── GMT+11
    │       │       │   ├── GMT+12
    │       │       │   ├── GMT+2
    │       │       │   ├── GMT+3
    │       │       │   ├── GMT+4
    │       │       │   ├── GMT+5
    │       │       │   ├── GMT+6
    │       │       │   ├── GMT+7
    │       │       │   ├── GMT+8
    │       │       │   ├── GMT+9
    │       │       │   ├── GMT-0
    │       │       │   ├── GMT-1
    │       │       │   ├── GMT-10
    │       │       │   ├── GMT-11
    │       │       │   ├── GMT-12
    │       │       │   ├── GMT-13
    │       │       │   ├── GMT-14
    │       │       │   ├── GMT-2
    │       │       │   ├── GMT-3
    │       │       │   ├── GMT-4
    │       │       │   ├── GMT-5
    │       │       │   ├── GMT-6
    │       │       │   ├── GMT-7
    │       │       │   ├── GMT-8
    │       │       │   ├── GMT-9
    │       │       │   ├── GMT0
    │       │       │   ├── Greenwich
    │       │       │   ├── UCT
    │       │       │   ├── UTC
    │       │       │   ├── Universal
    │       │       │   └── Zulu
    │       │       ├── Europe/
    │       │       │   ├── Amsterdam
    │       │       │   ├── Andorra
    │       │       │   ├── Astrakhan
    │       │       │   ├── Athens
    │       │       │   ├── Belfast
    │       │       │   ├── Belgrade
    │       │       │   ├── Berlin
    │       │       │   ├── Bratislava
    │       │       │   ├── Brussels
    │       │       │   ├── Bucharest
    │       │       │   ├── Budapest
    │       │       │   ├── Busingen
    │       │       │   ├── Chisinau
    │       │       │   ├── Copenhagen
    │       │       │   ├── Dublin
    │       │       │   ├── Gibraltar
    │       │       │   ├── Guernsey
    │       │       │   ├── Helsinki
    │       │       │   ├── Isle_of_Man
    │       │       │   ├── Istanbul
    │       │       │   ├── Jersey
    │       │       │   ├── Kaliningrad
    │       │       │   ├── Kiev
    │       │       │   ├── Kirov
    │       │       │   ├── Kyiv
    │       │       │   ├── Lisbon
    │       │       │   ├── Ljubljana
    │       │       │   ├── London
    │       │       │   ├── Luxembourg
    │       │       │   ├── Madrid
    │       │       │   ├── Malta
    │       │       │   ├── Mariehamn
    │       │       │   ├── Minsk
    │       │       │   ├── Monaco
    │       │       │   ├── Moscow
    │       │       │   ├── Nicosia
    │       │       │   ├── Oslo
    │       │       │   ├── Paris
    │       │       │   ├── Podgorica
    │       │       │   ├── Prague
    │       │       │   ├── Riga
    │       │       │   ├── Rome
    │       │       │   ├── Samara
    │       │       │   ├── San_Marino
    │       │       │   ├── Sarajevo
    │       │       │   ├── Saratov
    │       │       │   ├── Simferopol
    │       │       │   ├── Skopje
    │       │       │   ├── Sofia
    │       │       │   ├── Stockholm
    │       │       │   ├── Tallinn
    │       │       │   ├── Tirane
    │       │       │   ├── Tiraspol
    │       │       │   ├── Ulyanovsk
    │       │       │   ├── Uzhgorod
    │       │       │   ├── Vaduz
    │       │       │   ├── Vatican
    │       │       │   ├── Vienna
    │       │       │   ├── Vilnius
    │       │       │   ├── Volgograd
    │       │       │   ├── Warsaw
    │       │       │   ├── Zagreb
    │       │       │   ├── Zaporozhye
    │       │       │   └── Zurich
    │       │       ├── Factory
    │       │       ├── GB
    │       │       ├── GB-Eire
    │       │       ├── GMT
    │       │       ├── GMT+0
    │       │       ├── GMT-0
    │       │       ├── GMT0
    │       │       ├── Greenwich
    │       │       ├── HST
    │       │       ├── Hongkong
    │       │       ├── Iceland
    │       │       ├── Indian/
    │       │       │   ├── Antananarivo
    │       │       │   ├── Chagos
    │       │       │   ├── Christmas
    │       │       │   ├── Cocos
    │       │       │   ├── Comoro
    │       │       │   ├── Kerguelen
    │       │       │   ├── Mahe
    │       │       │   ├── Maldives
    │       │       │   ├── Mauritius
    │       │       │   ├── Mayotte
    │       │       │   └── Reunion
    │       │       ├── Iran
    │       │       ├── Israel
    │       │       ├── Jamaica
    │       │       ├── Japan
    │       │       ├── Kwajalein
    │       │       ├── Libya
    │       │       ├── MET
    │       │       ├── MST
    │       │       ├── MST7MDT
    │       │       ├── Mexico/
    │       │       │   ├── BajaNorte
    │       │       │   ├── BajaSur
    │       │       │   └── General
    │       │       ├── NZ
    │       │       ├── NZ-CHAT
    │       │       ├── Navajo
    │       │       ├── PRC
    │       │       ├── PST8PDT
    │       │       ├── Pacific/
    │       │       │   ├── Apia
    │       │       │   ├── Auckland
    │       │       │   ├── Bougainville
    │       │       │   ├── Chatham
    │       │       │   ├── Chuuk
    │       │       │   ├── Easter
    │       │       │   ├── Efate
    │       │       │   ├── Enderbury
    │       │       │   ├── Fakaofo
    │       │       │   ├── Fiji
    │       │       │   ├── Funafuti
    │       │       │   ├── Galapagos
    │       │       │   ├── Gambier
    │       │       │   ├── Guadalcanal
    │       │       │   ├── Guam
    │       │       │   ├── Honolulu
    │       │       │   ├── Johnston
    │       │       │   ├── Kanton
    │       │       │   ├── Kiritimati
    │       │       │   ├── Kosrae
    │       │       │   ├── Kwajalein
    │       │       │   ├── Majuro
    │       │       │   ├── Marquesas
    │       │       │   ├── Midway
    │       │       │   ├── Nauru
    │       │       │   ├── Niue
    │       │       │   ├── Norfolk
    │       │       │   ├── Noumea
    │       │       │   ├── Pago_Pago
    │       │       │   ├── Palau
    │       │       │   ├── Pitcairn
    │       │       │   ├── Pohnpei
    │       │       │   ├── Ponape
    │       │       │   ├── Port_Moresby
    │       │       │   ├── Rarotonga
    │       │       │   ├── Saipan
    │       │       │   ├── Samoa
    │       │       │   ├── Tahiti
    │       │       │   ├── Tarawa
    │       │       │   ├── Tongatapu
    │       │       │   ├── Truk
    │       │       │   ├── Wake
    │       │       │   ├── Wallis
    │       │       │   └── Yap
    │       │       ├── Poland
    │       │       ├── Portugal
    │       │       ├── ROC
    │       │       ├── ROK
    │       │       ├── Singapore
    │       │       ├── Turkey
    │       │       ├── UCT
    │       │       ├── US/
    │       │       │   ├── Alaska
    │       │       │   ├── Aleutian
    │       │       │   ├── Arizona
    │       │       │   ├── Central
    │       │       │   ├── East-Indiana
    │       │       │   ├── Eastern
    │       │       │   ├── Hawaii
    │       │       │   ├── Indiana-Starke
    │       │       │   ├── Michigan
    │       │       │   ├── Mountain
    │       │       │   ├── Pacific
    │       │       │   └── Samoa
    │       │       ├── UTC
    │       │       ├── Universal
    │       │       ├── W-SU
    │       │       ├── WET
    │       │       ├── Zulu
    │       │       ├── iso3166.tab
    │       │       ├── leapseconds
    │       │       ├── tzdata.zi
    │       │       ├── zone.tab
    │       │       └── zone1970.tab
    │       ├── setuptools-65.5.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── setuptools/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── _deprecation_warning.cpython-310.pyc
    │       │   │   ├── _entry_points.cpython-310.pyc
    │       │   │   ├── _imp.cpython-310.pyc
    │       │   │   ├── _importlib.cpython-310.pyc
    │       │   │   ├── _itertools.cpython-310.pyc
    │       │   │   ├── _path.cpython-310.pyc
    │       │   │   ├── _reqs.cpython-310.pyc
    │       │   │   ├── archive_util.cpython-310.pyc
    │       │   │   ├── build_meta.cpython-310.pyc
    │       │   │   ├── dep_util.cpython-310.pyc
    │       │   │   ├── depends.cpython-310.pyc
    │       │   │   ├── discovery.cpython-310.pyc
    │       │   │   ├── dist.cpython-310.pyc
    │       │   │   ├── errors.cpython-310.pyc
    │       │   │   ├── extension.cpython-310.pyc
    │       │   │   ├── glob.cpython-310.pyc
    │       │   │   ├── installer.cpython-310.pyc
    │       │   │   ├── launch.cpython-310.pyc
    │       │   │   ├── logging.cpython-310.pyc
    │       │   │   ├── monkey.cpython-310.pyc
    │       │   │   ├── msvc.cpython-310.pyc
    │       │   │   ├── namespaces.cpython-310.pyc
    │       │   │   ├── package_index.cpython-310.pyc
    │       │   │   ├── py34compat.cpython-310.pyc
    │       │   │   ├── sandbox.cpython-310.pyc
    │       │   │   ├── unicode_utils.cpython-310.pyc
    │       │   │   ├── version.cpython-310.pyc
    │       │   │   ├── wheel.cpython-310.pyc
    │       │   │   └── windows_support.cpython-310.pyc
    │       │   ├── _deprecation_warning.py
    │       │   ├── _distutils/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── _collections.cpython-310.pyc
    │       │   │   │   ├── _functools.cpython-310.pyc
    │       │   │   │   ├── _macos_compat.cpython-310.pyc
    │       │   │   │   ├── _msvccompiler.cpython-310.pyc
    │       │   │   │   ├── archive_util.cpython-310.pyc
    │       │   │   │   ├── bcppcompiler.cpython-310.pyc
    │       │   │   │   ├── ccompiler.cpython-310.pyc
    │       │   │   │   ├── cmd.cpython-310.pyc
    │       │   │   │   ├── config.cpython-310.pyc
    │       │   │   │   ├── core.cpython-310.pyc
    │       │   │   │   ├── cygwinccompiler.cpython-310.pyc
    │       │   │   │   ├── debug.cpython-310.pyc
    │       │   │   │   ├── dep_util.cpython-310.pyc
    │       │   │   │   ├── dir_util.cpython-310.pyc
    │       │   │   │   ├── dist.cpython-310.pyc
    │       │   │   │   ├── errors.cpython-310.pyc
    │       │   │   │   ├── extension.cpython-310.pyc
    │       │   │   │   ├── fancy_getopt.cpython-310.pyc
    │       │   │   │   ├── file_util.cpython-310.pyc
    │       │   │   │   ├── filelist.cpython-310.pyc
    │       │   │   │   ├── log.cpython-310.pyc
    │       │   │   │   ├── msvc9compiler.cpython-310.pyc
    │       │   │   │   ├── msvccompiler.cpython-310.pyc
    │       │   │   │   ├── py38compat.cpython-310.pyc
    │       │   │   │   ├── py39compat.cpython-310.pyc
    │       │   │   │   ├── spawn.cpython-310.pyc
    │       │   │   │   ├── sysconfig.cpython-310.pyc
    │       │   │   │   ├── text_file.cpython-310.pyc
    │       │   │   │   ├── unixccompiler.cpython-310.pyc
    │       │   │   │   ├── util.cpython-310.pyc
    │       │   │   │   ├── version.cpython-310.pyc
    │       │   │   │   └── versionpredicate.cpython-310.pyc
    │       │   │   ├── _collections.py
    │       │   │   ├── _functools.py
    │       │   │   ├── _macos_compat.py
    │       │   │   ├── _msvccompiler.py
    │       │   │   ├── archive_util.py
    │       │   │   ├── bcppcompiler.py
    │       │   │   ├── ccompiler.py
    │       │   │   ├── cmd.py
    │       │   │   ├── command/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _framework_compat.cpython-310.pyc
    │       │   │   │   │   ├── bdist.cpython-310.pyc
    │       │   │   │   │   ├── bdist_dumb.cpython-310.pyc
    │       │   │   │   │   ├── bdist_rpm.cpython-310.pyc
    │       │   │   │   │   ├── build.cpython-310.pyc
    │       │   │   │   │   ├── build_clib.cpython-310.pyc
    │       │   │   │   │   ├── build_ext.cpython-310.pyc
    │       │   │   │   │   ├── build_py.cpython-310.pyc
    │       │   │   │   │   ├── build_scripts.cpython-310.pyc
    │       │   │   │   │   ├── check.cpython-310.pyc
    │       │   │   │   │   ├── clean.cpython-310.pyc
    │       │   │   │   │   ├── config.cpython-310.pyc
    │       │   │   │   │   ├── install.cpython-310.pyc
    │       │   │   │   │   ├── install_data.cpython-310.pyc
    │       │   │   │   │   ├── install_egg_info.cpython-310.pyc
    │       │   │   │   │   ├── install_headers.cpython-310.pyc
    │       │   │   │   │   ├── install_lib.cpython-310.pyc
    │       │   │   │   │   ├── install_scripts.cpython-310.pyc
    │       │   │   │   │   ├── py37compat.cpython-310.pyc
    │       │   │   │   │   ├── register.cpython-310.pyc
    │       │   │   │   │   ├── sdist.cpython-310.pyc
    │       │   │   │   │   └── upload.cpython-310.pyc
    │       │   │   │   ├── _framework_compat.py
    │       │   │   │   ├── bdist.py
    │       │   │   │   ├── bdist_dumb.py
    │       │   │   │   ├── bdist_rpm.py
    │       │   │   │   ├── build.py
    │       │   │   │   ├── build_clib.py
    │       │   │   │   ├── build_ext.py
    │       │   │   │   ├── build_py.py
    │       │   │   │   ├── build_scripts.py
    │       │   │   │   ├── check.py
    │       │   │   │   ├── clean.py
    │       │   │   │   ├── config.py
    │       │   │   │   ├── install.py
    │       │   │   │   ├── install_data.py
    │       │   │   │   ├── install_egg_info.py
    │       │   │   │   ├── install_headers.py
    │       │   │   │   ├── install_lib.py
    │       │   │   │   ├── install_scripts.py
    │       │   │   │   ├── py37compat.py
    │       │   │   │   ├── register.py
    │       │   │   │   ├── sdist.py
    │       │   │   │   └── upload.py
    │       │   │   ├── config.py
    │       │   │   ├── core.py
    │       │   │   ├── cygwinccompiler.py
    │       │   │   ├── debug.py
    │       │   │   ├── dep_util.py
    │       │   │   ├── dir_util.py
    │       │   │   ├── dist.py
    │       │   │   ├── errors.py
    │       │   │   ├── extension.py
    │       │   │   ├── fancy_getopt.py
    │       │   │   ├── file_util.py
    │       │   │   ├── filelist.py
    │       │   │   ├── log.py
    │       │   │   ├── msvc9compiler.py
    │       │   │   ├── msvccompiler.py
    │       │   │   ├── py38compat.py
    │       │   │   ├── py39compat.py
    │       │   │   ├── spawn.py
    │       │   │   ├── sysconfig.py
    │       │   │   ├── text_file.py
    │       │   │   ├── unixccompiler.py
    │       │   │   ├── util.py
    │       │   │   ├── version.py
    │       │   │   └── versionpredicate.py
    │       │   ├── _entry_points.py
    │       │   ├── _imp.py
    │       │   ├── _importlib.py
    │       │   ├── _itertools.py
    │       │   ├── _path.py
    │       │   ├── _reqs.py
    │       │   ├── _vendor/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── ordered_set.cpython-310.pyc
    │       │   │   │   ├── typing_extensions.cpython-310.pyc
    │       │   │   │   └── zipp.cpython-310.pyc
    │       │   │   ├── importlib_metadata/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _adapters.cpython-310.pyc
    │       │   │   │   │   ├── _collections.cpython-310.pyc
    │       │   │   │   │   ├── _compat.cpython-310.pyc
    │       │   │   │   │   ├── _functools.cpython-310.pyc
    │       │   │   │   │   ├── _itertools.cpython-310.pyc
    │       │   │   │   │   ├── _meta.cpython-310.pyc
    │       │   │   │   │   └── _text.cpython-310.pyc
    │       │   │   │   ├── _adapters.py
    │       │   │   │   ├── _collections.py
    │       │   │   │   ├── _compat.py
    │       │   │   │   ├── _functools.py
    │       │   │   │   ├── _itertools.py
    │       │   │   │   ├── _meta.py
    │       │   │   │   └── _text.py
    │       │   │   ├── importlib_resources/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _adapters.cpython-310.pyc
    │       │   │   │   │   ├── _common.cpython-310.pyc
    │       │   │   │   │   ├── _compat.cpython-310.pyc
    │       │   │   │   │   ├── _itertools.cpython-310.pyc
    │       │   │   │   │   ├── _legacy.cpython-310.pyc
    │       │   │   │   │   ├── abc.cpython-310.pyc
    │       │   │   │   │   ├── readers.cpython-310.pyc
    │       │   │   │   │   └── simple.cpython-310.pyc
    │       │   │   │   ├── _adapters.py
    │       │   │   │   ├── _common.py
    │       │   │   │   ├── _compat.py
    │       │   │   │   ├── _itertools.py
    │       │   │   │   ├── _legacy.py
    │       │   │   │   ├── abc.py
    │       │   │   │   ├── readers.py
    │       │   │   │   └── simple.py
    │       │   │   ├── jaraco/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── context.cpython-310.pyc
    │       │   │   │   │   └── functools.cpython-310.pyc
    │       │   │   │   ├── context.py
    │       │   │   │   ├── functools.py
    │       │   │   │   └── text/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── __pycache__/
    │       │   │   │           └── __init__.cpython-310.pyc
    │       │   │   ├── more_itertools/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── more.cpython-310.pyc
    │       │   │   │   │   └── recipes.cpython-310.pyc
    │       │   │   │   ├── more.py
    │       │   │   │   └── recipes.py
    │       │   │   ├── ordered_set.py
    │       │   │   ├── packaging/
    │       │   │   │   ├── __about__.py
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __about__.cpython-310.pyc
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _manylinux.cpython-310.pyc
    │       │   │   │   │   ├── _musllinux.cpython-310.pyc
    │       │   │   │   │   ├── _structures.cpython-310.pyc
    │       │   │   │   │   ├── markers.cpython-310.pyc
    │       │   │   │   │   ├── requirements.cpython-310.pyc
    │       │   │   │   │   ├── specifiers.cpython-310.pyc
    │       │   │   │   │   ├── tags.cpython-310.pyc
    │       │   │   │   │   ├── utils.cpython-310.pyc
    │       │   │   │   │   └── version.cpython-310.pyc
    │       │   │   │   ├── _manylinux.py
    │       │   │   │   ├── _musllinux.py
    │       │   │   │   ├── _structures.py
    │       │   │   │   ├── markers.py
    │       │   │   │   ├── requirements.py
    │       │   │   │   ├── specifiers.py
    │       │   │   │   ├── tags.py
    │       │   │   │   ├── utils.py
    │       │   │   │   └── version.py
    │       │   │   ├── pyparsing/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── actions.cpython-310.pyc
    │       │   │   │   │   ├── common.cpython-310.pyc
    │       │   │   │   │   ├── core.cpython-310.pyc
    │       │   │   │   │   ├── exceptions.cpython-310.pyc
    │       │   │   │   │   ├── helpers.cpython-310.pyc
    │       │   │   │   │   ├── results.cpython-310.pyc
    │       │   │   │   │   ├── testing.cpython-310.pyc
    │       │   │   │   │   ├── unicode.cpython-310.pyc
    │       │   │   │   │   └── util.cpython-310.pyc
    │       │   │   │   ├── actions.py
    │       │   │   │   ├── common.py
    │       │   │   │   ├── core.py
    │       │   │   │   ├── diagram/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── __pycache__/
    │       │   │   │   │       └── __init__.cpython-310.pyc
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── helpers.py
    │       │   │   │   ├── results.py
    │       │   │   │   ├── testing.py
    │       │   │   │   ├── unicode.py
    │       │   │   │   └── util.py
    │       │   │   ├── tomli/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── _parser.cpython-310.pyc
    │       │   │   │   │   ├── _re.cpython-310.pyc
    │       │   │   │   │   └── _types.cpython-310.pyc
    │       │   │   │   ├── _parser.py
    │       │   │   │   ├── _re.py
    │       │   │   │   └── _types.py
    │       │   │   ├── typing_extensions.py
    │       │   │   └── zipp.py
    │       │   ├── archive_util.py
    │       │   ├── build_meta.py
    │       │   ├── cli-32.exe
    │       │   ├── cli-64.exe
    │       │   ├── cli-arm64.exe
    │       │   ├── cli.exe
    │       │   ├── command/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── alias.cpython-310.pyc
    │       │   │   │   ├── bdist_egg.cpython-310.pyc
    │       │   │   │   ├── bdist_rpm.cpython-310.pyc
    │       │   │   │   ├── build.cpython-310.pyc
    │       │   │   │   ├── build_clib.cpython-310.pyc
    │       │   │   │   ├── build_ext.cpython-310.pyc
    │       │   │   │   ├── build_py.cpython-310.pyc
    │       │   │   │   ├── develop.cpython-310.pyc
    │       │   │   │   ├── dist_info.cpython-310.pyc
    │       │   │   │   ├── easy_install.cpython-310.pyc
    │       │   │   │   ├── editable_wheel.cpython-310.pyc
    │       │   │   │   ├── egg_info.cpython-310.pyc
    │       │   │   │   ├── install.cpython-310.pyc
    │       │   │   │   ├── install_egg_info.cpython-310.pyc
    │       │   │   │   ├── install_lib.cpython-310.pyc
    │       │   │   │   ├── install_scripts.cpython-310.pyc
    │       │   │   │   ├── py36compat.cpython-310.pyc
    │       │   │   │   ├── register.cpython-310.pyc
    │       │   │   │   ├── rotate.cpython-310.pyc
    │       │   │   │   ├── saveopts.cpython-310.pyc
    │       │   │   │   ├── sdist.cpython-310.pyc
    │       │   │   │   ├── setopt.cpython-310.pyc
    │       │   │   │   ├── test.cpython-310.pyc
    │       │   │   │   ├── upload.cpython-310.pyc
    │       │   │   │   └── upload_docs.cpython-310.pyc
    │       │   │   ├── alias.py
    │       │   │   ├── bdist_egg.py
    │       │   │   ├── bdist_rpm.py
    │       │   │   ├── build.py
    │       │   │   ├── build_clib.py
    │       │   │   ├── build_ext.py
    │       │   │   ├── build_py.py
    │       │   │   ├── develop.py
    │       │   │   ├── dist_info.py
    │       │   │   ├── easy_install.py
    │       │   │   ├── editable_wheel.py
    │       │   │   ├── egg_info.py
    │       │   │   ├── install.py
    │       │   │   ├── install_egg_info.py
    │       │   │   ├── install_lib.py
    │       │   │   ├── install_scripts.py
    │       │   │   ├── launcher manifest.xml
    │       │   │   ├── py36compat.py
    │       │   │   ├── register.py
    │       │   │   ├── rotate.py
    │       │   │   ├── saveopts.py
    │       │   │   ├── sdist.py
    │       │   │   ├── setopt.py
    │       │   │   ├── test.py
    │       │   │   ├── upload.py
    │       │   │   └── upload_docs.py
    │       │   ├── config/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── _apply_pyprojecttoml.cpython-310.pyc
    │       │   │   │   ├── expand.cpython-310.pyc
    │       │   │   │   ├── pyprojecttoml.cpython-310.pyc
    │       │   │   │   └── setupcfg.cpython-310.pyc
    │       │   │   ├── _apply_pyprojecttoml.py
    │       │   │   ├── _validate_pyproject/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── __pycache__/
    │       │   │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   │   ├── error_reporting.cpython-310.pyc
    │       │   │   │   │   ├── extra_validations.cpython-310.pyc
    │       │   │   │   │   ├── fastjsonschema_exceptions.cpython-310.pyc
    │       │   │   │   │   ├── fastjsonschema_validations.cpython-310.pyc
    │       │   │   │   │   └── formats.cpython-310.pyc
    │       │   │   │   ├── error_reporting.py
    │       │   │   │   ├── extra_validations.py
    │       │   │   │   ├── fastjsonschema_exceptions.py
    │       │   │   │   ├── fastjsonschema_validations.py
    │       │   │   │   └── formats.py
    │       │   │   ├── expand.py
    │       │   │   ├── pyprojecttoml.py
    │       │   │   └── setupcfg.py
    │       │   ├── dep_util.py
    │       │   ├── depends.py
    │       │   ├── discovery.py
    │       │   ├── dist.py
    │       │   ├── errors.py
    │       │   ├── extension.py
    │       │   ├── extern/
    │       │   │   ├── __init__.py
    │       │   │   └── __pycache__/
    │       │   │       └── __init__.cpython-310.pyc
    │       │   ├── glob.py
    │       │   ├── gui-32.exe
    │       │   ├── gui-64.exe
    │       │   ├── gui-arm64.exe
    │       │   ├── gui.exe
    │       │   ├── installer.py
    │       │   ├── launch.py
    │       │   ├── logging.py
    │       │   ├── monkey.py
    │       │   ├── msvc.py
    │       │   ├── namespaces.py
    │       │   ├── package_index.py
    │       │   ├── py34compat.py
    │       │   ├── sandbox.py
    │       │   ├── script (dev).tmpl
    │       │   ├── script.tmpl
    │       │   ├── unicode_utils.py
    │       │   ├── version.py
    │       │   ├── wheel.py
    │       │   └── windows_support.py
    │       ├── six-1.16.0.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   └── top_level.txt
    │       ├── six.py
    │       ├── snowballstemmer-3.0.1.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   ├── licenses/
    │       │   │   └── COPYING
    │       │   └── top_level.txt
    │       ├── snowballstemmer/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── among.cpython-310.pyc
    │       │   │   ├── arabic_stemmer.cpython-310.pyc
    │       │   │   ├── armenian_stemmer.cpython-310.pyc
    │       │   │   ├── basestemmer.cpython-310.pyc
    │       │   │   ├── basque_stemmer.cpython-310.pyc
    │       │   │   ├── catalan_stemmer.cpython-310.pyc
    │       │   │   ├── danish_stemmer.cpython-310.pyc
    │       │   │   ├── dutch_porter_stemmer.cpython-310.pyc
    │       │   │   ├── dutch_stemmer.cpython-310.pyc
    │       │   │   ├── english_stemmer.cpython-310.pyc
    │       │   │   ├── esperanto_stemmer.cpython-310.pyc
    │       │   │   ├── estonian_stemmer.cpython-310.pyc
    │       │   │   ├── finnish_stemmer.cpython-310.pyc
    │       │   │   ├── french_stemmer.cpython-310.pyc
    │       │   │   ├── german_stemmer.cpython-310.pyc
    │       │   │   ├── greek_stemmer.cpython-310.pyc
    │       │   │   ├── hindi_stemmer.cpython-310.pyc
    │       │   │   ├── hungarian_stemmer.cpython-310.pyc
    │       │   │   ├── indonesian_stemmer.cpython-310.pyc
    │       │   │   ├── irish_stemmer.cpython-310.pyc
    │       │   │   ├── italian_stemmer.cpython-310.pyc
    │       │   │   ├── lithuanian_stemmer.cpython-310.pyc
    │       │   │   ├── nepali_stemmer.cpython-310.pyc
    │       │   │   ├── norwegian_stemmer.cpython-310.pyc
    │       │   │   ├── porter_stemmer.cpython-310.pyc
    │       │   │   ├── portuguese_stemmer.cpython-310.pyc
    │       │   │   ├── romanian_stemmer.cpython-310.pyc
    │       │   │   ├── russian_stemmer.cpython-310.pyc
    │       │   │   ├── serbian_stemmer.cpython-310.pyc
    │       │   │   ├── spanish_stemmer.cpython-310.pyc
    │       │   │   ├── swedish_stemmer.cpython-310.pyc
    │       │   │   ├── tamil_stemmer.cpython-310.pyc
    │       │   │   ├── turkish_stemmer.cpython-310.pyc
    │       │   │   └── yiddish_stemmer.cpython-310.pyc
    │       │   ├── among.py
    │       │   ├── arabic_stemmer.py
    │       │   ├── armenian_stemmer.py
    │       │   ├── basestemmer.py
    │       │   ├── basque_stemmer.py
    │       │   ├── catalan_stemmer.py
    │       │   ├── danish_stemmer.py
    │       │   ├── dutch_porter_stemmer.py
    │       │   ├── dutch_stemmer.py
    │       │   ├── english_stemmer.py
    │       │   ├── esperanto_stemmer.py
    │       │   ├── estonian_stemmer.py
    │       │   ├── finnish_stemmer.py
    │       │   ├── french_stemmer.py
    │       │   ├── german_stemmer.py
    │       │   ├── greek_stemmer.py
    │       │   ├── hindi_stemmer.py
    │       │   ├── hungarian_stemmer.py
    │       │   ├── indonesian_stemmer.py
    │       │   ├── irish_stemmer.py
    │       │   ├── italian_stemmer.py
    │       │   ├── lithuanian_stemmer.py
    │       │   ├── nepali_stemmer.py
    │       │   ├── norwegian_stemmer.py
    │       │   ├── porter_stemmer.py
    │       │   ├── portuguese_stemmer.py
    │       │   ├── romanian_stemmer.py
    │       │   ├── russian_stemmer.py
    │       │   ├── serbian_stemmer.py
    │       │   ├── spanish_stemmer.py
    │       │   ├── swedish_stemmer.py
    │       │   ├── tamil_stemmer.py
    │       │   ├── turkish_stemmer.py
    │       │   └── yiddish_stemmer.py
    │       ├── soupsieve-2.8.3.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── WHEEL
    │       │   └── licenses/
    │       │       └── LICENSE.md
    │       ├── soupsieve/
    │       │   ├── __init__.py
    │       │   ├── __meta__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── __meta__.cpython-310.pyc
    │       │   │   ├── css_match.cpython-310.pyc
    │       │   │   ├── css_parser.cpython-310.pyc
    │       │   │   ├── css_types.cpython-310.pyc
    │       │   │   ├── pretty.cpython-310.pyc
    │       │   │   └── util.cpython-310.pyc
    │       │   ├── css_match.py
    │       │   ├── css_parser.py
    │       │   ├── css_types.py
    │       │   ├── pretty.py
    │       │   ├── py.typed
    │       │   └── util.py
    │       ├── sqlparse-0.4.3.dist-info/
    │       │   ├── AUTHORS
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── sqlparse/
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── __main__.cpython-310.pyc
    │       │   │   ├── cli.cpython-310.pyc
    │       │   │   ├── compat.cpython-310.pyc
    │       │   │   ├── exceptions.cpython-310.pyc
    │       │   │   ├── formatter.cpython-310.pyc
    │       │   │   ├── keywords.cpython-310.pyc
    │       │   │   ├── lexer.cpython-310.pyc
    │       │   │   ├── sql.cpython-310.pyc
    │       │   │   ├── tokens.cpython-310.pyc
    │       │   │   └── utils.cpython-310.pyc
    │       │   ├── cli.py
    │       │   ├── compat.py
    │       │   ├── engine/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── filter_stack.cpython-310.pyc
    │       │   │   │   ├── grouping.cpython-310.pyc
    │       │   │   │   └── statement_splitter.cpython-310.pyc
    │       │   │   ├── filter_stack.py
    │       │   │   ├── grouping.py
    │       │   │   └── statement_splitter.py
    │       │   ├── exceptions.py
    │       │   ├── filters/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   ├── __init__.cpython-310.pyc
    │       │   │   │   ├── aligned_indent.cpython-310.pyc
    │       │   │   │   ├── others.cpython-310.pyc
    │       │   │   │   ├── output.cpython-310.pyc
    │       │   │   │   ├── reindent.cpython-310.pyc
    │       │   │   │   ├── right_margin.cpython-310.pyc
    │       │   │   │   └── tokens.cpython-310.pyc
    │       │   │   ├── aligned_indent.py
    │       │   │   ├── others.py
    │       │   │   ├── output.py
    │       │   │   ├── reindent.py
    │       │   │   ├── right_margin.py
    │       │   │   └── tokens.py
    │       │   ├── formatter.py
    │       │   ├── keywords.py
    │       │   ├── lexer.py
    │       │   ├── sql.py
    │       │   ├── tokens.py
    │       │   └── utils.py
    │       ├── tomli-2.0.1.dist-info/
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   └── WHEEL
    │       ├── tomli/
    │       │   ├── __init__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   ├── _parser.cpython-310.pyc
    │       │   │   ├── _re.cpython-310.pyc
    │       │   │   └── _types.cpython-310.pyc
    │       │   ├── _parser.py
    │       │   ├── _re.py
    │       │   ├── _types.py
    │       │   └── py.typed
    │       ├── yapf-0.32.0.dist-info/
    │       │   ├── AUTHORS
    │       │   ├── INSTALLER
    │       │   ├── LICENSE
    │       │   ├── METADATA
    │       │   ├── RECORD
    │       │   ├── REQUESTED
    │       │   ├── WHEEL
    │       │   ├── entry_points.txt
    │       │   └── top_level.txt
    │       ├── yapf/
    │       │   ├── __init__.py
    │       │   ├── __main__.py
    │       │   ├── __pycache__/
    │       │   │   ├── __init__.cpython-310.pyc
    │       │   │   └── __main__.cpython-310.pyc
    │       │   ├── third_party/
    │       │   │   ├── __init__.py
    │       │   │   ├── __pycache__/
    │       │   │   │   └── __init__.cpython-310.pyc
    │       │   │   └── yapf_diff/
    │       │   │       ├── __init__.py
    │       │   │       ├── __pycache__/
    │       │   │       │   ├── __init__.cpython-310.pyc
    │       │   │       │   └── yapf_diff.cpython-310.pyc
    │       │   │       └── yapf_diff.py
    │       │   └── yapflib/
    │       │       ├── __init__.py
    │       │       ├── __pycache__/
    │       │       │   ├── __init__.cpython-310.pyc
    │       │       │   ├── blank_line_calculator.cpython-310.pyc
    │       │       │   ├── comment_splicer.cpython-310.pyc
    │       │       │   ├── continuation_splicer.cpython-310.pyc
    │       │       │   ├── errors.cpython-310.pyc
    │       │       │   ├── file_resources.cpython-310.pyc
    │       │       │   ├── format_decision_state.cpython-310.pyc
    │       │       │   ├── format_token.cpython-310.pyc
    │       │       │   ├── identify_container.cpython-310.pyc
    │       │       │   ├── line_joiner.cpython-310.pyc
    │       │       │   ├── logical_line.cpython-310.pyc
    │       │       │   ├── object_state.cpython-310.pyc
    │       │       │   ├── py3compat.cpython-310.pyc
    │       │       │   ├── pytree_unwrapper.cpython-310.pyc
    │       │       │   ├── pytree_utils.cpython-310.pyc
    │       │       │   ├── pytree_visitor.cpython-310.pyc
    │       │       │   ├── reformatter.cpython-310.pyc
    │       │       │   ├── split_penalty.cpython-310.pyc
    │       │       │   ├── style.cpython-310.pyc
    │       │       │   ├── subtype_assigner.cpython-310.pyc
    │       │       │   ├── subtypes.cpython-310.pyc
    │       │       │   ├── verifier.cpython-310.pyc
    │       │       │   └── yapf_api.cpython-310.pyc
    │       │       ├── blank_line_calculator.py
    │       │       ├── comment_splicer.py
    │       │       ├── continuation_splicer.py
    │       │       ├── errors.py
    │       │       ├── file_resources.py
    │       │       ├── format_decision_state.py
    │       │       ├── format_token.py
    │       │       ├── identify_container.py
    │       │       ├── line_joiner.py
    │       │       ├── logical_line.py
    │       │       ├── object_state.py
    │       │       ├── py3compat.py
    │       │       ├── pytree_unwrapper.py
    │       │       ├── pytree_utils.py
    │       │       ├── pytree_visitor.py
    │       │       ├── reformatter.py
    │       │       ├── split_penalty.py
    │       │       ├── style.py
    │       │       ├── subtype_assigner.py
    │       │       ├── subtypes.py
    │       │       ├── verifier.py
    │       │       └── yapf_api.py
    │       └── yapftests/
    │           ├── __init__.py
    │           ├── __pycache__/
    │           │   ├── __init__.cpython-310.pyc
    │           │   ├── blank_line_calculator_test.cpython-310.pyc
    │           │   ├── comment_splicer_test.cpython-310.pyc
    │           │   ├── file_resources_test.cpython-310.pyc
    │           │   ├── format_decision_state_test.cpython-310.pyc
    │           │   ├── format_token_test.cpython-310.pyc
    │           │   ├── line_joiner_test.cpython-310.pyc
    │           │   ├── logical_line_test.cpython-310.pyc
    │           │   ├── main_test.cpython-310.pyc
    │           │   ├── pytree_unwrapper_test.cpython-310.pyc
    │           │   ├── pytree_utils_test.cpython-310.pyc
    │           │   ├── pytree_visitor_test.cpython-310.pyc
    │           │   ├── reformatter_basic_test.cpython-310.pyc
    │           │   ├── reformatter_buganizer_test.cpython-310.pyc
    │           │   ├── reformatter_facebook_test.cpython-310.pyc
    │           │   ├── reformatter_pep8_test.cpython-310.pyc
    │           │   ├── reformatter_python3_test.cpython-310.pyc
    │           │   ├── reformatter_style_config_test.cpython-310.pyc
    │           │   ├── reformatter_verify_test.cpython-310.pyc
    │           │   ├── split_penalty_test.cpython-310.pyc
    │           │   ├── style_test.cpython-310.pyc
    │           │   ├── subtype_assigner_test.cpython-310.pyc
    │           │   ├── utils.cpython-310.pyc
    │           │   ├── yapf_test.cpython-310.pyc
    │           │   └── yapf_test_helper.cpython-310.pyc
    │           ├── blank_line_calculator_test.py
    │           ├── comment_splicer_test.py
    │           ├── file_resources_test.py
    │           ├── format_decision_state_test.py
    │           ├── format_token_test.py
    │           ├── line_joiner_test.py
    │           ├── logical_line_test.py
    │           ├── main_test.py
    │           ├── pytree_unwrapper_test.py
    │           ├── pytree_utils_test.py
    │           ├── pytree_visitor_test.py
    │           ├── reformatter_basic_test.py
    │           ├── reformatter_buganizer_test.py
    │           ├── reformatter_facebook_test.py
    │           ├── reformatter_pep8_test.py
    │           ├── reformatter_python3_test.py
    │           ├── reformatter_style_config_test.py
    │           ├── reformatter_verify_test.py
    │           ├── split_penalty_test.py
    │           ├── style_test.py
    │           ├── subtype_assigner_test.py
    │           ├── utils.py
    │           ├── yapf_test.py
    │           └── yapf_test_helper.py
    ├── Scripts/
    │   ├── Activate.ps1
    │   ├── __pycache__/
    │   │   └── django-admin.cpython-310.pyc
    │   ├── activate
    │   ├── activate.bat
    │   ├── deactivate.bat
    │   ├── django-admin.exe
    │   ├── django-admin.py
    │   ├── faker.exe
    │   ├── flake8.exe
    │   ├── pip.exe
    │   ├── pip3.10.exe
    │   ├── pip3.exe
    │   ├── py.test.exe
    │   ├── pycodestyle.exe
    │   ├── pydocstyle.exe
    │   ├── pyflakes.exe
    │   ├── pytest.exe
    │   ├── python.exe
    │   ├── pythonw.exe
    │   ├── sqlformat.exe
    │   ├── yapf-diff.exe
    │   └── yapf.exe
    └── pyvenv.cfg# django_sprint4