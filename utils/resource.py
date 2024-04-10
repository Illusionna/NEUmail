'''
# System --> Windows & Python3.10.0
# File ----> resource.py
# Author --> Illusionna
# Create --> 2024/03/29 20:52:31
'''
# -*- Encoding: UTF-8 -*-


class RESOURCE:
    """生成静态资源类.
    """
    
    STANDARD_STATIC_HASH: dict = {
        "./static/config/assets/css/fontawesome-all.min.css": "24926431fdf5baff0c1929f104152a0726dedf19181876f04cfbc78c98ee318f",
        "./static/config/assets/css/main.css": "bdd6130d073d5bfdcd56d39aa21f40f04e258b90d44d6995a39a48c70e79c0a9",
        "./static/config/assets/css/noscript.css": "87ebc3db5a07e20232459d06935123811251d5e337cba62408f5aeda8c65dc23",
        "./static/config/assets/js/breakpoints.min.js": "309febcd6d6e0cf092201532215f03a6a9f30b30f26203272a4861d704e7cd52",
        "./static/config/assets/js/browser.min.js": "c4217feebdd357e8a952e0ffbaa02791e5323482b8e3d80b3f714b84b1664103",
        "./static/config/assets/js/jquery.min.js": "ff1523fb7389539c84c65aba19260648793bb4f5e29329d2ee8804bc37a3fe6e",
        "./static/config/assets/js/main.js": "a89606e33da93035f178da8275567837911f5af2ac02b2e44f909e848529c883",
        "./static/config/assets/sass/main.scss": "6235dde73484779654fb8126912dc3f9f91797cd62c1fec60b6252f9217d9143",
        "./static/config/assets/sass/noscript.scss": "82f6709b69f8b92e885826efc86b87165445ac0eec21d912e518908eed3399ef",
        "./static/config/assets/sass/base/_page.scss": "1f5b032ad89afd5208a08c7675afe0495bee1212778dc4fafc2019e53d1bfca4",
        "./static/config/assets/sass/base/_reset.scss": "cefe6e962cbb8c9cd633fc3ddb7b59dbce4dedc16404d552c706285d52aa3a94",
        "./static/config/assets/sass/base/_typography.scss": "03e2eae10b970904a3b53babc7824a9243e5a0894794fce6657ec12629a6d414",
        "./static/config/assets/sass/components/_actions.scss": "911dbea5c8bf29829c75211e6ee4c4ac20e12dbcda9452ce0e9b86fce02ffed8",
        "./static/config/assets/sass/components/_button.scss": "6cc35e7a7cdc6e96930acc6cc84017fdc13a94c5368f665aba8fe5788461eb88",
        "./static/config/assets/sass/components/_contact-icons.scss": "6f94c2f673d5d14b16a428ce39d112049b0718f1e7e03f36228e75e01f2b962d",
        "./static/config/assets/sass/components/_form.scss": "316bbbf67b9f1ec16ae51c43193ceedea3d368b0ac774c1c8120a0de8fc4cf2c",
        "./static/config/assets/sass/components/_gallery.scss": "a15fc8718536f8054f4d2acffa5ffaa4239e5035765ded29cd3caadd0c1cbc8b",
        "./static/config/assets/sass/components/_grid-icons.scss": "f99abafc29917b8ded940d3af837d58aed5a1948006936c49385748a6ebee44a",
        "./static/config/assets/sass/components/_icon.scss": "57d57060e3934f1678df28908c09cd23accbc18278262adc3ad83b757e2094a5",
        "./static/config/assets/sass/components/_icons.scss": "8641423c63298059fb8a54ca250f37a1ff8a4a39d204313847d73a0a0418ceba",
        "./static/config/assets/sass/components/_image.scss": "1ae011080bfc650f37b653945335d0136a06113645a60451c0133a48e529926b",
        "./static/config/assets/sass/components/_list.scss": "79d3ebcc11b1cb337c7e1c6e58445fdb845775c2da7c9b30dc36b0e7ce539b51",
        "./static/config/assets/sass/components/_panel-banner.scss": "c35350f7f29c40e8f3cd99413bc2c3ac464f221243add094a41e6f30043ac934",
        "./static/config/assets/sass/components/_panel-spotlight.scss": "1d3b29e3458b3acedff6b14e606b4436ffe77940c22955563ac22c4096c0ac6c",
        "./static/config/assets/sass/components/_panel.scss": "37ab60c1880ec36ad9c58871bf221e8df53f4d16d9ceb18ec33c319b2bac2faa",
        "./static/config/assets/sass/components/_table.scss": "a0a1df6a39c11b8330a03b9d231e72f3a970a89f6e123c86a8be8650e3e4100e",
        "./static/config/assets/sass/layout/_page-wrapper.scss": "eac8fd6ca882d0815a7fea31308b802cb12f1065b6b10e1e1a3f138e26886070",
        "./static/config/assets/sass/layout/_wrapper.scss": "5a84eb728ae2324f929f2a2dea39657e4089c02eaabee55ca672378563c416ac",
        "./static/config/assets/sass/libs/_breakpoints.scss": "acda021bb809760083b40a54e76454bc58a56a2ec90965ea5a6820e2fb67f286",
        "./static/config/assets/sass/libs/_functions.scss": "fc832d9ccc89117bb05beed1e5fb328e7f909845d2220a1060375142f51b7e5d",
        "./static/config/assets/sass/libs/_mixins.scss": "63a02894ddc14717b0d58982ba6220f58bf20c3b9fdfc58f70a282168cb35c85",
        "./static/config/assets/sass/libs/_vars.scss": "f903f560734d0385ae74d6b842669ff36306435d3e96fbfab302ed6955aa5cec",
        "./static/config/assets/sass/libs/_vendor.scss": "f081f8ff029549e642a7ff5a615752e1e9032258b635abcef39f59e747d39d12",
        "./static/config/assets/webfonts/fa-brands-400.eot": "e4299464e7b012968eed63ac2db1c9509f56bca409ef9f71f2926a8c3c80b2a9",
        "./static/config/assets/webfonts/fa-brands-400.svg": "a3b9817780214caf01e8aec20bcdc2305a1ff34a15fae81ecd0923df9cd5cd0a",
        "./static/config/assets/webfonts/fa-brands-400.ttf": "cda59d6efffa685830fd95b55f64ae9cb51279cd34b2410b69f84c7ec30157d9",
        "./static/config/assets/webfonts/fa-brands-400.woff": "f9217f66874b0c01cd8c10b6a295dbc4f609acb6f5adc41c37da46641b57eb02",
        "./static/config/assets/webfonts/fa-brands-400.woff2": "8ea8791754915a898a3100e63e32978a6d1763be6df8e73a39d3a90d691cdeef",
        "./static/config/assets/webfonts/fa-regular-400.eot": "79d088064beb3826054fb88165416235897a856ca952fca1498b1c59b16aaa48",
        "./static/config/assets/webfonts/fa-regular-400.svg": "be0a084962d8066884f7fe9bd27ec16e51f5a93b72a502c92c5a24dc87eb2ebc",
        "./static/config/assets/webfonts/fa-regular-400.ttf": "e8711bbb871afd8e9dea60e16d30f00c7e4837bbc9807065017475b849fa2313",
        "./static/config/assets/webfonts/fa-regular-400.woff": "cb9e9e693192413cde2b1f21c1dc1d44b6fe7b27cc2b458e8b359d18f9ff8f4e",
        "./static/config/assets/webfonts/fa-regular-400.woff2": "e42a88444448ac3d60549cc7c1ff2c8a9cac721034c073d80a14a44e79730cca",
        "./static/config/assets/webfonts/fa-solid-900.eot": "373c04fd2418f5c77eea49d514731058f1907a94ff3b4e5d7c3e5767e8b53d8b",
        "./static/config/assets/webfonts/fa-solid-900.svg": "9674eb1bd5504717903837093a67668ea88f2ed006d91367d0d4b7aa1f9211fc",
        "./static/config/assets/webfonts/fa-solid-900.ttf": "af6397503fcefbd613976c21ad5c1e37298c18bbe07d096db03ccd3af6e05ba8",
        "./static/config/assets/webfonts/fa-solid-900.woff": "3f6d3488cf65374f6f676c315340b0ac2be832bd55240c809448e36ef9b96326",
        "./static/config/assets/webfonts/fa-solid-900.woff2": "9834b82ad26e2a37583d22676a12dd2eb0fe7c80356a2114d0db1aa8b3899537",
        "./static/config/images/background.jpg": "19c57c4cf669713d59527a9744bcc0302ee7db0f72b767634abb28eb7e7360f6",
        "./static/config/images/config.jpg": "95b7f17a751975f51d749d47009918af337807a3a5994c4db30378f742efad40",
        "./static/config/images/logPlane.jpg": "f77eef5351eb7128843c9385461112f2063996a7df002b2bf6d6332c485efca5",
        "./static/config/images/overlay.png": "4c428513c7cdbea61bb9ee507df06436c3b8a0e2721a2016f45b5eee8c71924a",
        "./static/download/assets/css/fontawesome-all.min.css": "24926431fdf5baff0c1929f104152a0726dedf19181876f04cfbc78c98ee318f",
        "./static/download/assets/css/main.css": "2941dfa9497db376589f25c0699b1db0c5f78a3fb0b9f2a3c697d91d7e3d7d56",
        "./static/download/assets/css/noscript.css": "f22765cc7959f7052b0290a7fd8b5f23188c1689c69ca373990c2402821e565b",
        "./static/download/assets/css/images/overlay.png": "0d8bb43605a20138d45cbdb530fc70355d26748fd8ebd6bfe121463139b5523d",
        "./static/download/assets/js/breakpoints.min.js": "309febcd6d6e0cf092201532215f03a6a9f30b30f26203272a4861d704e7cd52",
        "./static/download/assets/js/browser.min.js": "c4217feebdd357e8a952e0ffbaa02791e5323482b8e3d80b3f714b84b1664103",
        "./static/download/assets/js/jquery.min.js": "ff1523fb7389539c84c65aba19260648793bb4f5e29329d2ee8804bc37a3fe6e",
        "./static/download/assets/js/jquery.scrollex.min.js": "fc25b75fb3fc8b42756413be387e0d7a602813125283d2384551961d73ea784e",
        "./static/download/assets/js/jquery.scrolly.min.js": "8b6571ea2c3631ff50bb4b96e7f9081c6e33ebaadef9cb2ca5955d5e0b625a02",
        "./static/download/assets/js/main.js": "a05ce2241de6131d25627c8491632b55155c90a71b62640a9a85bcabf786e1bf",
        "./static/download/assets/js/util.js": "c2e1e72b0de356f6ce184e3af4fa8ab6590a2581162905a27d77886b2d960e00",
        "./static/download/assets/sass/main.scss": "ece932ad4df9a665f203e040b568ffd64a2a05c890a0b562423919064eba2feb",
        "./static/download/assets/sass/noscript.scss": "a7b5cce37e3c37125f022800a4c5b402455a376f5c159e836e9a8311b3aabff6",
        "./static/download/assets/sass/base/_page.scss": "a635fcf785cfecb4fbc06d43286f057d83c293bb341b7380cba1ffabb9478127",
        "./static/download/assets/sass/base/_reset.scss": "245a821f12108ad42428f81ae0c0f4b10364734157102855e10f774a66d22516",
        "./static/download/assets/sass/base/_typography.scss": "3e54c9a2b2f544fe2f34d642e9f185f356d6ecd05492d3b2eb86f46b31a97281",
        "./static/download/assets/sass/components/_actions.scss": "0e3c6d973dd50023bb1716fab88a5e9c28b37a9bd35f0834aa703faa99a6ee5e",
        "./static/download/assets/sass/components/_box.scss": "71f7242e0959dcca87d418b6bfa6e8044fb2f2f47973234ccda5def8ac26cf51",
        "./static/download/assets/sass/components/_button.scss": "94b6e64a8f3196053ff235dcb51efd62759cffcedbddecca5db96557948a0fa8",
        "./static/download/assets/sass/components/_features.scss": "9edf9209b9397bf15f5fe59b76561512c5f5ab92a8a5443bf201241c0b1d906b",
        "./static/download/assets/sass/components/_form.scss": "0022b45480c3785951df42f62ad2a4c9d4f88f3258df36d23534e5313ec1fc09",
        "./static/download/assets/sass/components/_icon.scss": "8b254259b371b2c2dc7b857fcbfdcc4ef831b43bbd3a0e56e5e3048c9b7a62d3",
        "./static/download/assets/sass/components/_icons.scss": "f0f4fbc349abf5952d274796888f1024a741e0bf5a0ce0bed4b0271451774a21",
        "./static/download/assets/sass/components/_image.scss": "e03b648ee9fb72cfb274ea4ca12d80f9bd2eeba67ed9e76caff1d81e4de784af",
        "./static/download/assets/sass/components/_list.scss": "09a46cc15081045f1bb619f9bf8a3932ea9d072e34667509e01c6815362ba095",
        "./static/download/assets/sass/components/_row.scss": "f551282eed17504d3fd42d97e807e692faa8b6cd46ec65fd356075f808f21415",
        "./static/download/assets/sass/components/_section.scss": "d9b952a89bee028e6ee5e60426c95be220fac9db78a04338da35f97434165956",
        "./static/download/assets/sass/components/_spotlight.scss": "1191099a83336af858e5b5c8e460635c84aa76529e91a4ce0fe1663d4addd0b1",
        "./static/download/assets/sass/components/_statistics.scss": "716d8ef0fad00d8616f083f8376a2c6f503fe390c662244302bea35afc24364b",
        "./static/download/assets/sass/components/_table.scss": "0d3bd0e2ccca281af66a2e931f457e1bec84f525d094d183dec9da132e874978",
        "./static/download/assets/sass/layout/_footer.scss": "2b41bfd15354d772ef5176026d39af370406534a3b761a622c7964bed0ab516d",
        "./static/download/assets/sass/layout/_header.scss": "4153ae44a187882b5f41869f2b7b69cc9387fe9b0a20a5e66f3c944a87b05bd1",
        "./static/download/assets/sass/layout/_main.scss": "0fdde2145fd0f27e94e6750510fd202ea4e824797bd5c5bb4629e0a3a25f2525",
        "./static/download/assets/sass/layout/_nav.scss": "0a3f54c59ff6334233227a7d044dfc9de1d1a564d3e7edd126e7fde3a3adb2b7",
        "./static/download/assets/sass/layout/_wrapper.scss": "f94800c0ed48d453bbb13895fec291afeeb6bf3e70ce498fea63fe1918512477",
        "./static/download/assets/sass/libs/_breakpoints.scss": "acda021bb809760083b40a54e76454bc58a56a2ec90965ea5a6820e2fb67f286",
        "./static/download/assets/sass/libs/_functions.scss": "fc832d9ccc89117bb05beed1e5fb328e7f909845d2220a1060375142f51b7e5d",
        "./static/download/assets/sass/libs/_html-grid.scss": "423fd36f530e34b329996d06b0db7c8543fc2034d0c12d479246fc0e498cc662",
        "./static/download/assets/sass/libs/_mixins.scss": "63a02894ddc14717b0d58982ba6220f58bf20c3b9fdfc58f70a282168cb35c85",
        "./static/download/assets/sass/libs/_vars.scss": "6ff7a91491153c2ff3189cdb3ec8ed3f07fa2aa7e588e5b220cb1ba14bce934b",
        "./static/download/assets/sass/libs/_vendor.scss": "f081f8ff029549e642a7ff5a615752e1e9032258b635abcef39f59e747d39d12",
        "./static/download/assets/webfonts/fa-brands-400.eot": "e4299464e7b012968eed63ac2db1c9509f56bca409ef9f71f2926a8c3c80b2a9",
        "./static/download/assets/webfonts/fa-brands-400.svg": "a3b9817780214caf01e8aec20bcdc2305a1ff34a15fae81ecd0923df9cd5cd0a",
        "./static/download/assets/webfonts/fa-brands-400.ttf": "cda59d6efffa685830fd95b55f64ae9cb51279cd34b2410b69f84c7ec30157d9",
        "./static/download/assets/webfonts/fa-brands-400.woff": "f9217f66874b0c01cd8c10b6a295dbc4f609acb6f5adc41c37da46641b57eb02",
        "./static/download/assets/webfonts/fa-brands-400.woff2": "8ea8791754915a898a3100e63e32978a6d1763be6df8e73a39d3a90d691cdeef",
        "./static/download/assets/webfonts/fa-regular-400.eot": "79d088064beb3826054fb88165416235897a856ca952fca1498b1c59b16aaa48",
        "./static/download/assets/webfonts/fa-regular-400.svg": "be0a084962d8066884f7fe9bd27ec16e51f5a93b72a502c92c5a24dc87eb2ebc",
        "./static/download/assets/webfonts/fa-regular-400.ttf": "e8711bbb871afd8e9dea60e16d30f00c7e4837bbc9807065017475b849fa2313",
        "./static/download/assets/webfonts/fa-regular-400.woff": "cb9e9e693192413cde2b1f21c1dc1d44b6fe7b27cc2b458e8b359d18f9ff8f4e",
        "./static/download/assets/webfonts/fa-regular-400.woff2": "e42a88444448ac3d60549cc7c1ff2c8a9cac721034c073d80a14a44e79730cca",
        "./static/download/assets/webfonts/fa-solid-900.eot": "373c04fd2418f5c77eea49d514731058f1907a94ff3b4e5d7c3e5767e8b53d8b",
        "./static/download/assets/webfonts/fa-solid-900.svg": "9674eb1bd5504717903837093a67668ea88f2ed006d91367d0d4b7aa1f9211fc",
        "./static/download/assets/webfonts/fa-solid-900.ttf": "af6397503fcefbd613976c21ad5c1e37298c18bbe07d096db03ccd3af6e05ba8",
        "./static/download/assets/webfonts/fa-solid-900.woff": "3f6d3488cf65374f6f676c315340b0ac2be832bd55240c809448e36ef9b96326",
        "./static/download/assets/webfonts/fa-solid-900.woff2": "9834b82ad26e2a37583d22676a12dd2eb0fe7c80356a2114d0db1aa8b3899537",
        "./static/download/images/demo.pdf": "74a7d628df5449b103bce1080cde568f961dfbf55c5af5a6432a7e8f2c3b2594",
        "./static/intro/css/bootstrap-icons.css": "4ffa6bea4304d2eda418683f56261685ed47bf00995039f27e5ad62d53938d2d",
        "./static/intro/css/bootstrap.min.css": "520478e1b0ea1cc5711e26ae400313d54a90fb25f307114f5ae6db25c84d4f2a",
        "./static/intro/css/daterangepicker.css": "abc74bc35a6ad6e383b7e7964017547bb6a3518d3f2e6bde3c506bea59e58472",
        "./static/intro/css/style.css": "ff4072306e1894ff010db0c7edfec64479d43820b6345b6d88192d54e3555980",
        "./static/intro/css/fonts/bootstrap-icons.woff": "bb1de989b83970f6f4e54de1cd974c5cba55b73582da5e1b225a6d0edf029483",
        "./static/intro/css/fonts/bootstrap-icons.woff2": "476adf42b40325098fcfa8b36ab3e769186bb4f6ce6a249753e2e1a9c22bf99e",
        "./static/intro/images/background.jpg": "19c57c4cf669713d59527a9744bcc0302ee7db0f72b767634abb28eb7e7360f6",
        "./static/intro/images/black.jpg": "031b1db5965486cd0e2ffdd66a1892f4537df0b8f8b9ebcb984f1622e4d99f5e",
        "./static/intro/images/fig1.jpg": "9eb2d38b3c97e800ffcab2a158d3eb229539de59d4e034c1952b751cfd14a9d4",
        "./static/intro/images/fig2.jpg": "fe14e433321ec6ceb646c6b252d6ab7e80de7db27b01e5cd6ae99d520e8be206",
        "./static/intro/images/fig3.jpg": "79aee492fe95820fb17dcfdb37d7eb15d215e0980505707347de3997f1378716",
        "./static/intro/images/green.jpg": "62bcc0eb0c2e30097abc3cb9fd34c9bea13b2d06db6e1ae063675634773dc343",
        "./static/intro/images/logPlane.jpg": "f77eef5351eb7128843c9385461112f2063996a7df002b2bf6d6332c485efca5",
        "./static/intro/images/overlay.png": "4c428513c7cdbea61bb9ee507df06436c3b8a0e2721a2016f45b5eee8c71924a",
        "./static/intro/images/R-C.gif": "3b4006921f4c818c266d0ee8d85013e60d9da3d8b565454e7d38d2154282f84d",
        "./static/intro/js/bootstrap.min.js": "14e65cbf9d85a144653a645ac4fc269a35bbd44501bb2f8bcedf7401c7960611",
        "./static/intro/js/daterangepicker.min.js": "6a3c4c1257df1919d04742a72ab27a5ab49ccf98d10af21dced9df82a78c104f",
        "./static/intro/js/jquery-3.6.0.min.js": "4b1777fcc4d9a333dd31b8e383c0d7f8b1e293210d0bd303cc025941d49fe1f0",
        "./static/intro/js/moment.min.js": "fab7a39382e03e2dd73f859cf2c15e16f5a88b1183de03b4bcfde5dad9e62168",
        "./static/intro/js/script.js": "5028b5c86d40579f3a7a281a6686eb6f6adea0d99de4c4fc210a43e1fd306552",
        "./static/intro/video/126.mp4": "7e7900b433e56ffd16de9867ec61be867f4b37ba67716d27757da5ae3877110f",
        "./static/intro/video/163.mp4": "7ad9bbb500021f65a049f723aa4c0f0aca21e009a200e41c12fb466c928caf15",
        "./static/intro/video/qq.mp4": "1dc7594150218965519035af2238ea2095245c86707e6be2c77e7dd7d3b7eb44"
    }
    
    INTRO: str = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>汤汁讯邮</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='intro/css/bootstrap.min.css') }}">
    <!-- 引入bootstrap-icons的CSS，做小问号 -->
    <link rel="stylesheet" href="{{ url_for('static', filename='intro/css/bootstrap-icons.css') }}">
    <!-- 引入daterangepicker的CSS -->
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='intro/css/daterangepicker.css') }}" />
    <link rel="stylesheet" href="{{ url_for('static', filename='intro/css/style.css') }}">
