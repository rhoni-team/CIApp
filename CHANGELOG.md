# CHANGELOG



## v0.7.0 (2025-01-09)

### Build

* build: change to shared network ([`df00a62`](https://github.com/rhoni-team/CIApp/commit/df00a62137118fbfb8ef21b9d20728f9acea1493))

* build: change time of blocking server ([`b0be1a8`](https://github.com/rhoni-team/CIApp/commit/b0be1a80e3b7b4293e9f680f793daf325c63c946))

* build: add drf token authentication ([`289117b`](https://github.com/rhoni-team/CIApp/commit/289117bc5b977bba4030ec11a1cbc4e2ddd51606))

* build: add throttle classes of drf ([`77f85b8`](https://github.com/rhoni-team/CIApp/commit/77f85b8931f006007e0bc1a720085d764d454e54))

* build: add site to preload list ([`3d65636`](https://github.com/rhoni-team/CIApp/commit/3d656364a3376ae50fb37300ef2e4f4b9ec0ec25))

* build: add secure hsts seconds ([`b19a14c`](https://github.com/rhoni-team/CIApp/commit/b19a14ce1809df0e91cdc967406971ba8413d891))

* build: include subdomains in https ([`8d32709`](https://github.com/rhoni-team/CIApp/commit/8d32709e7dc10b3d83439de8c8d24608e67df8eb))

* build: use 443 ssl nginx configuration ([`74fac3e`](https://github.com/rhoni-team/CIApp/commit/74fac3e7742915302d351eec5dc2baf205bc0734))

* build: replace whitenoise by nginx ([`a935cf1`](https://github.com/rhoni-team/CIApp/commit/a935cf1c088e0b279578ea7af74b3a4acf8cb3ad))

* build: replace .env variables for Vite default variables ([`e475c22`](https://github.com/rhoni-team/CIApp/commit/e475c22585cd281edc8fa34ab42df532b402da16))

* build: add postgres to docker compose ([`94f2b6f`](https://github.com/rhoni-team/CIApp/commit/94f2b6f5b083824d522abd4590fec1c2ff7cde77))

* build: move and improve file ([`a4cbdad`](https://github.com/rhoni-team/CIApp/commit/a4cbdad62095985a08c71566d4a0b28fd4d27933))

* build: django docker compose ([`523ab27`](https://github.com/rhoni-team/CIApp/commit/523ab27743c296579e9bce04aab2a259fa2899be))

* build: dockerfile django and postgres ([`2a72ff2`](https://github.com/rhoni-team/CIApp/commit/2a72ff21bec5818d86206c3d106b94522797a3ed))

### Chore

* chore: security settings only in production ([`23b1f1c`](https://github.com/rhoni-team/CIApp/commit/23b1f1cbffb2d8c195f1ea90947b1665422dd1c7))

* chore: remove nginx folder ([`9d89308`](https://github.com/rhoni-team/CIApp/commit/9d893085735191963c41422f1c2cfe8a27097437))

* chore: remove cerbot from docker compose ([`39df9d7`](https://github.com/rhoni-team/CIApp/commit/39df9d786d2d10250170f7f2ce545895d7171dcb))

* chore: change service name ([`3eecab8`](https://github.com/rhoni-team/CIApp/commit/3eecab8af267d0be2a37be4a55741ca50430eccb))

* chore: rename volumes ([`a955ecf`](https://github.com/rhoni-team/CIApp/commit/a955ecf3e8bee1219dd25fd42005519e31dd8b91))

* chore: remove restart from cerbot ([`ee1c609`](https://github.com/rhoni-team/CIApp/commit/ee1c609679c73eb93da1914d472fef134e3b8090))

* chore: add and modify volumes names ([`6efbeb4`](https://github.com/rhoni-team/CIApp/commit/6efbeb4e795291bfaeb637e5ee2301580c9e5bd2))

* chore: remove commented lines ([`466f78e`](https://github.com/rhoni-team/CIApp/commit/466f78e9a98c2ce988abb149566c3a44edf61ea5))

* chore: comment cerbot dependency on nginx service ([`50d61e9`](https://github.com/rhoni-team/CIApp/commit/50d61e92cc2e8c83dc019ce9b3e7aa1fd2347412))

* chore: add volumes to django ([`4fcf23f`](https://github.com/rhoni-team/CIApp/commit/4fcf23f9544f57bff995342604a6b6b5e2153289))

* chore: uncomment cerbot container ([`9b6f24d`](https://github.com/rhoni-team/CIApp/commit/9b6f24db3a22e1eb20eec3e78ae4a43e3ce5fa7b))

* chore: change restart type ([`a107703`](https://github.com/rhoni-team/CIApp/commit/a10770324283f701a61cf118e2d601e08c95ddef))

* chore: add restart to containers ([`5449124`](https://github.com/rhoni-team/CIApp/commit/54491240057c138032b50417856edd3fdf9817ae))

* chore: https cookie and ssl redirect to django settings ([`0e7381e`](https://github.com/rhoni-team/CIApp/commit/0e7381e922fc0dd7622565dd27f456b7310cf57a))

* chore: comment cerbot command ([`34ee1e0`](https://github.com/rhoni-team/CIApp/commit/34ee1e0f7d568d04c3daae23356569a6767cfb55))

* chore: add location to redirect ([`2831730`](https://github.com/rhoni-team/CIApp/commit/2831730e1535f71191edf1294abee7191f62a866))

* chore: redirect to https and add content security policy header ([`55e3513`](https://github.com/rhoni-team/CIApp/commit/55e3513e4334c337f8d1a401db31ac68eb310395))

* chore: add root cerbot to nginx conf ([`cbc96fe`](https://github.com/rhoni-team/CIApp/commit/cbc96fe2adc72c455b1c7907d473819fddda3913))

* chore: remove www subdomain from command ([`12a1fa6`](https://github.com/rhoni-team/CIApp/commit/12a1fa6af2b7eca41c68d7794d7b2b37a6792fd4))

* chore: remove www from subdomain ([`27e5aa5`](https://github.com/rhoni-team/CIApp/commit/27e5aa55c7d26dddb04a96d9a946224019c346ed))

* chore: fix typo ([`d3981c8`](https://github.com/rhoni-team/CIApp/commit/d3981c8717daf4cb8cf97cd647c490a2b24fb6d0))

* chore: add webroot path ([`4fa3d77`](https://github.com/rhoni-team/CIApp/commit/4fa3d77c067b4feb343845147e39f77affd4ac91))

* chore: add location of acme-challenge ([`088d6a1`](https://github.com/rhoni-team/CIApp/commit/088d6a1960b3b56215ce40566f85ac300695db8d))

* chore: add .env.staging.cerbot ([`3ec77fd`](https://github.com/rhoni-team/CIApp/commit/3ec77fdde877221a32eace4d70a84f5aa6f6662c))

* chore: add cerbot container ([`014fd4c`](https://github.com/rhoni-team/CIApp/commit/014fd4c3f5c145e7fc9949b800b82c7cadd4d135))

* chore: add www url ([`08433c9`](https://github.com/rhoni-team/CIApp/commit/08433c91aeae272a9556fc2b9f1a13aa680e93da))

* chore: changing ports to default ports ([`188fd5d`](https://github.com/rhoni-team/CIApp/commit/188fd5d26516f992e5466f2aae32e1c319142126))

* chore: comment ssl configuration ([`7b1b995`](https://github.com/rhoni-team/CIApp/commit/7b1b9955f2c5553f45613b376bdccbac994dc89b))

* chore: copy nginx conf file ([`588681a`](https://github.com/rhoni-team/CIApp/commit/588681a28c66d0d8430e683ef13fe0f4153bcd5a))

* chore: comment acme-companion container ([`2a64be1`](https://github.com/rhoni-team/CIApp/commit/2a64be13d34db8e304a4250d6a4f639cd649f4b6))

* chore: change volume vhost to default ([`0f9d76c`](https://github.com/rhoni-team/CIApp/commit/0f9d76c25b193bfce49944ac6516a55ca0bff44f))

* chore: change dockerfile to default file ([`872a91b`](https://github.com/rhoni-team/CIApp/commit/872a91bdddb6966319dcbee30a6ace9c08a7f0d1))

* chore: fix dockerfile typo ([`0b21e9e`](https://github.com/rhoni-team/CIApp/commit/0b21e9ef35c2c7c3d6b681c4dfb85aac2548fd52))

* chore: change dockerfile ([`cfbdeb0`](https://github.com/rhoni-team/CIApp/commit/cfbdeb06c5341fc19c26b04050a2571095aa7168))

* chore: build nginx from image ([`3e4c864`](https://github.com/rhoni-team/CIApp/commit/3e4c8649eaeb8457cbd331ea67cee8eb8fd57ef1))

* chore: ignore dockerfile ([`40f70df`](https://github.com/rhoni-team/CIApp/commit/40f70dfb226c619203be09462ae96b64314f1b51))

* chore: vhost rhonidev file ([`6ef6d41`](https://github.com/rhoni-team/CIApp/commit/6ef6d4193b1bb7e304fb33ec572777b23de9257f))

* chore: copy conf file ([`abcd23b`](https://github.com/rhoni-team/CIApp/commit/abcd23b560675d874f14224133b77307c6f4f22e))

* chore: add acme challenge location ([`6e7fea5`](https://github.com/rhoni-team/CIApp/commit/6e7fea55233fdbcdcea50c69b337d3b8e63a4fa9))

* chore: testing default ports ([`406cd0e`](https://github.com/rhoni-team/CIApp/commit/406cd0ef5d97ea76b49349d0a7ea82e8f789ecf3))

* chore: add headers to nginx conf ([`9bd32a1`](https://github.com/rhoni-team/CIApp/commit/9bd32a152c021d4a7a6454e4fa8ba78fda5b6901))

* chore: add acme companion to docker compose ([`2b0c286`](https://github.com/rhoni-team/CIApp/commit/2b0c286873d4e99c7ba16d71208ab1057ad6b39e))

* chore: env staging to gitignore ([`9822d8d`](https://github.com/rhoni-team/CIApp/commit/9822d8d2fedb4dae4820ddad2d9f5903b0104c93))

* chore: change nginx to proxy ([`2f1263f`](https://github.com/rhoni-team/CIApp/commit/2f1263ff78994c0b664a40b765fabb941daf1f3a))

* chore: load variable from env ([`fe18bbc`](https://github.com/rhoni-team/CIApp/commit/fe18bbc6a3327fda8c2120d7dc9e930a93c16e99))

* chore: read allowed host from .env files ([`0633a56`](https://github.com/rhoni-team/CIApp/commit/0633a56dd0d2bac89c8d5d4ed6668b9a7d3dba32))

* chore: change default time to test security ([`7ee6dcf`](https://github.com/rhoni-team/CIApp/commit/7ee6dcf1ce47c827bf72429b9905f796a1047b9b))

* chore: remove commented lines ([`9e12c23`](https://github.com/rhoni-team/CIApp/commit/9e12c23b42aaaf10b4cd4331ec594b502482387a))

* chore: add nginx to docker compose ([`428d4e6`](https://github.com/rhoni-team/CIApp/commit/428d4e608578c01d845baf3a2837bbb7f79cb3c1))

* chore: add nginx dockerfile ([`14379ca`](https://github.com/rhoni-team/CIApp/commit/14379ca40b96dca074b8346592b56889c1cdff87))

* chore: add nginx configuration ([`7cc563d`](https://github.com/rhoni-team/CIApp/commit/7cc563d3a3213b75cd440f94cacb2b6b1d27dbc9))

* chore: add bash file to run docker ([`7ae2026`](https://github.com/rhoni-team/CIApp/commit/7ae202679f44cbaaaf793a7829ce8818ebf3c339))

* chore: run container by using gunicorn ([`4fad3aa`](https://github.com/rhoni-team/CIApp/commit/4fad3aafd3646eb448b4ac7b387ee3e96c9a111e))

* chore: add install of gunicorn ([`800348e`](https://github.com/rhoni-team/CIApp/commit/800348e95cbcf3f0086217f61464fdbe0fbaac1e))

* chore: remove secret key from settings ([`9eefbca`](https://github.com/rhoni-team/CIApp/commit/9eefbca494fbdb2cd7affe893f242ee7aac84e24))

* chore: read env variables with django-environ ([`a87fcc3`](https://github.com/rhoni-team/CIApp/commit/a87fcc326e1f357b4ffca805dbc782f17df2289f))

* chore: move file ([`597ce78`](https://github.com/rhoni-team/CIApp/commit/597ce78a693d89f1112a1e00a29ba02a2da12086))

* chore: load different env files ([`756003e`](https://github.com/rhoni-team/CIApp/commit/756003ef6d84de8630cc1f01a8e6f47cb433fd95))

* chore: add env prod and env dev to gitignore ([`33043cc`](https://github.com/rhoni-team/CIApp/commit/33043ccb7b342f6e7f71dd1a50ec7cd0679f3423))

* chore: Add badges for cautions and isolation elements ([`4eeac86`](https://github.com/rhoni-team/CIApp/commit/4eeac86aabfaedb7217c404bf9ee6a76391ec59b))

### Ci

* ci: add env variable ([`96282ef`](https://github.com/rhoni-team/CIApp/commit/96282ef912231a8ad66be23d0e7190e3a3950724))

* ci: add env variable DJANGO_ALLOWED_HOSTS ([`6c24f52`](https://github.com/rhoni-team/CIApp/commit/6c24f52986a3b3797d337dfebf7ec04bd31e9853))

* ci: change env variable for django and docker ([`e08af8a`](https://github.com/rhoni-team/CIApp/commit/e08af8a38ee746e2a4572f4d4ebd6774d77d6c66))

### Feature

* feat: change external port ([`26e7f4b`](https://github.com/rhoni-team/CIApp/commit/26e7f4b47329adb035b0a050570f8987b6462f69))

* feat: security settings ([`e0cd2eb`](https://github.com/rhoni-team/CIApp/commit/e0cd2eb91995c037de17a837c04a4b51a53c2c81))

### Unknown

* Merge pull request #72 from rhoni-team/with_external_cerbot

With external cerbot ([`810568a`](https://github.com/rhoni-team/CIApp/commit/810568ac7cef7e8c5733a12b16ffb0bd53c25a2b))

* Merge branch &#39;connect_external_nginx&#39; of github.com:rhoni-team/AppCI into connect_external_nginx ([`6895f8d`](https://github.com/rhoni-team/CIApp/commit/6895f8d6be4b26d49435651525fbe6db90233a58))

* Merge branch &#39;connect_external_nginx&#39; of github.com:rhoni-team/AppCI into connect_external_nginx ([`c4c0e6b`](https://github.com/rhoni-team/CIApp/commit/c4c0e6b48799a38ebfac6d3dec02387e414486aa))

* change copy of conf file ([`da9ec46`](https://github.com/rhoni-team/CIApp/commit/da9ec468ce6f9454681b38b4f80bac98657a905e))

* add ssl configuration ([`7363888`](https://github.com/rhoni-team/CIApp/commit/7363888180c917c0881ca0068881981c73d8764d))

* Merge pull request #62 from rhoni-team/60.add_gunicorn_to_docker

Add gunicorn to docker for deployment ([`ed69473`](https://github.com/rhoni-team/CIApp/commit/ed694739d916b82969aa15b24f1cb8477a4613a0))

* Merge pull request #58 from rhoni-team/56.dockerize_django_for_deployment

56.dockerize django for deployment ([`0def66a`](https://github.com/rhoni-team/CIApp/commit/0def66a902231db20d99bfee07401bd01954f4b9))

* Merge pull request #55 from rhoni-team/create-diseases-badges

Add badges for cautions and isolation elements ([`4d9cd71`](https://github.com/rhoni-team/CIApp/commit/4d9cd71b3354fe126c0f6b493cb02c00b6e0bde1))


## v0.6.0 (2024-06-20)

### Chore

* chore: Add a new blank end line ([`4e87ea0`](https://github.com/rhoni-team/CIApp/commit/4e87ea0a8c831ecf756a177e0ef32a3b6d94bb95))

* chore: Add new interfaces and types ([`b3ad5b7`](https://github.com/rhoni-team/CIApp/commit/b3ad5b78a88c350a1ec257b1b38fcf1933d59289))

* chore: Create a declaration file for DiseasesAPI JS file ([`51b20d6`](https://github.com/rhoni-team/CIApp/commit/51b20d6f6c79c25a526b3ca9310a3345baa914e4))

* chore: run autopep and pylint ([`6009350`](https://github.com/rhoni-team/CIApp/commit/6009350034c4d46dee2dd7d7e056faf4df1bd7f9))

### Feature

* feat: add types ([`dfd86a4`](https://github.com/rhoni-team/CIApp/commit/dfd86a4e64cfdf7cf68863ee701e3d3cd2f0df3c))

* feat: call api to get disease detailed data ([`bd41ae0`](https://github.com/rhoni-team/CIApp/commit/bd41ae0ff84c241468951b8e0393a870887916bd))

* feat: send ordered data to client ([`2fcb165`](https://github.com/rhoni-team/CIApp/commit/2fcb165015e9c8673bb708c58488483de10ef8a3))

* feat: functions to order api data ([`cb5a7d1`](https://github.com/rhoni-team/CIApp/commit/cb5a7d1b50acbcdedbf3cfde8c20e33b25c892f0))

* feat: send prop of disease list to input component ([`d27e29f`](https://github.com/rhoni-team/CIApp/commit/d27e29fcf688431c48d11d8ce0fb0a53eca1f887))

* feat: show label and emit id on input ([`cf80b86`](https://github.com/rhoni-team/CIApp/commit/cf80b86ff7377f7005c4f26f193ef295307f8d1f))

### Fix

* fix: Fix component imports and rendering sections ([`eaf37e2`](https://github.com/rhoni-team/CIApp/commit/eaf37e24f70c097aea504c6ce644fe64643c432a))

* fix: Fix missing imports and remove console logs ([`bc69115`](https://github.com/rhoni-team/CIApp/commit/bc691151a0a820ca7d772c3ec22291a5aa5df5ae))

* fix: Add a missing type ([`897e184`](https://github.com/rhoni-team/CIApp/commit/897e184a458110fec69cbd7c2b46bf4ed4965713))

* fix: set null as diseaseDetail default ([`ffa0036`](https://github.com/rhoni-team/CIApp/commit/ffa00364ecb20d9ef10db57d8514a4a3b71625fe))

* fix: lint errors ([`558d847`](https://github.com/rhoni-team/CIApp/commit/558d847f8811fe4200d3691873bba8077b2451fb))

* fix: show label in warnings ([`8cd0054`](https://github.com/rhoni-team/CIApp/commit/8cd005449f05e1397d5f05260aedd14869388d8a))

* fix: add warning to  disease data ([`7fe8680`](https://github.com/rhoni-team/CIApp/commit/7fe8680749f4e3ad5ae1c974e1b7bd52379c6656))

### Refactor

* refactor: replace datasheet component with disease parameters ([`dd6ce67`](https://github.com/rhoni-team/CIApp/commit/dd6ce6732dd86aad53023c5303abc8410529edd6))

* refactor: change file name ([`e33ab0d`](https://github.com/rhoni-team/CIApp/commit/e33ab0d41be3d2d6fb029a12f0979d436ce7d090))

### Unknown

* Merge pull request #46 from rhoni-team/31.connect_frontend_and_backend

31.connect frontend and backend ([`9209744`](https://github.com/rhoni-team/CIApp/commit/9209744b28beca5f123cbfea5b0188b853bf1b7f))

* improve: Add a new icon file ([`b1e839e`](https://github.com/rhoni-team/CIApp/commit/b1e839ec081442a9dc6a577bf7ceaf080c6f1fbd))

* Merge branch &#39;main&#39; into 31.connect_frontend_and_backend ([`6ee1136`](https://github.com/rhoni-team/CIApp/commit/6ee1136ac6b0ad1071df1008b1a687a1c4048c58))


## v0.5.0 (2024-06-06)

### Unknown

* Merge pull request #43 from rhoni-team/calculator-component

Calculator component ([`89a6d3c`](https://github.com/rhoni-team/CIApp/commit/89a6d3ca4b85e4d0948e20aa5f3913980bba3971))

* Merge branch &#39;main&#39; into calculator-component ([`750ba1f`](https://github.com/rhoni-team/CIApp/commit/750ba1fb1d1d06c80488d9e7d655799dc8028c8b))


## v0.4.0 (2024-06-06)

### Build

* build: install axios ([`1282b57`](https://github.com/rhoni-team/CIApp/commit/1282b57b1fca4e124d0474635c3e775c44ad8be3))

### Chore

* chore: add temporary buttons to test API ([`9ab99a9`](https://github.com/rhoni-team/CIApp/commit/9ab99a9122900ca67fb95a1b21d6ba000df5bd99))

* chore: button to test diseases data list ([`097aeaa`](https://github.com/rhoni-team/CIApp/commit/097aeaa2974934d11bc4fcd095783d463f9b01f4))

* chore: remove hello rhonies view ([`8845152`](https://github.com/rhoni-team/CIApp/commit/88451521e5848c28a730b1591553d7141d026464))

* chore: install django rest framework ([`2ecb556`](https://github.com/rhoni-team/CIApp/commit/2ecb55633d2ec3c6463d188876a8b499b567204e))

* chore: Add icons to the top navbar component ([`db3d905`](https://github.com/rhoni-team/CIApp/commit/db3d9056ff0a955e8f71540cf3824b96a0c58dc1))

* chore: Delete unused files from assets ([`3047b3c`](https://github.com/rhoni-team/CIApp/commit/3047b3cc474faa4f979a8da3a2da0cc82685a451))

* chore: Add icons for the dark-light button component ([`cf02805`](https://github.com/rhoni-team/CIApp/commit/cf02805cef199b42414cf5166bf5e05f355f5b9f))

### Feature

* feat: get detail for a given disease ([`2fe0bac`](https://github.com/rhoni-team/CIApp/commit/2fe0bacc323b275ba3d81227ef80152e78892c4d))

* feat: add complete data disease serializer ([`335de98`](https://github.com/rhoni-team/CIApp/commit/335de98d3c2ac93fb426ad1e6e511351fd54ee51))

* feat: get diseases data list in frontend ([`3510799`](https://github.com/rhoni-team/CIApp/commit/351079936a40f16806a9b9d0babf409f198eb7c2))

* feat: url to get diseases list ([`2bbd59a`](https://github.com/rhoni-team/CIApp/commit/2bbd59a9e42888e45eda7bb1070a330b868e1b13))

* feat: view to get diseases list ([`2e70f44`](https://github.com/rhoni-team/CIApp/commit/2e70f4496be01a100860c2b3c00e529b8efd5da5))

* feat: diseases list serializer ([`59091ac`](https://github.com/rhoni-team/CIApp/commit/59091aca9aa6ef6fbd862850d39a9bd4291b89f2))

### Refactor

* refactor: Make changes to match the linter requirements ([`d00c413`](https://github.com/rhoni-team/CIApp/commit/d00c413b70c3fdcd768b2897bef7fcc4e0b9c49c))

### Unknown

* Merge pull request #42 from rhoni-team/34-disease-datasheet

34 disease datasheet ([`dfa906b`](https://github.com/rhoni-team/CIApp/commit/dfa906bb501fd51cb51cc80ecdb56a4b93ca725e))

* feat add detailed disease view ([`14242b8`](https://github.com/rhoni-team/CIApp/commit/14242b8873f91dc5ff2a6e76c12f15b4d670f259))

* improve: Change the data use logic to matching the &#39;Data Provider Pattern&#39; ([`d5663fa`](https://github.com/rhoni-team/CIApp/commit/d5663fabf56098f1e3e589b2d769eb8cfc772021))


## v0.3.0 (2024-06-04)

### Build

* build: Add dayjs dependencies ([`1e132f5`](https://github.com/rhoni-team/CIApp/commit/1e132f5653d0baf620aa7e5f0151494cbda75132))

* build: add pandas library ([`fcb7284`](https://github.com/rhoni-team/CIApp/commit/fcb728426bc25b28a7eb6d8cf8ff8bb814d2a6f7))

* build: Change the reference to main.js to main.ts ([`ad2b2ef`](https://github.com/rhoni-team/CIApp/commit/ad2b2ef2ce28a65ae2db12dc2bfbf62086a843df))

* build: install clean text rhoni package ([`3448e95`](https://github.com/rhoni-team/CIApp/commit/3448e95a5752aec8c451951ba4173d8ddb51b503))

### Chore

* chore: Remove clutter ([`b437ce2`](https://github.com/rhoni-team/CIApp/commit/b437ce2c0c2083675080a2cc2105e3577f717d13))

* chore: Add functionality to buttons at the bottom nav ([`f54a5e1`](https://github.com/rhoni-team/CIApp/commit/f54a5e1e20ee0e4539c0e1b664679006a5d44a27))

* chore: Add a view for the isolation calculator ([`4050ad0`](https://github.com/rhoni-team/CIApp/commit/4050ad047df6facff1e17529463fc4ddb8632f25))

* chore: Add necessary dependencies for date picker ([`aaf130c`](https://github.com/rhoni-team/CIApp/commit/aaf130c3bc55765e7cafaa3c0a5924636c1e0482))

* chore: Integrate the new components to de App and HomeView components ([`99fdf58`](https://github.com/rhoni-team/CIApp/commit/99fdf5866ef768a00a63b039e4f81749081c2a3f))

* chore: Add a mocked disease finder component ([`a4ec83d`](https://github.com/rhoni-team/CIApp/commit/a4ec83dd2586150175096170a5f4c562e185e5ca))

* chore: lint and autopep ([`398d495`](https://github.com/rhoni-team/CIApp/commit/398d49548a04c30a6e51eae2d1eb5f4aa7794e35))

* chore: remove prints ([`55e23c3`](https://github.com/rhoni-team/CIApp/commit/55e23c37fd5692596262cbcb3868b64100758383))

* chore: add init file to test ([`bd95cd4`](https://github.com/rhoni-team/CIApp/commit/bd95cd4eac62f88766bc9f0ba1444dbf5a5bd0a5))

* chore: Move the bottom navbar component from Homeview to main app.vue ([`943c185`](https://github.com/rhoni-team/CIApp/commit/943c18563e39112316866b43c7b630e3f4d11668))

* chore: add difteria data to special cases ([`d93d1ec`](https://github.com/rhoni-team/CIApp/commit/d93d1eccb6be7dd5caadee744497c339ba528b18))

* chore: replace csv with new data ([`8cb96fa`](https://github.com/rhoni-team/CIApp/commit/8cb96fadd9ddf31ec865df844207b93941df8f19))

* chore: remove isolation time migration ([`14d1f91`](https://github.com/rhoni-team/CIApp/commit/14d1f91f9c8ae0dee84625c753ad65c6d8328f3f))

* chore: remove example test ([`3cc8889`](https://github.com/rhoni-team/CIApp/commit/3cc888955fc69bf7e1b45c4a100d0bb14f33e3eb))

* chore: add test csv file to run tests ([`2c0dc20`](https://github.com/rhoni-team/CIApp/commit/2c0dc204cebf88fb973511ecda5e31884a5cbfe0))

* chore: add new data in migrations ([`bbfac0d`](https://github.com/rhoni-team/CIApp/commit/bbfac0da65dd5cd02466e1e2c54e4bcde36ec995))

* chore: add special cases isolation time data ([`27c3cd1`](https://github.com/rhoni-team/CIApp/commit/27c3cd1fac34fdf46f3829f5ec2b8fad23804f8a))

* chore: Add icons to assets ([`272cd41`](https://github.com/rhoni-team/CIApp/commit/272cd413695cf9f7ac7c84290355b778dfbd0f27))

* chore: Add styles and svg to assets ([`ebe3ee6`](https://github.com/rhoni-team/CIApp/commit/ebe3ee6a67a8415210dd8446e16f4b35845e731e))

* chore: Add types for disease datasheet ([`3966411`](https://github.com/rhoni-team/CIApp/commit/39664114631e3652be69a0b4615099022817f0ac))

* chore: Make some changes for typescript implementation ([`7af5553`](https://github.com/rhoni-team/CIApp/commit/7af555384f5ddfc48e207f1721c0c58a90c82de0))

* chore: Remove clutter ([`7331571`](https://github.com/rhoni-team/CIApp/commit/7331571ef1bc3cdd43f5dba3b841aa6b515e3803))

* chore: add disease data in csv format ([`5b1ae77`](https://github.com/rhoni-team/CIApp/commit/5b1ae774c876968b207d2907493b494ac9f54666))

* chore: add disease type data in migration ([`351223c`](https://github.com/rhoni-team/CIApp/commit/351223cfd2b2deae905bbc71c84a92a883501e62))

* chore: add isolation warnings migration ([`a844b41`](https://github.com/rhoni-team/CIApp/commit/a844b41f346517b01ea0e6e8fdacf5a9c9de7757))

* chore: add time related migrations ([`22966d6`](https://github.com/rhoni-team/CIApp/commit/22966d62ec6e6b888b92ee29ce7f0531b823d668))

* chore: add cleaning type data in migration ([`72068bf`](https://github.com/rhoni-team/CIApp/commit/72068bf2a22833c19e11b6c5e5ca7b67d6ef213e))

* chore: add isolation types data in migration ([`45f3e15`](https://github.com/rhoni-team/CIApp/commit/45f3e157152037f7d263008f7a6073da6fc1fb91))

* chore: add unaccent postgres extension ([`402531e`](https://github.com/rhoni-team/CIApp/commit/402531ee286a30fdef603dd2f8adfbd4b4b31283))

### Feature

* feat: Add the isolation calculator component ([`9ada26f`](https://github.com/rhoni-team/CIApp/commit/9ada26f9c809e2c7ac7caa588913f9c4d2a6c6cc))

* feat: Add a top navbar menu component ([`73da520`](https://github.com/rhoni-team/CIApp/commit/73da520064c367b3b9585b6f7b1e59294d0fbe8e))

* feat: Add a sidebar menu component ([`817fc19`](https://github.com/rhoni-team/CIApp/commit/817fc190771ed755c76fdfde997038f7210dc0fd))

* feat: Create a disease search selector input ([`2547851`](https://github.com/rhoni-team/CIApp/commit/2547851d135c66dec36770bfa7f794eebb71a124))

* feat: add observation qx data to disease instance ([`2edb7aa`](https://github.com/rhoni-team/CIApp/commit/2edb7aa478db4b8daa0a0d26e0e0125106d2d6b6))

* feat: add qx observation field to disease model ([`4642252`](https://github.com/rhoni-team/CIApp/commit/464225263d73da1c59d37375cdc72cdc76a165f4))

* feat: add si no boolean fields to disease instance ([`b25850f`](https://github.com/rhoni-team/CIApp/commit/b25850f8596f230ba79906ae737153327c9b276a))

* feat: Add a dark-light mode button ([`54aa232`](https://github.com/rhoni-team/CIApp/commit/54aa232435bb25477c86b9429b1c910850f1f959))

* feat: Add the disease datasheet component ([`97f682d`](https://github.com/rhoni-team/CIApp/commit/97f682db5078c8aecac4f2a3e342ea872357464b))

* feat: Add a bottom navbar ([`e9dbdfa`](https://github.com/rhoni-team/CIApp/commit/e9dbdfa4f74f0feae44ddcb017e9c66fb8481ca8))

* feat: add with atb and other isolation fx ([`5691b17`](https://github.com/rhoni-team/CIApp/commit/5691b1758e89232fc3923e0ac9a9e0ee59bc9fa7))

* feat: improve and clean migration file ([`e73cc5c`](https://github.com/rhoni-team/CIApp/commit/e73cc5cf712d302163b9ed73abf30e3147fe0f05))

* feat: class to add data to disease dictionary instance ([`c85e46a`](https://github.com/rhoni-team/CIApp/commit/c85e46ad1eec704c7bfaf43817ae71b04c2cdf56))

* feat: class to load csv data as pd df ([`530baae`](https://github.com/rhoni-team/CIApp/commit/530baae5b16a36b4b8f44699aa2e7aba2679f73b))

* feat: add auxiliary data and fx to clean column names ([`4a57273`](https://github.com/rhoni-team/CIApp/commit/4a572736f341e7e03f5c002525a10db70f4858ce))

* feat: Add the diseaseDatasheet component ([`458ddc5`](https://github.com/rhoni-team/CIApp/commit/458ddc5486f5b863ef59e42974ceb92af264e98d))

* feat: add disease model ([`f914fa4`](https://github.com/rhoni-team/CIApp/commit/f914fa4544d124484a58845e7683869869683783))

* feat: add disease type model ([`9d78bb9`](https://github.com/rhoni-team/CIApp/commit/9d78bb98d2d4357314e17ff44d718a22f9d8e0a2))

* feat: add time and warning models ([`4461cf7`](https://github.com/rhoni-team/CIApp/commit/4461cf7b4e51938eb6a4f7783324dd92b1734b88))

* feat: add cleaning type model ([`aa3287a`](https://github.com/rhoni-team/CIApp/commit/aa3287a277200bca5fe671bb37d2adb77e32c955))

* feat: add commands for recreate db and new migration file ([`f75df19`](https://github.com/rhoni-team/CIApp/commit/f75df19ed207634850ca8ca0c7725c8e1a1cd611))

* feat: starting initial migration ([`87dfd94`](https://github.com/rhoni-team/CIApp/commit/87dfd94c36f48417d2ba961c1b2886ee8fd7276c))

* feat: create isolation type model ([`ae559dd`](https://github.com/rhoni-team/CIApp/commit/ae559ddc50373d1a5e6dba9a7fdf5e08c479387c))

### Fix

* fix: remove null from many to many field ([`7ba8f3d`](https://github.com/rhoni-team/CIApp/commit/7ba8f3db6071f5233ff54c161372787d4131f110))

* fix: Disable calculator output result when isolation time value is zero ([`73bcb0b`](https://github.com/rhoni-team/CIApp/commit/73bcb0b1805c900556f559f98ae94d6d9767d1d6))

* fix: Hide the input checkbox from the dark-light button that appears after the tailwindcss-forms addition ([`a1a1e4c`](https://github.com/rhoni-team/CIApp/commit/a1a1e4c692367c783c6522a8cd2e580c67a4e88b))

* fix: Add configs to eslint for the TS parser ([`653eb31`](https://github.com/rhoni-team/CIApp/commit/653eb313287cd2ed6b32c16a93742ccba74842a2))

* fix: typo in column names ([`d8d4b12`](https://github.com/rhoni-team/CIApp/commit/d8d4b12422f20f724ed363b7dc53483322a3870b))

* fix: typo in declaracion obligatoria ([`52d8e92`](https://github.com/rhoni-team/CIApp/commit/52d8e92cf5c6e26d951bdac4051914012a030d4f))

* fix: mandatory declaration field name ([`5d0f89c`](https://github.com/rhoni-team/CIApp/commit/5d0f89cec5796701e246712bb6f1d8a03ccf47c5))

* fix: fk to special cases of isolation time ([`0b629aa`](https://github.com/rhoni-team/CIApp/commit/0b629aab8188af305656e98b67f40d1831389da6))

* fix: remove isolation time nan values ([`b4f3406`](https://github.com/rhoni-team/CIApp/commit/b4f34066cf88f6d3c0c66a0ba981b55bfa2a02b2))

* fix: cleaning type labels ([`214bf12`](https://github.com/rhoni-team/CIApp/commit/214bf12ba16b63be47c9066474d6602b44840e4b))

* fix: change to precautions type in migrations ([`b830043`](https://github.com/rhoni-team/CIApp/commit/b830043020d47c553fb87a64e13b83729bd2e077))

* fix: change isolation type model by precaution type model ([`531c749`](https://github.com/rhoni-team/CIApp/commit/531c7493473017a0339b8b0ef886a8bffac54daa))

* fix: Add compiler options to tsconfig ([`5d27744`](https://github.com/rhoni-team/CIApp/commit/5d277444fe8a0ab5bf4bd14160bc2231f76eac1f))

* fix: add room sharing field to disease model ([`b794c81`](https://github.com/rhoni-team/CIApp/commit/b794c8124ad45e9b461cf81a1c18d6d6fb958305))

* fix: isolation type fields ([`ae52263`](https://github.com/rhoni-team/CIApp/commit/ae522633f5779260703aa1011d24143da1052892))

### Refactor

* refactor: Change the defineProps definition for the DiseaseDatasheetComponent ([`9fd39a0`](https://github.com/rhoni-team/CIApp/commit/9fd39a0df67df247dfb9adf23d441a525c17c3e0))

* refactor: Changes to match eslint requirements ([`c1e666f`](https://github.com/rhoni-team/CIApp/commit/c1e666f032ad1765b8ebfd97a5e7067831423d4f))

### Style

* style: Add styles for the isolation calculator component ([`dbc1810`](https://github.com/rhoni-team/CIApp/commit/dbc181065ad82d9ca46f6f511164149a8bcaf493))

* style: Add style class for main app ([`2507caa`](https://github.com/rhoni-team/CIApp/commit/2507caaa233046b27ccf0f68e293ee1c4fe8380a))

### Test

* test: Add tests to assert the correctly loading for HomeView ([`07677b1`](https://github.com/rhoni-team/CIApp/commit/07677b11596ef811c56fc7e45106b4f297447079))

* test: add test for adding related instances to disease ([`992ec3b`](https://github.com/rhoni-team/CIApp/commit/992ec3b0e47d36d78bdd7e8ed0ff3075691f4b2a))

* test: add test to add disease data ([`1548856`](https://github.com/rhoni-team/CIApp/commit/154885617e5c2075b36d3ff3255b47b1c15cf3b2))

* test: add test to load csv data as df and create new columns ([`453eb70`](https://github.com/rhoni-team/CIApp/commit/453eb708f86eb9bb70af2a27b94d77a8a9984e5d))

* test: Change the dummy test to pass ([`a2a2918`](https://github.com/rhoni-team/CIApp/commit/a2a2918637cb9d8699db970a63838a84b5e30c66))

### Unknown

* Merge pull request #40 from rhoni-team/27.fill_database_and_create_models

27.fill database and create models ([`16b8506`](https://github.com/rhoni-team/CIApp/commit/16b8506bc1a5175d5dade45ffa868af5174c3d2b))

* improvement: Update the interface for diseaseDatasheet ([`5a977ed`](https://github.com/rhoni-team/CIApp/commit/5a977ed121e2c4d8451f56099361b02ce6dc648d))

* improvement: Create separate icons for the bottom navbar ([`e14cd4c`](https://github.com/rhoni-team/CIApp/commit/e14cd4cc7ca2cf6a056dab6e36845059e8ba6041))

* improve: Add the disease sheet component ([`2536048`](https://github.com/rhoni-team/CIApp/commit/253604843662660f372994c5e556424147bdcaa3))

* improve: Add typescript ([`2c7202f`](https://github.com/rhoni-team/CIApp/commit/2c7202fb6d7ed224167a6add2fe30f02ad48d409))


## v0.2.0 (2024-05-21)

### Chore

* chore: Some minor changes to the main view to test the UI styles ([`d3995da`](https://github.com/rhoni-team/CIApp/commit/d3995dad17410a85b1c76da08d3f5a18e13fa24a))

* chore: Add another monet painting to use the slider ([`bf2078f`](https://github.com/rhoni-team/CIApp/commit/bf2078f39049efd565695ab24b57908cf28e9b1c))

* chore: Add Tailwindcss Typography ([`937415c`](https://github.com/rhoni-team/CIApp/commit/937415cfbe9006b5a6a5354fba8e6be39fc6419f))

* chore: Remove the greetings message from django template ([`8309c72`](https://github.com/rhoni-team/CIApp/commit/8309c72f6e632870b65a5f7c8b5e273e82c3e7c2))

* chore: Add the static build folder to the linter&#39;s ignoring files configuration ([`f84ea9e`](https://github.com/rhoni-team/CIApp/commit/f84ea9e19d54903d75ec6b7a7dbf842ee374fab6))

* chore: Add daisyUI ([`d43ff37`](https://github.com/rhoni-team/CIApp/commit/d43ff3787a82f8293b2d9b2b1042f6500e721626))

* chore: Update ci-cd.yml (vitest) ([`142f9fd`](https://github.com/rhoni-team/CIApp/commit/142f9fdcb7123ed56738509a9ea48f0de3d66218))

* chore: Update ci-cd.yml (Vitest) ([`cb7d9b8`](https://github.com/rhoni-team/CIApp/commit/cb7d9b8e76d9f9f8a14d8bac2f9b5ebb7e154191))

* chore: Update ci-cd.yml (Vitest) ([`c0335d4`](https://github.com/rhoni-team/CIApp/commit/c0335d4c321de081a4605fe9d9d4c32708d2bbb4))

### Feature

* feat: Add a light/dark mode button selector ([`b709835`](https://github.com/rhoni-team/CIApp/commit/b709835167f92bcb0972e4da3a35b9e7b13c6f83))

### Refactor

* refactor: Edit the code to match the linter requirements ([`74b11d3`](https://github.com/rhoni-team/CIApp/commit/74b11d3fab7978d72ad1bd96c251ab0e5f811be4))

### Test

* test: Change the assertion to pass the test ([`7c6a9b1`](https://github.com/rhoni-team/CIApp/commit/7c6a9b185a4e179225c38e0fde83993bb0395344))

### Unknown

* Merge pull request #26 from rhoni-team/set-css-styles

Set css styles ([`c2762bd`](https://github.com/rhoni-team/CIApp/commit/c2762bd8aff6b738a72a034b2e73b092637f693a))

* Update ci-cd.yml: Remove the continue-on-error

They didn&#39;t work as I expected, so I had to remove them again ([`f675de1`](https://github.com/rhoni-team/CIApp/commit/f675de180832a90905b6afff57d07a8b291ed3b1))

* Update ci-cd: Add continue-on-error to the linter and testing steps ([`baf3573`](https://github.com/rhoni-team/CIApp/commit/baf35738ce1b6b6f67b6db56906cf0bf73047028))

* Update ci-cd.yml ([`7e1c4b9`](https://github.com/rhoni-team/CIApp/commit/7e1c4b9871f38ed473e1224efd9b73f7cd41b0db))

* Update ci-cd.yml ([`30b328a`](https://github.com/rhoni-team/CIApp/commit/30b328ab53e4c1f8c83b223e9d0d46d668a659aa))

* Update ci-cd.yml ([`c17d6dd`](https://github.com/rhoni-team/CIApp/commit/c17d6dd752dcc1ac8e95da9b46d6401571db007c))

* Update ci-cd.yml ([`b74fb01`](https://github.com/rhoni-team/CIApp/commit/b74fb015e7076a77567a3427bd48bb445620a03c))

* Update ci-cd.yml ([`3bfc8bb`](https://github.com/rhoni-team/CIApp/commit/3bfc8bba65e2e0a2427ffb6c5a316e2d821aeb39))

* Update: ci-cd.yml ([`ad0a4e7`](https://github.com/rhoni-team/CIApp/commit/ad0a4e7a0e612ec0a87b1dada4f3e91601e8c962))

* Update: Add ESLint step to ci-cd workflow ([`973d16a`](https://github.com/rhoni-team/CIApp/commit/973d16abbeb426fba0e2b79ba5845e04bab40ade))


## v0.1.0 (2024-05-08)

### Build

* build: install python semantic release ([`1a86880`](https://github.com/rhoni-team/CIApp/commit/1a868800d7018c5127d4c291e4bdceb42c6dd36b))

* build: add autopep configuration ([`8871f6c`](https://github.com/rhoni-team/CIApp/commit/8871f6cdd577b1b2569533d5986dbcb3fe4487dd))

* build: install autopep ([`2079f47`](https://github.com/rhoni-team/CIApp/commit/2079f47762900ba1a58dd0b2cb69a571aba1a8aa))

* build: change module naming style to any ([`e9cc064`](https://github.com/rhoni-team/CIApp/commit/e9cc0649cca0090eedb32778c055d1845c683c9c))

* build: add makefile with lint command ([`b55bda9`](https://github.com/rhoni-team/CIApp/commit/b55bda90fba91f27778a839d85bc343e91565496))

* build: add pylint configuration file ([`f6270f6`](https://github.com/rhoni-team/CIApp/commit/f6270f62c2e1899b9298126db709f90b77e2fc95))

* build: add plugin pylint-django ([`b853382`](https://github.com/rhoni-team/CIApp/commit/b8533828ebf0b9ce4919128bd2106fe8d41a6dbe))

* build: change psycopg2 for binary version ([`6071307`](https://github.com/rhoni-team/CIApp/commit/6071307a7878a915e18a0c0ca8ebdfaa6e844dcc))

* build: install pylint ([`af9a78d`](https://github.com/rhoni-team/CIApp/commit/af9a78dee394f1f58d83b20b60adc90cf9632f0a))

* build: install psycopg2 ([`0cc8428`](https://github.com/rhoni-team/CIApp/commit/0cc8428840af79ea59de9b8be4b5327b968922ad))

* build: install whitenoise and dotenv ([`4a118ad`](https://github.com/rhoni-team/CIApp/commit/4a118adeb6d0f3bb6202e32a01b97356ae747b91))

* build: install django vite and cors dependencies ([`d744d35`](https://github.com/rhoni-team/CIApp/commit/d744d35651df71fa7e52e459445dd7bbaad154bc))

### Chore

* chore: add semantic release configuration ([`5484386`](https://github.com/rhoni-team/CIApp/commit/5484386b274fc4819b835b3a37225dfeed68c9c3))

* chore: add make test command ([`ca51efb`](https://github.com/rhoni-team/CIApp/commit/ca51efba32b3d02dce81e9c0882215f0eb2e8e19))

* chore: are dummy test to test CI ([`4c3deb7`](https://github.com/rhoni-team/CIApp/commit/4c3deb73d35f057523423705a895599b05f1d443))

* chore: add autopep command to makefile ([`ff3910d`](https://github.com/rhoni-team/CIApp/commit/ff3910dc084c65454ac62735e9422b7d761a1618))

* chore: Change eslint rules from essential to recommended ([`9b0e509`](https://github.com/rhoni-team/CIApp/commit/9b0e509092d8f34985eccb7a377e77b8a50f6aaf))

* chore: add globals to eslint for node modules ([`0dd9f3a`](https://github.com/rhoni-team/CIApp/commit/0dd9f3a008fa23a55946371ab07f929b04b27ba1))

* chore: Add some Eslint dependencies ([`c3c9906`](https://github.com/rhoni-team/CIApp/commit/c3c9906f599962924a2b8b91334ceddc9677937e))

* chore: add static to gitignore ([`4e05142`](https://github.com/rhoni-team/CIApp/commit/4e05142a94badfa35deb917c4a4740ab9f006bce))

### Ci

* ci: reorder actions ([`2f3cb89`](https://github.com/rhoni-team/CIApp/commit/2f3cb895980bd6896eedf51eddc8df42f1e08981))

* ci: starting ci-cd file with new actions versions ([`04e3934`](https://github.com/rhoni-team/CIApp/commit/04e3934ec09614421d0c1d2aefff196fffb5fef0))

### Documentation

* docs: add badge of pylint to readme ([`4540385`](https://github.com/rhoni-team/CIApp/commit/4540385d7cc46789b0ffd346ea9a8d71e53b70dd))

* docs: add base readme file ([`c8332fc`](https://github.com/rhoni-team/CIApp/commit/c8332fca8622ff09f367d3104995a696fe7a3664))

### Feature

* feat: add postgres configuration ([`54a0641`](https://github.com/rhoni-team/CIApp/commit/54a064130e65d2a1d35e0b0f70ff9ff9ce42dea5))

* feat: add vite manifest path ([`0ec2f8c`](https://github.com/rhoni-team/CIApp/commit/0ec2f8c76e87cab5814bcee40a132cdc3b0740f7))

* feat: add middleware whitenose configuration ([`47268d7`](https://github.com/rhoni-team/CIApp/commit/47268d72dd0b47b260e8a187407c71ebabadbd3d))

* feat: read env by using dotenv ([`c4a6e84`](https://github.com/rhoni-team/CIApp/commit/c4a6e8438aebb4cd0887e8c13eab7fea68939f51))

* feat: add whitenoise configuration ([`c319f8a`](https://github.com/rhoni-team/CIApp/commit/c319f8aa031f339254f4cb545189bb219606b17c))

* feat: django vite configuration ([`ed26146`](https://github.com/rhoni-team/CIApp/commit/ed26146d0ca7f7ebd5eb61ab1aad11c8b756c3cc))

* feat: django corsheaders configuration ([`af1ce1c`](https://github.com/rhoni-team/CIApp/commit/af1ce1c58e4404dc1d536076c56e8bf00fb94515))

* feat: static files configuration ([`ffd613f`](https://github.com/rhoni-team/CIApp/commit/ffd613ffd3770b579b31bf23bc8d62548e6cc888))

* feat: load vite in django entry point ([`dd4fdb6`](https://github.com/rhoni-team/CIApp/commit/dd4fdb69f79731bc9abb81ce91409d1520f22e80))

* feat(frontend): import preload of modules ([`0ca77a5`](https://github.com/rhoni-team/CIApp/commit/0ca77a57c7065bb7013c81eb6bee700bf3271ac2))

* feat(frontend): vite configuration using django-vite ([`3e3e6a2`](https://github.com/rhoni-team/CIApp/commit/3e3e6a22efd98ea88ade9dbbd91dabc9a9fe4abf))

* feat(frontend): install dependencies ([`bc00c80`](https://github.com/rhoni-team/CIApp/commit/bc00c80cb05f7de445f20593b74ca80d45e32d11))

* feat: add index template ([`942c7d5`](https://github.com/rhoni-team/CIApp/commit/942c7d594a76e3431f57356a610c56363b5e8417))

* feat: add entry point template ([`3bc0469`](https://github.com/rhoni-team/CIApp/commit/3bc04692518b57b3f933fcfaad41d5304d588f2f))

* feat: add requirements.txt ([`968b4dc`](https://github.com/rhoni-team/CIApp/commit/968b4dcfa99faf2b40698c330a5dcdec523dddae))

* feat: add template for testing app configuration ([`22a099c`](https://github.com/rhoni-team/CIApp/commit/22a099c5576e6653787a9090f2e6169ffd862209))

* feat: base urls configuration ([`12489ed`](https://github.com/rhoni-team/CIApp/commit/12489ed79d9ba5b62c412cd3b2ee2d5c179ae113))

* feat: templates and app config ([`1aa97c6`](https://github.com/rhoni-team/CIApp/commit/1aa97c6e046de7abfd299c341a15308bfa3a0806))

* feat: start django project and backend app ([`8ec4f70`](https://github.com/rhoni-team/CIApp/commit/8ec4f70622ada022f2b81df1f1d67b5152a784e8))

### Fix

* fix: frontend path and postgres image ([`ca0fdcb`](https://github.com/rhoni-team/CIApp/commit/ca0fdcbe76840b34e28550b435006318a9063d9d))

* fix: move github folder ([`e12f2bf`](https://github.com/rhoni-team/CIApp/commit/e12f2bf94a2d6868a920ee268cff25d6e1252bb9))

* fix: add html standard mode ([`0b0cad8`](https://github.com/rhoni-team/CIApp/commit/0b0cad875520f9a68cfc3a2bc87a580500430d44))

* fix: remove statics from backend dir ([`19b95c1`](https://github.com/rhoni-team/CIApp/commit/19b95c15024a0143fc111d8e511a294e7dea11e1))

### Refactor

* refactor: run lint ([`acd0fdf`](https://github.com/rhoni-team/CIApp/commit/acd0fdf89556a5bfc8f7839a914df060c36ae202))

* refactor: Fixes by ESLint ([`33c51ad`](https://github.com/rhoni-team/CIApp/commit/33c51ad4172f72c40af81e90d34ccb5d9bfadda1))

* refactor: Change tabulation ([`6409413`](https://github.com/rhoni-team/CIApp/commit/640941392941ac168666187f1a8c2e9aab581fde))

* refactor: add image to test production mode ([`a810a59`](https://github.com/rhoni-team/CIApp/commit/a810a59ab2fd55b1e6aa58b9306e5df4cf42bb7d))

* refactor(frontend): change hello message ([`8516316`](https://github.com/rhoni-team/CIApp/commit/8516316598217b5b9564e65d17f7f4e95f083c35))

### Style

* style: use autopep to fix style ([`4d0d00c`](https://github.com/rhoni-team/CIApp/commit/4d0d00c73c5f34879bca4ef4afed04c447b9b551))

* style: style code with pylint ([`fc028c4`](https://github.com/rhoni-team/CIApp/commit/fc028c4bd43f7c7784baaaf3b5535dcc62048b17))

### Unknown

* Merge pull request #23 from rhoni-team/5.add_ci

fix: move github folder ([`236309a`](https://github.com/rhoni-team/CIApp/commit/236309a1738c6132e76a287e8b032e32a08acd65))

* Merge pull request #22 from rhoni-team/5.add_ci

5.add ci ([`1285a1f`](https://github.com/rhoni-team/CIApp/commit/1285a1f9c90315175131947dd01ecef449c7a1a0))

* Merge remote-tracking branch &#39;origin/main&#39; into 5.add_ci ([`263b9d9`](https://github.com/rhoni-team/CIApp/commit/263b9d99b701221b184573d282b1973229d75c80))

* Merge pull request #21 from rhoni-team/7.pylint_and_autopep_config

7.pylint and autopep config ([`2596ce5`](https://github.com/rhoni-team/CIApp/commit/2596ce5b12788ba34887d1d04136b2d92141e4cf))

* Merge remote-tracking branch &#39;origin/main&#39; into 7.pylint_and_autopep_config ([`235cb48`](https://github.com/rhoni-team/CIApp/commit/235cb48e62018093d505d8166b60536e9d3ab6a9))

* Merge pull request #18 from rhoni-team/11.connect_postgres_db

11.connect postgres db ([`d9c849c`](https://github.com/rhoni-team/CIApp/commit/d9c849c55657e768136756e2e5c2075bcc8b340a))

* Merge pull request #15 from rhoni-team/4.connect_django_vue_for_production

4.connect django vue for production ([`778a4f8`](https://github.com/rhoni-team/CIApp/commit/778a4f825799e1c42efb7b3a7b96b02d3d3b6fe8))

* Merge remote-tracking branch &#39;origin/main&#39; into 4.connect_django_vue_for_production ([`02b9859`](https://github.com/rhoni-team/CIApp/commit/02b9859f09d5941c66f1ae4d8d2f8f58b416aead))

* Merge pull request #17 from rhoni-team/10-add-eslint

10 add eslint ([`47779f2`](https://github.com/rhoni-team/CIApp/commit/47779f2ca3fba2f216df61a29b39417aeefe1b7d))

* Create ESLint configuration file and scripts ([`e30c246`](https://github.com/rhoni-team/CIApp/commit/e30c246ed816928b8d3becbc21e41a65b8bf20a4))

* Add eslint dependencies ([`ac9e555`](https://github.com/rhoni-team/CIApp/commit/ac9e555d027bb27874d9349a9c1f81fffc700a1a))

* Create a mock test ([`260a284`](https://github.com/rhoni-team/CIApp/commit/260a28407d8469759c145f8b956d69b0f6f8b81d))

* Set the main view as a non dynamic import ([`c4d24a4`](https://github.com/rhoni-team/CIApp/commit/c4d24a473361eb4c48011a4d6d7eeecb24a99c27))

* Set up config for testing with vitest ([`96e152d`](https://github.com/rhoni-team/CIApp/commit/96e152dca6ab2e524940951e657b7b1a865e5f1b))

* Add jsdom plugin to run tests in a web development environment ([`e3c947d`](https://github.com/rhoni-team/CIApp/commit/e3c947d98208ed8acbd2e3dc6226edc0682ddda8))

* Add vue test-utils to the project ([`7b6856b`](https://github.com/rhoni-team/CIApp/commit/7b6856b68196daa8ff09107b979e581bd7259cec))

* Merge pull request #13 from rhoni-team/3.connect_django_vue_for_development

3.connect django vue for development ([`3b00130`](https://github.com/rhoni-team/CIApp/commit/3b00130d53c54bb4be98f2fc940ca04d52d0f1f2))

* Merge pull request #12 from rhoni-team/2-create-vue3-app

2 create vue3 app ([`3b16366`](https://github.com/rhoni-team/CIApp/commit/3b16366f9b7085fbdb3f3dd22113a89af0affd86))

* Create a dynamic import for the main view ([`79f4819`](https://github.com/rhoni-team/CIApp/commit/79f481917082fa701e50da877b1d6134c22b7c83))

* Create the router folder for vueRouter for a better scaffolding ([`6eafd8f`](https://github.com/rhoni-team/CIApp/commit/6eafd8f9ff98daf8298fbd30af967ad344bccf80))

* Add a missing blank line at the end of some files ([`e8310c2`](https://github.com/rhoni-team/CIApp/commit/e8310c2e1bd2dbf1c94e31ffaa9629d296a9b8dd))

* Add configs to enhance DX ([`3a035b0`](https://github.com/rhoni-team/CIApp/commit/3a035b0ad3772aa50803fed5b07e775b272f4528))

* Add VueRouter to the project ([`3566755`](https://github.com/rhoni-team/CIApp/commit/3566755fa989151e65d6f37d85ba731d157d0d4f))

* Remove clutter ([`baa5d1a`](https://github.com/rhoni-team/CIApp/commit/baa5d1aa53dfcb2f7eff877b6195305248601207))

* Add TailwindCSS to the project ([`6bd0e19`](https://github.com/rhoni-team/CIApp/commit/6bd0e19f65731d781491467522d4b69803604744))

* Add vitest to the project ([`bd7b509`](https://github.com/rhoni-team/CIApp/commit/bd7b5096d08e4b64868da0eaab68134118ffb2f9))

* Add package-lock.json file to gitignore ([`9a2ac1c`](https://github.com/rhoni-team/CIApp/commit/9a2ac1cecd973068eba46478dcc4f3f5a28936fa))

* Create vite+vue frontend app ([`7f9e97e`](https://github.com/rhoni-team/CIApp/commit/7f9e97eacd05b04c43cb32655ec2375d0faa05d3))

* Merge pull request #8 from rhoni-team/1.create_django_project_and_backend_app

1.create django project and backend app ([`4350c1f`](https://github.com/rhoni-team/CIApp/commit/4350c1f66f430eae708ee3c92f20c91206f3f535))

* Add package-lock.json to the gitignore ([`f2feb55`](https://github.com/rhoni-team/CIApp/commit/f2feb5547d2dd0242b413355bf976c14ea466396))

* Initial commit ([`6fdfd2b`](https://github.com/rhoni-team/CIApp/commit/6fdfd2b1976218c27b183a52c37c6e4ba07ff4e4))