</head>
<body>

<div class="modal-container">
    <!-- 介绍模态框 -->
    <div class="modal-page" id="intro">
        <div class="modal-content">
            <h2>欢迎来到引导教程</h2>
            <button class="btn btn-primary next">开始</button>
        </div>
    </div>

    <!-- 邮箱输入模态框 -->
    <div class="modal-page" id="email">
        <div class="modal-content">
            <h2>请输入您的邮箱地址</h2>
            <input type="email" id="emailInput" class="form-control" placeholder="example@mail.com">
            <button class="btn btn-primary next">下一步</button>
        </div>
    </div>

    <!-- 信息介绍模态框 -->
    <div class="modal-page adjustable-size" id="info">
        <div class="modal-content">
            
        <h2>协议开通视频教程</h2>
        <h3 class="custom-margin">请根据下面的视频教程，填写协议、服务器信息和协议密码</h3>
        
            <!-- 输入框 -->
        <div class="input-group">
            
            <label for="protocolSelect">协议选择:</label>
            <select id="protocolSelect" class="custom-select">
                <option value="POP" selected>POP</option> <!-- 设置POP为默认选项 -->
                <option value="IMAP">IMAP</option>
            </select>
            <label for="protocolOutput">服务器地址:</label>
            <input type="text" id="protocolOutput" class="form-control" placeholder="自动生成，可填写">
            <label for="passwordInput">协议密码:</label>
            <input type="password" id="passwordInput" class="form-control" placeholder="请输入协议密码">
            
        </div>

        <div class="modal-footer">
            <button class="btn btn-secondary prev">上一步</button>
            <button class="btn btn-primary next btn-small">下一步</button>
        </div>

        <p>下面只有QQ、126、163邮箱的教学视频，其他邮箱请参考，点击可全屏，部分浏览器支持画中画模式，方便边看边操作</p>

            <!-- 新增的视频容器开始 -->
            <div class="video-container">
                <div class="video-wrapper">
                    <h3>QQ邮箱设置指南</h3> <!-- 添加的小标题 -->
                    <video class="video" controls>
                        <source src="{{ url_for('static', filename='intro/video/qq.mp4') }}" controls></video>
                    </video>
                </div>

                <div class="video-wrapper">
                    <h3>126邮箱设置指南</h3> <!-- 添加的小标题 -->
                    <video class="video" controls>
                        <source src="{{ url_for('static', filename='intro/video/126.mp4') }}" controls></video>
                    </video>
                </div>

                <div class="video-wrapper">
                    <h3>163邮箱设置指南</h3> <!-- 添加的小标题 -->
                    <video class="video" controls>
                        <source src="{{ url_for('static', filename='intro/video/163.mp4') }}" controls></video>
                    </video>
                </div>
            </div>

        </div>
    </div>
    
    <!-- 信息输入模态框 -->
    <div class="modal-page" id="additional-info">
        <div class="modal-content">
            <h2>请输入附加信息</h2>
            <!-- 输入框组开始 -->
            <div class="info-inputs">

                <div class="input-group mb-3" >
                    <label class="input-label" for="emailAttachmentPath">附件保存路径:</label>
                    <input type="text" id="emailAttachmentPath" class="form-control" placeholder="选填，例如：C:/Users/Osrrceoy/Desktop/Attachment">
                    <div class="input-group-append">
                        <span class="input-group-text info-icon" data-info="路径填写说明">
                            <i class="bi bi-question-circle-fill"></i>
                            <span class="tooltip-text">默认保存到桌面Attachment文件夹</span>
                        </span> 
                    </div>
                </div>

                <div class="input-group mb-3">
                    <label class="input-label" for="topEmailCount">顶部邮件数量:</label>
                    <input type="number" id="topEmailCount" class="form-control" placeholder="请输入顶部邮件数量" value="1000000" min="0">
                    <div class="input-group-append">
                        <span class="input-group-text info-icon" data-info="邮件数量填写说明">
                            <i class="bi bi-question-circle-fill"></i>
                            <span class="tooltip-text">默认一个大数表示收取所有附件</span>
                        </span> 
                    </div>
                    
                    <label class="input-label custom-margin-left" for="attachmentOverwrite">附件是否覆盖:</label>
                    <select class="custom-select" id="attachmentOverwrite">
                        <option value="true">True</option>
                        <option value="false" selected>False</option>
                    </select>
                    <div class="input-group-append">
                        <span class="input-group-text info-icon" data-info="覆盖填写说明">
                            <i class="bi bi-question-circle-fill"></i>
                            <span class="tooltip-text">若选择是则收取同名文件的最新版，否则不覆盖</span>
                        </span>  
                    </div>

                    
                </div>

                <div class="input-group mb-3">
                    <label class="input-label" for="attachmentSaveMode">附件保存模式:</label>
                    <select class="custom-select" id="attachmentSaveMode">
                        <option value="所有附件一个文件夹" selected>所有附件一个文件夹</option>
                        <option value="每个主题一个文件夹">每个主题一个文件夹</option>
                        <option value="每个邮箱一个文件夹">每个邮箱一个文件夹</option>
                        <option value="每个昵称一个文件夹">每个昵称一个文件夹</option>
                        <option value="每个主题多个邮箱一个文件夹">每个主题多个邮箱一个文件夹</option>
                    </select>
                    <div class="input-group-append">
                        <span class="input-group-text info-icon" data-info="保存形式填写说明">
                            <i class="bi bi-question-circle-fill"></i>
                            <span class="tooltip-text">选择附件保存到文件夹的形式</span>
                        </span> 
                    </div>
                    
                    <label class="input-label" for="timezoneSelect">时区选择:</label>
                    <select class="custom-select" id="timezoneSelect">
                        <option value="GMT-12">GMT-12</option>
                        <option value="GMT-11">GMT-11</option>
                        <option value="GMT-10">GMT-10</option>
                        <option value="GMT-9">GMT-9</option>
                        <option value="GMT-8">GMT-8</option>
                        <option value="GMT-7">GMT-7</option>
                        <option value="GMT-6">GMT-6</option>
                        <option value="GMT-5">GMT-5</option>
                        <option value="GMT-4">GMT-4</option>
                        <option value="GMT-3">GMT-3</option>
                        <option value="GMT-2">GMT-2</option>
                        <option value="GMT-1">GMT-1</option>
                        <option value="GMT+1">GMT+1</option>
                        <option value="GMT+2">GMT+2</option>
                        <option value="GMT+3">GMT+3</option>
                        <option value="GMT+4">GMT+4</option>
                        <option value="GMT+5">GMT+5</option>
                        <option value="GMT+6">GMT+6</option>
                        <option value="GMT+7">GMT+7</option>
                        <option value="GMT+8" selected>GMT+8</option>
                        <option value="GMT+9">GMT+9</option>
                        <option value="GMT+10">GMT+10</option>
                        <option value="GMT+11">GMT+11</option>
                        <option value="GMT+12">GMT+12</option>
                    </select>
                    <div class="input-group-append">
                        <span class="input-group-text info-icon" data-info="时区填写说明">
                            <i class="bi bi-question-circle-fill"></i>
                            <span class="tooltip-text">默认为北京时间（东八区）</span>
                        </span>  
                    </div>


                </div>

                <div class="input-group mb-3">
                    <div class="input-group mb-3">
                        <label class="input-label" >附件收取时间:</label>
                        <input type="text" id="startTime" class="form-control" placeholder="开始时间，选填" readonly>
                        <span class="mx-2">-</span>
                        <input type="text" id="endTime" class="form-control" placeholder="结束时间，选填" readonly>
                        <div class="input-group-append">
                            <span class="input-group-text info-icon" data-info="收取时间填写说明">
                                <i class="bi bi-question-circle-fill"></i>
                                <span class="tooltip-text">若不填则代表收取时间无限延伸</span>
                            </span> 
                        </div>
                    </div>
                </div>

                <div class="input-group mb-3">
                    <label class="input-label" for="filterEmail">过滤邮箱:</label>
                    <input type="text" id="filterEmail" class="form-control" placeholder="选填，若有多项则用&nbsp;||&nbsp;隔开">
                    <div class="input-group-append">
                        <span class="input-group-text info-icon" data-info="过滤邮箱填写说明">
                            <i class="bi bi-question-circle-fill"></i>
                            <span class="tooltip-text">发件邮箱黑名单</span>
                        </span> 
                    </div>
                </div>

                <div class="input-group mb-3">
                    <label class="input-label" for="filterNickname">过滤昵称:</label>
                    <input type="text" id="filterNickname" class="form-control" placeholder="选填，若有多项则用&nbsp;||&nbsp;隔开">
                    <div class="input-group-append">
                        <span class="input-group-text info-icon" data-info="过滤昵称填写说明">
                            <i class="bi bi-question-circle-fill"></i>
                            <span class="tooltip-text">发件昵称黑名单</span>
                        </span> 
                    </div>
                </div>

                <div class="input-group mb-3">
                    <label class="input-label" for="filterSubject">过滤主题:</label>
                    <input type="text" id="filterSubject" class="form-control" placeholder="选填，若有多项则用&nbsp;||&nbsp;隔开">
                    <div class="input-group-append">
                        <span class="input-group-text info-icon" data-info="过滤主题填写说明">
                            <i class="bi bi-question-circle-fill"></i>
                            <span class="tooltip-text">邮件主题黑名单</span>
                        </span> 
                    </div>
                </div>

                <!-- 按钮部分 -->
                <div class="modal-footer">
                    <button class="btn btn-secondary prev">上一步</button>
                    <button class="btn btn-primary next btn-small">下一步</button>
                </div>
            </div>
        </div>
    </div>

    <!-- 完成模态框 -->
    <div class="modal-page" id="finish">
        <div class="modal-content">
            <h2>您已成功完成所有步骤！</h2>
            <p>点击完成以保存配置，而后请重启软件进入主界面</p>
            <div class="modal-footer">
                <button class="btn btn-secondary prev">上一步</button>
                <button class="btn btn-primary btn-small" id="finish-button">完成</button>
            </div>
        </div>
    </div>   

    <!-- 警告模态框 -->
    <div id="customModal" style="display:none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1050;">
        <div style="background: white; padding: 20px; border-radius: 5px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); min-width: 200px;">
            <p id="customModalMessage">这是一个消息</p>
            <button id="customModalClose" style="float: right;">确定</button>
        </div>
    </div>
    

</div>


<script src="{{ url_for('static', filename='intro/js/jquery-3.6.0.min.js') }}"></script>
<script src="{{ url_for('static', filename='intro/js/bootstrap.min.js') }}"></script>
<!-- 引入daterangepicker的JS -->
<script src="{{ url_for('static', filename='intro/js/moment.min.js') }}"></script>
<script src="{{ url_for('static', filename='intro/js/daterangepicker.min.js') }}"></script>
<script>
  $(function() {
    var locale = {
        //日历设计
        format: 'YYYY-MM-DD HH:mm:ss',
        applyLabel: "应用",
        cancelLabel: "清除",
        fromLabel: "从",
        toLabel: "到",
        customRangeLabel: "自定义",
        weekLabel: "周",
        daysOfWeek: ["日", "一", "二", "三", "四", "五", "六"],
        monthNames: ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"],
        firstDay: 1
    };

    var options = {
        autoUpdateInput: false, // 不自动填充初始值
        singleDatePicker: true, // 单个日期选择器
        showDropdowns: true, // 显示年月下拉选择
        timePicker: true, // 允许选择时间
        timePicker24Hour: true, // 24小时制
        timePickerSeconds: true, // 允许选择秒
        locale: locale, // 使用中文界面
        ranges: {
            '今天': [moment().startOf('day'), moment().endOf('day')],
            '昨天': [moment().subtract(1, 'days').startOf('day'), moment().subtract(1, 'days').endOf('day')],
            '过去7天': [moment().subtract(6, 'days').startOf('day'), moment().endOf('day')],
            '过去30天': [moment().subtract(29, 'days').startOf('day'), moment().endOf('day')],
            '这个月初': [moment().startOf('month'), moment().endOf('month')],
            '上个月初': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        }
    };

    $('#startTime').daterangepicker(options).on('apply.daterangepicker', function(ev, picker) {
        $(this).val(picker.startDate.format(locale.format));
    }).on('cancel.daterangepicker', function(ev, picker) {
        $(this).val('');
    });

    $('#endTime').daterangepicker(options).on('apply.daterangepicker', function(ev, picker) {
        $(this).val(picker.startDate.format(locale.format));
    }).on('cancel.daterangepicker', function(ev, picker) {
        $(this).val('');
    });
});

</script>
<script>
    //提示框换行函数
     function insertLineBreaks(selector, everyNChars) {
        const elements = document.querySelectorAll(selector);
        elements.forEach(element => {
            let originalText = element.innerText;
            let newText = '';
            for (let i = 0; i < originalText.length; i += everyNChars) {
                let slice = originalText.slice(i, i + everyNChars);
                newText += slice + '\n'; // 使用换行符强制换行
            }
            element.innerText = newText;
        });
    }
    
    // 要在每7个字符后插入换行符
    insertLineBreaks('.tooltip-text', 7);
</script>
       
<script>
    // 显示模态对话框的函数
    function showGlobalAlert(message) {
        document.getElementById('customModalMessage').textContent = message;
        document.getElementById('customModal').style.display = 'block';
    }

    // 当用户点击“确定”按钮时，隐藏模态对话框
    document.getElementById('customModalClose').addEventListener('click', function() {
        document.getElementById('customModal').style.display = 'none';
    });

</script>

<script src="{{ url_for('static', filename='intro/js/script.js') }}"></script>
</body>
</html>
"""

    CONFIG: str = r"""<!DOCTYPE HTML>
<html>
    <head>
        <title>Email Attachments Download</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="static/config/assets/css/main.css" />
		<noscript><link rel="stylesheet" href="static/config/assets/css/noscript.css" /></noscript>
        <style>
            .progress-div {
            width: 100%;
            background-color: #f0f0f0;
            border-radius: 5px;
            margin: 10px 0;
            }
            .progress-bar {
                width: 0;
                height: 18px;
                background: linear-gradient(to right, #FFC371, #FF5F6D);
                text-align: center;
                line-height: 20px;
                color: white;
                border-radius: 5px;
                transition: width 0.3s ease-in-out;
            }
        </style>
    </head>
    <body class="is-preload">
        <div id="page-wrapper">
            <div id="wrapper">
                <section class="panel banner right">
                    <div class="content color0 span-3-75">
                        <div class="inner columns divided">
                            <div class="span-3-25">
                                <form id="Go" method="post" action="http://localhost:8888/capture">
                                    <div class="fields"><div class="field half">
                                        <label for="email">邮箱地址</label>
                                        <input type="email" placeholder="例如: example@163.com" value="{{ emailAddress }}" name="email" id="email" />
                                    </div>
                                    <div class="field half">
                                        <label for="password">协议密码</label>
                                        <input type="password" name="password" id="password" placeholder="请输入协议密码" value="{{ protocolPassword }}" maxlength="120" />
                                    </div>
                                    <div class="field half">
                                        <label for="protocol">协议类型</label>
                                        <div class="select-wrapper">
                                            <select name="protocol" id="protocol">
                                                <option value="{{ protocol }}">{{ protocol }}</option>
                                                <option value="POP3">POP3</option>
                                                <option value="IMAP">IMAP</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="field half">
                                        <label for="server">服务器地址</label>
                                        <input type="text" placeholder="例如: pop.163.com" value="{{ serverAddress }}" name="server" id="server" />
                                    </div>
                                    <div class="field half">
                                        <label for="attachment">附件保存路径</label>
                                        <input type="text" name="attachment" id="attachment" placeholder="请输入附件保存目录" value="{{ attachmentSaveDirectory }}" />
                                    </div>
                                    <div class="field half">
                                        <label for="method">附件保存模式</label>
                                        <div class="select-wrapper">
                                            <select name="method" id="method">
                                                <option value="{{ attachmentSaveMode }}">{{ attachmentSaveMode }}</option>
                                                <option value="所有附件一个文件夹">所有附件一个文件夹</option>
                                                <option value="每个邮箱一个文件夹">每个邮箱一个文件夹</option>
                                                <option value="每个主题一个文件夹">每个主题一个文件夹</option>
                                                <option value="每个昵称一个文件夹">每个昵称一个文件夹</option>
                                                <option value="每个主题多个邮箱一个文件夹">每个主题多个邮箱一个文件夹</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="field half">
                                        <label for="headSeveralEmail">顶部邮件数量</label>
                                        <input type="text" name="headSeveralEmail" id="headSeveralEmail" value="{{ headSeveralEmail }}">
                                    </div>
                                    <div class="field half">
                                        <label for="overwrite">覆盖附件</label>
                                        <div class="select-wrapper">
                                            <select name="overwrite" id="overwrite">
                                                <option value={{ isOverwrite }}>{{ isOverwrite }}</option>
                                                <option value="0">False</option>
                                                <option value="1">True</option>
                                            </select>
                                        </div>
                                    </div></div>
                                    <ul class="actions">
                                        <li><button onclick="RedirectToAdvanced()" type="button" id="add">Advanced</button></li>
                                        <li></li><li></li><li></li><li></li><li></li><li></li>
                                        <li></li><li></li><li></li><li></li><li></li><li></li>
                                        <li></li><li></li><li></li><li></li><li></li><li></li>
                                        <li><button id="CUSTOM" class="button primary color1 circle icon solid fa-angle-right" type="submit" onclick="submit_query()">Go</button></li>
                                    </ul>
                                    <div class="progress-div">
	                                    <div class="progress">
	                                        <div class="progress-bar progress-bar-striped active" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="min-width: 2em; width: 2%;">0%
	                                         </div>
	                                    </div>
	                                </div>
                                </form>
                                {% if error %}
                                    <script>
                                        alert(
                                            "哎呀? 一不小心配置出现错误, 不灰心, 就要成功啦 (●'◡'●) 尝试检查.\n\n    1. 服务器地址类比以下四个:\n        pop.163.com        imap.neuq.edu.cn\n        pop.stu.neuq.edu.cn        imap.qq.com\n\n    2. 邮箱地址:\n        例如团队邮箱 zoliomarling@qq.com 发现规律了不?\n        @ 号后面的内容就是服务器地址的后缀 ~ o(*￣▽￣*)o\n        pop 更快更兼容, imap 更准更全面\n        只需要选择协议加上后缀就可以构成服务器地址嘞\n\n    3. 协议密钥:\n        授权口令并非登录邮箱的密码\n        参考视频教学文档: https://illusionna.vercel.app\n\n    4. 下载路径:\n        默认是自动在桌面创建附件文件夹\n        如果修改了目录, 请确保路径的正确性哟 (＾Ｕ＾)ノ~ＹＯ\n\n以上都不成功, 最后尝试重启程序, 不是关电脑哈. (●ˇ∀ˇ●)"
                                        );
                                        window.history.back();
                                    </script>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                <div class="image filtered span-1-75" data-position="25% 25%">
                    <img src="static/config/images/config.jpg" alt="(⊙﹏⊙) Oops ????" />
                </div>
                </section>
            </div>
        </div>
        <script src="static/config/assets/js/jquery.min.js"></script>
        <script src="static/config/assets/js/browser.min.js"></script>
        <script src="static/config/assets/js/breakpoints.min.js"></script>
        <script src="static/config/assets/js/main.js"></script>
    </body>

    <script>
        function RedirectToAdvanced() {
            window.open("{{ url_for('Advanced') }}", "_blank");
        }
    </script>

    <script>
        function submit_query(btn) {
            var timer = window.setInterval(() => {
                var prog_url = '/progress'
                $.getJSON(prog_url, function(num_progress){
                    if (num_progress.error){
                        window.clearInterval(timer);    // 如果异常, 则不向后端 GET /progress 请求.
                        return;
                    }
                    $('.progress-div').css('visibility', 'visible');
                    $('.progress-bar').css('width', num_progress.res + '%');
                    $('.progress-bar').css('background', 'linear-gradient(120deg, orange 20%, cyan)');
                    $('.progress-bar').css('text-align', 'center');
                    $('.progress-bar').text(num_progress.res + '%');
                });
            }, 500);   // 每 500ms 一次, 请求速度不能太快, 否则前端会一直转圈圈.
            

    /*// 当用户重新提交表单时清除计时器
    
    */
btn.addEventListener('click', function() {
        window.clearInterval(timer);
    });

            var this_url = '/capture'
            $.getJSON(this_url, function(res){
                cleanInterval(sitv);
                alert("/capture 被调用了.");
                if(res.res != null){
                    $('.progress-bar').css('width', '100%');
                    $('.progress-bar').text('100%');
                    setTimeout(function(){
                        alert('下载完成');
                    }, 100);
                }else{
                    $('.progress-bar').css('background', 'red');
                    setTimeout(function(){
                        alert('响应超时(不影响下载)');
                    }, 1);
                }
            });
        }
        </script>
</html>"""

    DOWNLOAD: str = r"""<!DOCTYPE HTML>
<html>
    <head>
		<title>Email Attachments Download</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="static/download/assets/css/main.css" />
		<noscript><link rel="stylesheet" href="static/download/assets/css/noscript.css" /></noscript>
	</head>
    
    <body class="is-preload">
        <div id="wrapper">
            <header id="header">
                <h1>下载报告</h1>
                <ul class="actions">
                    <li><a href="http://localhost:8888" class="button">Back</a></li>
                </ul>
            </header>

            <div id="main">
                <section id="content" class="main">
                    <span style="float: right;"><a href="http://localhost:8888/export" class="button icon solid fa-upload" onclick="ShowMessage('{{ exportDir }}')">导出 Excel</a></span>

                    <h2>总览概况</h2>
                    <p>
                        解析 {{parseNumber}} 份 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 累计新增 {{increaseNumber}} 份 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 筛选过滤 {{filterNumber}} 份 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 本地磁盘共 {{diskFilesNumber}} 份 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 附件父目录磁盘大小 {{spaceUsage}}
                    </p>
                    <p>
                        附件保存路径 {{attachmentSaveDirectory}}
                    </p>

                    <h2>附件日志</h2>
                    <div class="span-3">
                        <div class="table-wrapper">
                            <table>
                                <thead>
                                    <tr>
                                        <th>邮箱地址</th>
                                        <th>附件</th>
                                        <th>主题</th>
                                        <th>时间</th>
                                    </tr>
                                </thead>
                                <tbody>
                                {% for emailAddress, attachments, subject, date in products %}
                                    <tr>
                                        <td>{{emailAddress}}</td>
                                        <td>{{attachments}}</td>
                                        <td>{{subject}}</td>
                                        <td>{{date}}</td>
                                    </tr>
                                {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>
            </div>

            <footer id="footer">
                <section>
                    <ul class="actions">
                        <li><a href="#" class="button">Top</a></li>
                    </ul>
                </section>
            </footer>
        </div>

        <script>
            function ShowMessage(exportDir){
                alert('导出成功路径为: ' + exportDir);
            }
        </script>

        <script src="static/download/assets/js/jquery.min.js"></script>
        <script src="static/download/assets/js/jquery.scrollex.min.js"></script>
        <script src="static/download/assets/js/jquery.scrolly.min.js"></script>
        <script src="static/download/assets/js/browser.min.js"></script>
        <script src="static/download/assets/js/breakpoints.min.js"></script>
        <script src="static/download/assets/js/util.js"></script>
        <script src="static/download/assets/js/main.js"></script>

        <script>
            document.addEventListener('DOMContentLoaded', function(){
                const backButton = document.querySelector('.button.primary');
                backButton.addEventListener('click', function(event){
                    event.preventDefault();
                    history.back();
                });
            });
        </script>
    </body>
</html>"""

    ADVANCED: str = r"""<!DOCTYPE HTML>
<html>
    <head>
        <title>Email Attachments Download</title>
        <meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="static/download/assets/css/main.css" />
		<noscript><link rel="stylesheet" href="static/download/assets/css/noscript.css" /></noscript>
        <style>
            .container {
                display: flex;
                justify-content: space-around;
                margin-top: 20px;
            }
            .list-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-top: 10px;
            }
            li.selected {
                background-color: #D8D8D8;
            }
        </style>
    </head>

    <body class="is-preload">
        <div id="wrapper">
            <header id="header">
                <ul class="actions">
                    <li><button onclick="ShowMessage()" class="button icon solid fa-save" id="SaveButton" style="text-align: center;">保存</button><li>
                </ul>
            </header>

            <div id="main">
                <section id="content" class="main">
                    <section>
                        <div class="col-12">
                            <h3>GMT 格林威治标准时区</h3>
                            <h6></h6>
                            <select name="timeZone" id="timeZone">
                                <option value="{{ timeZone }}">{{ timeZone }}</option>
                                <option value="GMT+1">GMT+1</option>
                                <option value="GMT+2">GMT+2</option>
                                <option value="GMT+3">GMT+3</option>
                                <option value="GMT+4">GMT+4</option>
                                <option value="GMT+5">GMT+5</option>
                                <option value="GMT+6">GMT+6</option>
                                <option value="GMT+7">GMT+7</option>
                                <option value="GMT+8">GMT+8</option>
                                <option value="GMT+9">GMT+9</option>
                                <option value="GMT+10">GMT+10</option>
                                <option value="GMT+11">GMT+11</option>
                                <option value="GMT+12">GMT+12</option>
                                <option value="GMT-12">GMT-12</option>
                                <option value="GMT-11">GMT-11</option>
                                <option value="GMT-10">GMT-10</option>
                                <option value="GMT-9">GMT-9</option>
                                <option value="GMT-8">GMT-8</option>
                                <option value="GMT-7">GMT-7</option>
                                <option value="GMT-6">GMT-6</option>
                                <option value="GMT-5">GMT-5</option>
                                <option value="GMT-4">GMT-4</option>
                                <option value="GMT-3">GMT-3</option>
                                <option value="GMT-2">GMT-2</option>
                                <option value="GMT-1">GMT-1</option>
                            </select>
                        </div>
                        <h1></h1>
                        <h3>收取附件时间段</h3>
                        <div>
                            开始时间
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <input type="datetime-local" id="startTime" name="start-time" step="1" value="{{ startTime }}">
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            截止时间
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <input type="datetime-local" id="endTime" name="end-time" step="1" value="{{ terminalTime }}">
                        </div>
                        <h1></h1>
                        <h3>过滤屏蔽邮箱地址</h3>
                        <div class="list-container" style="cursor: pointer">
                            <input type="email" id="inputText1" placeholder="【增加】【删除】后记得保存哟" style="color: red; width: 300px; height: 50px;">
                            <div style="display: flex;">
                                <button onclick="AddItem(1)" style="margin-left: 0px;">增加</button>
                                <button onclick="RemoveItem(1)" style="margin-left: 10px;">点击删除</button>
                            </div>
                            <ul id="itemList1">
                                {% for email in filterEmailAddress %}
                                    <li>{{ email }}</li>
                                {% endfor %}
                            </ul>
                        </div>

                        <h1></h1>
                        <h3>过滤屏蔽邮件主题</h3>
                        <div class="list-container" style="cursor: pointer">
                            <input type="text" id="inputText2" placeholder="【增加】【删除】后记得保存哟" style="color: green; width: 300px; height: 50px;">
                            <div style="display: flex;">
                                <button onclick="AddItem(2)" style="margin-left: 0px;">增加</button>
                                <button onclick="RemoveItem(2)" style="margin-left: 10px;">点击删除</button>
                            </div>
                            <ul id="itemList2">
                                {% for subject in filterSubject %}
                                    <li>{{ subject }}</li>
                                {% endfor %}
                            </ul>
                        </div>

                        <h1></h1>
                        <h3>过滤屏蔽发件人昵称</h3>
                        <div class="list-container" style="cursor: pointer">
                            <input type="text" id="inputText3" placeholder="【增加】【删除】后记得保存哟" style="color: blue; width: 300px; height: 50px;">
                            <div style="display: flex;">
                                <button onclick="AddItem(3)" style="margin-left: 0px;">增加</button>
                                <button onclick="RemoveItem(3)" style="margin-left: 10px;">点击删除</button>
                            </div>
                            <ul id="itemList3">
                                {% for nickname in filterNickname %}
                                    <li>{{ nickname }}</li>
                                {% endfor %}
                            </ul>
                        </div>


                        {% if error %}
                            <script>
                                alert("配置出现异常, 请检查...\n \n参考文档: https://illusionna.vercel.app");
                                window.history.back();
                            </script>
                        {% endif %}
                    </section>
                </section>
            </div>

            <footer id="footer">
                <section>
                    <ul class="actions">
                        <li><a href="#" class="button">Top</a></li>
                    </ul>
                </section>
            </footer>
        </div>

        <script>
            function AddItem(listNum) {
                const inputText = document.getElementById('inputText' + listNum).value;
                if (inputText.trim() !== '') {
                    const itemList = document.getElementById('itemList' + listNum);
                    const li = document.createElement('li');
                    li.textContent = inputText;
                    itemList.appendChild(li);
                    document.getElementById('inputText' + listNum).value = '';
                }
            }

            function RemoveItem(listNum) {
                const itemList = document.getElementById('itemList' + listNum);
                const selectedItems = itemList.querySelectorAll('li.selected');

                selectedItems.forEach(item => {
                    itemList.removeChild(item);
                });
            }

            document.querySelectorAll('.list-container').forEach((container, index) => {
                container.addEventListener('click', function(e) {
                    const itemList = container.querySelector('ul');
                    const selectedItems = itemList.querySelectorAll('li.selected');
                    selectedItems.forEach(item => {
                        item.classList.remove('selected');
                    });

                    if (e.target.tagName === 'LI') {
                        e.target.classList.toggle('selected');
                    }
                });
            });
        </script>

        

        <script>
            function ShowMessage(){
                const startTime = document.getElementById("startTime").value;
                const endTime = document.getElementById("endTime").value;

                if (startTime && endTime) {
                    if (endTime < startTime){
                        
                    }
                    else{


                        var message = document.createElement('div');
              message.textContent = '保存成功';
              message.style.position = 'fixed';
              message.style.top = '50%';
              message.style.left = '50%';
              message.style.transform = 'translate(-50%, -50%)';
              message.style.background = '#4CAF50';
              message.style.color = '#fff';
              message.style.padding = '10px 20px';
              message.style.borderRadius = '5px';
              message.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
              message.style.transition = 'opacity 1s linear';
              document.body.appendChild(message);
              setTimeout(function() {
                message.style.opacity = 0;
                setTimeout(function() {
                  document.body.removeChild(message);
                }, 1000);
              }, 1000);


                    }
                }

            }
        </script>



        <script>
            document.getElementById("SaveButton").addEventListener("click", function() {
                const timeZone = document.getElementById("timeZone").value;
                const startTime = document.getElementById("startTime").value;
                const endTime = document.getElementById("endTime").value;

                const filterEmailAddressList = [];
                const filterEmailAddressItems = document.querySelectorAll('#itemList1 li');
                filterEmailAddressItems.forEach(item => {
                    filterEmailAddressList.push(item.textContent);
                });

                const filterSubjectList = [];
                const filterSubjectItems = document.querySelectorAll('#itemList2 li');
                filterSubjectItems.forEach(item => {
                    filterSubjectList.push(item.textContent);
                });

                const filterNicknameList = [];
                const filterNicknameItems = document.querySelectorAll('#itemList3 li');
                filterNicknameItems.forEach(item => {
                    filterNicknameList.push(item.textContent);
                });


                if (startTime && endTime) {
                    if (endTime < startTime) {
                        alert('结束时间不能早于开始时间，请重新选择时间范围！');
                    } else {
                        
                        const data = {
                            timeZone: timeZone,
                            startTime: startTime,
                            endTime: endTime,
                            filterEmailAddress: filterEmailAddressList,
                            filterSubject: filterSubjectList,
                            filterNickname: filterNicknameList
                        };
        
                        fetch('/save', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify(data),
                        })
                        .then(response => response.json())
                        .then(data => {
                            console.log('成功:', data);
        
                        })
                        .catch((error) => {
                            console.error('错误:', error);
        
                        });
                        
                    }
                } else {
                    
                    const data = {
                        timeZone: timeZone,
                        startTime: startTime,
                        endTime: endTime,
                        filterEmailAddress: filterEmailAddressList,
                        filterSubject: filterSubjectList,
                        filterNickname: filterNicknameList
                    };
    
                    fetch('/save', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(data),
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log('成功:', data);
    
                    })
                    .catch((error) => {
                        console.error('错误:', error);
    
                    });

                }
            });
        </script>



        <script src="static/download/assets/js/jquery.min.js"></script>
        <script src="static/download/assets/js/jquery.scrollex.min.js"></script>
        <script src="static/download/assets/js/jquery.scrolly.min.js"></script>
        <script src="static/download/assets/js/browser.min.js"></script>
        <script src="static/download/assets/js/breakpoints.min.js"></script>
        <script src="static/download/assets/js/util.js"></script>
        <script src="static/download/assets/js/main.js"></script>
    </body>
</html>"""

    ERROR: str = r"""<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>404</title>

    <style>
        html, body {
            height: 100%;
            min-height: 450px;
            font-size: 32px;
            font-weight: 500;
            color: #5d7399;
            margin: 0;
            padding: 0;
            border: 0;
        }

        .content {
            height: 100%;
            position: relative;
            z-index: 1;
            background-color: #d2e1ec;
            background-image: -webkit-linear-gradient(top, #bbcfe1 0%, #e8f2f6 80%);
            background-image: linear-gradient(to bottom, #bbcfe1 0%, #e8f2f6 80%);
            overflow: hidden;
        }

        .snow {
            position: absolute;
            top: 0;
            left: 0;
            pointer-events: none;
            z-index: 20;
        }

        .main-text {
            padding: 20vh 20px 0 20px;
            text-align: center;
            line-height: 2em;
            font-size: 5vh;
        }

        .main-text h1 {
            font-size: 45px;
            line-height: 48px;
            margin: 0;
            padding: 0;
        }

        .main-text-a {
            height: 32px;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
        }

        .main-text-a a {
            font-size: 16px;
            text-decoration: none;
            color: #0066CC;
        }

        .main-text-a a:hover {
            color: #000;
        }

        .home-link {
            font-size: 0.6em;
            font-weight: 400;
            color: inherit;
            text-decoration: none;
            opacity: 0.6;
            border-bottom: 1px dashed rgba(93, 115, 153, 0.5);
        }

        .home-link:hover {
            opacity: 1;
        }

        .ground {
            height: 160px;
            width: 100%;
            position: absolute;
            bottom: 0;
            left: 0;
            background: #f6f9fa;
            box-shadow: 0 0 10px 10px #f6f9fa;
        }

        .ground:before, .ground:after {
            content: '';
            display: block;
            width: 250px;
            height: 250px;
            position: absolute;
            top: -62.5px;
            z-index: -1;
            background: transparent;
            -webkit-transform: scaleX(0.2) rotate(45deg);
            transform: scaleX(0.2) rotate(45deg);
        }

        .ground:after {
            left: 50%;
            margin-left: -166.66667px;
            box-shadow: -340px 260px 15px #8193b2, -620px 580px 15px #8193b2, -900px 900px 15px #b0bccf, -1155px 1245px 15px #b4bed1, -1515px 1485px 15px #8193b2, -1755px 1845px 15px #8a9bb8, -2050px 2150px 15px #91a1bc, -2425px 2375px 15px #bac4d5, -2695px 2705px 15px #a1aec6, -3020px 2980px 15px #8193b2, -3315px 3285px 15px #94a3be, -3555px 3645px 15px #9aa9c2, -3910px 3890px 15px #b0bccf, -4180px 4220px 15px #bac4d5, -4535px 4465px 15px #a7b4c9, -4840px 4760px 15px #94a3be;
        }

        .ground:before {
            right: 50%;
            margin-right: -166.66667px;
            box-shadow: 325px -275px 15px #b4bed1, 620px -580px 15px #adb9cd, 925px -875px 15px #a1aec6, 1220px -1180px 15px #b7c1d3, 1545px -1455px 15px #7e90b0, 1795px -1805px 15px #b0bccf, 2080px -2120px 15px #b7c1d3, 2395px -2405px 15px #8e9eba, 2730px -2670px 15px #b7c1d3, 2995px -3005px 15px #9dabc4, 3285px -3315px 15px #a1aec6, 3620px -3580px 15px #8193b2, 3880px -3920px 15px #aab6cb, 4225px -4175px 15px #9dabc4, 4510px -4490px 15px #8e9eba, 4785px -4815px 15px #a7b4c9;
        }

        .mound {
            margin-top: -80px;
            font-weight: 800;
            font-size: 180px;
            text-align: center;
            color: #dd4040;
            pointer-events: none;
        }

        .mound:before {
            content: '';
            display: block;
            width: 600px;
            height: 200px;
            position: absolute;
            left: 50%;
            margin-left: -300px;
            top: 50px;
            z-index: 1;
            border-radius: 100%;
            background-color: #e8f2f6;
            background-image: -webkit-linear-gradient(top, #dee8f1, #f6f9fa 60px);
            background-image: linear-gradient(to bottom, #dee8f1, #f6f9fa 60px);
        }

        .mound:after {
            content: '';
            display: block;
            width: 28px;
            height: 6px;
            position: absolute;
            left: 50%;
            margin-left: -150px;
            top: 68px;
            z-index: 2;
            background: #dd4040;
            border-radius: 100%;
            -webkit-transform: rotate(-15deg);
            transform: rotate(-15deg);
            box-shadow: -56px 12px 0 1px #dd4040, -126px 6px 0 2px #dd4040, -196px 24px 0 3px #dd4040;
        }

        .mound_text {
            -webkit-transform: rotate(6deg);
            transform: rotate(6deg);
        }

        .mound_spade {
            display: block;
            width: 35px;
            height: 30px;
            position: absolute;
            right: 50%;
            top: 42%;
            margin-right: -250px;
            z-index: 0;
            -webkit-transform: rotate(35deg);
            transform: rotate(35deg);
            background: #dd4040;
        }

        .mound_spade:before, .mound_spade:after {
            content: '';
            display: block;
            position: absolute;
        }

        .mound_spade:before {
            width: 40%;
            height: 30px;
            bottom: 98%;
            left: 50%;
            margin-left: -20%;
            background: #dd4040;
        }

        .mound_spade:after {
            width: 100%;
            height: 30px;
            top: -55px;
            left: 0%;
            box-sizing: border-box;
            border: 10px solid #dd4040;
            border-radius: 4px 4px 20px 20px;
        }
    </style>

</head>

<body translate="no">
<div class="content">
    <canvas class="snow" id="snow" width="1349" height="400"></canvas>
    <div class="main-text">
        <h1>(灬ꈍ ꈍ灬) 哎呀? 一不小心配置出现错误呐!</h1>
        <h1>不灰心, 就要成功啦~ (●'◡'●)</h1>
        <h3></h3>
        <div>
            尝试检查配置或重新启动程序.
        </div>
        <h4>参考文档直达: <a href="https://senu.email">https://senu.email</a></h4>
    </div>
    <div class="ground">
        <div class="mound">
            <div class="mound_text">404</div>
            <div class="mound_spade"></div>
        </div>
    </div>
</div>


<script>
    (function () {
        function ready(fn) {
            if (document.readyState != 'loading') {
                fn();
            } else {
                document.addEventListener('DOMContentLoaded', fn);
            }
        }

        function makeSnow(el) {
            var ctx = el.getContext('2d');
            var width = 0;
            var height = 0;
            var particles = [];

            var Particle = function () {
                this.x = this.y = this.dx = this.dy = 0;
                this.reset();
            }

            Particle.prototype.reset = function () {
                this.y = Math.random() * height;
                this.x = Math.random() * width;
                this.dx = (Math.random() * 1) - 0.5;
                this.dy = (Math.random() * 0.5) + 0.5;
            }

            function createParticles(count) {
                if (count != particles.length) {
                    particles = [];
                    for (var i = 0; i < count; i++) {
                        particles.push(new Particle());
                    }
                }
            }

            function onResize() {
                width = window.innerWidth;
                height = window.innerHeight;
                el.width = width;
                el.height = height;

                createParticles((width * height) / 10000);
            }

            function updateParticles() {
                ctx.clearRect(0, 0, width, height);
                ctx.fillStyle = '#f6f9fa';

                particles.forEach(function (particle) {
                    particle.y += particle.dy;
                    particle.x += particle.dx;

                    if (particle.y > height) {
                        particle.y = 0;
                    }

                    if (particle.x > width) {
                        particle.reset();
                        particle.y = 0;
                    }

                    ctx.beginPath();
                    ctx.arc(particle.x, particle.y, 5, 0, Math.PI * 2, false);
                    ctx.fill();
                });

                window.requestAnimationFrame(updateParticles);
            }

            onResize();
            updateParticles();
        }

        ready(function () {
            var canvas = document.getElementById('snow');
            makeSnow(canvas);
        });
    })();
</script>

</body>
</html>"""